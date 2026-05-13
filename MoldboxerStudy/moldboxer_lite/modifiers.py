"""
Factory di modificatori Blender, ricostruito da decompiled_py/modifiers.py.

Ogni `Modifier` è un dict dichiarativo {name, properties}. La classe `Object`
(in object_wrapper.py) sa applicarli copiando le properties su un modifier
appena aggiunto allo stack.

Default presi 1:1 dal bytecode Moldboxer.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any, Dict

from .constants import DEFAULT_BOOLEAN_SOLVER


@dataclass
class Modifier:
    name: str                                         # tipo Blender: "BOOLEAN", "REMESH", ecc.
    properties: Dict[str, Any] = field(default_factory=dict)

    def display_name(self) -> str:
        """Etichetta breve usata come nome del modifier nello stack."""
        return self.name.lower()


# ---------------------------------------------------------------------------
# Boolean
# ---------------------------------------------------------------------------

def _boolean(op: str, solver: str = DEFAULT_BOOLEAN_SOLVER) -> Modifier:
    return Modifier(
        name="BOOLEAN",
        properties={"operation": op, "solver": solver},
    )


def diff_mod(solver: str = DEFAULT_BOOLEAN_SOLVER) -> Modifier:
    return _boolean("DIFFERENCE", solver)


def union_mod(solver: str = DEFAULT_BOOLEAN_SOLVER) -> Modifier:
    return _boolean("UNION", solver)


def intersect_mod(solver: str = DEFAULT_BOOLEAN_SOLVER) -> Modifier:
    return _boolean("INTERSECT", solver)


# ---------------------------------------------------------------------------
# Remesh / voxel
# ---------------------------------------------------------------------------

def build_voxel_modifier(voxel_size: float = 0.2, smooth_shading: bool = False, adaptivity: float = 0.0) -> Modifier:
    """Remesh in modalità VOXEL — quello che Moldboxer usa per costruire il wrapper.
    `voxel_size` è in mm (Blender lo legge in metri ma noi lavoriamo in scale_length=0.001)."""
    return Modifier(
        name="REMESH",
        properties={
            "mode": "VOXEL",
            "voxel_size": voxel_size,
            "use_smooth_shade": smooth_shading,
            "adaptivity": adaptivity,
        },
    )


def build_sharp_modifier(octree_depth: int = 8) -> Modifier:
    """Remesh SHARP — usato dal splitter per ridurre disconnessioni."""
    return Modifier(
        name="REMESH",
        properties={
            "mode": "SHARP",
            "octree_depth": octree_depth,
            "use_remove_disconnected": False,
        },
    )


# ---------------------------------------------------------------------------
# Decimate
# ---------------------------------------------------------------------------

def build_decimate_collapse(ratio: float = 0.2) -> Modifier:
    return Modifier(
        name="DECIMATE",
        properties={"decimate_type": "COLLAPSE", "ratio": ratio},
    )


def build_decimate_planar(degrees: float) -> Modifier:
    """DISSOLVE: fonde facce coplanari entro `degrees`."""
    from math import radians
    return Modifier(
        name="DECIMATE",
        properties={
            "decimate_type": "DISSOLVE",
            "angle_limit": radians(degrees),
            "delimit": {"NORMAL"},
        },
    )


# ---------------------------------------------------------------------------
# Shrinkwrap (Moldboxer usa SHRINKWRAP per "shape" il box sul master)
# ---------------------------------------------------------------------------

def build_wrap_modifier(distance: float = 0.1, target=None) -> Modifier:
    return Modifier(
        name="SHRINKWRAP",
        properties={
            "wrap_method": "NEAREST_SURFACEPOINT",
            "offset": distance,
            "target": target,
        },
    )


def build_inside_wrap_modifier(distance: float = 1.0, target=None) -> Modifier:
    return Modifier(
        name="SHRINKWRAP",
        properties={
            "wrap_method": "NEAREST_SURFACEPOINT",
            "wrap_mode": "INSIDE",
            "offset": distance,
            "target": target,
        },
    )


def shrink_mod_outside(offset: float = 6.0, target=None) -> Modifier:
    """Shrinkwrap "outside" — il pattern Moldboxer per gonfiare il wrapper verso il master."""
    return Modifier(
        name="SHRINKWRAP",
        properties={
            "wrap_method": "NEAREST_SURFACEPOINT",
            "wrap_mode": "OUTSIDE",
            "offset": offset,
            "target": target,
        },
    )


# ---------------------------------------------------------------------------
# Array
# ---------------------------------------------------------------------------

def build_array_modifier(n_copies: int, distance) -> Modifier:
    """`distance`: lista o tuple di 3 float (mm per asse)."""
    if len(distance) != 3:
        raise ValueError(f"Array distance must have 3 components, got {len(distance)}")
    return Modifier(
        name="ARRAY",
        properties={
            "fit_type": "FIXED_COUNT",
            "count": n_copies,
            "use_relative_offset": False,
            "use_constant_offset": True,
            "constant_offset_displace": tuple(distance),
            "use_merge_vertices": True,
        },
    )


# ---------------------------------------------------------------------------
# Subsurf (raramente usato in Moldboxer ma utile)
# ---------------------------------------------------------------------------

def build_subdivide_modifier(levels: int = 3, subdivision_type: str = "CATMULL_CLARK") -> Modifier:
    return Modifier(
        name="SUBSURF",
        properties={"levels": levels, "render_levels": levels, "subdivision_type": subdivision_type},
    )
