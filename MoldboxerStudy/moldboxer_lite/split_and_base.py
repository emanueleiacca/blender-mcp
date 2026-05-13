"""
Split del mold in 2 metà + aggiunta della base e dei pin.
Ricostruisce la parte server-side di `/confirm-silicone-mold/`.

Componenti:
- split_box_on_y: taglia il box (= silicone_mold cavato) sul piano Y=0 in 2 metà.
- build_master_base_pin: pin maschio+femmina per centrare il master sulla base.
- add_basing_to_system: aggiunge la base piana sotto al box (oppure unisce il master).
- add_interlock_keys: piramidi tronche sulla superficie di split (qualità di chiusura).
"""

from __future__ import annotations
from typing import Optional, Tuple
import bpy
from mathutils import Vector, Matrix
from math import radians

from .object_wrapper import Object
from .constants import WING_WIDTH, BOX_THICKNESS
from .primitives import create_cube_primitive


# ---------------------------------------------------------------------------
# Split su asse Y (default Moldboxer)
# ---------------------------------------------------------------------------

def split_box_on_y(box: Object, gap: float = 0.001) -> Tuple[Object, Object]:
    """Taglia il box sul piano Y=0 in due metà. Restituisce (box_l, box_r) cioè
    (metà negativa di Y, metà positiva di Y).

    `gap`: micro-tolleranza in mm per evitare facce coincidenti.
    """
    neg, pos = box.split(plane_normal=Vector((0, 1, 0)), plane_point=Vector((0, 0, 0)), tolerance=gap)
    neg.name = "box_l"
    pos.name = "box_r"
    return neg, pos


# ---------------------------------------------------------------------------
# Pin master-base
# ---------------------------------------------------------------------------

def build_master_base_pin(base: Object, patron: Object) -> Tuple[Object, Object]:
    """Crea pin maschio+femmina per allineare patron sopra la base.
    Pattern Moldboxer: cubi di 3.5 e 3.7 mm rispettivamente, top-face scalata 0.7
    su X/Y (forma tronco di piramide). Restituisce (male, female).
    """
    SIZE_MALE = 3.5
    SIZE_FEMALE = 3.7
    TOP_SCALE = 0.7  # tronco di piramide
    Z_OFFSET = 0.5

    cx, cy = (base.min_x + base.max_x) / 2, (base.min_y + base.max_y) / 2

    male = _build_pin(SIZE_MALE, TOP_SCALE, location=(cx, cy, patron.min_z - Z_OFFSET))
    male.name = "base_pin_male"
    female = _build_pin(SIZE_FEMALE, TOP_SCALE, location=(cx, cy, patron.min_z - Z_OFFSET))
    female.name = "base_pin_female"
    return male, female


def _build_pin(base_size: float, top_scale: float, location) -> Object:
    """Crea un cubo size×size con la top-face scalata di top_scale (tronco piramide)."""
    cube = create_cube_primitive(size=base_size, location=location)
    obj = Object(cube)
    # Scala i 4 vertici "top" verso il centro lungo X e Y.
    from .object_wrapper import BMeshEdit
    z_max = max(v.co.z for v in cube.data.vertices)
    with BMeshEdit(cube) as bm:
        for v in bm.verts:
            if abs(v.co.z - z_max) < 1e-4:
                v.co.x *= top_scale
                v.co.y *= top_scale
    return obj


def pin_patron_to_base(base: Object, patron: Object, master_base_pin: bool = True) -> Object:
    """Aggiunge il pin maschio sulla base e sottrae il femmina dal patron.
    Restituisce la base modificata."""
    if not master_base_pin:
        return base
    male, female = build_master_base_pin(base, patron)
    patron -= female
    if patron.has_empty_boolean:
        raise RuntimeError("pin_patron_to_base: boolean female from patron failed (empty modifier)")
    base += male
    female.remove()
    male.remove()
    return base


# ---------------------------------------------------------------------------
# Base + wing (alettone) con testo volume
# ---------------------------------------------------------------------------

def add_basing_to_system(
    box: Object,
    patron: Optional[Object],
    volume_mm3: float,
    join_patron: bool = True,
    master_base_pin: bool = True,
    base_thickness: float = BOX_THICKNESS,
    wing_width: float = WING_WIDTH,
    add_volume_text: bool = True,
) -> Object:
    """Aggiunge una base piana sotto al box, opzionalmente joinando il patron.

    Args:
        box: il box mold (con cavità già scavata).
        patron: il master (necessario solo se join_patron o master_base_pin).
        volume_mm3: per scrivere il volume sul wing.
        join_patron: se True, il patron viene unito al base così che master e mold
                     siano un pezzo solo (modalità Fixed Master).
        master_base_pin: se True E join_patron=False, aggiunge pin di centratura.
        base_thickness: spessore della base (default = BOX_THICKNESS = 4 mm).
        wing_width: larghezza del wing laterale dove va il volume text.
        add_volume_text: se True, scrive il volume in ml sul wing.
    """
    # --- 1. Crea la base: cubo che copre l'intera footprint XY del box ---
    base_cx = (box.min_x + box.max_x) / 2
    base_cy = (box.min_y + box.max_y) / 2
    base_z = box.min_z - base_thickness / 2
    base_w = box.width + 2 * base_thickness
    base_d = box.depth + 2 * base_thickness

    # Bambu primitive_cube_add(size=N) creates a cube with side=N (verts at +/-N/2).
    # We want a unit cube with side=2 so the subsequent scale(dim/2) yields side=dim.
    base_cube = create_cube_primitive(size=2.0, location=(base_cx, base_cy, base_z))
    base = Object(base_cube, name="base")
    base.scale(base_w / 2.0, 0)
    base.scale(base_d / 2.0, 1)
    base.scale(base_thickness / 2.0, 2)
    base.apply_all_transforms()

    # --- 2. Pin / join patron ---
    if patron is not None:
        if join_patron:
            base += patron  # consuma il patron, fonde col base
        elif master_base_pin:
            pin_patron_to_base(base, patron, master_base_pin=True)

    # --- 3. Wing laterale (alettone +X per il volume text) ---
    if add_volume_text and wing_width > 0:
        # See base_cube comment: use size=2 unit cube so scale(dim/2) yields side=dim.
        wing_cube = create_cube_primitive(size=2.0)
        wing = Object(wing_cube, name="wing")
        wing.scale(wing_width / 2.0, 0)
        wing.scale(box.depth / 2.0, 1)
        wing.scale(base_thickness / 2.0, 2)
        wing.apply_all_transforms()
        wing.translate_whole(Vector((
            box.max_x + wing_width / 2,
            base_cy,
            base_z,
        )))
        wing.apply_all_transforms()

        # Aggiungi il testo del volume sul wing.
        from .silicone_mold import create_volume_text
        text = create_volume_text(volume_mm3, size=6.0)
        # Posiziona al centro del wing.
        text.translate_whole(Vector((
            wing.max_x - 12.0,
            base_cy,
            wing.max_z + 0.1,
        )))
        text.apply_all_transforms()
        wing += text
        text.remove()
        base += wing
        wing.remove()

    # --- 4. Unisci la base al box ---
    box += base
    base.remove()
    # NOTE: the original reconstruction called `box.clean_bot(2)` here as
    # "pulizia bordo basso", but `clean_bot(h)` in object_wrapper.py actually
    # KEEPS ONLY the top `h` mm of the mesh (cut from max_z-h upward),
    # which annihilates the whole mold (live-tested 2026-05-13 — left only
    # a 15.9x15.9x2mm sliver near the funneler top).
    # The base cube is already a clean rectangular slab, so no bottom cleanup
    # is needed. If a bevel is desired, use box.cut_bot(0.5) to shave the
    # bottom edge — never clean_bot in this context.
    return box


# ---------------------------------------------------------------------------
# Interlock keys sulla superficie di split (qualità chiusura)
# ---------------------------------------------------------------------------

def add_interlock_keys(
    box_l: Object,
    box_r: Object,
    key_count: int = 4,
    key_size: float = 4.0,
    key_tolerance: float = 0.2,
) -> Tuple[Object, Object]:
    """Aggiunge `key_count` piramidi tronche sulla superficie di split.
    Maschi su box_l (+chiave), femmine su box_r (−chiave + tolerance).

    Strategia:
      - Identifica il piano di split (Y=0).
      - Distribuisce N punti lungo l'asse X del box, a z = z_center.
      - Per ogni punto, crea un cubo di lato `key_size` centrato sulla split plane.
      - Box_l += key → maschio
      - Box_r -= key (scalato di key_tolerance) → femmina con clearance
    """
    # Bounding box combinata (le due metà condividono la stessa estensione X/Z).
    x_min = min(box_l.min_x, box_r.min_x)
    x_max = max(box_l.max_x, box_r.max_x)
    z_center = (min(box_l.min_z, box_r.min_z) + max(box_l.max_z, box_r.max_z)) / 2

    margin = key_size + 2.0
    if key_count < 2:
        positions = [(x_min + x_max) / 2]
    else:
        positions = [
            x_min + margin + i * (x_max - x_min - 2 * margin) / (key_count - 1)
            for i in range(key_count)
        ]

    for px in positions:
        # Maschio: cubo piccolo da unire a box_l.
        male = create_cube_primitive(size=key_size, location=(px, 0, z_center))
        male_obj = Object(male, name=f"key_m_{int(px)}")
        # Spostiamo il centro lungo Y così che il pin "sporga" da box_l (Y<0 → centro a Y = -key_size/4).
        male_obj.translate_whole(Vector((0, -key_size / 4, 0)))
        male_obj.apply_all_transforms()
        box_l += male_obj
        # Femmina: stessa forma ma con tolerance.
        female = create_cube_primitive(
            size=key_size + 2 * key_tolerance,
            location=(px, -key_size / 4, z_center),
        )
        female_obj = Object(female, name=f"key_f_{int(px)}")
        box_r -= female_obj
        male_obj.remove()
        female_obj.remove()

    return box_l, box_r
