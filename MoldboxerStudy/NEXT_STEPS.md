# NEXT_STEPS.md — stato corrente e backlog

> **Scopo**: documento "where we left off". Apri questo per sapere a che punto siamo prima di proporre azioni.

Ultimo aggiornamento: 2026-05-13.

---

## Stato per area

| Area | Stato | Cosa serve per "verde" |
|---|---|---|
| 📖 Documentazione studio | ✅ Completa | — |
| 🧩 Decompilazione `.pyc` → pseudo-Python | ✅ 32/32 file | (opz.) decompilazione vera con pylingual |
| 🧰 Libreria `moldboxer_lite/` foundations | ✅ Sintassi OK + smoke test | Live test in Blender |
| 🧰 `auto_flat`, `auto_box`, `confirm` | ✅ Scritti | Live test + tuning |
| 🧰 Feature Pro (`inner_cavity`, `2-part silicone`) | ❌ Non iniziato | Vedi RECONSTRUCTION.md §3 |
| 🧰 `clear_extraction` (utility che apre canali undercut) | ❌ Non iniziato | Riferimento in `decompiled_py/components/extraction.py` |
| 🔌 Integrazione MCP | ✅ Wiring fatto (6 tool `mb_*` registrati, addon v1.6.0) | Live test pending (P0.1) |
| 🎯 Tuning parametri empirici | ⏳ Non iniziato | Servono test visivi su mesh reali |

---

## Backlog prioritizzato

Ogni voce dichiara: **dipendenze** (cosa devi avere prima), **dove guardare**, **definizione di "fatto"**.

### P0 — sblocca tutto il resto

#### P0.1 — Live test della pipeline esistente

- **Perché**: senza un test live non sappiamo se `auto_box` / `auto_flat` / `confirm` producono mesh sane su un master vero.
- **Dipendenze**: MCP Blender attivo (`mcp__blender__execute_blender_code` risponde), Blender 4.2+ per solver MANIFOLD.
- **Dove**: [moldboxer_lite/tests/live_test_in_blender.py](moldboxer_lite/tests/live_test_in_blender.py).
- **Come**:
  1. Verifica MCP: `execute_blender_code` di `import bpy; print(bpy.app.version_string)`.
  2. Copia il contenuto di `live_test_in_blender.py` (sistema il `sys.path.insert` con il path reale della cartella) e mandalo via `execute_blender_code`.
  3. Cattura uno screenshot finale con `get_viewport_screenshot`.
- **Fatto quando**: il test non solleva eccezioni, `box_l` e `box_r` esistono in scena, e lo screenshot mostra due metà visibilmente sane.

#### P0.2 — Integrazione nel tuo MCP ✅ FATTA 2026-05-13

- **Status**: Wiring completato in `blender-mcp` (questa repo).
- **Strategia adottata**: 6 tool consolidati `mb_*` (anziché 13 atomici), libreria `moldboxer_lite/` resta in `MoldboxerStudy/` e l'addon Blender bootstrappa `sys.path` al primo uso.
- **Tool MCP registrati** (`server.py`):
  - `mb_setup_mm()` — configura mm
  - `mb_preprocess_patron(object_name?, master_quality, center, isolate)`
  - `mb_auto_box(patron_name, box_gap, box_quality, channel_width, channel_depth, …)`
  - `mb_auto_flat(patron_name, box_gap, box_quality, grip_height, …)`
  - `mb_confirm_mold(patron_name, box_name, n_splits, add_keys, key_count, …)`
  - `mb_export_parts(dir_path, apply_modifiers)`
- **Handler Blender** (`addon.py`): 6 metodi `BlenderMCPServer.mb_*` + `_bootstrap_moldboxer()` per `sys.path`. Bump addon v1.5.5 → **v1.6.0**.
- **Prompt MCP**: aggiunto `mold_strategy()` con decision tree (auto_box vs auto_flat) + workflow step-by-step.
- **Validazione**:
  - ✅ `py_compile addon.py` + `py_compile server.py` puliti
  - ✅ smoke test `moldboxer_lite/tests/test_import_smoke.py` verde (13 API + costanti)
- **Manca** (P0.1): live test dentro Blender quando l'utente avvia l'MCP.

### P1 — qualità "Moldboxer-like"

#### P1.1 — Tuning canali

- **Perché**: i canali oggi sono distribuiti uniformemente. Il prodotto originale li adatta al contorno.
- **Dipendenze**: P0.1 (test visivo) per confrontare.
- **Dove**: [moldboxer_lite/channels.py](moldboxer_lite/channels.py) → `CHANNEL_SPACING_FACTOR`, e funzione `build_channels`.
- **Strategia**: per `adjust_to_contour=True`, raycast da `(x_pos, ±box.max_y, z_center)` verso il centro del box e snappa il cilindro al punto di contatto.
- **Fatto quando**: su un master arrotondato (es. il chicken model del video) i canali seguono visibilmente la curvatura.

#### P1.2 — Interlock keys piramidali

- **Perché**: oggi sono cubi. Il prodotto originale usa piramidi tronche (più estetiche e meglio sealing).
- **Dove**: [moldboxer_lite/split_and_base.py](moldboxer_lite/split_and_base.py) → `add_interlock_keys`.
- **Riferimento**: `_build_pin` nello stesso file usa già il pattern tronco-piramide. Riusalo con `base_size = key_size` e `top_scale = 0.7`.
- **Fatto quando**: la metà L e R si incastrano lateralmente senza bisogno di tolleranza extra.

#### P1.3 — clear_extraction

- **Perché**: senza questo, i mold con undercut non si demoldano. Feature documentata nel video [10:09-10:51].
- **Dove**: implementa in `moldboxer_lite/extraction.py` (NUOVO file). Riferimento: [decompiled_py/components/extraction.py](decompiled_py/components/extraction.py).
- **API**: `clear_horizontal_extraction_path(box, extrude_dist, voxel_size)`. Da chiamare in `auto_box.py` dopo aver costruito il box, se `clear_extraction=True`.
- **Fatto quando**: testando con il teddy bear del video [10:09], il mold si apre senza bloccarsi sulle gambe.

### P2 — feature Pro

#### P2.1 — Inner cavity

- **Perché**: feature Pro Moldboxer (vedi `pro_inner_cavity` in `properties.py`).
- **Dove**: nuovo modulo `moldboxer_lite/inner_cavity.py`. Riferimento: [decompiled_py/components/inner_core.py](decompiled_py/components/inner_core.py) (server-dependent — qui devi ricostruire da zero).
- **Difficoltà**: alta. Richiede analisi topologica del silicone_mold per trovare cavità interne.
- **Fatto quando**: su un master a "vaso" (concavo dall'alto), genera un filler interno che riduce il volume di silicone di almeno il 30%.

#### P2.2 — 2-part silicone

- **Perché**: feature Pro Moldboxer (vedi `pro_two_part_silicone`).
- **Dove**: nuovo modulo `moldboxer_lite/two_parts.py`. Riferimento (parziale, lato client): [decompiled_py/components/two_parts.py](decompiled_py/components/two_parts.py).
- **Difficoltà**: alta. Genera un mold a 2 silicone separati per produzione di pezzi a 2 componenti.
- **Fatto quando**: il flow è eseguibile end-to-end con `pro_two_part_silicone=True`.

### P3 — nice to have

- **Decompilazione vera con pylingual**: l'utente autorizza `pip install pylingual`, sostituiamo il pseudo-Python con sorgente pulito. Rigenera `decompiled_py/`.
- **Volume text 3D più curato**: oggi è un decimate ratio=0.5; il prodotto originale usa voxel 0.05 + decimate 0.5 (qualità superiore).
- **Materiali colorati per i 3 oggetti finali**: il prodotto colora silicone preview / mold / master di colori diversi. Vedi `decompiled_py/materials.py`.

---

## Dipendenze esterne (non controllabili da noi)

- **MCP Blender attivo**: necessario per P0.1, P1.1, e validazione di qualunque modifica futura. Senza, lavoriamo sintassi-only.
- **Blender 4.2+**: per il solver boolean MANIFOLD. Su 3.x/4.0/4.1 funziona ma con possibili artefatti sui boolean concatenati.
- **Pylingual (opzionale)**: per decompilazione vera. Richiede autorizzazione utente per pip install.

---

## Come aggiornare questo file

Quando completi un task:
1. Sposta la sua riga da "❌/⏳" a "✅" nella tabella stato.
2. Cancella la voce dal backlog se non serve più rilavorarci.
3. Aggiungi un breve commit log in fondo con la data, così tracciamo l'evoluzione.

## Log

- **2026-05-13** — Setup iniziale: documentazione completa, libreria foundations + auto_flat + auto_box + confirm scritti e validati a sintassi. P0 da fare: live test + integrazione MCP.
- **2026-05-13 (later)** — P0.2 ✅: integrazione MCP completata. 6 tool `mb_*` in `server.py`, 6 handler in `addon.py` (bump v1.6.0), nuovo prompt `mold_strategy()`. `sys.path` bootstrap automatico verso `MoldboxerStudy/moldboxer_lite/`. Smoke test verde. P0.1 (live test in Blender) ancora pending — richiede avvio addon Blender.
