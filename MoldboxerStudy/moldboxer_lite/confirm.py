"""
Ricostruzione client-side di `silicone.confirm` (sostituisce POST /confirm-silicone-mold/).

Flusso completo del confirm:
  1. Ricava il volume del silicone (silicone_mold = box - patron).
  2. Aggiunge base + wing + volume text + pin master (opzionale).
  3. Split del box in 2 metà sull'asse Y.
  4. Aggiunge interlock keys sulla superficie di split.
  5. Distanzia i 3 oggetti finali (patron, mold, silicone_preview).

Questa è la combinazione delle operazioni che il server fa in /confirm-silicone-mold/.
"""

from __future__ import annotations
from typing import Optional, Tuple
import bpy
from mathutils import Vector

from .object_wrapper import Object
from .silicone_mold import build_silicone_mold_preview
from .split_and_base import add_basing_to_system, split_box_on_y, add_interlock_keys


def confirm_mold(
    patron: Object,
    box: Object,
    join_patron: bool = True,
    master_base_pin: bool = True,
    n_splits: int = 2,
    add_keys: bool = True,
    key_count: int = 4,
    key_size: float = 4.0,
    key_tolerance: float = 0.2,
    voxel_size: float = 0.8,
    space_objects: bool = True,
) -> dict:
    """Finalizza il mold. Restituisce un dict con riferimenti agli oggetti generati.

    Args:
        patron: il master preprocessato.
        box: il box mold (già con cavità scavata, prodotto da auto_box).
        join_patron: Fixed Master mode — master e base diventano un unico pezzo.
        master_base_pin: aggiungi pin di centratura master sulla base (solo se join_patron=False).
        n_splits: 0 (nessuno split) o 2 (split su Y).
        add_keys: se True, aggiungi interlock keys sulla superficie di split.
        key_count, key_size, key_tolerance: parametri delle keys.
        voxel_size: pulizia voxel finale.
        space_objects: se True, sposta gli oggetti nello spazio per visualizzazione (Moldboxer fa così).

    Returns:
        {"box": Object | None, "box_l": Object | None, "box_r": Object | None,
         "silicone_mold": Object | None, "patron": Object, "volume_mm3": float}
    """
    # --- 1. Calcola volume del silicone ---
    volume_mm3 = build_silicone_mold_preview(patron, box, voxel_size=voxel_size)

    # --- 2. Base + wing + volume text + pin master ---
    box = add_basing_to_system(
        box=box,
        patron=patron if (join_patron or master_base_pin) else None,
        volume_mm3=volume_mm3,
        join_patron=join_patron,
        master_base_pin=master_base_pin,
        add_volume_text=True,
    )

    result = {
        "box": None,
        "box_l": None,
        "box_r": None,
        "silicone_mold": bpy.data.objects.get("silicone_mold"),
        "patron": patron if not join_patron else None,
        "volume_mm3": volume_mm3,
    }

    # --- 3. Split su Y ---
    if n_splits == 2:
        box_l, box_r = split_box_on_y(box)
        if add_keys:
            box_l, box_r = add_interlock_keys(
                box_l, box_r,
                key_count=key_count,
                key_size=key_size,
                key_tolerance=key_tolerance,
            )
        result["box_l"] = box_l
        result["box_r"] = box_r
    else:
        result["box"] = box

    # --- 4. Spaziatura visiva ---
    if space_objects:
        space_mold_system(result)

    return result


def space_mold_system(parts: dict) -> None:
    """Sposta i pezzi finali per visualizzazione 3-up:
      - patron a sinistra (X-),
      - mold al centro,
      - silicone preview a destra (X+).
    Replica di space_mold_system (decompiled).
    """
    box = parts.get("box") or parts.get("box_l")
    if box is None:
        return
    sil = parts.get("silicone_mold")
    pat = parts.get("patron")

    box_width = box.width if hasattr(box, "width") else 100.0

    if sil is not None:
        sil_obj = Object(sil)
        sil_obj.translate_whole(Vector((box_width + sil_obj.width / 2 + 20, 0, 0)))

    if pat is not None:
        pat.translate_whole(Vector((-box_width - pat.width / 2 - 20, 0, 0)))
