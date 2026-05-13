# INTEGRATION.md — wirare moldboxer_lite nel tuo MCP Blender

> Guida pratica per esporre le 13 API della libreria come **tool MCP** richiamabili da un LLM client.

---

## 0. Prerequisiti

- Repo MCP funzionante che usa Blender (struttura tipica: `src/`, `mcp.json`, tool come `mcp__blender__execute_blender_code`).
- Blender 4.2+ installato (per il solver boolean MANIFOLD).
- Cartella `MoldboxerStudy/` (o solo `moldboxer_lite/`) raggiungibile da Python eseguito da Blender.

---

## 1. Strategia di integrazione (scegli UNA)

### A — Subpackage (raccomandato)

Pro: pulito, isolato, aggiornabile come dipendenza separata.
Contro: l'utente deve aggiungere `sys.path.insert` o installare come package editabile.

```
your_mcp_repo/
├── src/
│   └── tools/
│       └── moldboxer/        ← copia qui l'intera cartella `moldboxer_lite/`
│           ├── __init__.py
│           ├── constants.py
│           └── ...
└── ...
```

### B — Vendoring inline

Pro: zero setup, file dell'MCP self-contained.
Contro: se vuoi aggiornare devi ri-fondere.

Copia il contenuto di `moldboxer_lite/` direttamente sotto i tool MCP, rinominando gli import relativi.

### C — Eseguibile via `execute_blender_code`

Pro: nessuna modifica al repo MCP, nessun import statico.
Contro: ogni chiamata deve passare il path `sys.path.insert(0, "...")` e ricaricare il modulo.

Esempio (chiamata MCP):
```python
import sys
if "C:/Users/emanu/Desktop/MoldboxerStudy" not in sys.path:
    sys.path.insert(0, "C:/Users/emanu/Desktop/MoldboxerStudy")
from moldboxer_lite import auto_box, preprocess_patron
# ... usa
```

---

## 2. Le 13 API → 13 tool MCP

Mapping diretto dai 13 export pubblici in [`__init__.py`](__init__.py) (`__all__`).

| Tool MCP | Funzione `moldboxer_lite` | Parametri principali |
|---|---|---|
| `mb_preprocess_patron` | `preprocess_patron(target?, master_quality, center, isolate)` | quality FAST/MID/HIGH/ULTRA |
| `mb_configure_mm_units` | `configure_metric_millimeter_units()` | nessuno |
| `mb_heal_mesh` | `heal_mesh(obj, master_quality)` | quality |
| `mb_center_to_origin` | `center_to_origin(obj)` | obj name |
| `mb_auto_flat` | `auto_flat(patron, box_gap, box_quality, grip_height, ...)` | gap mm, quality |
| `mb_auto_box` | `auto_box(patron, box_gap, box_quality, channel_width, channel_depth, adjust_to_contour, larger_back, funneler, safe_mode)` | tutti i toggle Settings |
| `mb_confirm_mold` | `confirm_mold(patron, box, join_patron, master_base_pin, n_splits, add_keys, key_count, key_size, key_tolerance, voxel_size, space_objects)` | flag finalizzazione |
| `mb_silicone_preview` | `build_silicone_mold_preview(patron, box, voxel_size)` | restituisce volume_mm3 |
| `mb_place_volume_text` | `place_volume_text(box, volume_mm3, side)` | side="X+" / "Y-" |
| `mb_split_box_on_y` | `split_box_on_y(box, gap)` | restituisce (box_l, box_r) |
| `mb_add_basing` | `add_basing_to_system(box, patron, volume_mm3, join_patron, master_base_pin, ...)` | flag base |
| `mb_add_keys` | `add_interlock_keys(box_l, box_r, key_count, key_size, key_tolerance)` | quantità/dim |
| `mb_export_all_parts` | `export_all_parts(dir_path, apply_modifiers)` | output dir |
| `mb_get_voxel_size` | `get_box_voxel_size(quality, candidate)` / `get_master_voxel_size(...)` | helper |

**Naming**: usa il prefisso `mb_` per evitare collisione con i tool esistenti del MCP Blender. Adatta se hai una convenzione tua.

---

## 3. Checklist passo-passo

> Quando l'utente dice "integra moldboxer_lite nel mio MCP", esegui questi step in ordine. Spunta man mano.

### 3.1 Identifica l'MCP

- [ ] `ls ../` mostra `mcp.json` / `package.json` / `src/index.ts` o file simili?
- [ ] Apri il file di registrazione tool (es. `src/tools.ts`, `src/server.py`, `mcp.json`).
- [ ] Conferma il pattern: come sono definiti i tool esistenti? (TypeScript decorator, dict Python, JSON schema, ...).

### 3.2 Sposta/integra la libreria (strategia A consigliata)

- [ ] Crea `src/tools/moldboxer/` (o nome conforme al repo).
- [ ] Copia `moldboxer_lite/*.py` dentro (mantieni la struttura).
- [ ] **Non** copiare `tests/` (non serve in produzione). Tienili nella cartella di studio.
- [ ] Verifica che gli import relativi (`from .object_wrapper import Object`) restino funzionanti — sono già relativi al package, dovrebbe filare.

### 3.3 Registra i tool

Per ogni tool della tabella §2:

- [ ] Crea una funzione wrapper nel tuo MCP che:
  1. Riceve parametri JSON dal client LLM.
  2. Risolve gli oggetti per nome (es. `bpy.data.objects.get(patron_name)`).
  3. Wrappa in `Object()` se necessario.
  4. Chiama la funzione di `moldboxer_lite`.
  5. Restituisce un dict JSON con i nomi degli oggetti creati e metriche utili (volume, bbox).

Esempio (Python, MCP-agnostic):

```python
def mb_auto_box(patron_name: str, box_gap: float = 4.5, box_quality: str = "MID",
                channel_width: float = 5.0, channel_depth: float = 6.0,
                funneler: bool = True, **kwargs) -> dict:
    from moldboxer_lite import Object, auto_box
    import bpy
    patron_bpy = bpy.data.objects.get(patron_name)
    if patron_bpy is None:
        return {"error": f"Object '{patron_name}' not found"}
    patron = Object(patron_bpy)
    box = auto_box(patron, box_gap=box_gap, box_quality=box_quality,
                   channel_width=channel_width, channel_depth=channel_depth,
                   funneler=funneler, **kwargs)
    return {
        "box_name": box.name,
        "dimensions_mm": [box.width, box.depth, box.height],
        "min_z": box.min_z,
    }
```

### 3.4 Tool description per l'LLM

Per ogni tool registrato, fornisci una description che dica:
- **Cosa fa** (1 frase concreta).
- **Quando usarlo** (pre-condizioni: deve esistere un patron preprocessato).
- **Parametri chiave** con range tipici e default.
- **Cosa restituisce** (nome del nuovo oggetto, metriche).

Esempio:

```
mb_auto_box:
  Genera un mold a 2 metà attorno al master Blender chiamato `patron_name`.
  Pre: il patron deve essere già preprocessato (chiamare mb_preprocess_patron prima).
  Default: box_gap=4.5mm (spessore silicone), box_quality=MID, channel_width=5mm.
  Restituisce: nome del nuovo oggetto 'box' + dimensioni in mm.
  Non chiama questo se vuoi un mold flat — usa mb_auto_flat.
```

### 3.5 Test end-to-end via MCP

- [ ] Lancia il MCP server localmente.
- [ ] Da un client (Claude Code), chiedi: "Importa /path/Suzanne.stl, preprocessalo, genera auto_box, conferma, esporta".
- [ ] Verifica che la sequenza chiamate sia: `mb_configure_mm_units` → import STL → `mb_preprocess_patron` → `mb_auto_box` → `mb_confirm_mold` → `mb_export_all_parts`.
- [ ] Cattura screenshot finale per verifica visiva.

### 3.6 Aggiorna [../NEXT_STEPS.md](../NEXT_STEPS.md)

- [ ] Sposta P0.2 a ✅ quando tutti i 13 tool sono registrati e testati.

---

## 4. Errori comuni e fix

| Errore | Causa probabile | Fix |
|---|---|---|
| `ModuleNotFoundError: moldboxer_lite` da Blender | `sys.path` non include la cartella | Aggiungi `sys.path.insert(0, "C:/...")` all'inizio del codice, o installa il package come editabile (`pip install -e .` con Python di Blender) |
| `RuntimeError: Object 'patron' not found` | L'LLM ha saltato il preprocess | Nel tool description scrivi esplicitamente "PRE: chiama mb_preprocess_patron prima" |
| `Error: 'MANIFOLD' is not a valid enum item` | Blender < 4.2 | In `moldboxer_lite/constants.py` cambia `DEFAULT_BOOLEAN_SOLVER = "EXACT"`. Più lento ma compatibile |
| `box.has_empty_boolean is True` | Un Boolean modifier ha target=None (di solito perché un oggetto intermedio è stato rimosso prima) | Riordina le chiamate: rimuovi gli oggetti temporanei DOPO `apply_modifier`, non prima |
| Mold visibile ma cavità interna vuota/sbagliata | Patron non manifold o invertito | Lancia `mb_heal_mesh` prima di `mb_auto_box`. Verifica con `mcp__blender__analyze_mesh_for_print` |
| Pipeline lenta su master 100k+ poligoni | Voxel remesh concatenati | Aumenta voxel_size (quality FAST/MID), o decima il master prima del preprocess |

---

## 5. Pattern d'uso per il client LLM

Una "ricetta di mold" tipica che l'LLM dovrebbe imparare a generare:

```
USER: "Crea un mold per stamparlo, ho il file /path/to/master.stl, voglio uno spessore di 4mm e 2 metà"

LLM (sequenza chiamate MCP):
1. mb_configure_mm_units()
2. mcp__blender__import_stl(filepath="/path/to/master.stl", object_name="master_in")
3. mb_preprocess_patron(target_name="master_in", master_quality="HIGH", center=True)
   → patron name = "patron"
4. mb_auto_box(patron_name="patron", box_gap=4.0, box_quality="MID")
   → box name = "box"
5. mb_confirm_mold(patron_name="patron", box_name="box", n_splits=2, add_keys=True)
   → box_l, box_r, silicone_mold
6. mb_export_all_parts(dir_path="/tmp/mold_out/")
7. mcp__blender__get_viewport_screenshot()  ← per verifica visiva
```

---

## 6. Una volta integrato: cosa dire all'LLM client

Aggiungi al system prompt o tool documentation del tuo MCP qualcosa tipo:

> Quando l'utente chiede di generare uno stampo in silicone da un modello 3D:
> 1. Importa il file (mcp__blender__import_stl).
> 2. Preprocessa (mb_preprocess_patron).
> 3. Scegli auto_flat per modelli piatti, auto_box per modelli 3D complessi.
> 4. Conferma con mb_confirm_mold (split=2 per modelli a 2 pezzi, split=0 per un solo pezzo).
> 5. Esporta con mb_export_all_parts.
> Tutte le distanze sono in mm. La voxel quality FAST è veloce ma rozza, ULTRA è lenta ma dettagliata.

Il client LLM dovrebbe imparare la pipeline da questo prompt + le tool description del §3.4.
