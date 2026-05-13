# CLAUDE.md — entry point per LLM

> **Sei un LLM (probabilmente Claude Code) che ha appena aperto questa cartella.**
> Questa pagina ti dice in 60 secondi dove sei, cosa c'è, e cosa fare per la richiesta dell'utente.
> Leggi prima questo, poi salta al doc giusto. Non rispondere all'utente prima di aver capito la struttura.

---

## 1. Dove sei

Cartella **MoldboxerStudy** — materiale di studio del bundle commerciale **Moldboxer Blender 5.0.1** + add-on `moldboxer_silicone` v1.4.9, e **libreria di ricostruzione** (`moldboxer_lite/`) che replica client-side la maggior parte delle sue feature.

L'utente è quasi sempre in uno di questi due contesti:

| Contesto | Sintomo | Cosa significa per te |
|---|---|---|
| **Studio standalone** | La cartella è isolata (Desktop, Downloads) | Aiuta a capire/documentare il prodotto. |
| **Dentro un MCP Blender repo** | La cartella è sottocartella di un repo che ha `mcp.json`, `package.json` con `@modelcontextprotocol/sdk`, o tool `mcp__blender__*` | L'utente vuole **integrare** `moldboxer_lite/` come tool MCP. Vedi [moldboxer_lite/INTEGRATION.md](moldboxer_lite/INTEGRATION.md). |

**Controllo rapido del contesto**: `ls ..` e cerca `mcp.json`, `tools/`, `src/index.ts` o file simili. Se vedi un MCP, sei nel secondo caso.

---

## 2. Cosa c'è (mappa)

```
MoldboxerStudy/
├── CLAUDE.md                  ← SEI QUI
├── INDEX.md                   mappa fisica della cartella
├── FEATURES.md                catalogo prodotto: cosa fa per ogni piano (Lite/Core/Pro)
├── RECONSTRUCTION.md          teoria/strategia: confine client/server, ricette ricostruzione
├── NEXT_STEPS.md              ⭐ stato corrente + backlog prioritizzato (leggilo se aiuti a continuare)
├── Moldboxer Guide – Part 1 Core Tools.txt    trascrizione tutorial ufficiale
│
├── moldboxer_silicone/        l'add-on originale (sorgente parziale + .pyc compilati)
├── decompiled_py/             pseudo-Python ricostruito da ogni .pyc (LEGGIBILE)
├── decompiled/                disassembly bytecode raw (fallback)
├── portable_config/           preset Blender preconfigurati nel bundle
│
├── moldboxer_lite/ ⭐⭐        LIBRERIA RICOSTRUITA (Python puro per Blender)
│   ├── __init__.py            API pubblica (13 export)
│   ├── README.md              overview libreria
│   ├── INTEGRATION.md         ⭐ come wirearla in un MCP (leggi se aiuti a integrare)
│   ├── HOWTO.md               ⭐ ricette per task tipici (leggi se l'utente vuole modificare/estendere)
│   ├── constants.py, modifiers.py, primitives.py, voxel_size.py
│   ├── object_wrapper.py (classe Object con boolean overload)
│   ├── wrapper.py, preprocess.py, silicone_mold.py, channels.py
│   ├── auto_flat.py, auto_box.py, split_and_base.py, confirm.py
│   ├── export.py
│   └── tests/
│       ├── test_import_smoke.py     stdlib-only, lanciabile sempre
│       └── live_test_in_blender.py  da eseguire in Blender via MCP
│
└── tools/
    ├── pyc_inspect.py         dumper bytecode → markdown
    └── pyc_to_pseudo.py       convertitore bytecode → pseudo-Python
```

---

## 3. Reading order — quale doc per quale domanda

| L'utente chiede… | Apri prima | Poi se serve |
|---|---|---|
| "Cos'è Moldboxer? cosa fa?" | [FEATURES.md](FEATURES.md) | [Moldboxer Guide – Part 1.txt](Moldboxer%20Guide%20%E2%80%93%20Part%201%20Core%20Tools.txt) |
| "Come funzionano i piani Lite/Core/Pro?" | [FEATURES.md](FEATURES.md) §1-4 | [decompiled_py/operator_access.py](decompiled_py/operator_access.py) |
| "Cosa va al server? cosa no?" | [RECONSTRUCTION.md](RECONSTRUCTION.md) §1-3 | [decompiled_py/components/server.py](decompiled_py/components/server.py) |
| "Come fa l'auto-box / confirm / flat?" | [moldboxer_lite/](moldboxer_lite) source | [decompiled_py/components/](decompiled_py/components) per il riferimento Moldboxer |
| "Come integro questo nel mio MCP?" | [moldboxer_lite/INTEGRATION.md](moldboxer_lite/INTEGRATION.md) | [NEXT_STEPS.md](NEXT_STEPS.md) |
| "Come aggiungo un tool nuovo / modifico X?" | [moldboxer_lite/HOWTO.md](moldboxer_lite/HOWTO.md) | il file specifico in `moldboxer_lite/` |
| "Come testo che funziona?" | [moldboxer_lite/HOWTO.md §Test](moldboxer_lite/HOWTO.md) | [tests/live_test_in_blender.py](moldboxer_lite/tests/live_test_in_blender.py) |
| "A che punto siamo? cosa manca?" | [NEXT_STEPS.md](NEXT_STEPS.md) | [moldboxer_lite/README.md §Stato](moldboxer_lite/README.md) |
| "Cosa fa la funzione X di Moldboxer?" | grep `X` in [decompiled_py/](decompiled_py) | [decompiled/](decompiled) per il bytecode |
| "Voglio decompilare meglio i .pyc" | autorizza `pip install pylingual` e rilancia | [tools/pyc_to_pseudo.py](tools/pyc_to_pseudo.py) per la versione stdlib |

---

## 4. Playbook — comportamenti per task tipici

> Queste sono regole operative. **Seguile**, non improvvisare.

### 4.1 L'utente chiede di **integrare moldboxer_lite nel suo MCP**

1. Verifica che siamo dentro un MCP repo (vedi §1 controllo rapido).
2. Apri [moldboxer_lite/INTEGRATION.md](moldboxer_lite/INTEGRATION.md). Segui la checklist.
3. **Non** copiare/spostare i file di `moldboxer_lite/` prima di aver discusso lo stile di import preferito dall'utente (subpackage vs file flat).
4. Le 13 API pubbliche sono in `moldboxer_lite/__init__.py` (`__all__`). Mappale 1:1 ai tool MCP.
5. Aggiorna [NEXT_STEPS.md](NEXT_STEPS.md) man mano che spunti i task.

### 4.2 L'utente chiede di **testare la pipeline live in Blender**

1. Controlla che l'MCP `mcp__blender__execute_blender_code` sia disponibile (carica via ToolSearch se è deferred).
2. Apri [moldboxer_lite/tests/live_test_in_blender.py](moldboxer_lite/tests/live_test_in_blender.py).
3. Passa il file path corretto a Python all'inizio del code, poi inseriscilo come `code` per `execute_blender_code`.
4. Se fallisce su qualche step, **non** sopprimere l'errore — riportalo all'utente con il traceback completo e il file/line. Probabile causa: tuning empirico sbagliato, edge case sull'STL master, o solver MANIFOLD non disponibile su Blender < 4.2.

### 4.3 L'utente chiede di **aggiungere una feature mancante** (es. clear_extraction, inner_cavity, contour-adapted channels)

1. Trova il riferimento Moldboxer: cerca in [decompiled_py/components/](decompiled_py/components) il file omonimo.
2. Apri [moldboxer_lite/HOWTO.md §Implementare una nuova feature](moldboxer_lite/HOWTO.md).
3. Crea il modulo nuovo in `moldboxer_lite/`. Mantieni le costanti in `constants.py`.
4. Esponilo in `__init__.py` e aggiorna `__all__`.
5. Aggiungi una sezione al README della libreria.
6. Se è un task >1 ora, usa TodoWrite per spezzarlo.

### 4.4 L'utente chiede di **tunare un parametro** (es. channel spacing che non corrisponde al video)

1. Identifica il parametro in `moldboxer_lite/` (cerca con grep). I parametri empirici sono dichiarati come costanti uppercase in cima al file (es. `CHANNEL_SPACING_FACTOR` in `channels.py`).
2. Apri il video transcript [Moldboxer Guide.txt](Moldboxer%20Guide%20%E2%80%93%20Part%201%20Core%20Tools.txt) e cerca il timestamp pertinente.
3. Proponi una modifica, **non applicare** finché l'utente conferma — il tuning è soggettivo.
4. Se modifichi, lancia il live test su Suzanne per regression-check visiva.

### 4.5 L'utente chiede di **capire perché qualcosa non funziona** (debugging)

1. Riproduci il problema: chiedi un mesh master di esempio (path o link) o usa Suzanne.
2. Riduci al minimo: isola lo step che fallisce (preprocess? auto_box? confirm?). Non fissare a caso.
3. Le 5 chiamate boolean concatenate sono il sospetto principale. Su solver MANIFOLD vanno; su EXACT a volte producono geometry vuota — controlla `box.has_empty_boolean`.
4. Il pseudo-Python in `decompiled_py/` è il ground truth. Confrontalo con `moldboxer_lite/` per vedere se hai divergenze.

### 4.6 L'utente chiede di **leggere/spiegare il codice di Moldboxer** (non ricostruire)

1. Sorgente in chiaro: [moldboxer_silicone/__init__.py](moldboxer_silicone/__init__.py), `operators.py`, `panels.py`, `properties.py`.
2. Logica core (compilata): `decompiled_py/<modulo>.py` (pseudo-Python leggibile, NON eseguibile).
3. Se il pseudo-Python ha `# decompile error` su una funzione che ti interessa, vai al bytecode raw in `decompiled/<modulo>.md`.
4. **Non** spacciare per certo qualcosa di ambiguo dal bytecode. Se c'è ambiguità, dichiarala.

### 4.7 L'utente fa una domanda **fuori scope** (es. "rifai questo prodotto da zero", "vendi moldboxer concorrenza")

Rifiuta gentilmente l'aspetto problematico. Il materiale è **per studio/MCP personale**, non per replicare il prodotto commerciale. Riformula in scope.

---

## 5. Stato di completamento (a colpo d'occhio)

Vedi [NEXT_STEPS.md](NEXT_STEPS.md) per il dettaglio.

- ✅ Decompilazione bytecode → pseudo-Python di 32 file `.pyc`
- ✅ Documentazione: INDEX, FEATURES, RECONSTRUCTION, README libreria
- ✅ Libreria `moldboxer_lite/` 14 moduli, ~2300 righe, smoke test verde
- ✅ **Wiring nel MCP `blender-mcp` (2026-05-13)** — 6 tool `mb_*` registrati in `server.py`, handler in `addon.py` v1.6.0, prompt `mold_strategy()` per LLM
- ⏳ Live test in Blender (richiede MCP attivo per validare) — P0.1
- ⏳ Tuning parametri empirici (canali, funneler, keys) — P1
- ❌ Feature Pro avanzate (inner_cavity, 2-part silicone)
- ❌ clear_extraction (locale, è in `decompiled_py/components/extraction.py`)

**Tool MCP esposti (post-integrazione 2026-05-13)**:
- `mb_setup_mm()` — configura unità mm
- `mb_preprocess_patron(object_name?, master_quality, center, isolate)`
- `mb_auto_box(patron_name, box_gap, box_quality, channel_width, channel_depth, …)`
- `mb_auto_flat(patron_name, box_gap, box_quality, grip_height, …)`
- `mb_confirm_mold(patron_name, box_name, n_splits, add_keys, key_count, …)`
- `mb_export_parts(dir_path, apply_modifiers)`

Più il prompt `mold_strategy()` per istruire un LLM client sul decision tree
(auto_box vs auto_flat) e workflow step-by-step.

---

## 6. Vincoli operativi

- **Lingua**: rispondi in italiano se l'utente scrive in italiano (default qui).
- **Concisione**: l'utente preferisce risposte brevi e azione veloce. Non riassumere lavoro già fatto, non duplicare la doc nella chat.
- **No modifiche destruttive senza permesso**: non eliminare/rinominare file della libreria o della cartella di studio. Aggiungere è OK.
- **Non installare pacchetti pip**: l'auto-mode classifier blocca per supply-chain. Se serve un decompilatore vero, chiedi autorizzazione esplicita all'utente.
- **Non chiamare Moldboxer server**: niente requests verso `*.moldboxer.com`. La libreria è offline by design.
- **Quando in dubbio**: chiedi. Una riga di chiarimento costa meno di rifare 200 righe di codice.

---

## 7. Cosa fare se è la tua prima interazione con l'utente

1. Apri [NEXT_STEPS.md](NEXT_STEPS.md) per sapere a che punto siamo.
2. Saluta con UNA frase che dimostra di aver capito il contesto (non con elenchi infiniti).
3. Aspetta la richiesta. Non proporre 10 cose a caso.
4. Quando arriva la richiesta, usa il playbook §4 corrispondente.
