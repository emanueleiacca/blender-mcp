"""
Smoke test stdlib-only: importa l'intero pacchetto moldboxer_lite con stub di bpy/bmesh.

NON esegue alcuna logica geometrica (Blender non è in esecuzione). Il punto è
assicurarsi che:
1. Tutti i moduli si caricano senza errori di sintassi/import.
2. Le API pubbliche siano esposte come attesi.
3. Non ci siano riferimenti a simboli inesistenti negli stub di Blender API.

Lancialo con:
    python test_import_smoke.py
"""

from __future__ import annotations
import sys
import types
import pathlib


# ----------------------------------------------------------------------
# 1. Costruisci stub minimi di bpy / bmesh / mathutils per permettere l'import
# ----------------------------------------------------------------------

def _build_stubs():
    # mathutils (forniamo Vector + Matrix con il minimo necessario per import)
    mathutils = types.ModuleType("mathutils")

    class _V:
        def __init__(self, t=(0, 0, 0)):
            self._t = tuple(float(x) for x in t)
        def __getitem__(self, i): return self._t[i]
        def __iter__(self): return iter(self._t)
        @property
        def x(self): return self._t[0]
        @property
        def y(self): return self._t[1]
        @property
        def z(self): return self._t[2]
        def __add__(self, o): return _V((self._t[0]+o._t[0], self._t[1]+o._t[1], self._t[2]+o._t[2]))
        def __sub__(self, o): return _V((self._t[0]-o._t[0], self._t[1]-o._t[1], self._t[2]-o._t[2]))
        def __mul__(self, s): return _V((self._t[0]*s, self._t[1]*s, self._t[2]*s))
        __rmul__ = __mul__
        def __truediv__(self, s): return _V((self._t[0]/s, self._t[1]/s, self._t[2]/s))
        def __neg__(self): return _V((-self._t[0], -self._t[1], -self._t[2]))
        @property
        def length(self):
            return (self._t[0]**2 + self._t[1]**2 + self._t[2]**2) ** 0.5
        def normalized(self):
            l = self.length
            return _V((self._t[0]/l, self._t[1]/l, self._t[2]/l)) if l else _V((0,0,0))
        def rotation_difference(self, o): return _Quat()
        def cross(self, o): return _V((0,0,0))
        def dot(self, o): return 0.0

    class _Quat:
        pass

    class _M:
        @staticmethod
        def Scale(*args, **kwargs): return _M()
        @staticmethod
        def Rotation(*args, **kwargs): return _M()
        @staticmethod
        def Translation(v): return _M()
        @staticmethod
        def Identity(n): return _M()
        def to_4x4(self): return self
        def __matmul__(self, o): return _M()
        def copy(self): return _M()
        row = [_V()]

    mathutils.Vector = _V
    mathutils.Matrix = _M

    # bpy
    bpy = types.ModuleType("bpy")
    bpy.app = types.SimpleNamespace(version_string="stub", version=(0, 0, 0))
    bpy.data = types.SimpleNamespace(objects={})
    bpy.context = types.SimpleNamespace(
        scene=types.SimpleNamespace(
            unit_settings=types.SimpleNamespace(
                system="METRIC", scale_length=0.001, length_unit="MILLIMETERS",
            ),
            objects=[],
        ),
        view_layer=types.SimpleNamespace(objects=types.SimpleNamespace(active=None)),
        window=None,
        active_object=None,
    )
    bpy.path = types.SimpleNamespace(abspath=lambda p: p)
    bpy.ops = types.SimpleNamespace(
        object=types.SimpleNamespace(
            select_all=lambda **k: None,
            origin_set=lambda **k: None,
            transform_apply=lambda **k: None,
            duplicate=lambda **k: None,
            modifier_apply=lambda **k: None,
            modifier_move_to_index=lambda **k: None,
            join=lambda **k: None,
            text_add=lambda **k: None,
        ),
        mesh=types.SimpleNamespace(
            primitive_cube_add=lambda **k: None,
            primitive_cylinder_add=lambda **k: None,
            primitive_circle_add=lambda **k: None,
            primitive_plane_add=lambda **k: None,
            primitive_uv_sphere_add=lambda **k: None,
            separate=lambda **k: None,
        ),
        wm=types.SimpleNamespace(stl_export=lambda **k: None),
        export_mesh=types.SimpleNamespace(stl=lambda **k: None),
    )
    bpy.types = types.SimpleNamespace(Object=type("Object", (), {}), Modifier=type("Modifier", (), {}))

    # bmesh
    bmesh = types.ModuleType("bmesh")
    bmesh.new = lambda: types.SimpleNamespace(
        from_mesh=lambda m: None,
        to_mesh=lambda m: None,
        free=lambda: None,
        verts=types.SimpleNamespace(ensure_lookup_table=lambda: None),
        edges=types.SimpleNamespace(ensure_lookup_table=lambda: None),
        faces=types.SimpleNamespace(ensure_lookup_table=lambda: None),
        normal_update=lambda: None,
        calc_volume=lambda signed=False: 1000.0,
    )
    bmesh.types = types.SimpleNamespace(BMesh=type("BMesh", (), {}))
    bmesh.ops = types.SimpleNamespace(scale=lambda *a, **k: None)

    sys.modules["bpy"] = bpy
    sys.modules["bmesh"] = bmesh
    sys.modules["mathutils"] = mathutils


def main():
    _build_stubs()

    # Aggiungi la cartella parent al path così possiamo importare il package.
    here = pathlib.Path(__file__).resolve()
    parent = here.parent.parent.parent
    sys.path.insert(0, str(parent))

    print("Stub di bpy/bmesh/mathutils installati.")
    print("Importo moldboxer_lite...")
    import moldboxer_lite

    print(f"  moldboxer_lite v{moldboxer_lite.__version__}")
    expected = {
        "Object", "Wrapper", "preprocess_patron", "auto_flat", "auto_box",
        "confirm_mold", "build_silicone_mold_preview", "split_box_on_y",
        "add_basing_to_system", "add_interlock_keys", "export_all_parts",
        "get_box_voxel_size", "get_master_voxel_size",
    }
    actual = set(moldboxer_lite.__all__)
    missing = expected - actual
    extra = actual - expected
    if missing:
        print(f"  ERR: missing exports: {missing}")
        return 1
    print(f"  OK: tutte le {len(expected)} API pubbliche esposte (+{len(extra)} extra).")

    # Test che le costanti siano caricate.
    from moldboxer_lite.constants import BOX_QUALITY_MAP, MASTER_QUALITY_MAP, WING_WIDTH, BOX_THICKNESS
    assert BOX_QUALITY_MAP == {"FAST": 2.0, "MID": 1.6, "HIGH": 1.2, "ULTRA": 0.8}, "BOX_QUALITY_MAP mismatch"
    assert MASTER_QUALITY_MAP == {"FAST": 0.3, "MID": 0.2, "HIGH": 0.15, "ULTRA": 0.1}, "MASTER_QUALITY_MAP mismatch"
    assert WING_WIDTH == 15.0
    assert BOX_THICKNESS == 4.0
    print("  OK: costanti Moldboxer caricate correttamente.")

    # Test voxel_size con un fake object.
    from moldboxer_lite.voxel_size import get_box_voxel_size, get_master_voxel_size
    class _FakeObj:
        width = 100.0
        depth = 100.0
        height = 100.0
    v = get_box_voxel_size("HIGH", _FakeObj())
    expected_v = 1.2 * (100.0 / 150.0)
    assert abs(v - max(expected_v, 0.5)) < 1e-9, f"voxel calc mismatch: {v}"
    print(f"  OK: get_box_voxel_size('HIGH', 100mm) = {v:.4f} mm (clipped a 0.5)")

    m = get_master_voxel_size("ULTRA", _FakeObj())
    expected_m = 0.1 * (100.0 / 150.0)
    assert abs(m - max(expected_m, 0.05)) < 1e-9, f"master voxel mismatch: {m}"
    print(f"  OK: get_master_voxel_size('ULTRA', 100mm) = {m:.4f} mm")

    print("\nSMOKE TEST PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
