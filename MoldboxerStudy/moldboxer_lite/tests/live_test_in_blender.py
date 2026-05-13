"""
Live test da eseguire DENTRO Blender (4.2+).

Come usarlo:
  - Apri Blender.
  - Apri il Text Editor.
  - Apri questo file e premi "Run Script" (Alt+P).

OPPURE via MCP:
  - exec_blender_code con questo file come `code`.

Crea un master di prova (Suzanne), lo preprocessa, e prova auto_flat + auto_box.
Verifica che ogni funzione non sollevi eccezioni e produca oggetti col nome
atteso (`patron`, `box`, `silicone_mold`, `box_l`, `box_r`).
"""

import sys
import pathlib

# Aggiungi la cartella moldboxer_lite/.. al path.
HERE = pathlib.Path(__file__).resolve()
PARENT = HERE.parent.parent.parent
if str(PARENT) not in sys.path:
    sys.path.insert(0, str(PARENT))

import bpy

# Resetta scena pulita.
bpy.ops.wm.read_factory_settings(use_empty=True)

from moldboxer_lite import (
    Object,
    preprocess_patron,
    auto_flat,
    auto_box,
    confirm_mold,
    configure_metric_millimeter_units,
)
from moldboxer_lite.voxel_size import get_box_voxel_size


def _add_suzanne(scale=30.0):
    """Aggiunge una Suzanne come master di test, scalata a ~60mm di larghezza."""
    bpy.ops.mesh.primitive_monkey_add(size=2.0)
    obj = bpy.context.view_layer.objects.active
    obj.scale = (scale, scale, scale)
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    return obj


def test_preprocess():
    print("\n[TEST] preprocess_patron on a fresh Suzanne master")
    suzanne = _add_suzanne()
    bpy.context.view_layer.objects.active = suzanne
    patron = preprocess_patron(target=Object(suzanne), master_quality="HIGH", center=True)
    assert patron.name == "patron", f"name = {patron.name}"
    # Dopo center: min_z deve essere ~0 e centro XY ~0.
    assert abs(patron.min_z) < 0.5, f"min_z = {patron.min_z}"
    print(f"  patron: w={patron.width:.1f} d={patron.depth:.1f} h={patron.height:.1f} mm, min_z={patron.min_z:.2f}")
    return patron


def test_voxel_sizing(patron):
    print("\n[TEST] voxel sizing")
    v_box = get_box_voxel_size("MID", patron)
    print(f"  box voxel (MID, size={max(patron.width, patron.depth, patron.height):.0f}mm) = {v_box:.3f} mm")


def test_auto_flat(patron):
    print("\n[TEST] auto_flat")
    box = auto_flat(patron, box_gap=4.5, box_quality="MID", grip_height=10.0)
    print(f"  flat box: w={box.width:.1f} d={box.depth:.1f} h={box.height:.1f} mm, vol={box.volume/1000:.1f} ml")
    return box


def test_auto_box_pipeline():
    print("\n[TEST] auto_box + confirm pipeline")
    # Scena pulita per il secondo test.
    bpy.ops.wm.read_factory_settings(use_empty=True)
    configure_metric_millimeter_units()
    suzanne = _add_suzanne()
    bpy.context.view_layer.objects.active = suzanne
    patron = preprocess_patron(target=Object(suzanne), master_quality="HIGH", center=True)

    box = auto_box(
        patron,
        box_gap=4.5,
        box_quality="MID",
        channel_width=5.0,
        channel_depth=6.0,
        adjust_to_contour=False,  # versione semplice
        larger_back=True,
        funneler=True,
    )
    print(f"  auto box: w={box.width:.1f} d={box.depth:.1f} h={box.height:.1f} mm")

    parts = confirm_mold(
        patron,
        box,
        join_patron=True,
        master_base_pin=False,
        n_splits=2,
        add_keys=True,
        key_count=3,
    )
    print(f"  confirm done: volume={parts['volume_mm3']/1000:.1f} ml")
    print(f"    box_l: {parts['box_l'].name if parts['box_l'] else None}")
    print(f"    box_r: {parts['box_r'].name if parts['box_r'] else None}")
    print(f"    silicone_mold: {parts['silicone_mold'].name if parts['silicone_mold'] else None}")


def main():
    print("=" * 60)
    print("moldboxer_lite live test in Blender")
    print(f"Blender: {bpy.app.version_string}")
    print("=" * 60)
    configure_metric_millimeter_units()

    patron = test_preprocess()
    test_voxel_sizing(patron)
    test_auto_flat(patron)
    test_auto_box_pipeline()

    print("\nDONE — controlla la viewport per ispezione visiva.")


main()
