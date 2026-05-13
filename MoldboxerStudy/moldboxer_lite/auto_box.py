"""
Ricostruzione client-side di `silicone.auto_box` (sostituisce POST /auto-box/).

Genera un mold a 2 metà con:
- Box wrapper aderente al master (offset di `box_gap`).
- Canali strutturali sui lati.
- Funneler (deposit) sul top per la colata.
- Pin di allineamento clamps tra le due metà.

Pipeline:
  1. Wrapper(patron, voxel_size, distance=box_gap, ...) → box
  2. Aggiungi channels (build_channels) → box += channel
  3. Aggiungi funneler → box += deposit
  4. Sottrai patron dal box → cavità interna (silicone_mold)
  5. (più tardi, in confirm) split su Y + base + pins
"""

from __future__ import annotations
from typing import Optional
import bpy
from mathutils import Vector

from .object_wrapper import Object
from .wrapper import Wrapper
from .voxel_size import get_box_voxel_size
from .modifiers import build_voxel_modifier
from .channels import build_channels, build_funneler


def auto_box(
    patron: Object,
    box_gap: float = 4.5,
    box_quality: str = "MID",
    channel_width: float = 5.0,
    channel_depth: float = 6.0,
    adjust_to_contour: bool = True,
    larger_back: bool = True,
    funneler: bool = True,
    safe_mode: bool = False,
) -> Object:
    """Costruisce il box "Automatic Box" senza chiamare il server.

    Restituisce l'Object 'box' (mold rigido a 2 metà, prima dello split).
    NB: lo split + base + pins è fatto da `confirm.confirm_mold()`.
    """
    voxel = get_box_voxel_size(box_quality, patron)

    # --- 1. Box wrapper aderente al master ---
    box = Wrapper(
        target=patron,
        voxel_size=voxel,
        distance=box_gap,
        decimate=True,
        n_wraps=3,
        cut_bot=True,
        build_from_sphere=safe_mode,
        target_shrinkwrap=True,  # importante: spinge i vertici verso il master a distanza box_gap
    )

    # --- 2. Aggiungi canali sui lati ---
    channels = build_channels(
        box=box,
        channel_width=channel_width,
        channel_depth=channel_depth,
        adjust_to_contour=adjust_to_contour,
        larger_back=larger_back,
        split_axis=1,  # split su Y
    )
    for ch in channels:
        box += ch
        ch.remove()

    # --- 3. Funneler / deposit: foro PASSANTE nella parete superiore ---
    # IMPORTANTE: il funneler è un foro per versare silicone, NON una colonna piena.
    # Il tutorial (02:43) dice esplicitamente "an opening where the silicone is poured".
    # FIX 2026-05-13: era erroneamente "box += dep" (univa il cilindro come colonna piena
    # sopra al box). Ora è "box -= dep" (sottrazione = buco). Il cilindro generato da
    # build_funneler è lungo box.height + 10 mm, quindi attraversa completamente la
    # parete superiore e arriva fino alla cavità interna del patron — il silicone
    # versato dall'imboccatura scende fino al top del master e riempie il gap laterale.
    if funneler:
        dep = build_funneler(box)
        box -= dep
        dep.remove()

    # --- 4. Voxel di pulizia dopo i boolean (DISABILITATO) ---
    # Era un voxel-remesh finale dopo le boolean union dei canali + funneler.
    # In pratica degrada il dettaglio (Wrapper.shape già fa 3 voxel passes con
    # decimate(0.3)) e arrotonda gli spigoli del funneler / dei canali.
    # Riattivabile solo se servono cleanup di residui boolean visibili.
    # if voxel > 0:
    #     box.apply_modifier(build_voxel_modifier(voxel))

    # --- 5. Sottrai il patron per creare la cavità interna ---
    # Lavoriamo su una copia per non distruggere il patron.
    patron_copy = patron.duplicate(name_adder="_for_cavity")
    box -= patron_copy
    patron_copy.remove()

    return box
