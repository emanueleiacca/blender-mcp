"""
Classe `Object`: wrapper OO sopra `bpy.types.Object`.
Ricostruita da decompiled_py/object.py.

Decisioni di design:
- Boolean overload (__add__, __sub__, __and__) modifica self in-place e restituisce self,
  esattamente come fa Moldboxer. Permette idiomi tipo `box -= patron`.
- apply_modifier muove sempre il modifier in posizione 0 prima di applicarlo
  (Moldboxer fa così — l'ordine importa per i Boolean concatenati).
- Le proprietà geometriche (max_x, min_z, width, ecc.) leggono SEMPRE da bound_box
  trasformato per matrix_world, quindi sono valori world-space coerenti dopo
  rotazioni/scaling.
"""

from __future__ import annotations
from typing import List, Optional, Tuple
import bpy
import bmesh
import mathutils
from mathutils import Vector, Matrix

from .modifiers import (
    Modifier,
    diff_mod,
    intersect_mod,
    union_mod,
    build_voxel_modifier,
)


# ---------------------------------------------------------------------------
# Context manager per editing BMesh sicuro
# ---------------------------------------------------------------------------

class BMeshEdit:
    """Context manager: bm = BMeshEdit(obj). Apre bmesh.new() da mesh data,
    yield bm, poi bm.to_mesh() + bm.free()."""

    def __init__(self, obj: bpy.types.Object):
        self.obj = obj
        self.bm: Optional[bmesh.types.BMesh] = None

    def __enter__(self) -> bmesh.types.BMesh:
        self.bm = bmesh.new()
        self.bm.from_mesh(self.obj.data)
        self.bm.verts.ensure_lookup_table()
        self.bm.edges.ensure_lookup_table()
        self.bm.faces.ensure_lookup_table()
        self.bm.normal_update()
        return self.bm

    def __exit__(self, exc_type, exc, tb):
        if self.bm is not None and exc_type is None:
            self.bm.to_mesh(self.obj.data)
            self.obj.data.update()
        if self.bm is not None:
            self.bm.free()
        self.bm = None
        return False


# ---------------------------------------------------------------------------
# Classe Object
# ---------------------------------------------------------------------------

class Object:
    """Wrapper su un bpy_object. Mai None: il costruttore solleva se l'oggetto
    passato non esiste."""

    def __init__(self, blender_object: bpy.types.Object, name: Optional[str] = None):
        if blender_object is None:
            raise ValueError("Object() got None — wrap an existing bpy object")
        self.object = blender_object
        self._vertex_groups: dict = {}
        if name is not None:
            self.name = name  # usa il setter che dedupa

    # -------------------------------------------------------------------- name
    @property
    def name(self) -> str:
        return self.object.name

    @name.setter
    def name(self, value: str) -> None:
        # Se il nome è già preso da un altro oggetto, accoda un suffisso numerico.
        if value in bpy.data.objects and bpy.data.objects[value] is not self.object:
            i = 1
            while f"{value}{i}" in bpy.data.objects:
                i += 1
            value = f"{value}{i}"
        self.object.name = value

    # ------------------------------------------------------------- bound box
    @property
    def matrix_world(self) -> Matrix:
        return self.object.matrix_world

    @property
    def world_bound_box(self) -> List[Vector]:
        """8 corner del bound box trasformati in world space."""
        mw = self.matrix_world
        return [mw @ Vector(corner) for corner in self.object.bound_box]

    def _bound_axis(self, axis: int, fn) -> float:
        return fn(v[axis] for v in self.world_bound_box)

    @property
    def max_x(self) -> float: return self._bound_axis(0, max)
    @property
    def min_x(self) -> float: return self._bound_axis(0, min)
    @property
    def max_y(self) -> float: return self._bound_axis(1, max)
    @property
    def min_y(self) -> float: return self._bound_axis(1, min)
    @property
    def max_z(self) -> float: return self._bound_axis(2, max)
    @property
    def min_z(self) -> float: return self._bound_axis(2, min)

    @property
    def width(self) -> float: return self.max_x - self.min_x
    @property
    def depth(self) -> float: return self.max_y - self.min_y
    @property
    def height(self) -> float: return self.max_z - self.min_z

    @property
    def center_coords(self) -> Vector:
        b = self.world_bound_box
        return sum(b, Vector((0, 0, 0))) / 8

    @property
    def volume(self) -> float:
        """Volume con segno calcolato da bmesh (mm³)."""
        with BMeshEdit(self.object) as bm:
            return bm.calc_volume(signed=False)

    # -------------------------------------------------------- manifold/health
    def is_manifold(self) -> bool:
        with BMeshEdit(self.object) as bm:
            for e in bm.edges:
                if not e.is_manifold:
                    return False
            return True

    @property
    def has_empty_boolean(self) -> bool:
        """True se ha modificatori Boolean senza target valido. Li rimuove e
        ritorna True. Pattern Moldboxer per detect-and-clean."""
        removed = False
        for m in list(self.object.modifiers):
            if m.type == "BOOLEAN" and m.object is None:
                self.object.modifiers.remove(m)
                removed = True
        return removed

    # ------------------------------------------------------------- selection
    def select(self, active: bool = True) -> None:
        """Deseleziona tutto, poi seleziona questo oggetto come active."""
        bpy.ops.object.select_all(action="DESELECT")
        self.object.select_set(True)
        if active:
            bpy.context.view_layer.objects.active = self.object

    # --------------------------------------------------------- transform ops
    def apply_all_transforms(self) -> None:
        self.select()
        bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)

    def geometry_to_origin(self) -> None:
        self.select()
        bpy.ops.object.origin_set(type="GEOMETRY_ORIGIN", center="BOUNDS")

    def origin_to_geometry(self) -> None:
        self.select()
        bpy.ops.object.origin_set(type="ORIGIN_GEOMETRY", center="BOUNDS")

    def origin_to_cursor(self) -> None:
        self.select()
        bpy.ops.object.origin_set(type="ORIGIN_CURSOR")

    def translate_whole(self, vector) -> "Object":
        self.object.location = self.object.location + Vector(vector)
        return self

    def rotate_whole(self, rotation_matrix: Matrix, center: Vector = Vector((0, 0, 0))) -> "Object":
        # Ruota la mesh attorno al centro dato, in world space.
        mw = self.object.matrix_world.copy()
        translate_to_origin = Matrix.Translation(-center)
        translate_back = Matrix.Translation(center)
        rot4 = rotation_matrix.to_4x4() if rotation_matrix.row[0].to_tuple().__len__() == 3 else rotation_matrix
        self.object.matrix_world = translate_back @ rot4 @ translate_to_origin @ mw
        return self

    def scale(self, factor: float, axis: int) -> "Object":
        """Scala la mesh su un singolo asse (0=X, 1=Y, 2=Z) in object space."""
        axis_vec = Vector((1, 0, 0)) if axis == 0 else Vector((0, 1, 0)) if axis == 1 else Vector((0, 0, 1))
        with BMeshEdit(self.object) as bm:
            bmesh.ops.scale(bm, vec=Vector((
                factor if axis == 0 else 1,
                factor if axis == 1 else 1,
                factor if axis == 2 else 1,
            )), verts=bm.verts)
        return self

    def scale_uniform(self, factor: float) -> "Object":
        with BMeshEdit(self.object) as bm:
            bmesh.ops.scale(bm, vec=Vector((factor, factor, factor)), verts=bm.verts)
        return self

    def scale_to(self, size: float, axis: int) -> "Object":
        """Scala UNIFORMEMENTE finché la dimensione su `axis` è `size`."""
        current = (self.width, self.depth, self.height)[axis]
        if current <= 0:
            return self
        f = size / current
        return self.scale_uniform(f)

    def scale_normals(self, offset: float) -> "Object":
        """Espande la mesh outward muovendo ogni vertice lungo la sua normale
        di `offset` mm. Usato da Wrapper come "inflate" del master."""
        with BMeshEdit(self.object) as bm:
            for v in bm.verts:
                v.co = v.co + v.normal * offset
        return self

    # -------------------------------------------------------------- modifier
    def add_modifier(
        self,
        modifier: Modifier,
        target: Optional[bpy.types.Object] = None,
        index_first: bool = True,
        show_viewport: bool = True,
    ) -> bpy.types.Modifier:
        m = self.object.modifiers.new(name=modifier.display_name(), type=modifier.name)
        for prop, value in modifier.properties.items():
            if value is None:
                continue
            try:
                setattr(m, prop, value)
            except (AttributeError, TypeError):
                # Property non valida per questo tipo di modifier: ignora.
                pass
        if target is not None and hasattr(m, "object"):
            m.object = target
        if hasattr(m, "show_viewport"):
            m.show_viewport = show_viewport
        if index_first:
            self._move_modifier_to_top(m)
        return m

    def _move_modifier_to_top(self, m: bpy.types.Modifier) -> None:
        # Su Blender 4.x usa modifiers.move(from_index, 0).
        mods = self.object.modifiers
        if mods[0] is m:
            return
        try:
            from_idx = list(mods).index(m)
            mods.move(from_idx, 0)
        except Exception:
            # Fallback API: bpy.ops.object.modifier_move_to_index
            self.select()
            try:
                bpy.ops.object.modifier_move_to_index(modifier=m.name, index=0)
            except Exception:
                pass

    def apply_modifier(self, modifier: Modifier, target: Optional[bpy.types.Object] = None) -> "Object":
        m = self.add_modifier(modifier, target=target, index_first=True)
        self.select()
        bpy.ops.object.modifier_apply(modifier=m.name)
        return self

    def apply_all_modifiers(self) -> "Object":
        self.select()
        for m in list(self.object.modifiers):
            try:
                bpy.ops.object.modifier_apply(modifier=m.name)
            except RuntimeError:
                # Modifier non applicabile (es. multires su mesh vuota) — skip.
                pass
        return self

    # ------------------------------------------------------ boolean overload
    def _boolean_with(self, other: "Object", mod_factory) -> "Object":
        if not isinstance(other, Object):
            other = Object(other)
        self.apply_modifier(mod_factory(), target=other.object)
        return self

    def __add__(self, other: "Object") -> "Object":
        """Union: self ∪ other → self."""
        return self._boolean_with(other, union_mod)

    def __sub__(self, other: "Object") -> "Object":
        """Difference: self − other → self."""
        return self._boolean_with(other, diff_mod)

    def __and__(self, other: "Object") -> "Object":
        """Intersection: self ∩ other → self."""
        return self._boolean_with(other, intersect_mod)

    # ----------------------------------------------------------- duplicate/remove
    def duplicate(self, name_adder: str = "") -> "Object":
        self.select()
        bpy.ops.object.duplicate()
        new_obj = bpy.context.view_layer.objects.active
        if name_adder:
            new_obj.name = self.name + name_adder
        return Object(new_obj)

    def remove(self) -> None:
        bpy.data.objects.remove(self.object, do_unlink=True)

    # ------------------------------------------------------------- face ops
    def get_limit_face_idx(self, axis: int = 2, max_co: bool = True, flat: bool = False) -> Optional[int]:
        """Trova la faccia con baricentro estremo lungo `axis`. Se `flat=True`,
        filtra solo le facce con normale ~allineata all'asse (|cos| > 0.99)."""
        with BMeshEdit(self.object) as bm:
            best_idx: Optional[int] = None
            best_co: Optional[float] = None
            for f in bm.faces:
                if flat:
                    n = f.normal
                    if abs(n[axis]) < 0.99:
                        continue
                    if (max_co and n[axis] < 0.99) or ((not max_co) and n[axis] > -0.99):
                        continue
                center = f.calc_center_median()[axis]
                if best_co is None:
                    best_idx, best_co = f.index, center
                elif max_co and center > best_co:
                    best_idx, best_co = f.index, center
                elif (not max_co) and center < best_co:
                    best_idx, best_co = f.index, center
            return best_idx

    def cut_plane(self, plane_normal: Vector, plane_point: Vector) -> "Object":
        """Taglia self con un piano: tutto ciò che è sul lato della normale
        viene rimosso. Implementato come Boolean DIFFERENCE con un cubo grande."""
        from .primitives import create_cube_primitive
        max_size = max(self.width, self.depth, self.height) * 10 + 100
        cube = create_cube_primitive(size=max_size)
        cube_obj = Object(cube)
        # Posiziona il cubo: il suo bottom-face deve combaciare con plane_point,
        # con normale orientata come plane_normal.
        # Approccio semplice: trasla così che il centro del cubo sia spostato lungo
        # +plane_normal di (max_size/2) dal plane_point, poi ruota per allinearsi.
        n = Vector(plane_normal).normalized()
        cube_obj.translate_whole(Vector(plane_point) + n * (max_size / 2))
        # Ruota il cubo per allineare il suo asse +Z (default top normal) con n.
        z_axis = Vector((0, 0, 1))
        if (n - z_axis).length > 1e-6:
            quat = z_axis.rotation_difference(n)
            cube_obj.object.rotation_mode = "QUATERNION"
            cube_obj.object.rotation_quaternion = quat
            cube_obj.apply_all_transforms()
        self._boolean_with(cube_obj, diff_mod)
        cube_obj.remove()
        return self

    def split(self, plane_normal: Vector, plane_point: Vector, tolerance: float = 0.001) -> Tuple["Object", "Object"]:
        """Divide self in due metà tagliate da un piano. Restituisce (negative_side, positive_side).
        Lascia un piccolo gap `tolerance` per evitare facce coincidenti."""
        n = Vector(plane_normal).normalized()
        neg_side = self.duplicate(name_adder="_neg")
        pos_side = self.duplicate(name_adder="_pos")
        self.remove()
        # neg_side: rimuove il lato positivo (taglia con normale +n, offset -tolerance)
        neg_side.cut_plane(n, Vector(plane_point) + n * tolerance)
        # pos_side: rimuove il lato negativo (taglia con normale -n, offset +tolerance)
        pos_side.cut_plane(-n, Vector(plane_point) - n * tolerance)
        return neg_side, pos_side

    # ------------------------------------------------ clean top/bot helpers
    def clean_top(self, height: float) -> "Object":
        """Rimuove tutto sopra Z = min_z + height. Equivalente a un cut su asse +Z."""
        return self.cut_plane(Vector((0, 0, 1)), Vector((0, 0, self.min_z + height)))

    def clean_bot(self, height: float) -> "Object":
        """Rimuove tutto sotto Z = max_z - height (cioè tiene solo gli ultimi `height` mm dall'alto)."""
        return self.cut_plane(Vector((0, 0, -1)), Vector((0, 0, self.max_z - height)))

    def cut_bot(self, height: float) -> "Object":
        """Taglia tutto sotto min_z + height (livella il fondo)."""
        return self.cut_plane(Vector((0, 0, -1)), Vector((0, 0, self.min_z + height)))

    def clean_all_top(self) -> "Object":
        """Rimuove tutto eccetto un sottile strato basale (height - 0.1)."""
        return self.clean_top(self.height - 0.1)

    # ---------------------------------------------------------------- grid
    def grid_obj(self, rows: int, columns: int, distance: float) -> "Object":
        """Duplica con array X+Y. Distance = spazio tra i bordi di copie adiacenti."""
        from .modifiers import build_array_modifier
        # Array X: spazia di width + distance.
        array_x = build_array_modifier(columns, [self.width + distance, 0, 0])
        self.apply_modifier(array_x)
        # Array Y: dopo aver applicato X, depth è la stessa.
        array_y = build_array_modifier(rows, [0, self.depth + distance, 0])
        self.apply_modifier(array_y)
        return self
