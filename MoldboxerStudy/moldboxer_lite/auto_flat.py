"""
Ricostruzione client-side di `silicone.flat_auto_box` (sostituisce POST /auto-flat/).

Cosa fa:
- Genera un mold piatto a UN pezzo con top completamente aperto e un grip laterale.
- Adatto per master corti o piatti che si demoldano "tirando" il silicone fuori dall'alto.

Differenze rispetto al server originale:
- Il server probabilmente usa logica più sofisticata per il fitting al profilo XY.
  Qui usiamo un footprint rettangolare allargato di `box_gap` su tutti i lati.
- Niente "intelligenza" sul posizionamento del grip — viene messo a +X.
"""

from __future__ import annotations
import bpy
from mathutils import Vector

from .object_wrapper import Object
from .constants import BOX_THICKNESS
from .voxel_size import get_box_voxel_size
from .modifiers import build_voxel_modifier
from .primitives import create_cube_primitive


def auto_flat(
    patron: Object,
    box_gap: float = 4.5,
    box_quality: str = "MID",
    grip_height: float = 10.0,
    open_top_margin: float = 2.0,
    add_volume_text: bool = False,
) -> Object:
    """Genera il mold flat. Restituisce l'oggetto `box` finale.

    Args:
        patron: il master già preprocessato (Object).
        box_gap: spessore silicone in mm (Moldboxer default 4.5).
        box_quality: FAST/MID/HIGH/ULTRA — controlla la voxel_size.
        grip_height: altezza del grip in mm.
        open_top_margin: quanto del top viene tagliato per lasciare l'apertura.
        add_volume_text: se True, scrive il volume in ml sul lato.
    """
    voxel = get_box_voxel_size(box_quality, patron)

    # --- 1. Box rettangolare attorno al footprint XY del patron ---
    bbox_min = Vector((patron.min_x, patron.min_y, patron.min_z))
    bbox_max = Vector((patron.max_x, patron.max_y, patron.max_z))

    # Dimensioni interne del box = bbox + box_gap su X/Y, + box_gap solo su Z+.
    inner_w = (bbox_max.x - bbox_min.x) + 2 * box_gap
    inner_d = (bbox_max.y - bbox_min.y) + 2 * box_gap
    inner_h = (bbox_max.z - bbox_min.z) + box_gap  # solo top
    # Outer = inner + 2*box_thickness su X/Y, + box_thickness su Z-.
    outer_w = inner_w + 2 * BOX_THICKNESS
    outer_d = inner_d + 2 * BOX_THICKNESS
    outer_h = inner_h + BOX_THICKNESS

    # Centro X/Y del box = centro del patron.
    cx = (bbox_min.x + bbox_max.x) / 2
    cy = (bbox_min.y + bbox_max.y) / 2
    cz_bottom = bbox_min.z - BOX_THICKNESS
    cz_center = cz_bottom + outer_h / 2

    # primitive_cube_add(size=N) creates a cube with side=N. We want a unit cube
    # with side=2 so that scale(dim/2.0) yields the desired final side=dim.
    box_cube = create_cube_primitive(size=2.0, location=(cx, cy, cz_center))
    box = Object(box_cube, name="box")
    box.scale(outer_w / 2.0, 0)
    box.scale(outer_d / 2.0, 1)
    box.scale(outer_h / 2.0, 2)
    box.apply_all_transforms()

    # --- 2. Cavità interna = patron + offset box_gap, sottratto dal box ---
    # Approccio semplice e robusto: usa un cubo interno alle dimensioni interne.
    inner_cube = create_cube_primitive(
        size=2.0,
        location=(cx, cy, bbox_min.z + inner_h / 2),
    )
    inner = Object(inner_cube, name="_inner_cavity")
    inner.scale(inner_w / 2.0, 0)
    inner.scale(inner_d / 2.0, 1)
    inner.scale(inner_h / 2.0, 2)
    inner.apply_all_transforms()

    # --- 3. Sottrai il patron così da preservare il dettaglio del master ---
    # Strategia: sottrai prima la cavità rettangolare (semplifica), poi sottrai il patron stesso.
    box -= inner

    # Sottrai il patron — questa è la cavità "fine" che lascia l'impronta del master.
    box -= patron

    # --- 4. Apri il top: taglia tutto sopra (top_z - open_top_margin) ---
    # Equivale al "Clean All Top" — lascia solo i lati e il fondo.
    top_z = box.max_z
    box.cut_plane(Vector((0, 0, 1)), Vector((0, 0, top_z - open_top_margin)))

    # --- 5. Aggiungi grip su +X ---
    grip = _build_side_grip(box, height=grip_height)
    box += grip
    grip.remove()  # già unito, rimuovi l'oggetto temporaneo

    # --- 6. Voxel finale per pulire i risultati boolean ---
    if voxel > 0:
        box.apply_modifier(build_voxel_modifier(voxel))

    # --- 7. Volume text opzionale ---
    if add_volume_text:
        from .silicone_mold import build_silicone_mold_preview, place_volume_text
        vol = build_silicone_mold_preview(patron, box, voxel_size=voxel)
        place_volume_text(box, vol, side="X+")

    return box


def _build_side_grip(box: Object, height: float) -> Object:
    """Costruisce un grip cubico sul lato +X del box.
    Pattern Moldboxer: cubo di lato `height`, allineato col top del box,
    spostato fuori dal box di ~20mm."""
    grip_cube = create_cube_primitive(size=1.0)
    grip = Object(grip_cube, name="grip")
    # Scala al lato `height`.
    grip.scale(height / 2.0, 0)
    grip.scale(height / 2.0, 1)
    grip.scale(height / 2.0, 2)
    grip.apply_all_transforms()
    # Posiziona: top del grip allineato col top del box, X = box.max_x + height/2.
    grip.translate_whole(Vector((
        box.max_x + height / 2 - grip.width / 2,
        (box.min_y + box.max_y) / 2,
        box.max_z - grip.height / 2,
    )))
    grip.apply_all_transforms()
    return grip
