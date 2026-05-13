"""
Classe `Wrapper(Object)`: costruisce il "box" che avvolge il master.

Ricostruita da decompiled_py/components/wrapper.py.

Ricetta (verificata sul bytecode Moldboxer 1.4.9):
  1. Applica le trasformazioni al target (così bound_box è in world space).
  2. Se geometry_to_origin: centra il target sull'origine.
  3. Se build_from_sphere (safe mode): parte da una UV sphere centrata e scalata
     attorno al target. Altrimenti: duplica il target e applica
     scale_normals(2) — gonfia outward la geometria.
  4. Iter n_wraps volte:
       applica un voxel remesh (REMESH VOXEL con voxel_size)
     (NB: nel codice originale c'è anche uno shrinkwrap intermedio sul target;
      qui lo omettiamo nella v1 — il voxel da solo già produce un wrap accettabile.
      Si può abilitare passando `target_shrinkwrap=True`.)
  5. Se decimate: collapse decimate ratio=0.3.
  6. Se cut_bot: livella il fondo a Z=min_z (rimuove la mezza-pancia inferiore).

Il risultato è un Object chiamato 'box' (+ name_adder opzionale).
"""

from __future__ import annotations
import bpy
from mathutils import Vector

from .object_wrapper import Object
from .modifiers import (
    build_voxel_modifier,
    build_decimate_collapse,
    shrink_mod_outside,
)
from .primitives import create_uv_sphere_primitive


class Wrapper(Object):
    def __init__(
        self,
        target: Object,
        voxel_size: float = 1.0,
        distance: float = 6.0,
        decimate: bool = True,
        n_wraps: int = 3,
        name_adder: str = "",
        geometry_to_origin: bool = False,
        cut_bot: bool = True,
        build_from_sphere: bool = False,
        target_shrinkwrap: bool = False,
    ):
        target.apply_all_transforms()
        if geometry_to_origin:
            target.geometry_to_origin()

        if build_from_sphere:
            # Parti da una UV sphere centrata sul target, scalata per coprire tutta la bbox.
            # Scala = (max dimensione target × 0.75), così il diametro = 1.5 × max_dim
            # (margine sufficiente perché il successivo shrinkwrap arrivi al target).
            sphere_obj = create_uv_sphere_primitive(1.0)
            super().__init__(sphere_obj, name="box" + name_adder)
            target_max = max(target.width, target.depth, target.height)
            self.scale_uniform(target_max * 0.75)
            self.translate_whole(target.center_coords)
            self.apply_all_transforms()
        else:
            # Duplica il target e espandi outward con scale_normals.
            # Il valore di inflation deve essere LEGGERMENTE MAGGIORE del `distance`
            # target (= box_gap) così che il successivo shrinkwrap abbia margine per
            # "spingere indietro" la geometria fino alla distanza esatta.
            # FIX 2026-05-13: prima era costante 2.0 mm (=ignorava box_gap); ora scala
            # con distance × 1.2 (per box_gap=4.5 → inflation 5.4 mm, sufficiente).
            wrapper_obj = target.duplicate(name_adder="_wrap_tmp")
            inflation = max(distance * 1.2, 2.0)  # min 2mm per master molto piccoli
            wrapper_obj.scale_normals(inflation)
            super().__init__(wrapper_obj.object, name="box" + name_adder)

        self.build_from_sphere = build_from_sphere
        self.decimate = decimate
        self.voxel_size = voxel_size
        self.distance = distance
        self.n_wraps = n_wraps
        self.cut_bot_flag = cut_bot
        self.target_shrinkwrap = target_shrinkwrap

        self.shape(target)

    def shape(self, target: Object) -> None:
        """Ripete il pattern voxel-remesh (+ shrinkwrap se richiesto) n_wraps volte.
        Il risultato è una mesh chiusa che avvolge il target a distanza ~uniforme."""
        for _ in range(self.n_wraps):
            if self.target_shrinkwrap:
                # Shrinkwrap che spinge i vertici verso la superficie del target con offset = distance.
                self.apply_modifier(shrink_mod_outside(offset=self.distance, target=target.object))
            # Voxel remesh: chiude eventuali buchi, riprende una topologia regolare.
            self.apply_modifier(build_voxel_modifier(self.voxel_size))

        if self.decimate:
            self.apply_modifier(build_decimate_collapse(0.3))

        if self.cut_bot_flag:
            # Livella il fondo a Z = target.min_z (riferito al target world-space).
            target_min_z = target.min_z
            if self.min_z < target_min_z - 0.01:
                self.cut_plane(Vector((0, 0, -1)), Vector((0, 0, target_min_z)))
