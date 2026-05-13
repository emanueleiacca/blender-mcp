"""
Preprocessing del master.
Ricostruito da decompiled_py/components/preprocess.py + bl_utils.py.

Flusso `preprocess_patron`:
  1. Garantisce che la scena Blender sia configurata in millimetri.
  2. Wrappa l'active object come Object con nome 'patron'.
  3. (opz.) Se ci sono mesh isolate scollegate, le filtra per volume >= 1 e le joina.
  4. (opz.) Centra a origine (XY=0, Z=0 al fondo).
  5. Applica tutte le trasformazioni.
  6. Se non manifold: voxel remesh per ripararlo.
"""

from __future__ import annotations
from typing import Optional
import bpy
from mathutils import Vector

from .object_wrapper import Object
from .voxel_size import get_master_voxel_size
from .modifiers import build_voxel_modifier


def configure_metric_millimeter_units(context=None) -> None:
    """Imposta la scena Blender in millimetri.
    Replica di bl_utils.configure_metric_millimeter_units (decompiled)."""
    if context is None:
        context = bpy.context
    scene = context.scene
    scene.unit_settings.system = "METRIC"
    scene.unit_settings.scale_length = 0.001
    scene.unit_settings.length_unit = "MILLIMETERS"
    # Imposta clipping della viewport per evitare clipping di oggetti grandi.
    for area in (context.window.screen.areas if context.window else []):
        if area.type == "VIEW_3D":
            for space in area.spaces:
                if space.type == "VIEW_3D":
                    space.clip_start = 0.1
                    space.clip_end = 10000.0
                    space.overlay.grid_scale = 0.01
                    space.overlay.grid_subdivisions = 10


def heal_mesh(obj: Object, master_quality: str = "HIGH") -> None:
    """Voxel remesh del master. Equivalente a `silicone.heal_patron`."""
    voxel = get_master_voxel_size(master_quality, obj)
    obj.apply_modifier(build_voxel_modifier(voxel))


def center_to_origin(obj: Object) -> None:
    """Porta il modello a (0, 0, *) con il fondo a Z=0.
    Equivalente a `silicone.center_obj` dall'operators.py."""
    obj.select()
    bpy.ops.object.origin_set(type="GEOMETRY_ORIGIN", center="BOUNDS")
    obj.object.location.x = 0
    obj.object.location.y = 0
    obj.object.location.z -= obj.min_z


def preprocess_patron(
    target: Optional[Object] = None,
    master_quality: str = "HIGH",
    center: bool = True,
    isolate: bool = False,
) -> Object:
    """Pipeline completa di pre-elaborazione master.

    Args:
        target: Object da preprocessare. Se None, prende l'active object.
        master_quality: FAST/MID/HIGH/ULTRA — usato solo se serve heal.
        center: porta al centro scena con fondo a Z=0.
        isolate: se True, joina eventuali mesh disconnesse di volume >= 1.

    Returns:
        L'Object rinominato 'patron', pronto per il pipeline mold.
    """
    configure_metric_millimeter_units()

    if target is None:
        active = bpy.context.view_layer.objects.active
        if active is None:
            raise RuntimeError("preprocess_patron: no active object and no target passed")
        target = Object(active)

    target.name = "patron"

    if isolate:
        _join_disconnected_meshes(target, master_quality)

    if center:
        center_to_origin(target)

    target.apply_all_transforms()

    if not target.is_manifold():
        heal_mesh(target, master_quality)

    return target


def _join_disconnected_meshes(target: Object, master_quality: str) -> None:
    """Quando l'STL ha più gusci scollegati, li joina dopo aver filtrato i piccoli.
    Versione semplificata rispetto a Moldboxer: separiamo per loose parts via bmesh,
    rimuoviamo quelli con volume < 1 mm³, e applichiamo un voxel remesh sul resto."""
    target.select()
    bpy.ops.mesh.separate(type="LOOSE")
    # Ora ci sono più oggetti col prefisso del target. Filtra per volume.
    candidates = [
        obj for obj in bpy.data.objects
        if obj.name.startswith(target.object.name)
    ]
    keep = []
    for obj in candidates:
        try:
            vol = Object(obj).volume
        except Exception:
            vol = 0.0
        if vol >= 1.0:
            keep.append(obj)
        else:
            bpy.data.objects.remove(obj, do_unlink=True)

    if not keep:
        raise RuntimeError("preprocess_patron isolate: all sub-meshes filtered out (volume < 1mm³)")

    # Re-join: seleziona keep, active il primo, join.
    bpy.ops.object.select_all(action="DESELECT")
    for obj in keep:
        obj.select_set(True)
    bpy.context.view_layer.objects.active = keep[0]
    bpy.ops.object.join()

    # Rebind del wrapper sull'oggetto joinato.
    target.object = bpy.context.view_layer.objects.active
    target.name = "patron"

    # Heal con voxel.
    heal_mesh(target, master_quality)
