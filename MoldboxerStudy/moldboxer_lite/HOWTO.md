# HOWTO.md — ricette per task tipici sulla libreria

> Step-by-step per i task più comuni di chi modifica/estende `moldboxer_lite/`.
> Ogni ricetta è autonoma — non serve leggerne altre.

---

## Ricetta 1: Lanciare il smoke test stdlib-only

**Quando**: dopo qualunque modifica, prima di fare altro. Verifica che la libreria importi senza errori.

```bash
cd /path/to/MoldboxerStudy
python moldboxer_lite/tests/test_import_smoke.py
```

**Output atteso**:
```
moldboxer_lite v0.1.0
  OK: tutte le 13 API pubbliche esposte (+5 extra).
  OK: costanti Moldboxer caricate correttamente.
  OK: get_box_voxel_size('HIGH', 100mm) = 0.8000 mm (clipped a 0.5)
  OK: get_master_voxel_size('ULTRA', 100mm) = 0.0667 mm

SMOKE TEST PASSED
```

Se fallisce: errore di sintassi o import. Il traceback ti dice il file. Fixa, rilancia.

---

## Ricetta 2: Lanciare il live test in Blender via MCP

**Quando**: dopo modifiche logiche, per verificare che la pipeline produca davvero mesh sane.

**Pre**: MCP `mcp__blender__execute_blender_code` disponibile, Blender 4.2+ aperto.

1. Verifica MCP:
   ```python
   # via execute_blender_code
   import bpy; print(bpy.app.version_string)
   ```

2. Leggi [tests/live_test_in_blender.py](tests/live_test_in_blender.py). Sostituisci il `sys.path.insert` in cima con il path reale della cartella MoldboxerStudy.

3. Mandalo tutto via `execute_blender_code` come `code`. Il test crea Suzanne, preprocessa, e prova auto_flat + auto_box + confirm.

4. Cattura uno screenshot finale:
   ```python
   # via mcp__blender__get_viewport_screenshot
   ```

**Cosa cercare nello screenshot**:
- Suzanne (master) visibile a sinistra.
- 2 metà del box (`box_l`, `box_r`) al centro/destra.
- Niente facce vuote o boolean falliti.

Se uno step solleva, leggi il traceback: ti dice quale modulo (`auto_box.py`, `confirm.py`, ...) e quale operazione (boolean, voxel, split). Vai al codice e debugga.

---

## Ricetta 3: Aggiungere un nuovo tool / funzione pubblica

**Esempio**: aggiungere `cut_with_plane(obj_name, point, normal)` come tool MCP.

1. **Esiste già il metodo sulla classe Object?** Apri [object_wrapper.py](object_wrapper.py) e cerca. `Object.cut_plane(plane_normal, plane_point)` esiste già. Puoi esporlo direttamente, non serve nuovo modulo.

2. **Aggiungi una funzione top-level** in `object_wrapper.py` (o in un nuovo modulo se è una pipeline più complessa):
   ```python
   def cut_with_plane(obj_name: str, point: tuple, normal: tuple) -> dict:
       """Taglia un oggetto con un piano. Restituisce dimensioni risultanti."""
       import bpy
       from mathutils import Vector
       bpy_obj = bpy.data.objects.get(obj_name)
       if bpy_obj is None:
           raise ValueError(f"Object '{obj_name}' not found")
       obj = Object(bpy_obj)
       obj.cut_plane(Vector(normal), Vector(point))
       return {"name": obj.name, "dimensions_mm": [obj.width, obj.depth, obj.height]}
   ```

3. **Esponi in `__init__.py`**:
   ```python
   from .object_wrapper import Object, cut_with_plane
   __all__ = [..., "cut_with_plane"]
   ```

4. **Aggiungi nel README** (`moldboxer_lite/README.md`, sezione "Mapping con il prodotto originale"): una riga che spiega cosa fa il tool.

5. **Registra come tool MCP** nel tuo MCP repo (vedi [INTEGRATION.md §3.3](INTEGRATION.md)).

6. **Rilancia il smoke test** (ricetta 1).

---

## Ricetta 4: Implementare una feature mancante

**Esempio**: implementare `clear_extraction` (P1.3 nel backlog).

1. **Trova il riferimento**: [../decompiled_py/components/extraction.py](../decompiled_py/components/extraction.py). Leggi `clear_horizontal_extraction_path` — è la ricetta originale.

2. **Capisci la semantica**: dal pseudo-Python:
   - Duplica box come `box_original`.
   - Calcola normale di taglio ruotata di 90° attorno a Z.
   - Crea 2 mold_box (sinistra e destra) con `cut_and_extrude`.
   - Somma, clean_bot(2) / clean_top(3), voxel, clean_bot(1) / clean_top(1).
   - Rinomina in `box`.

3. **Crea il nuovo modulo** `moldboxer_lite/extraction.py`:
   ```python
   """clear_extraction: apre canali nella direzione di split per evitare undercut bloccanti."""
   from __future__ import annotations
   from mathutils import Vector
   from math import radians

   from .object_wrapper import Object
   from .modifiers import build_voxel_modifier, build_array_modifier

   def clear_horizontal_extraction_path(box: Object, extra_extrussion_dist: float = 10.0, voxel_size: float = 0.8) -> Object:
       """Apre un canale lungo la direzione di estrazione orizzontale (asse Y, split direction)."""
       # ... porta la logica dal decompiled_py
       ...
       return box
   ```

4. **Integralo nel pipeline**: in `auto_box.py`, dopo aver costruito il box wrapper, aggiungi:
   ```python
   if clear_extraction:  # nuovo parametro
       from .extraction import clear_horizontal_extraction_path
       box = clear_horizontal_extraction_path(box, extra_extrussion_dist=(channel_width + 2) / 2, voxel_size=voxel)
   ```

5. **Esponi nell'API**: `__init__.py`, `__all__`, README.

6. **Test live** su un master con undercut evidente (es. modello teddy bear con gambe separate). Verifica che il mold si possa "aprire" virtualmente senza che la geometria del master blocchi.

7. **Aggiorna [../NEXT_STEPS.md](../NEXT_STEPS.md)**: sposta P1.3 da ❌ a ✅.

---

## Ricetta 5: Tunare un parametro empirico

**Esempio**: i canali sui lati lunghi sembrano troppo distanti rispetto al video Moldboxer.

1. **Identifica la costante**: cerca con grep. `CHANNEL_SPACING_FACTOR` è in [channels.py](channels.py).

2. **Verifica visualmente**: lancia il live test (ricetta 2), cattura screenshot.

3. **Confronta** con uno screenshot del video Moldboxer (timestamp da [Moldboxer Guide.txt](../Moldboxer%20Guide%20%E2%80%93%20Part%201%20Core%20Tools.txt)). Cerca "channels" nel video — appaiono attorno a [11:15-13:50].

4. **Misura** approssimativamente: quanti canali per lato? Quanto distanti in mm rispetto alla dimensione X del box?

5. **Modifica** la costante. Documenta la motivazione con un commento:
   ```python
   # Tuned 2026-05-15 against video [11:30] — chicken model ~80mm shows 3 channels/side.
   CHANNEL_SPACING_FACTOR = 25.0
   ```

6. **Re-test** live. Itera.

7. **Non modificare** le costanti prese 1:1 da Moldboxer (sezione "Costanti hardcoded estratte da Moldboxer" in [README.md](README.md)). Quelle sono ground truth.

---

## Ricetta 6: Debuggare un boolean fallito

**Sintomo**: il mold appare "bucato", o il `silicone_mold` è vuoto, o vedi `<EMPTY>` in scena.

1. **Controlla i Boolean modifiers vuoti**:
   ```python
   for obj in bpy.data.objects:
       for m in obj.modifiers:
           if m.type == "BOOLEAN" and m.object is None:
               print(f"EMPTY BOOLEAN on {obj.name}: {m.name}")
   ```
   Equivalente: `Object(obj).has_empty_boolean` ritorna True.

2. **Riproduci con boolean MANIFOLD vs EXACT**: in [constants.py](constants.py) cambia `DEFAULT_BOOLEAN_SOLVER` a `EXACT` e rilancia. Se EXACT funziona ma MANIFOLD no → bug Blender o mesh degenere. Considera di forzare un voxel remesh prima del boolean.

3. **Verifica manifold**: chiama `Object.is_manifold()`. Se False → fai heal prima.

4. **Controlla l'ordine**: in Moldboxer, `apply_modifier(mod, index_first=True)` sposta il modifier in posizione 0 PRIMA di applicarlo. Se hai deviato da questo, fixa.

5. **Isola**: riduci il problema a `simple_cube - simple_sphere`. Se anche questo fallisce, è un bug Blender. Se funziona, il problema è specifico della tua mesh.

---

## Ricetta 7: Aggiungere una costante o parametro al sistema

**Esempio**: vuoi un nuovo parametro `key_pyramid_top_scale` per `add_interlock_keys`.

1. **Dichiara in [constants.py](constants.py)** se è una costante "magica":
   ```python
   DEFAULT_KEY_PYRAMID_TOP_SCALE = 0.7  # tronco di piramide, Moldboxer-style
   ```

2. **Aggiungi alla signature** della funzione, con default che punta alla costante:
   ```python
   def add_interlock_keys(..., key_pyramid_top_scale: float = DEFAULT_KEY_PYRAMID_TOP_SCALE):
       ...
   ```

3. **Documenta in [README.md](README.md)** nella tabella "Costanti TUNATE EMPIRICAMENTE".

4. **Esponi via INTEGRATION** se è un tool MCP: aggiungi al §2 dei mapping.

---

## Ricetta 8: Aggiornare la documentazione dopo un cambio significativo

Quando completi un task del backlog:

1. **Aggiorna [../NEXT_STEPS.md](../NEXT_STEPS.md)**:
   - Sposta la riga del task da `❌/⏳` a `✅` nella tabella stato.
   - Cancella la voce dal backlog se chiusa definitivamente.
   - Aggiungi log entry in fondo (data + riga di cosa hai fatto).

2. **Aggiorna [README.md](README.md)** sezione "Stato di completamento" se il task riguardava un componente.

3. **Aggiorna [INTEGRATION.md](INTEGRATION.md) §2** se hai aggiunto/modificato API pubbliche.

4. **Rilancia smoke test** (ricetta 1) per essere sicuro che nulla si sia rotto.

---

## Ricetta 9: Rigenerare la decompilazione (se il pyc cambia o vuoi pylingual)

Stdlib version (sempre disponibile):
```bash
"C:/Users/.../Blender/5.0/python/bin/python.exe" \
  ../tools/pyc_to_pseudo.py \
  --tree ../moldboxer_silicone/source ../decompiled_py
```

Versione pylingual (richiede `pip install pylingual` autorizzato):
```bash
pylingual ../moldboxer_silicone/source/<file>.pyc -o ../decompiled_real_py/
```

---

## Cose da NON fare

- **Non modificare i file in `../decompiled_py/`** — sono output rigenerabili.
- **Non chiamare `*.moldboxer.com`** da `moldboxer_lite/`. La libreria è offline by design.
- **Non duplicare costanti** già in [constants.py](constants.py). Centralizza.
- **Non cambiare le costanti "1:1 Moldboxer"** (BOX_QUALITY_MAP, WING_WIDTH, ecc.) senza motivo forte. Sono ground truth dal bytecode.
- **Non saltare il smoke test** dopo modifiche. Sono 2 secondi.
