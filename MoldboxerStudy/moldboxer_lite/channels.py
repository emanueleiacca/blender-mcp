"""
Generazione canali strutturali sui lati del box.
Sostituisce la parte server di `/auto-box/` e `/channels-deposit/` relativa
ai canali e al funneler (deposit).

Cosa sono i canali:
- Cilindri verticali sui lati Y- e Y+ del box (perché lo split è su Y).
- Servono a 1) supporto da capovolto, 2) rinforzo silicone sottile, 3) flusso colata.
- `adjust_to_contour=True`: i cilindri vengono "snappati" al profilo del master.
- `larger_back=True`: il canale sul lato Y+ è più grande.

Cosa è il funneler (deposit):
- Cilindro verticale al centro del top, foro per colata silicone.
"""

from __future__ import annotations
from typing import List, Tuple
import bpy
from mathutils import Vector

from .object_wrapper import Object
from .primitives import create_cylinder_primitive


# Parametri di tuning empirici. Da affinare visualmente confrontando con screenshot
# Moldboxer originale (vedi `screen video tutorial/`). I valori sotto sono educated
# guesses basati sui frame del video del gallo, NON estratti dal bytecode.
CHANNEL_SPACING_FACTOR = 30.0      # mm: spaziatura target tra canali sui lati lunghi.
                                    # n_channels = max(2, round(side_len / SPACING) + 1).
                                    # Valore tipico Moldboxer: 25–35 mm.
LARGER_BACK_RADIUS_FACTOR = 1.3    # raggio canale posteriore (+Y) × questo fattore
                                    # quando larger_back=True. Il canale posteriore è
                                    # più grande perché lì il silicone defluisce dopo
                                    # essere stato versato dal funneler frontale/centrale.
FUNNELER_RADIUS = 8.0              # mm: raggio del foro funneler (= imboccatura colata).
                                    # Diametro 16 mm = compatibile con beccuccio standard
                                    # tubetti silicone industriali.
FUNNELER_INSET = 0.5               # mm: il cilindro funneler è centrato leggermente
                                    # sotto box.max_z così sporge solo per la differenza
                                    # (box.height + 10 - 0.5). Dopo il `box -= dep` il
                                    # foro attraversa la parete top fino alla cavità.


def _raycast_contour_y(box: Object, x_pos: float, z: float, side_idx: int) -> float:
    """Raycast contro la superficie del box per trovare la Y effettiva del contorno.

    Sparato da (x_pos, ±box.max_y, z) verso il centro Y=0. Restituisce la Y del
    primo hit (= il bordo esterno del box in quella posizione X). Se il box è
    rettangolare la Y ritornata == box.min_y o box.max_y; se il box è un wrapper
    aderente al master, la Y "rientra" verso il centro nelle zone strette.

    Args:
        box: l'oggetto box su cui raycast.
        x_pos: posizione X del cilindro candidato.
        z: quota Z del raycast (== centro verticale).
        side_idx: 0 = lato -Y (origine raycast a +Y_far), 1 = lato +Y.

    Returns:
        Y del primo hit in world space, oppure box.min_y/max_y se nessun hit
        (fallback: lato del bbox).
    """
    import bpy
    from mathutils import Vector
    if side_idx == 0:
        origin_y = box.max_y + 10.0  # far side
        fallback = box.min_y
    else:
        origin_y = box.min_y - 10.0
        fallback = box.max_y
    origin = Vector((x_pos, origin_y, z))
    direction = Vector((0.0, 1.0 if side_idx == 0 else -1.0, 0.0))
    mat_inv = box.object.matrix_world.inverted()
    local_origin = mat_inv @ origin
    local_dir = (mat_inv.to_3x3() @ direction).normalized()
    hit, loc, normal, idx = box.object.ray_cast(local_origin, local_dir)
    if not hit:
        return fallback
    return (box.object.matrix_world @ loc).y


def build_channels(
    box: Object,
    channel_width: float = 5.0,
    channel_depth: float = 6.0,
    adjust_to_contour: bool = True,
    larger_back: bool = True,
    split_axis: int = 1,
) -> List[Object]:
    """Crea i cilindri "canale" sui lati del box.

    Args:
        box: il box wrapper già esistente in scena.
        channel_width: diametro del canale (mm).
        channel_depth: distanza dal centro del cilindro alla superficie esterna del box.
        adjust_to_contour: se True, ogni cilindro viene snappato al contorno reale
            del box via raycast. Utile su wrapper aderenti al master (silhouette
            non rettangolare): i canali "rientrano" nelle zone strette invece di
            sospendere nel vuoto al di fuori della parete. FIX 2026-05-13: prima
            era ignorato (versione "uniforme" sul bbox).
        larger_back: il canale sul lato +Y è più grande.
        split_axis: asse di split (0=X, 1=Y, default Y). I canali stanno sui lati di quest'asse.

    Returns:
        Lista degli Object channel creati (già in scena, non ancora uniti al box).
    """
    radius = channel_width / 2.0

    # Lato lungo del box = quello opposto al split axis sul piano XY.
    # split_axis=1 (Y) → i canali stanno sui lati Y- e Y+, distribuiti lungo X.
    if split_axis == 1:
        long_axis = 0  # X
        long_min, long_max = box.min_x, box.max_x
        side_axis = 1  # Y
        side_neg = box.min_y
        side_pos = box.max_y
    elif split_axis == 0:
        long_axis = 1  # Y
        long_min, long_max = box.min_y, box.max_y
        side_axis = 0
        side_neg = box.min_x
        side_pos = box.max_x
    else:
        raise ValueError(f"split_axis must be 0 (X) or 1 (Y), got {split_axis}")

    long_len = long_max - long_min
    z_center = (box.min_z + box.max_z) / 2.0
    height = box.height + 4.0  # un po' più alto del box, verrà clippato dal boolean

    # Quanti canali per lato. Almeno 2 (uno a ogni estremità del lato).
    n_channels = max(2, int(round(long_len / CHANNEL_SPACING_FACTOR)) + 1)
    # Distribuzione equispaziata lungo l'asse "long".
    margins = radius + 2.0  # non mettere canali troppo vicini agli spigoli
    if n_channels == 2:
        positions = [long_min + margins, long_max - margins]
    else:
        positions = [
            long_min + margins + i * (long_len - 2 * margins) / (n_channels - 1)
            for i in range(n_channels)
        ]

    channels: List[Object] = []
    for side_idx, side_co in enumerate([side_neg, side_pos]):
        is_back = (side_idx == 1)  # +Y è il lato "back" convenzionale
        r = radius * (LARGER_BACK_RADIUS_FACTOR if (is_back and larger_back) else 1.0)
        # Posizione del centro del cilindro lungo l'asse laterale:
        # vogliamo che il cilindro sia "annegato" nel box di `channel_depth - r`
        # così la parete esterna del cilindro dista `r + (channel_depth - r) = channel_depth`
        # dalla superficie esterna del box.
        depth_offset = channel_depth - r

        for p in positions:
            loc = [0.0, 0.0, z_center]
            loc[long_axis] = p
            # Adjust to contour via raycast (solo se split_axis=1, i.e. canali lungo Y)
            if adjust_to_contour and split_axis == 1:
                actual_side_co = _raycast_contour_y(box, p, z_center, side_idx)
            else:
                actual_side_co = side_co
            if side_idx == 0:
                side_center = actual_side_co + depth_offset
            else:
                side_center = actual_side_co - depth_offset
            loc[side_axis] = side_center
            cyl = create_cylinder_primitive(radius=r, height=height, location=tuple(loc), vertices=24)
            obj = Object(cyl, name=f"channel_{side_idx}_{int(p)}")
            channels.append(obj)

    return channels


def build_funneler(box: Object, radius: float = FUNNELER_RADIUS) -> Object:
    """Crea il cilindro funneler (deposit) per la colata.
    Posizionato al centro XY del top del box, alto abbastanza da bucarlo passante."""
    cx = (box.min_x + box.max_x) / 2.0
    cy = (box.min_y + box.max_y) / 2.0
    height = box.height + 10.0
    z_center = box.max_z - FUNNELER_INSET
    cyl = create_cylinder_primitive(
        radius=radius,
        height=height,
        location=(cx, cy, z_center),
        vertices=32,
    )
    return Object(cyl, name="deposit")


# NOTE: a previous version of this module had a `build_clamp_pins(box, split_axis)`
# function that generated cylindrical pins running ALONG the split axis through the
# whole box. It was never called from auto_box / confirm. The "Clamp Pin" feature
# toggle in the Moldboxer UI is actually materialized by `add_interlock_keys` in
# split_and_base.py (truncated-pyramid keys on the split surface), not by axis-
# parallel through-pins. Removed 2026-05-13 to avoid confusion. If you need
# through-the-box clamping bolts (a different concept), implement it as a separate
# helper and wire it explicitly in confirm.py.
