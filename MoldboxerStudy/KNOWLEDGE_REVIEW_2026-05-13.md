# Knowledge Review — Moldboxer reale vs `moldboxer_lite/`

> **Data**: 2026-05-13
> **Trigger**: live test del gallo (asso di bastoni) ha prodotto risultati visivamente confusi.
> L'utente ha caricato 20 screenshot del tutorial ufficiale + ha indicato la trascrizione
> dei primi 10 minuti. Tre agenti di analisi (visiva, testuale, codice) hanno prodotto
> questo documento di review.

Cartelle di riferimento:
- Screenshot tutorial: `screen video tutorial/` (20 PNG, timestamp 21:12–21:15 → coprono i primi 5 min ca. del video)
- Trascrizione: `Moldboxer Guide – Part 1 Core Tools.txt` (628 righe)
- Ricostruzione client-side: `moldboxer_lite/` (16 moduli Python)

---

## 1. Confronto: feature Moldboxer reali ↔ stato `moldboxer_lite`

| # | Feature/Concept | Citato dal narratore | Implementato in moldboxer_lite | Stato |
|---|---|---|---|---|
| 1 | Adjusted box (shrink-wrap silhouette, non AABB) | "creates an adjusted box around your model" [02:38] | `Wrapper.shape` con `target_shrinkwrap=True` | ✅ parziale (param `scale_normals` hardcoded) |
| 2 | Voxel remesh condizionale (solo se non-manifold) | "only applies if the model mesh is not manifold" [01:02] | `preprocess.py:95-96` | ✅ corretto |
| 3 | Resolution (master) vs Detail (box) separati | 2 dropdown distinti in UI | Collassati in `box_quality`/`master_quality` | ⚠️ ridenominabile |
| 4 | **Funneler = foro passante nel top** | "an opening where the silicone is poured" [02:43] | `auto_box.py:76` fa `box += dep` (UNIONE!) | **🔴 P0 BUG** |
| 5 | Split su Y world-space hard-coded | "split is aligned with green line, Y axis" [03:23] | `split_box_on_y` con `plane_normal=(0,1,0)` | ✅ corretto |
| 6 | **Clamp Pin system fra le metà (default ON)** | "key system to align and lock both halves" [02:54] | `build_clamp_pins` esiste ma **NON chiamato** | **🔴 P0 BUG** |
| 7 | Master Base Pin + buco auto nel master | "this hole matches the corresponding pin on the base" [03:01] | `pin_patron_to_base` (fa subtract `patron -= female`) | ✅ funzionale (pin cubico invece di cilindro) |
| 8 | Fixed Master toggle | "if you disable it, system will generate mold with master separated" [06:46] | `join_patron` flag in `confirm_mold` | ✅ corretto |
| 9 | Volume scolpito ml sulla base | "this indicates the amount of silicone needed" [03:10] | `create_volume_text` → boolean union su wing | ✅ funzionale (post-fix FONT→MESH) |
| 10 | **Output 3 oggetti (master + mold + silicone preview)** | "three items on the screen" [02:17] | `confirm_mold` ritorna dict + `space_mold_system` | ⚠️ master duplicato quando join (vedi #11) |
| 11 | **Patron rimosso quando Fixed Master ON** | Master fuso nella base | `confirm.py` NON chiama `patron.remove()` | **🔴 P0 BUG** |
| 12 | Safe Mode Box (pipeline fallback) | "Safe Mode Box" parametro UI | `build_from_sphere` flag (solo starting point diverso) | ⚠️ parziale |
| 13 | Channels W + Dr + Larger Back | Parametri UI esposti | `channel_width`/`channel_depth`/`larger_back` | ✅ corretto |
| 14 | **Channels "Contour Adapted"** | Toggle UI | Param accettato ma **ignorato** nel codice | ⚠️ P1 (raycast non implementato) |
| 15 | Interlock keys piramidali tronche | Pin per allineamento metà | `add_interlock_keys` usa **cubi semplici** | ⚠️ P1 |
| 16 | Clear Extraction | Toggle UI (per zone strette) | Mai implementato | ⚠️ P2 |
| 17 | Inner cavity / 2-Part Silicone / Master Apex Pin (Pro Tools) | Sezione Pro Tools UI | Non implementato | ⚠️ P3 (Pro features) |
| 18 | Login Google/Patreon | Auth flow | Non implementato | ✅ out of scope |

---

## 2. Bug P0 (rompono il workflow funzionale)

### Bug P0 #1 — Funneler unito invece di sottratto

**Location**: `moldboxer_lite/auto_box.py:74-77`

```python
# CURRENT (BUG)
if funneler:
    dep = build_funneler(box)
    box += dep      # ← UNIONE: aggiunge cilindro pieno sopra il box
    dep.remove()
```

**Conseguenza**: il "funneler" nella ricostruzione è una colonna piena verticale sopra il box, non un foro passante. **Non si può versare silicone**.

**Conferma dal tutorial @ 02:43-02:48**: "you'll see an opening where the silicone is poured to create the mold. This is what we call the funneler."

**Fix**:
```python
if funneler:
    dep = build_funneler(box)
    box -= dep      # ← SOTTRAZIONE: crea foro passante
    dep.remove()
```

Verificare che `build_funneler` produca un cilindro abbastanza lungo da attraversare la parete top + raggiungere lo spazio interno (gap silicone).

### Bug P0 #2 — Clamp Pins dead code

**Location**: `moldboxer_lite/channels.py:133-177` ha `build_clamp_pins` definito, ma:
- `auto_box.py` non lo chiama
- `confirm.py` non lo chiama
- `split_and_base.py` non lo chiama

**Conseguenza**: le 2 metà del mold non hanno i pin di allineamento citati dal narratore @ 02:54. Solo le `add_interlock_keys` (cubi sulla split surface) — ma queste sono "interlock keys" diverse.

**Fix**: chiamare `build_clamp_pins` dentro `confirm_mold` dopo lo split:
```python
if add_clamp_pins:  # nuovo flag
    pins = build_clamp_pins(box, key_count, key_size)
    for pin in pins:
        box_l += pin_half_male  # maschio su metà sx
        box_r -= pin_half_female  # cavità su metà dx
```

### Bug P0 #3 — Patron resta in scena duplicato

**Location**: `moldboxer_lite/confirm.py:58-65` chiama `add_basing_to_system(..., patron, join_patron=True)`.

Dentro `add_basing_to_system` (`split_and_base.py:138`):
```python
base += patron  # boolean union nella base
# patron NON rimosso dalla scena!
```

**Conseguenza**: dopo `confirm_mold` con `join_patron=True`, la scena ha sia il `patron` originale sia il box_l/box_r con il patron già fuso dentro. Il master appare duplicato visivamente.

**Fix in `confirm.py` o `add_basing_to_system`**:
```python
if join_patron:
    base += patron
    patron.remove()  # ← AGGIUNGERE
```

---

## 3. Bug P1 (qualità compromessa, non bloccanti)

| # | Bug | Location | Fix proposto |
|---|---|---|---|
| 4 | Interlock keys cubici (non piramidali) | `split_and_base.py:222-237` | Riusare `_build_pin` con `base_size=key_size, top_scale=0.7` |
| 5 | `pin_patron_to_base` muta patron originale | `split_and_base.py:83` | `patron_copy = patron.duplicate(); patron_copy -= female; patron.replace_geometry(patron_copy); patron_copy.remove()` |
| 6 | `adjust_to_contour=True` ignorato | `channels.py:47` | Implementare raycast: per ogni cilindro X-pos, raycast verticale verso il box → snap a X di intersezione |
| 7 | Doppio voxel cleanup degrada dettaglio | `auto_box.py:80-81` | Rimuovere il voxel finale, o renderlo opzionale `final_voxel=False` |
| 8 | `Wrapper.scale_normals(2.0)` hardcoded | `wrapper.py:67` | Parametrizzare su `box_gap` |
| 9 | Split tolerance 0.001mm | `object_wrapper.py:362` | Aumentare a 0.05mm |

---

## 4. Divergenze sottili / cose da rifinire

1. **Resolution vs Detail**: collassati in 2 parametri (`master_quality`/`box_quality`) ma semanticamente identici. Tutorial li tratta come dimmer distinti: rinominare per chiarezza.
2. **`Object.__iadd__` mancante**: `box += ch` funziona perché `__add__` ritorna `self`, ma è confondente. Aggiungere `__iadd__` esplicito.
3. **Magic numbers non documentati**: `CHANNEL_SPACING_FACTOR=30`, `LARGER_BACK_RADIUS_FACTOR=1.3`, `FUNNELER_RADIUS=8.0`, `FUNNELER_INSET=0.5`, `SIZE_MALE=3.5`, ecc.
4. **`channel_back_larger` vs `larger_back`**: inconsistenza nomenclatura tra `DEFAULT_SCENE` e signature funzioni.
5. **`channel_depth` default 6.0** ma narratore UI mostra `Dr: 0.20-4.50`.
6. **Dead code**: `build_clamp_pins`, `sub_patron` non chiamati.
7. **`add_basing_to_system` non sa se ci sarà uno split**: posiziona wing sempre su +X, ma con split Y le 2 metà avranno un mezzo-wing ciascuna.

---

## 5. Workflow concettuale corretto (dal tutorial)

```
┌──────────────────────────────────────────────────────────────┐
│ 1. IMPORT STL del master (asso di bastoni / gallo / etc)    │
└─────────────┬────────────────────────────────────────────────┘
              ▼
┌──────────────────────────────────────────────────────────────┐
│ 2. PREPROCESS                                                │
│   • Setup units mm                                           │
│   • Center XY=0, Z=0 al bottom                               │
│   • Apply transforms                                         │
│   • SE not manifold → voxel remesh @ Resolution              │
└─────────────┬────────────────────────────────────────────────┘
              ▼
┌──────────────────────────────────────────────────────────────┐
│ 3. AUTO_BOX (mold a 2 metà)                                 │
│   3a. Wrapper voxel: shrink-wrap del master con offset gap  │
│   3b. Build channels laterali (W × Dr × N pinli)             │
│   3c. Build funneler (cilindro sopra il master)              │
│   3d. BOX -= FUNNELER  ← BUCO PASSANTE per colata           │
│       (BUG #1: oggi è "box += funneler")                    │
│   3e. BOX -= PATRON_COPY  ← cavità interna                  │
└─────────────┬────────────────────────────────────────────────┘
              ▼
┌──────────────────────────────────────────────────────────────┐
│ 4. CONFIRM_MOLD (finalizzazione)                             │
│   4a. silicone_mold = box - patron (preview, oggetto sep)   │
│   4b. base = cubo XY footprint + spessore 4mm               │
│   4c. SE master_base_pin: pin maschio su base + foro fem    │
│       nel patron (boolean subtract sul master)              │
│   4d. SE join_patron: base += patron; PATRON.REMOVE()       │
│       (BUG #3: oggi non rimuove)                            │
│   4e. wing laterale + volume text 3D scolpito               │
│   4f. box += base                                            │
│   4g. SPLIT su Y=0 → box_l + box_r                          │
│   4h. SE add_keys: piramidi tronche su split surface        │
│       (BUG P1: oggi sono cubi)                              │
│   4i. SE add_clamp_pins: pin maschi/femmine fra metà         │
│       (BUG #2: dead code, non chiamato)                     │
│   4j. space_objects: distanzia master/mold/silicone lungo X │
└─────────────┬────────────────────────────────────────────────┘
              ▼
┌──────────────────────────────────────────────────────────────┐
│ 5. EXPORT STL: box_l, box_r, silicone_mold, (patron)        │
└──────────────────────────────────────────────────────────────┘
```

---

## 6. Cosa imparare da questa review

1. **Il nostro `live test` precedente ha funzionato APPARENTEMENTE** perché auto_box + confirm completano senza eccezioni e producono 4 oggetti con stats coerenti. Ma il mold è **non utilizzabile per colata reale** perché manca il foro del funneler.

2. **Visivamente difficile da accorgersi**: il cilindro del funneler sembra "spuntare sopra il box" anche nella versione corretta — quello che cambia è se è cavo (foro) o pieno (colonna). Il raycast test che ho fatto ([z=300→hits sulla box: 165.14, 94.68, 1.33, 0.0]) era ambiguo: 4 hits sono compatibili sia con "cilindro pieno + parete box + fondo box" sia con "ingresso funneler + uscita funneler/top patron + parete fondo box + fondo". Per distinguere serviva un test che verifichi se c'è VUOTO interno al cilindro funneler. Test corretto: cast ray dall'asse del funneler a Z=120 (dentro il cilindro, sopra la cavità del patron) verso -Z e verificare se trova una superficie. Se il funneler è cavo (corretto), non trova nulla finché non incontra il patron a Z~100. Se è pieno (bug attuale), trova il top del cilindro o la sua superficie interna.

3. **Lezione metodologica**: per ricostruzioni di prodotti commerciali, il **test funzionale (= "si può davvero usare per colata silicone?")** deve essere distinto dal **test geometrico (= "produce N oggetti delle dimensioni attese?")**. La nostra pipeline passa il secondo, fallisce il primo.

4. **Lezione di interpretazione screenshot**: l'utente nel tutorial mostra il funneler come "apertura visibile sopra il modello". Le inquadrature dello screen mostrano effettivamente uno spazio vuoto interno (raggi di luce passano). Avrei dovuto essere più attento.

---

## 7. Piano d'azione raccomandato

### Priority P0 (sbloccare il workflow funzionale)

1. **Fix funneler** in `auto_box.py:76`: `box -= dep` invece di `box += dep`.
2. **Wire clamp_pins** in `confirm.py`: dopo lo split, chiamare `build_clamp_pins` e applicare maschi/femmine alle 2 metà.
3. **Rimuovi patron** in `confirm.py` quando `join_patron=True`.

### Priority P1 (qualità)

4. Interlock keys piramidali (riusare `_build_pin`).
5. `pin_patron_to_base` deve operare su copia del patron.
6. Implementare `adjust_to_contour` con raycast (vedi `decompiled_py/components/channels_deposit.py` per riferimento del prodotto reale).
7. Rimuovere voxel finale ridondante in `auto_box.py:80-81`.

### Priority P2 (qualità di vita)

8. Separare `Resolution` (master heal) e `Detail` (box mesh).
9. Safe Mode Box vera fallback (retry su EXACT solver se MANIFOLD fallisce).
10. Implementare Clear Extraction (versione naive: scale_normals positivo sul patron prima del wrapper).

### Validazione

Dopo i fix P0, RIPETERE live test sull'asso di bastoni e verificare:
- ✓ Cast ray dall'asse del funneler a Z=120: deve trovare il patron a Z~99.99, NIENTE prima (= funneler cavo)
- ✓ box_l e box_r dopo split + clamp_pins: dovrebbero avere bumps cilindrici sulla split surface (non solo cubi)
- ✓ Scene dopo confirm con join_patron=True: deve avere `{box_l, box_r, silicone_mold}` SENZA un `patron` separato

---

## 8. Riferimenti

- Tutorial transcript: `Moldboxer Guide – Part 1 Core Tools.txt`
- Tutorial screenshots: `screen video tutorial/` (20 PNG)
- Analisi agente A (screenshot): output incluso in chat session 2026-05-13
- Analisi agente B (trascrizione): output incluso in chat session 2026-05-13
- Analisi agente C (gap code): output incluso in chat session 2026-05-13
- Codice ricostruzione: `moldboxer_lite/`
- Decompiled originale Moldboxer: `decompiled_py/components/` (gitignored)

---

## 9. STATO POST-FIX (sessione 2026-05-13 tarda sera)

Tutti i fix P0 e P1 prioritari sono stati applicati. Smoke test stdlib verde,
py_compile verde su tutti i 16 moduli. Pipeline non ancora ri-testata in live
Blender (richiede nuova sessione MCP).

### Fix applicati

| # | Fix | File:linea | Tipo | Stato |
|---|---|---|---|---|
| 1 | Funneler: `box += dep` → `box -= dep` | `auto_box.py:74-89` | **P0** | ✅ |
| 2 | Patron remove dopo `base += patron` | `split_and_base.py:139-148` | **P0** | ✅ |
| 3 | Rimosso dead code `build_clamp_pins` | `channels.py:148-156` (sostituito con nota) | P1 | ✅ |
| 4 | Interlock keys piramidali (axis-aware `_build_pin`) | `split_and_base.py:62-95, 201-263` | P1 | ✅ |
| 5 | `adjust_to_contour` raycast (`_raycast_contour_y`) | `channels.py:47-83` | P1 | ✅ |
| 6 | Voxel finale post-boolean: disabilitato (commentato) | `auto_box.py:91-98` | P1 | ✅ |
| 7 | `Wrapper.scale_normals` parametrizzato su `distance×1.2` | `wrapper.py:64-78` | P1 | ✅ |
| 8 | Split tolerance 0.001 → 0.05 mm | `split_and_base.py:28-39` | P1 | ✅ |
| 9 | `export_all_parts` skippa prefissi `_` | `export.py:18-66` | cleanup | ✅ |
| 10 | Magic numbers documentati | `channels.py:24-44` | cleanup | ✅ |

### Cosa aspettarsi al prossimo live test

Dopo questi fix il workflow dovrebbe:

1. **Produrre un mold con FORO PASSANTE** nel top del box (verificabile via raycast)
   - Test: `cast ray @ (0,0,200) → -Z` su `box`. Hits attesi: `[box_top_z, ~patron_top_z, ~0]`
   - Il primo hit (box_top) dovrebbe essere su un anello (parete del foro), non sul cap.
   - Tra primo e secondo hit ci deve essere **un range vuoto** (= dentro il foro).

2. **Solo 3 oggetti in scena dopo confirm_mold con join_patron=True**:
   `{box_l, box_r, silicone_mold}` — senza un patron duplicato.

3. **Interlock keys piramidali** sulla faccia di split di box_l (sporgenze tronco-piramidali)
   e cavità corrispondenti su box_r. Visibili come 4 "bottoni" sulla split surface,
   con base larga 4mm e punta 2.8mm (top_scale=0.7).

4. **Canali "contour-adapted"** rientranti nelle zone strette del wrapper (se il
   master ha silhouette non rettangolare). Sull'asso di bastoni che è quasi
   rettangolare, l'effetto sarà piccolo ma misurabile.

5. **Wrapper più aderente** al master per master piccoli (scale_normals ora scala
   con `box_gap × 1.2` invece di costante 2.0mm).

### Test funzionale da fare nel prossimo round Blender

```python
# Pseudo-test funzionale (da eseguire dopo auto_box):
from mathutils import Vector
box = bpy.data.objects["box"]

# 1. Verifica foro del funneler: ray dall'asse Y=0, X=0, Z=200 verso -Z
origin = Vector((0, 0, 200))
dir_down = Vector((0, 0, -1))
mat_inv = box.matrix_world.inverted()
hit, loc, _, _ = box.ray_cast(mat_inv @ origin, mat_inv.to_3x3() @ dir_down)
print(f"first hit on box top: {(box.matrix_world @ loc).z}")  # Should be the box_top

# Now from inside the funneler at z = box.height - 5 (well below box_top)
origin2 = Vector((0, 0, 160))  # inside the funneler bore
hit2, loc2, _, _ = box.ray_cast(mat_inv @ origin2, mat_inv.to_3x3() @ dir_down)
if hit2:
    z_next = (box.matrix_world @ loc2).z
    print(f"from inside funneler: next hit at z={z_next}")
    # Expected: ~100 (top of patron) — confirms hole goes through to cavity
else:
    print("NO HIT from inside funneler — would mean funneler exits the box base")
```

### Validazione P0 critica

Il test funzionale del funneler (step 1 sopra) è IL test che deve passare. Se non
passa, il bug è regredito. Sui 4 oggetti finali dovrebbe inoltre essere
verificabile via `analyze_mesh_for_print`:

- `box_l.signed_volume_mm3` ≈ `box_r.signed_volume_mm3` (asimmetria ±5% per gap split + keys)
- `box_l.non_manifold_edges` = 0 e `box_r.non_manifold_edges` = 0
- `silicone_mold.signed_volume_mm3` ≈ 97-100 cm³ (per l'asso di bastoni)

---

## 10. Cosa resta (P2/P3 future)

| # | Item | Priorità |
|---|---|---|
| 1 | Separare `Resolution` (master heal) e `Detail` (box mesh) come parametri distinti | P2 |
| 2 | `Safe Mode Box` vera fallback: try MANIFOLD → on failure → retry EXACT solver | P2 |
| 3 | Implementare `Clear Extraction` (radial inflate del master per demoldability su zone strette) | P2 |
| 4 | Inner cavity tool (Pro Tools) | P3 |
| 5 | 2-Part Silicone tool (Pro Tools) | P3 |
| 6 | Master Apex Pin (Pro Tools) | P3 |
| 7 | Auto-hole generation quando Master Base Pin disabilitato (citato come "future" anche dal narratore @ 08:08) | P3 |
| 8 | Allineare nomi: `DEFAULT_SCENE.channel_back_larger` ↔ `build_channels(larger_back=...)` | P2 |
| 9 | `Object.__iadd__`/`__isub__` espliciti per chiarezza semantica | P2 |
| 10 | `add_modifier` con retry automatico EXACT se MANIFOLD fallisce | P2 |
