"""
Helper per creare mesh primitive in Blender.
Ricostruito da decompiled_py/primitives.py.

Tutti restituiscono un `bpy.types.Object` con la mesh appena creata.
Il pattern è: confronta `bpy.context.scene.objects` prima e dopo il
`bpy.ops.mesh.primitive_*_add` per identificare il nuovo oggetto.

Usiamo `bpy.ops` invece di costruire la mesh da zero perché:
1. Moldboxer fa esattamente così (compatibilità di comportamento).
2. Gli operator nativi gestiscono già UV, normals, ecc.
"""

from __future__ import annotations
import bpy


def _capture_new_object(op_func, **kwargs) -> bpy.types.Object:
    """Esegue un operatore di primitive e restituisce l'oggetto creato."""
    before = set(bpy.context.scene.objects)
    op_func(**kwargs)
    after = set(bpy.context.scene.objects)
    new_objs = list(after - before)
    if not new_objs:
        # Fallback: il nuovo oggetto potrebbe non essere ancora linkato — prova active
        active = bpy.context.view_layer.objects.active
        if active is not None and active not in before:
            return active
        raise RuntimeError(f"primitive op {op_func.__name__} did not create a new object")
    return new_objs[0]


def create_cube_primitive(size: float = 1.0, location=(0.0, 0.0, 0.0)) -> bpy.types.Object:
    return _capture_new_object(bpy.ops.mesh.primitive_cube_add, size=size, location=location)


def create_cylinder_primitive(radius: float, height: float, location=(0.0, 0.0, 0.0), vertices: int = 32) -> bpy.types.Object:
    return _capture_new_object(
        bpy.ops.mesh.primitive_cylinder_add,
        radius=radius,
        depth=height,
        location=location,
        vertices=vertices,
    )


def create_circle_primitive(radius: float, location=(0.0, 0.0, 0.0), vertices: int = 32) -> bpy.types.Object:
    return _capture_new_object(
        bpy.ops.mesh.primitive_circle_add,
        radius=radius,
        location=location,
        vertices=vertices,
        fill_type="NGON",
    )


def create_plane_primitive(size: float = 2.0, location=(0.0, 0.0, 0.0)) -> bpy.types.Object:
    return _capture_new_object(bpy.ops.mesh.primitive_plane_add, size=size, location=location)


def create_uv_sphere_primitive(radius: float, location=(0.0, 0.0, 0.0), segments: int = 32, ring_count: int = 16) -> bpy.types.Object:
    return _capture_new_object(
        bpy.ops.mesh.primitive_uv_sphere_add,
        radius=radius,
        location=location,
        segments=segments,
        ring_count=ring_count,
    )


def create_text_object(
    text: str,
    size: float,
    location=(0.0, 0.0, 0.0),
    extrude_height: float = 20.0,
) -> bpy.types.Object:
    """Testo 3D estruso — usato per scrivere il volume del silicone sul box."""
    before = set(bpy.context.scene.objects)
    bpy.ops.object.text_add(location=location)
    after = set(bpy.context.scene.objects)
    new_obj = next(iter(after - before), None)
    if new_obj is None:
        raise RuntimeError("text_add did not create a new object")
    new_obj.data.body = text
    new_obj.data.size = size
    new_obj.data.extrude = extrude_height / 2.0
    return new_obj
