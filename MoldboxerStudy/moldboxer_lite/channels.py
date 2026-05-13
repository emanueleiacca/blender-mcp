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


# Parametri di tuning empirici. Da affinare visualmente confrontando con screenshot Moldboxer.
CHANNEL_SPACING_FACTOR = 30.0      # mm: spaziatura target tra canali sui lati lunghi
LARGER_BACK_RADIUS_FACTOR = 1.3    # ↑ raggio canale posteriore quando larger_back=True
FUNNELER_RADIUS = 8.0              # mm: raggio del funneler/deposit
FUNNELER_INSET = 0.5               # mm: quanto il funneler "affonda" nel box


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
        adjust_to_contour: se True, i cilindri seguono il contorno del box (snapping).
                          NB: la versione "vera" del server fa proiezione raycast.
                          Qui implementiamo una versione semplificata: i cilindri sono
                          posizionati sulla mediana XZ del box, ma il box li "abbraccia"
                          grazie al boolean union.
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
        if side_idx == 0:
            side_center = side_co + depth_offset  # interno verso +Y dal lato min
        else:
            side_center = side_co - depth_offset  # interno verso -Y dal lato max

        for p in positions:
            loc = [0.0, 0.0, z_center]
            loc[long_axis] = p
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


def build_clamp_pins(box: Object, split_axis: int = 1) -> Tuple[Object, Object]:
    """Pin di allineamento tra le due metà del box, sull'asse di split.
    Si posizionano sui lati lunghi a 1/3 e 2/3 del box. Restituisce due Object cilindrici.

    Logica:
      - asse del pin = split_axis (passa attraverso il piano di taglio)
      - posizione lungo il lato lungo = box_long/3 e 2*box_long/3
      - raggio = ~2 mm (Moldboxer hardcoded), altezza = box.depth o box.width + 6
    """
    pin_radius = 2.0
    if split_axis == 1:
        long_min, long_max = box.min_x, box.max_x
        long_axis = 0
        pin_len_axis_co = box.depth + 6.0
    else:
        long_min, long_max = box.min_y, box.max_y
        long_axis = 1
        pin_len_axis_co = box.width + 6.0

    z_center = (box.min_z + box.max_z) / 2.0
    long_len = long_max - long_min
    third = long_min + long_len / 3.0
    two_third = long_min + 2 * long_len / 3.0

    pins = []
    for p in [third, two_third]:
        loc = [0.0, 0.0, z_center]
        loc[long_axis] = p
        # Pin "in piedi" lungo split_axis: usiamo un cilindro orientato di default su Z
        # e poi lo ruoteremo applicando alle trasformazioni.
        cyl = create_cylinder_primitive(radius=pin_radius, height=pin_len_axis_co, location=tuple(loc), vertices=16)
        obj = Object(cyl, name=f"clamp_pin_{int(p)}")
        # Ruota 90° per allinearsi a split_axis.
        from mathutils import Matrix
        from math import radians
        if split_axis == 1:
            # Cilindro verticale → orizzontale su Y. Rotazione attorno a X di 90°.
            rot = Matrix.Rotation(radians(90), 4, "X")
        else:
            # → orizzontale su X. Rotazione attorno a Y di 90°.
            rot = Matrix.Rotation(radians(90), 4, "Y")
        obj.object.matrix_world = rot @ obj.object.matrix_world
        obj.apply_all_transforms()
        pins.append(obj)
    return pins[0], pins[1]
