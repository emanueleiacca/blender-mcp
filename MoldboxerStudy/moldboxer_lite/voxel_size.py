"""
Voxel size adattivo, ricostruito 1:1 da decompiled_py/voxel_size.py.

Formula:    voxel_size = base[quality] * (max_dim / REFERENCE_MAX_DIMENSION)
con clip a MIN_BOX_VOXEL_SIZE o MIN_MASTER_VOXEL_SIZE.

Esempio (master alto 150mm, quality HIGH):
    base = 1.2, voxel = 1.2 * 150/150 = 1.2 mm
Esempio (master alto 50mm, quality HIGH):
    base = 1.2, voxel = 1.2 * 50/150 = 0.4 → clip a 0.5 mm

Le costanti `REFERENCE_MAX_DIMENSION=150`, `MIN_BOX_VOXEL_SIZE=0.5`,
`MIN_MASTER_VOXEL_SIZE=0.05` sono state estratte dal bytecode Moldboxer.
"""

from __future__ import annotations
from typing import Optional, Union

from .constants import (
    BOX_QUALITY_MAP,
    MASTER_QUALITY_MAP,
    MIN_BOX_VOXEL_SIZE,
    MIN_MASTER_VOXEL_SIZE,
    REFERENCE_MAX_DIMENSION,
)


def _resolve_dimensions(candidate) -> Optional[float]:
    """Restituisce la dimensione max (mm) di un oggetto Blender, o None."""
    if candidate is None:
        import bpy
        # Fallback: cerca un oggetto chiamato 'patron', poi l'active.
        patron = bpy.data.objects.get("patron")
        candidate = patron if patron is not None else bpy.context.active_object
    if candidate is None:
        return None
    # Accetta sia un wrapper Object (con .width/.depth/.height) sia un bpy_object
    if hasattr(candidate, "width") and hasattr(candidate, "depth") and hasattr(candidate, "height"):
        max_dim = max(candidate.width, candidate.depth, candidate.height)
    else:
        # bpy.types.Object → .dimensions è un Vector(x, y, z)
        dims = getattr(candidate, "dimensions", None)
        if dims is None:
            return None
        max_dim = max(dims.x, dims.y, dims.z)
    return max_dim if max_dim > 0 else None


def get_adaptive_voxel_size(quality: str, quality_map: dict, candidate=None) -> float:
    """Formula generica: base × (max_dim / 150). Se non si può misurare il candidate
    si torna alla base nuda."""
    if quality not in quality_map:
        raise ValueError(f"Unknown quality '{quality}'. Valid: {list(quality_map.keys())}")
    base = quality_map[quality]
    max_dim = _resolve_dimensions(candidate)
    if max_dim is None:
        return base
    return base * (max_dim / REFERENCE_MAX_DIMENSION)


def get_master_voxel_size(quality: str, candidate=None) -> float:
    """Voxel size per il remesh del master (heal). Clip a 0.05 mm."""
    v = get_adaptive_voxel_size(quality, MASTER_QUALITY_MAP, candidate)
    return max(v, MIN_MASTER_VOXEL_SIZE)


def get_box_voxel_size(quality: str, candidate=None) -> float:
    """Voxel size per il remesh del box (wrapper). Clip a 0.5 mm."""
    v = get_adaptive_voxel_size(quality, BOX_QUALITY_MAP, candidate)
    return max(v, MIN_BOX_VOXEL_SIZE)
