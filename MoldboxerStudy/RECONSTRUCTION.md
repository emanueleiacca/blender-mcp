# RECONSTRUCTION — cosa puoi fare offline, cosa devi ricostruire

> Obiettivo: istruire un MCP che usa Blender con capacità Moldboxer-like, senza copiare il software. Questa guida traccia il confine client/server, inventaria il codice utilizzabile come riferimento, e mappa cosa serve costruire per coprire i buchi.

---

## TL;DR

Il client Moldboxer fa ~80% delle operazioni in locale con Blender + bmesh. Il server fa il **20% "intelligente"**: la generazione geometrica del box che avvolge il master, l'inserimento di canali/inlet, e la finalizzazione boolean del silicone. Cinque endpoint server, tutto il resto è offline.

| Cosa | Quanto è ricostruibile |
|---|---|
| Tutte le 13 utility Blender wrapper (Object class, mesh ops, modifiers) | **Già a disposizione** in pseudo-Python decompilato — leggi e re-implementa |
| Pipeline orchestrazione (preprocess, split, base, materials, export, grip) | **Già a disposizione** completa in pseudo-Python |
| Auto-flat (mold piatto) | Server-dipendente, ma il setup intorno è chiaro → **medio-facile** ricostruire |
| Auto-box (mold a 2 pezzi) | Server-dipendente, parametri esatti noti → **medio** ricostruire |
| Channels + deposit (canali e funneler) | Server-dipendente, behavior chiaro dal video → **medio** ricostruire |
| Confirm silicone mold (boolean finale + split + keys) | Server-dipendente → **medio-difficile** (la qualità delle keys è marketing-visible) |
| Inner cavity (Pro) | Server-dipendente, semantica avanzata → **difficile** ma non bloccante |

---

## 1. Mappa client / server definitiva

### 1.1 Componenti puramente CLIENT (13 — tutti già in [decompiled_py/](decompiled_py))

Non chiamano mai `request_server`. Tutto bpy/bmesh/mathutils.

| Componente | Cosa fa | Riusabilità per MCP |
|---|---|---|
| [object.py](decompiled_py/object.py) | Classe `Object`: 100+ metodi su mesh (bbox, scale, cut_plane, split, apply_modifier, manifold check, vertex groups, ecc.) | ⭐⭐⭐ Riferimento diretto |
| [modifiers.py](decompiled_py/modifiers.py) | Helper `build_voxel_modifier`, `build_decimate_collapse`, ecc. | ⭐⭐⭐ Riferimento diretto |
| [primitives.py](decompiled_py/primitives.py) | `create_uv_sphere_primitive`, ecc. | ⭐⭐⭐ Riferimento diretto |
| [bl_utils.py](decompiled_py/bl_utils.py) | Import STL/OBJ, configurazione unità mm, viewport overlay | ⭐⭐⭐ |
| [materials.py](decompiled_py/materials.py) | Materiali generati per i mold parts | ⭐⭐ |
| [voxel_size.py](decompiled_py/voxel_size.py) | Mappatura `quality` enum → voxel size float | ⭐⭐⭐ |
| [preprocess.py](decompiled_py/components/preprocess.py) | `preprocess_patron`: join, voxel heal se non manifold, center, isolate | ⭐⭐⭐ |
| [wrapper.py](decompiled_py/components/wrapper.py) | Classe `Wrapper(Object)`: voxel-based offset hull (è LA ricetta locale per costruire il box iniziale) | ⭐⭐⭐ **chiave** |
| [box.py](decompiled_py/components/box.py) | `build_box`: costruisce il wrapper + clean_top se no funneler + extraction path | ⭐⭐⭐ |
| [splitter.py](decompiled_py/components/splitter.py) | `split(n_splits)`: divide il mold finale in 2 metà sull'asse Y | ⭐⭐⭐ |
| [base.py](decompiled_py/components/base.py) | `add_basing_to_system`: aggiunge base + pin master + volume text | ⭐⭐⭐ |
| [extraction.py](decompiled_py/components/extraction.py) | `clear_horizontal_extraction_path`, `clear_vertical_extraction_path`: rimuove undercuts | ⭐⭐⭐ **chiave per qualità** |
| [grip.py](decompiled_py/components/grip.py) | `build_grip`, `add_grip`: manico per flat molds | ⭐⭐⭐ |
| [export.py](decompiled_py/components/export.py) | Export STL multi-oggetto con nome `<obj>_<volume>ml.stl` | ⭐⭐⭐ |
| [silicone_mold.py](decompiled_py/components/silicone_mold.py) | `build_silicone_mold_preview`, `sub_patron`, `create_volume_text` | ⭐⭐⭐ |
| [split_connector.py](decompiled_py/components/split_connector.py) | Connettore cilindrico per split utility | ⭐⭐ |
| [two_parts.py](decompiled_py/components/two_parts.py) | Pro: orchestrazione flow 2-part silicone (chiama anche server) | ⭐⭐ misto |
| [auto_flat.py](decompiled_py/components/auto_flat.py) | Orchestrazione flat mold (chiama `open` che è server) | ⭐⭐ misto |
| [auth.py](decompiled_py/components/auth.py) | OAuth device code Google/Patreon | non rilevante per te |

### 1.2 Componenti SERVER-dipendenti (5)

Ogni file qui sotto contiene esattamente UNA chiamata `request_server(url, obj_names, params)`. Tutto il resto del file è preparazione e post-processing locale.

| Componente | Endpoint | Operatore che lo invoca | Obj inviati | Params inviati |
|---|---|---|---|---|
| [auto_box.py](decompiled_py/components/auto_box.py) | `POST /auto-box/` | `silicone.auto_box` (Auto Box) | `['box']` | `box_voxel_size, channel_width, n_splits, channel_depth, adjust_to_contour, larger_back, add_funneler, add_pins` |
| [channels_deposit.py](decompiled_py/components/channels_deposit.py) | `POST /channels-deposit/` | `silicone.build_box` (Advanced step 1) | (vedi decompiled) | (vedi decompiled) |
| [confirm_mold.py](decompiled_py/components/confirm_mold.py) | `POST /confirm-silicone-mold/` | `silicone.confirm` (Advanced step 2) | (vedi decompiled) | (vedi decompiled) |
| [open.py](decompiled_py/components/open.py) | `POST /auto-flat/` | `silicone.flat_auto_box` (Flat Auto Box) | (vedi decompiled) | (vedi decompiled) |
| [inner_core.py](decompiled_py/components/inner_core.py) | `POST /inner-core/` | Pro inner cavity | (vedi decompiled) | (vedi decompiled) |

Per i 4 endpoint dove non ho elencato i params (per brevità), basta `grep "KW_NAMES\|/.*/" decompiled/components/<file>.md` per trovarli — la struttura è sempre la stessa: keyword args impacchettati con `BUILD_CONST_KEY_MAP`.

### 1.3 Il pattern di chiamata server

Ogni chiamata server fa esattamente questa cosa (vedi `request_server` in [server.py](decompiled_py/components/server.py)):

```
1. Costruisce zip in temp_dir con PLY di ogni oggetto in obj_names
2. POST multipart al backend con:
   - file: zip
   - JSON params come query string (bool → 'true'/'false')
   - Authorization: Bearer <access_token>
3. Riceve zip in risposta
4. import_server_response: scompatta, importa i PLY come nuovi oggetti, RIMUOVE gli oggetti vecchi con lo stesso nome
```

Questo è esattamente quello che devi replicare se vuoi sostituire un endpoint: ricevi un mesh + params, ritorni un mesh.

---

## 2. Cosa puoi fare oggi senza il server (offline-only)

Con i 13 componenti client già decompilati puoi costruire da solo questi flussi:

### 2.1 Pre-elaborazione modello (100% locale)
- Import STL/OBJ → `import_model(path)` in [bl_utils.py](decompiled_py/bl_utils.py)
- Heal non-manifold → `Wrapper(target, voxel_size, n_wraps=1)` o direttamente voxel remesh modifier
- Center → `bpy.ops.object.origin_set(type='GEOMETRY_ORIGIN', center='BOUNDS')` + traslazione Z
- Scale → `selected_obj.scale(factor, axis)` (metodo della classe `Object`)
- Decimate → `selected_obj.apply_modifier(build_decimate_collapse(0.4))`
- Configure mm units → `configure_metric_millimeter_units()` in [bl_utils.py](decompiled_py/bl_utils.py)

### 2.2 Costruzione box wrapper locale (100% locale)
Il pezzo chiave è la classe `Wrapper` in [wrapper.py](decompiled_py/components/wrapper.py). La ricetta:

```python
# Costruisci un "box" che avvolge il master:
w = Wrapper(
    target=patron_object,        # il master 3D
    voxel_size=0.5,              # finezza voxel (mm)
    distance=6,                  # box_gap (spessore silicone)
    decimate=True,               # decimate finale 0.3
    n_wraps=3,                   # n. iterazioni voxel remesh
    geometry_to_origin=True,
    cut_bot=True,                # taglia il fondo a Z=0
    build_from_sphere=False      # True = parte da UV sphere (safe mode)
)
# Internamente fa:
#   se build_from_sphere: parte da UV sphere primitive scalata
#   altrimenti: duplica target, scale_normals(2) → mesh espansa outward
#   poi: voxel-remesh n_wraps volte
#   poi: decimate (0.3) se richiesto
#   poi: cut_bot a Z minimo se richiesto
```

Questo è il "box grezzo" che il client locale già produce. È lo stesso che viene inviato a `/auto-box/` come input — il server poi lo raffina.

### 2.3 Estrazione undercuts (100% locale)
`clear_horizontal_extraction_path(extrude_dist, voxel_size)` in [extraction.py](decompiled_py/components/extraction.py): apre un canale lungo l'asse di estrazione per evitare che il mold si blocchi durante il demolding. Funzione locale già scritta, ricetta probabilmente:
1. Trova le facce piatte sull'asse Y (split direction)
2. Estrudi verso l'esterno per extrude_dist
3. Sottrai dal box

### 2.4 Boolean silicone (100% locale)
- `build_silicone_mold_preview(voxel_size)` in [silicone_mold.py](decompiled_py/components/silicone_mold.py) — costruisce l'anteprima visibile del volume di silicone.
- `sub_patron(box_voxel_size)` — sottrae il master dal box per produrre la cavità del silicone.

Le boolean ops nel codice usano apparentemente l'overload di operatori della classe `Object`:
- `a + b` → unione (Boolean UNION modifier)
- `a - b` → sottrazione (Boolean DIFFERENCE)
- `a & b` → intersezione (Boolean INTERSECT)

Vedi [object.py](decompiled_py/object.py) per i metodi `__add__`, `__sub__`, `__and__`.

### 2.5 Split in metà (100% locale)
`split(n_splits)` in [splitter.py](decompiled_py/components/splitter.py): taglia l'assembled mold lungo l'asse Y in `n_splits` parti (0 o 2). Funzione locale.

### 2.6 Base + pin + volume text (100% locale)
`add_basing_to_system(volume, join_patron, master_base_pin)` in [base.py](decompiled_py/components/base.py): aggiunge base piana, pin di centratura del master, e scrive il testo del volume sul lato del box.

### 2.7 Grip (100% locale)
`build_grip(grip_height)` e `add_grip(box_voxel_size)` in [grip.py](decompiled_py/components/grip.py): genera il manico per i flat molds.

### 2.8 Export STL (100% locale)
`export(dir)` in [export.py](decompiled_py/components/export.py): salva ogni mesh come `<name>_<volume>ml.stl` o `<name>.stl`.

### 2.9 Utility taglio/pulizia (100% locale)
Tutti i `clean_top`, `clean_bot`, `cut_bot`, `clean_all_top` sono **metodi della classe `Object`** in [object.py](decompiled_py/object.py:80) (cerca quei nomi). Usano `cut_plane` (bmesh) + `extrude_selected`.

### 2.10 Grid multi-cavità (100% locale)
`Object.grid_obj(rows, cols, distance)` in [object.py](decompiled_py/object.py) — duplica il master con offset XY. Locale.

---

## 3. Cosa ti manca (server-side)

Per ognuno degli endpoint elenco:
- **Input esatto** (mesh + params) — sai cosa va dentro
- **Output esatto** (nuova mesh) — sai cosa torna
- **Comportamento visivo atteso** (dal video) — sai cosa deve fare
- **Ricetta proposta** per replicare la logica

### 3.1 `/auto-box/` — raffinamento box + canali + funneler + pin
- **Input**:
  - mesh: `box` (il wrapper grezzo già costruito da `Wrapper`)
  - params: `box_voxel_size, channel_width, n_splits, channel_depth, adjust_to_contour, larger_back, add_funneler, add_pins`
- **Output**: nuovo mesh `box` che sostituisce quello inviato.
- **Behavior atteso** (dal video [02:13-03:01] + [11:15-13:50]):
  - Box aderente al contorno con spessore costante = `channel_depth` (in realtà `box_gap` controlla la distanza, channel_depth è specifica dei canali — sono due cose diverse)
  - Canali "a colonna" sui lati verticali (numero non specificato, sembra calcolato dal contorno)
  - Se `add_funneler=True`: inlet cilindrico in cima (diametro non documentato — guarda screenshot video)
  - Se `add_pins=True`: pin di allineamento clamp tra le due metà
  - Se `adjust_to_contour=True`: i canali seguono il profilo; altrimenti dritti
  - Se `larger_back=True`: canale posteriore (asse +Y) più largo
- **Ricetta proposta** per ricostruirlo offline:
  ```python
  # PSEUDO — input: box_mesh (già wrapper-ato), params
  def fake_auto_box(box_mesh, params):
      # 1. ri-voxel se necessario
      box_mesh.apply_modifier(build_voxel_modifier(params.box_voxel_size))
      
      # 2. calcola posizione canali sui lati X (perché split è su Y)
      bbox = box_mesh.bound_box
      n_channels = max(2, int(bbox.x_width / 30))  # uno ogni ~30mm, da tarare
      channel_xs = linspace(bbox.x_min, bbox.x_max, n_channels)
      
      # 3. per ogni canale crea cilindro verticale
      for x in channel_xs:
          for y_sign in [-1, +1]:
              y = bbox.y_max if y_sign > 0 else bbox.y_min
              radius = params.channel_width / 2
              if y_sign > 0 and params.larger_back:
                  radius *= 1.3
              cyl = create_cylinder(x, y, z=bbox.z_center, radius=radius, height=bbox.z_height)
              if params.adjust_to_contour:
                  # snap il cilindro al profilo locale del master
                  snap_cylinder_to_contour(cyl, master)
              box_mesh = box_mesh + cyl  # union
      
      # 4. funneler in cima
      if params.add_funneler:
          funneler = create_cylinder(x=0, y=0, z=bbox.z_max, radius=8, height=20)
          box_mesh = box_mesh + funneler
      
      # 5. clamp pins
      if params.add_pins:
          for x in [-bbox.x_width/3, bbox.x_width/3]:
              pin = create_cylinder(x, 0, bbox.z_center, radius=2, height=bbox.z_height + 4)
              # va sull'asse di split, non union ma DIFFERENCE per fare il foro su una metà
              # (logica complessa — meglio rimandare a dopo lo split)
      
      return box_mesh
  ```
  Le costanti (8mm funneler, 30mm distanza canali, 1.3× back factor) sono **da tarare visivamente** confrontando con gli screenshot del video.

### 3.2 `/channels-deposit/` — stessi 3 oggetti SEPARATI
Identico a `/auto-box/` ma ritorna 3 oggetti distinti invece di uniti: `wrapper` (oro), `channels` (blu), `deposit` (verde-acqua). Servono per l'Advanced mode dove l'utente può spostarli singolarmente prima di unirli con Confirm.

> Video [14:24-14:30]: "In gold, the box wrapper that follows the shape of the model. In blue, the channels, in this case, not contour adapted. And in a more greenish tone, the deposit."

**Ricetta**: stessa di sopra ma senza l'union finale, ritornando 3 mesh distinte. Assegna i materiali dei 3 colori (vedi [materials.py](decompiled_py/materials.py)).

### 3.3 `/confirm-silicone-mold/` — finalizzazione
- **Input**: scena con `patron`, `wrapper`/`box`, `channels`, `deposit` (ora possibilmente spostati dall'utente)
- **Output**: mold system finale assemblato
- **Behavior** (dal video [14:50-15:36] + tutto il flusso AutoBox):
  - Union channels + deposit + wrapper → outer shell
  - Sottrai patron → silicone_mold (volume del silicone)
  - Aggiungi base + pin se richiesti
  - Split lungo Y in 2 metà
  - Aggiungi keys interlock sulla superficie di split
- **Ricetta proposta**:
  ```python
  def fake_confirm(patron, wrapper, channels, deposit, scene):
      # 1. Union shell
      shell = wrapper + channels + deposit
      
      # 2. Boolean sub master → silicone_mold (cavità)
      silicone_mold = shell - patron
      
      # 3. Base + pin
      shell = add_basing_to_system(volume=silicone_mold.volume,
                                    join_patron=scene.wing_join_patron,
                                    master_base_pin=scene.master_base_pin)
      
      # 4. Split su Y
      if scene.n_splits == 2:
          # Cut plane su Y=0
          half_a = shell.cut_plane(Vector(0,1,0), Vector(0,0,0))
          half_b = shell.cut_plane(Vector(0,-1,0), Vector(0,0,0))
          # Add keys on split surface
          add_interlock_keys(half_a, half_b, key_count=4)
      
      # 5. Volume text
      if not is_lite_tier:
          write_volume_text_on_box(silicone_mold.volume)
  ```
  
  **La parte tosta**: `add_interlock_keys` — keys triangolari/conici che combaciano. Approccio:
  - Sulla superficie di taglio, scegli N punti distribuiti
  - Su metà A: aggiungi piramidini in positivo
  - Su metà B: sottrai gli stessi piramidini con un piccolo offset (la "tolerance" Pro)

### 3.4 `/auto-flat/` — flat mold single piece
- **Input**: master + scene
- **Output**: mold piatto con top aperto + grip
- **Behavior** (video [04:40-05:30]):
  - Box rettangolare aderente alla footprint XY del master
  - Top completamente aperto
  - Grip su un lato (manico) per estrazione
- **Ricetta** (questo è il più semplice):
  ```python
  def fake_auto_flat(patron):
      # 1. Computa footprint XY del patron
      bbox = patron.bound_box
      
      # 2. Box rettangolare offsetato di box_gap
      gap = scene.box_gap
      box = create_box(
          x_min=bbox.x_min - gap, x_max=bbox.x_max + gap,
          y_min=bbox.y_min - gap, y_max=bbox.y_max + gap,
          z_min=0, z_max=bbox.z_max + gap  # un po' sopra il master
      )
      
      # 3. Voxel per addolcire (opzionale)
      # box.apply_modifier(build_voxel_modifier(box_voxel_size))
      
      # 4. Boolean sub patron
      box = box - patron
      
      # 5. Cut top open
      box.clean_top(bbox.z_max - 2)  # mantiene 2mm di rim
      
      # 6. Aggiungi grip su lato
      add_grip(box_voxel_size)
      
      return box
  ```

### 3.5 `/inner-core/` — inner cavity Pro
- **Input**: master + box + sensitivity (Aggressive/Balanced) + snap_tolerance
- **Output**: filler geometry "a vaso" inserita nel sistema
- **Behavior**: riduce il consumo di silicone creando un riempitivo interno che va inserito prima della colata.
- **Questa è davvero complessa**. La logica probabile:
  1. Voxelizza l'intero volume interno (silicone_mold)
  2. Erode con un kernel proporzionale a `sensitivity` (3=meno aggressivo, 1=più aggressivo)
  3. Rimuovi le componenti connesse troppo piccole
  4. Offset inverso per snap-fit con `snap_tolerance`
- **Suggerimento**: skippare per la prima iterazione MCP, non è una feature di base.

---

## 4. Strategia di ricostruzione consigliata per il tuo MCP

### Step 1: Tools che hai già pronti (zero ricostruzione)
Espone questi al tuo MCP basandoti direttamente sul pseudo-Python decompilato:

- `import_model(path)` — import STL/OBJ
- `heal_mesh(obj, quality)` — voxel remesh
- `center_object(obj)` — centra a origin
- `scale_to_height(obj, height_cm)` — scale uniforme per altezza
- `decimate(obj, factor)` — riduci poligoni
- `clean_top(obj, height)`, `clean_bot(obj, height)`, `cut_bot(obj, height)`, `clean_all_top(obj)` — taglio piano
- `grid_layout(obj, rows, cols, distance)` — multi-cavità
- `export_stl(obj, path)` — export
- `analyze_mesh_for_print(obj)` — già esposto come MCP tool, riusalo

Sono ~10 tool MCP a costo zero, ricavati dal codice in [decompiled_py/](decompiled_py).

### Step 2: Wrapper box locale (poco lavoro)
Re-implementa la classe `Wrapper` di [wrapper.py](decompiled_py/components/wrapper.py). È **40 righe** di codice quando re-scritto pulito (era pseudo-Python denso). Funzione:
```
wrap_master(obj, distance, voxel_size, n_wraps) -> wrapped_box
```
Pattern: duplica → scale_normals → voxel-remesh × n → decimate → cut_bot. Tutto bpy.

### Step 3: Boolean operations su Object
Re-implementa gli overload `+`, `-`, `&` per fare union/sub/intersect con i Boolean modifier di Blender. Pattern visibile in [object.py](decompiled_py/object.py).

### Step 4: Confirm "semplice" (l'80% del valore)
Re-implementa una versione "stupida" di `/confirm-silicone-mold/`:
- Union dei tre componenti
- Sub del master
- Split Y semplice (no keys)
- Base piana

Senza interlock keys il mold funziona comunque per stampaggi semplici. Le keys sono "qualità di vita" — ricostruibili dopo.

### Step 5: Auto-flat semplice
Re-implementa `/auto-flat/`. È il più facile dei server endpoints. Vedi ricetta 3.4 sopra.

### Step 6 (opzionale): Auto-box "approssimato"
Re-implementa `/auto-box/` con la ricetta 3.1. Le costanti vanno tarate visivamente. Punto debole: la qualità dei canali contour-adapted (richiede projection del cilindro sul profilo) — versione semplificata: canali dritti, niente contour adapt.

### Step 7 (avanzato): Interlock keys
Aggiungi le piramidi di interlock sulla superficie di split. Pattern: scegli N punti sulla split plane → aggiungi piramidi su una metà → sottrai con offset dall'altra.

### Step 8 (opzionale): Inner cavity
Solo se serve. Difficile.

---

## 5. Cosa NON è ricostruibile dal solo codice

Onestamente:
1. **I parametri di tuning interni del server** (es. quanti canali esattamente, dove esattamente, come adattano al contorno). Vanno tarati per replicare l'output visivo del video.
2. **La gestione delle edge cases** geometriche (modelli con concavità severe, mesh non manifold che il server "magicamente" ripara meglio del client). Le scopri solo testando.
3. **L'algoritmo esatto di contour-adapted channels** (probabilmente ray-cast o snap projection di cilindri sul profilo). Approssimabile ma non identico.
4. **L'algoritmo di rilevamento inner cavities** (servono primitive di analisi topologica come `compute_face_visibility_bvh` che è già esposto nel tuo MCP).

Buona notizia: per un MCP che istruisce un LLM su Blender, **non serve essere bit-identici a Moldboxer**. Ti basta:
- Esporre gli operatori giusti (i ~10 + 4-5 ricostruiti)
- Documentarli con i parametri corretti (questa cartella è già la fonte)
- Permettere all'LLM di comporli in flussi end-to-end

---

## 6. Mapping diretto: cosa serve nel tuo MCP

Tradotto in tool MCP da esporre:

| Tool MCP | Da dove | Note |
|---|---|---|
| `mb_import_model(path)` | [bl_utils.py](decompiled_py/bl_utils.py) `import_model` | STL/OBJ |
| `mb_heal_mesh(obj, quality)` | [wrapper.py](decompiled_py/components/wrapper.py) (voxel) | quality: FAST/MID/HIGH/ULTRA → voxel_size dal mapping in [voxel_size.py](decompiled_py/voxel_size.py) |
| `mb_center(obj)` | `silicone.center_obj` in [operators.py](moldboxer_silicone/operators.py:361) | trivial |
| `mb_scale_height(obj, height_cm)` | `silicone.scale_height` in [operators.py](moldboxer_silicone/operators.py:755) | |
| `mb_decimate(obj, factor)` | `silicone.decimate` in [operators.py](moldboxer_silicone/operators.py:585) | |
| `mb_clean_top(obj, height)` | `Object.clean_top` in [object.py](decompiled_py/object.py) | + clean_bot/cut_bot/clean_all_top |
| `mb_grid(obj, rows, cols, distance)` | `Object.grid_obj` in [object.py](decompiled_py/object.py) | |
| `mb_wrap_box(master, gap, voxel_size, n_wraps)` | [wrapper.py](decompiled_py/components/wrapper.py) | ricostruito ex novo |
| `mb_silicone_mold(master, box)` | Boolean - (vedi `sub_patron` in [silicone_mold.py](decompiled_py/components/silicone_mold.py)) | |
| `mb_split_mold(box, n_splits, axis='Y')` | [splitter.py](decompiled_py/components/splitter.py) | |
| `mb_add_base(box, master, with_pin)` | [base.py](decompiled_py/components/base.py) | |
| `mb_add_grip(box, voxel_size)` | [grip.py](decompiled_py/components/grip.py) | |
| `mb_auto_flat(master, gap)` | Ricetta 3.4 sopra | nuovo |
| `mb_auto_box(master, gap, channels, funneler, pins)` | Ricetta 3.1 sopra | nuovo |
| `mb_confirm(master, wrapper, channels, deposit)` | Ricetta 3.3 sopra | nuovo (senza keys) |
| `mb_export_stl(folder)` | [export.py](decompiled_py/components/export.py) | nome file con volume ml |

Tutti questi tool sarebbero **interamente Blender Python (bpy, bmesh, mathutils)** senza dipendenze esterne. Il tuo MCP `blender` già ha `execute_blender_code` come tool generico — questi sarebbero solo wrapper più mirati per il LLM.

---

## 7. File da leggere per implementare ogni pezzo

| Per implementare... | Leggi prima |
|---|---|
| Mesh utility (cut, scale, boolean) | [decompiled_py/object.py](decompiled_py/object.py) |
| Voxel remesh wrapper | [decompiled_py/components/wrapper.py](decompiled_py/components/wrapper.py) + [decompiled_py/modifiers.py](decompiled_py/modifiers.py) |
| Box generation locale | [decompiled_py/components/box.py](decompiled_py/components/box.py) |
| Extraction undercuts | [decompiled_py/components/extraction.py](decompiled_py/components/extraction.py) |
| Silicone preview | [decompiled_py/components/silicone_mold.py](decompiled_py/components/silicone_mold.py) |
| Split + base | [decompiled_py/components/splitter.py](decompiled_py/components/splitter.py) + [decompiled_py/components/base.py](decompiled_py/components/base.py) |
| Grip | [decompiled_py/components/grip.py](decompiled_py/components/grip.py) |
| Flat orchestration | [decompiled_py/components/auto_flat.py](decompiled_py/components/auto_flat.py) |
| Preprocess pipeline | [decompiled_py/components/preprocess.py](decompiled_py/components/preprocess.py) |
| Export | [decompiled_py/components/export.py](decompiled_py/components/export.py) |
| Mapping quality → voxel | [decompiled_py/voxel_size.py](decompiled_py/voxel_size.py) |

Quando un file ha `# decompile error` su una funzione che ti interessa, apri il `.md` corrispondente in [decompiled/](decompiled) per il bytecode raw — c'è sempre la verità lì.
