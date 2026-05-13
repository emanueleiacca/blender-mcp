"""
moldboxer_lite — Ricostruzione client-side delle funzionalità Moldboxer 1.4.9.

NON è un clone del prodotto. È una libreria didattica per:
1. Studiare l'architettura del prodotto originale.
2. Disporre di tool atomici componibili in Blender (per un MCP o uso diretto).
3. Riprodurre i flussi auto_flat / auto_box / confirm senza dipendere dal backend
   server.moldboxer.com.

Tutte le costanti, formule e default sono presi 1:1 dal codice decompilato
(decompiled_py/* e decompiled/*) del bundle Moldboxer per Blender 5.0.

Esempio d'uso (in Blender 4.2+):

    from moldboxer_lite import preprocess_patron, auto_box, confirm_mold, export_all_parts

    # 1. Importa STL e preprocessa.
    import bpy
    bpy.ops.import_mesh.stl(filepath="/path/to/master.stl")
    patron = preprocess_patron(master_quality="HIGH")

    # 2. Genera box automatico.
    box = auto_box(patron, box_gap=4.5, box_quality="MID")

    # 3. Finalizza con split, base, keys.
    parts = confirm_mold(patron, box, n_splits=2, add_keys=True)

    # 4. Esporta tutti i pezzi.
    export_all_parts("/tmp/mold_parts/")
"""

# Versione della libreria di ricostruzione. NON è la versione di Moldboxer.
__version__ = "0.1.0"

# API pubblica — ciò che dovrebbe essere esposto come tool MCP.
from .object_wrapper import Object
from .wrapper import Wrapper
from .preprocess import preprocess_patron, configure_metric_millimeter_units, heal_mesh, center_to_origin
from .auto_flat import auto_flat
from .auto_box import auto_box
from .confirm import confirm_mold
from .silicone_mold import build_silicone_mold_preview, place_volume_text
from .split_and_base import split_box_on_y, add_basing_to_system, add_interlock_keys
from .export import export_all_parts
from .voxel_size import get_box_voxel_size, get_master_voxel_size

__all__ = [
    "__version__",
    "Object",
    "Wrapper",
    "preprocess_patron",
    "configure_metric_millimeter_units",
    "heal_mesh",
    "center_to_origin",
    "auto_flat",
    "auto_box",
    "confirm_mold",
    "build_silicone_mold_preview",
    "place_volume_text",
    "split_box_on_y",
    "add_basing_to_system",
    "add_interlock_keys",
    "export_all_parts",
    "get_box_voxel_size",
    "get_master_voxel_size",
]
