"""
Anteprima del volume del silicone e testo volume sul box.
Ricostruito da decompiled_py/components/silicone_mold.py.

Logica chiave:
  silicone_mold = box - patron     (ciò che resta di silicone una volta colato)
  volume_text = oggetto testo 3D scritto in mm dalle parti laterali del box
"""

from __future__ import annotations
import bpy
from mathutils import Vector

from .object_wrapper import Object
from .modifiers import build_voxel_modifier, build_decimate_collapse
from .primitives import create_text_object


def build_silicone_mold_preview(
    patron: Object,
    box: Object,
    voxel_size: float = 0.8,
) -> float:
    """Crea un oggetto chiamato 'silicone_mold' che rappresenta il volume del silicone.
    Restituisce il volume calcolato (mm³).

    Pattern Moldboxer:
      1. Duplica patron, applica voxel modifier (per pulire).
      2. Duplica box.
      3. Box_copy -= patron_copy → silicone_mold.
      4. Calcola volume.
    """
    # Se esiste già un silicone_mold, restituisci il suo volume.
    existing = bpy.data.objects.get("silicone_mold")
    if existing is not None:
        return Object(existing).volume

    patron_copy = patron.duplicate(name_adder="_for_silicone")
    if voxel_size > 0:
        patron_copy.apply_modifier(build_voxel_modifier(voxel_size))

    box_copy = box.duplicate(name_adder="_silicone_preview")
    box_copy.name = "silicone_mold"
    box_copy -= patron_copy

    # Pulizia: rimuovi una sottile fetta in alto e in basso per evitare facce piatte
    # esattamente coincidenti con bbox del patron.
    box_copy.cut_plane(Vector((0, 0, 1)), Vector((0, 0, box_copy.max_z - 0.2)))
    box_copy.cut_plane(Vector((0, 0, -1)), Vector((0, 0, box_copy.min_z + 0.2)))

    patron_copy.remove()
    return box_copy.volume


def create_volume_text(volume_mm3: float, size: float = 8.0) -> Object:
    """Crea un oggetto testo 3D che dice "{ml}ml". Restituisce un Object pronto da unire.

    Fix 2026-05-13: convert FONT -> MESH prima di applicare il decimate; altrimenti
    Blender 4.x rifiuta `modifier_apply` su oggetti TEXT con "Cannot apply modifier
    for this object type" e l'intero `confirm_mold` fallisce.
    """
    volume_ml = volume_mm3 / 1000.0
    text_obj = create_text_object(f"{volume_ml:.0f}ml", size=size, extrude_height=2.0)
    # Convert the FONT object to MESH so that modifiers can be applied.
    bpy.ops.object.select_all(action="DESELECT")
    bpy.context.view_layer.objects.active = text_obj
    text_obj.select_set(True)
    bpy.ops.object.convert(target="MESH")
    wrapper = Object(text_obj, name="volume_text")
    # Riduci poligoni del testo (Moldboxer applica voxel 0.05 + decimate 0.5 — qui basta decimate).
    wrapper.apply_modifier(build_decimate_collapse(0.5))
    wrapper.origin_to_geometry()
    return wrapper


def place_volume_text(box: Object, volume_mm3: float, side: str = "X+") -> Object:
    """Crea e posiziona il testo sul lato richiesto del box. Restituisce il box."""
    text = create_volume_text(volume_mm3)
    if side == "X+":
        text.translate_whole(Vector((box.max_x + 0.5, 0, box.min_z + box.height / 4)))
    elif side == "Y-":
        text.translate_whole(Vector((0, box.min_y - 0.5, box.min_z + box.height / 4)))
    # Aggiungi al box come union.
    box += text
    text.remove()
    return box


def sub_patron(patron: Object, box: Object, box_voxel_size: float = 0.8) -> float:
    """Variante: il box dato DIVENTA il silicone_mold (in-place).
    Equivale a `silicone_mold.sub_patron` Moldboxer.
    Restituisce il volume in mm³."""
    box.name = "silicone_mold"
    if box_voxel_size > 0:
        patron_copy = patron.duplicate(name_adder="_for_sub")
        patron_copy.apply_modifier(build_voxel_modifier(box_voxel_size))
        box -= patron_copy
        patron_copy.remove()
    else:
        box -= patron
    return box.volume
