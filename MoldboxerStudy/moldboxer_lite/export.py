"""
Export STL multi-oggetto. Ricostruito da decompiled_py/components/export.py.

Comportamento Moldboxer:
- Itera tutti gli oggetti in scena.
- Se nome contiene 'patron' o 'silicone' → file `{name}_{volume:.0f}ml.stl`.
- Altrimenti → file `{name}.stl`.
- Usa apply_modifiers=True (mesh con modifier baked).
"""

from __future__ import annotations
from pathlib import Path
import bpy

from .object_wrapper import Object


def export_all_parts(dir_path: str, apply_modifiers: bool = True) -> list:
    """Esporta ogni oggetto della scena come STL nel dir indicato.
    Restituisce la lista dei file scritti."""
    out_dir = Path(bpy.path.abspath(dir_path))
    out_dir.mkdir(parents=True, exist_ok=True)
    if out_dir.suffix.lower() == ".blend":
        out_dir = out_dir.parent

    written = []
    for obj in list(bpy.data.objects):
        if obj.type != "MESH":
            continue
        name = obj.name
        wrapped = Object(obj)
        if "patron" in name or "silicone" in name:
            try:
                vol_ml = wrapped.volume / 1000.0
                filename = f"{name}_{vol_ml:.0f}ml.stl"
            except Exception:
                filename = f"{name}.stl"
        else:
            filename = f"{name}.stl"
        out_path = out_dir / filename

        wrapped.select()
        # Blender 4.x: bpy.ops.wm.stl_export.
        # Blender 3.x: bpy.ops.export_mesh.stl. Tentiamo entrambi.
        try:
            bpy.ops.wm.stl_export(
                filepath=str(out_path),
                export_selected_objects=True,
                apply_modifiers=apply_modifiers,
            )
        except AttributeError:
            bpy.ops.export_mesh.stl(
                filepath=str(out_path),
                use_selection=True,
                use_mesh_modifiers=apply_modifiers,
            )
        written.append(str(out_path))

    return written
