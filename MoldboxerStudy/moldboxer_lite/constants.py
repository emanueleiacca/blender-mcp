"""
Constants ricostruite dal codice Moldboxer 1.4.9.

Valori presi 1:1 da decompiled_py/constants.py — non sono creati ex novo,
sono stati estratti dal bytecode dell'add-on.

Unità: tutto in millimetri (la scena Blender è configurata con scale_length=0.001).
"""

VERSION = "1.4.9-lite-reconstruction"

# --- Geometria box ---
BOX_THICKNESS = 4.0                       # spessore di parete del box (mm)
WING_WIDTH = 15.0                         # larghezza dell'ala laterale dove va il testo volume

# --- Clamps (alette di chiusura tra le due metà) ---
CLAMP_WIDTH_DIFF_WITH_CHANNELS = 1.5      # quanto più largo il clamp rispetto ai canali
CLAMP_DEPTH = 8.0                         # profondità dei clamps

# --- Split connector (utility "Split with Connector") ---
SPLIT_CONNECTOR_LENGTH = 5.0
SPLIT_CONNECTOR_WIDTH = 10.0

# --- Voxel quality maps ---
# Mappa dal nome del preset all'unità base di voxel (mm).
# La voxel size effettiva è scalata in funzione della dimensione max del modello
# (vedi voxel_size.get_adaptive_voxel_size).
BOX_QUALITY_MAP = {
    "FAST": 2.0,
    "MID": 1.6,
    "HIGH": 1.2,
    "ULTRA": 0.8,
}

MASTER_QUALITY_MAP = {
    "FAST": 0.3,
    "MID": 0.2,
    "HIGH": 0.15,
    "ULTRA": 0.1,
}

# --- Scaling adattivo voxel ---
REFERENCE_MAX_DIMENSION = 150.0           # mm: dimensione "tipica" di un master
MIN_BOX_VOXEL_SIZE = 0.5                  # mm: floor sotto cui non scendiamo per il box
MIN_MASTER_VOXEL_SIZE = 0.05              # mm: floor per il master

# --- Solver boolean ---
# Moldboxer usa 'MANIFOLD'. Su Blender < 4.2 ricadi su 'EXACT'.
DEFAULT_BOOLEAN_SOLVER = "MANIFOLD"
FALLBACK_BOOLEAN_SOLVER = "EXACT"

# --- Default scene properties (replicano i defaults dell'addon) ---
# Riprodotti da moldboxer_silicone/properties.py.
DEFAULT_SCENE = {
    # quality
    "master_quality": "HIGH",
    "box_quality": "MID",
    "master_voxel_size": 0.15,
    # box geometry
    "box_gap": 4.5,                       # silicone thickness (mm)
    "wing_join_patron": True,             # fixed master
    "funneler": True,
    "clamp_pins": True,
    "build_from_sphere": False,           # safe mode
    "clear_extraction": True,
    "master_base_pin": True,
    # channels
    "channel_width": 5.0,
    "channel_depth": 6.0,
    "channel_adjust_to_contour": True,
    "channel_back_larger": True,
    # split
    "n_splits": 2,
    # casting input (utility)
    "casting_input_h": 5.0,
    "casting_input_diameter": 5.0,
    "casting_input_axis": "NEG_Z",
}
