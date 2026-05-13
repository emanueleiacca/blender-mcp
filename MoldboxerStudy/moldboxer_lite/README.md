# moldboxer_lite — libreria di ricostruzione

Libreria Python per Blender che ricostruisce client-side i flussi principali
del prodotto Moldboxer 1.4.9 (vedi `../moldboxer_silicone/` e `../decompiled_py/`).

**Non è un clone del prodotto.** È materiale di studio + tool atomici componibili,
pensati per essere esposti a un MCP che istruisce un LLM a usare Blender.

---

## Cosa contiene

```
moldboxer_lite/
├── __init__.py               API pubblica (import top-level)
├── constants.py              Costanti hardcoded di Moldboxer (BOX_QUALITY_MAP, WING_WIDTH, …)
├── modifiers.py              Factory di modificatori Blender (voxel, decimate, boolean, …)
├── primitives.py             Helper cube/cylinder/sphere/text
├── voxel_size.py             Scaling adattivo della voxel size in base alle dimensioni master
├── object_wrapper.py         Classe `Object` con 30+ metodi mesh + overload boolean (+, -, &)
├── preprocess.py             preprocess_patron: heal + center + units
├── wrapper.py                Classe `Wrapper(Object)`: costruisce il box che avvolge il master
├── silicone_mold.py          Volume silicone preview + testo volume in ml
├── channels.py               Generazione canali + funneler + clamp pins
├── auto_flat.py              Sostituto di POST /auto-flat/
├── auto_box.py               Sostituto di POST /auto-box/
├── split_and_base.py         Split su Y + base + pin master + interlock keys
├── confirm.py                Sostituto di POST /confirm-silicone-mold/
├── export.py                 Export STL multi-oggetto con volume nel filename
└── tests/
    ├── test_import_smoke.py  Smoke test stdlib-only (bpy stubbato)
    └── live_test_in_blender.py  Test live da eseguire dentro Blender
```

---

## Mapping con il prodotto originale

| Funzione Moldboxer (UI) | Operatore | Endpoint server | Libreria offline |
|---|---|---|---|
| Automatic Box | `silicone.auto_box` | `POST /auto-box/` | `auto_box.auto_box()` |
| Flat Automatic Box | `silicone.flat_auto_box` | `POST /auto-flat/` | `auto_flat.auto_flat()` |
| Build Box (advanced) | `silicone.build_box` | `POST /channels-deposit/` | `wrapper.Wrapper()` + `channels.build_channels()` |
| Confirm (advanced) | `silicone.confirm` | `POST /confirm-silicone-mold/` | `confirm.confirm_mold()` |
| Heal | `silicone.heal_patron` | (locale) | `preprocess.heal_mesh()` |
| Center | `silicone.center_obj` | (locale) | `preprocess.center_to_origin()` |
| Scale Z | `silicone.scale_height` | (locale) | `Object.scale_to(size, 2)` |
| Decimate | `silicone.decimate` | (locale) | `Object.apply_modifier(build_decimate_collapse(f))` |
| Clean Top/Bot, Cut Bot | varie | (locale) | `Object.clean_top()` / `.clean_bot()` / `.cut_bot()` |
| Grid | `silicone.grid` | (locale) | `Object.grid_obj()` |
| Export STL | `silicone.export_stl` | (locale) | `export.export_all_parts()` |
| Inner cavity (Pro) | — | `POST /inner-core/` | **non ricostruito** (vedi RECONSTRUCTION.md §3.5) |
| 2-Part Silicone (Pro) | — | mix di server | **parzialmente** (manca la logica di server) |

---

## Uso base in Blender

```python
import bpy, sys
sys.path.insert(0, "C:/Users/emanu/Desktop/MoldboxerStudy")

from moldboxer_lite import (
    preprocess_patron, auto_box, confirm_mold, export_all_parts,
    configure_metric_millimeter_units, Object,
)

# 1. Setup unità mm.
configure_metric_millimeter_units()

# 2. Importa STL del master.
bpy.ops.wm.stl_import(filepath="C:/Users/emanu/Desktop/some_master.stl")
patron = preprocess_patron(master_quality="HIGH", center=True)

# 3. Genera mold automatico.
box = auto_box(
    patron,
    box_gap=4.5,
    box_quality="MID",
    channel_width=5.0,
    channel_depth=6.0,
    funneler=True,
    larger_back=True,
)

# 4. Finalizza (split, base, keys).
parts = confirm_mold(
    patron, box,
    join_patron=True,            # Fixed Master mode
    n_splits=2,                  # 2 metà
    add_keys=True,
    key_count=3,
)
print(f"Volume silicone: {parts['volume_mm3']/1000:.1f} ml")

# 5. Esporta tutti i pezzi.
export_all_parts("C:/Users/emanu/Desktop/mold_parts/")
```

---

## Stato di completamento

| Componente | Stato | Note |
|---|---|---|
| Foundations (Object, modifiers, primitives, voxel_size) | ✅ Sintassi OK, smoke test passa | Riproduce 1:1 il codice decompilato |
| Wrapper class | ✅ Sintassi OK | Usa scale_normals + voxel n_wraps. La versione "vera" potrebbe usare shrinkwrap intermedio |
| Preprocess | ✅ Sintassi OK | Logica isolate semplificata rispetto all'originale |
| auto_flat | ✅ Sintassi OK | Versione "stupida" basata su bbox rettangolare. Il server originale fa fitting più aggressivo |
| auto_box | ✅ Sintassi OK | Canali in posizioni equispaziate (no contour-adapt vero). Funneler centrato. Tuning empirico |
| confirm | ✅ Sintassi OK | Split Y + base + interlock keys cubiche (no piramidali). Da rifinire visualmente |
| export | ✅ Sintassi OK | Compatibile Blender 3.x e 4.x |
| inner_cavity (Pro) | ❌ Non implementato | Vedi RECONSTRUCTION.md §3.5 |
| 2-part silicone (Pro) | ❌ Non implementato | Workflow complesso, server-dipendente |

**Validazione**: smoke test stdlib-only passa (`python tests/test_import_smoke.py`).
**Live test**: `tests/live_test_in_blender.py` da eseguire dentro Blender quando MCP attivo.

---

## Costanti hardcoded estratte da Moldboxer

Tutte presi 1:1 da `decompiled_py/constants.py`. **Non sono invenzioni**, sono i
valori esatti che gira il prodotto.

| Costante | Valore | Significato |
|---|---|---|
| `BOX_THICKNESS` | 4.0 mm | Spessore parete box |
| `WING_WIDTH` | 15.0 mm | Larghezza alettone con volume text |
| `BOX_QUALITY_MAP` | {FAST: 2, MID: 1.6, HIGH: 1.2, ULTRA: 0.8} | Base voxel size per box |
| `MASTER_QUALITY_MAP` | {FAST: 0.3, MID: 0.2, HIGH: 0.15, ULTRA: 0.1} | Base voxel size per master |
| `REFERENCE_MAX_DIMENSION` | 150.0 mm | Dimensione master di riferimento per scaling |
| `MIN_BOX_VOXEL_SIZE` | 0.5 mm | Floor voxel box |
| `MIN_MASTER_VOXEL_SIZE` | 0.05 mm | Floor voxel master |

Formula voxel adattivo: `voxel = base[quality] * (max_dim / 150)` con clip ai min.

---

## Costanti TUNATE EMPIRICAMENTE (non in Moldboxer)

Questi sono valori che ho dovuto scegliere io, perché il server originale li
calcola internamente senza esporli. Andrebbero affinati confrontando l'output
visivo con gli screenshot del video tutorial.

In `channels.py`:
| Costante | Valore | Funzione |
|---|---|---|
| `CHANNEL_SPACING_FACTOR` | 30.0 mm | Spaziatura target tra canali |
| `LARGER_BACK_RADIUS_FACTOR` | 1.3 | Moltiplicatore raggio canale +Y |
| `FUNNELER_RADIUS` | 8.0 mm | Raggio del deposit |
| `FUNNELER_INSET` | 0.5 mm | Quanto il funneler affonda nel box |

In `split_and_base.py`:
| Costante | Valore | Funzione |
|---|---|---|
| Pin master `SIZE_MALE` | 3.5 | Cubo maschio (esatto Moldboxer) |
| Pin master `SIZE_FEMALE` | 3.7 | Cubo femmina (esatto Moldboxer) |
| Pin `TOP_SCALE` | 0.7 | Scaling top per tronco piramide (esatto Moldboxer) |
| `Z_OFFSET` | 0.5 mm | Offset Z del pin sotto patron (esatto Moldboxer) |

---

## Limiti noti

1. **Canali non contour-adapted**: la versione `adjust_to_contour=True` nel codice originale
   probabilmente fa una raycast del cilindro contro il profilo del master per snappare la
   posizione laterale. Qui i canali sono distribuiti uniformemente lungo X. Per rendere il
   risultato più simile a Moldboxer servirebbe un passo aggiuntivo: per ogni cilindro,
   raycast da `(x_pos, y_extremo, z_center)` verso il centro fino a colpire il box, e
   spostare il cilindro al punto di contatto.

2. **Interlock keys cubiche, non piramidali**: il codice originale usa piramidi tronche
   (vedi `_build_pin` con `TOP_SCALE=0.7` in `split_and_base.py`). Le mie keys sono cubi
   semplici. Da migliorare riusando `_build_pin` con dimensioni più grandi.

3. **clear_extraction non implementato**: il flag `clear_extraction` nel codice originale
   apre canali nella direzione di split per evitare undercut bloccanti. Qui è omesso.
   Implementazione futura: vedi `decompiled_py/components/extraction.py` per la ricetta
   (cut + array + voxel).

4. **No fallback se MANIFOLD solver non disponibile**: Blender < 4.2 non ha il solver
   MANIFOLD per i boolean. La libreria userebbe EXACT (con cambio in `constants.py`),
   ma alcuni pattern boolean concatenati potrebbero generare artefatti. Su Blender 4.2+
   tutto OK.

5. **Performance**: l'auto_box su un master complesso (100k+ poligoni) può essere lento
   per via dei voxel remesh concatenati. Il server originale è probabilmente più
   ottimizzato (potrebbe usare openvdb diretto). Da profilare.

---

## Roadmap se vuoi affinare

In ordine di impatto:
1. **clear_extraction** (alta utilità — da `extraction.py` Moldboxer).
2. **Contour-adapted channels** (visivamente vicino all'originale).
3. **Interlock keys piramidali** (qualità chiusura).
4. **Inner cavity** (Pro feature, riduzione consumo silicone).
5. **2-part silicone** (Pro feature).

Per ognuno hai il pseudo-Python originale in `../decompiled_py/components/` come
riferimento di prima mano.
