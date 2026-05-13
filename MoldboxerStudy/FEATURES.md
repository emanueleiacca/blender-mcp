# FEATURES — inventario completo per piano

Mappa **ogni funzionalità del prodotto** al codice. Fonti incrociate:
- Trascrizione video "Moldboxer Guide – Part 1: Core Tools" (`Moldboxer Guide – Part 1 Core Tools.txt`).
- Codice in chiaro: `moldboxer_silicone/{__init__,operators,panels,properties}.py`.
- Pseudo-Python ricostruito: `decompiled_py/**`.

> ⚠️ Il **Part 2 (Pro Tools)** non è stato fornito come trascrizione. Le funzionalità Pro qui sotto sono state ricavate solo dal codice — le descrizioni "marketing" potrebbero differire da quelle ufficiali.

---

## 1. I piani in sintesi

| Piano | Codice tier | Stripe status | Cosa abilita |
|---|---|---|---|
| **Lite (Light)** | `T0` | qualunque (anche non loggato non passa il gate `has_active_server_access`) | Solo automatic box + flat automatic box, con default forzati. UI Settings/Advanced/Pro **disabilitati** (mostrano "Unlock with Core"/"Unlock with Pro") |
| **Free Trial** | `T0` (Lite) ma `auth_stripe_status = "FREE_BASIC_GOOGLE"` | concesso automaticamente al primo login Google | Stesso accesso del Lite + budget di **2 export STL** (`auth_trial_exports_remaining=2`, decrementato a ogni `silicone.export_stl`). Il video dichiara anche "1 day trial" → con buona probabilità il token server scade in 24h (non visibile nel client) |
| **Core** | `T1` o `T2` | (vario, server-side) | Tutta la sezione Settings, Channels, Advanced Mode (Build Box + Confirm), tutte le Utils (clean/cut/grid/scale/heal/decimate), Export STL illimitato. **Tutto Part 1 del video** |
| **Pro** | `T3` | (vario, server-side) | Tutto del Core + sezione **Pro Tools** (inner cavity con sensitivity, two-part silicone con keys/feet/open-base) |

L'UI mostra "Logged in - Lite/Core/Pro/Free Trial" sotto Account in base al testo ritornato da `get_login_status_text(provider, tier, stripe_status)` ([auth.py:312](decompiled_py/components/auth.py:312)).

**Nota su T1 vs T2**: entrambi sono trattati come Core da `is_core_tier()` ([operator_access.py](decompiled_py/operator_access.py)), ma `get_login_status_text` mostra "Core" solo per T2. T1 ricade nel fallback generico "Logged in". Probabilmente T1 = tier intermedio (legacy o ancora non rilasciato).

---

## 2. Architettura tier-gate (come funzionano i lucchetti)

Tre livelli di check, dal più permissivo al più stringente:

```python
has_active_server_access() → loggato + refresh_token + access_token valido
has_basic_server_access()  → has_active + NOT is_lite_tier        ← Core o superiore
has_pro_server_access()    → loggato + refresh_token + tier == 'T3'  ← solo Pro
```

E quattro modi di reagire quando il check fallisce:

| Funzione | Operatore dialog mostrato | Quando |
|---|---|---|
| `show_active_membership_required()` | `silicone.auth_required_dialog` | Non loggato / token scaduto |
| `show_basic_membership_required()` | `silicone.basic_required_dialog` | Lite cerca di fare cose Core |
| `show_pro_membership_required()` | `silicone.pro_required_dialog` | Core/Lite cerca di fare cose Pro |
| `show_export_license_required()` | `silicone.export_license_required_dialog` | Free Trial ha esaurito i 2 export |

In più i pannelli usano `is_lite_tier()` / `is_core_tier()` per **disabilitare visivamente** intere colonne (`col.enabled = not lite_tier`) e mostrare il bottone "Unlock with Core/Pro". Funzionalità "Lite-vietate" sui parametri scena hanno un guard updater che le **riresetta al default Lite** se l'utente tenta di cambiarle (`_make_lite_basic_guard` in [properties.py:29](moldboxer_silicone/properties.py:29)).

---

## 3. Endpoint server (cosa va dove)

Quando l'utente clicca un bottone "intelligente", il client zippa le PLY degli oggetti e fa POST a un endpoint del backend Moldboxer. La logica geometrica gira **lato server**, non lato client.

| Endpoint (HTTP POST) | Componente | Operatore UI | Tier |
|---|---|---|---|
| `/auto-box/` | [auto_box.py](decompiled_py/components/auto_box.py) | `silicone.auto_box` (Auto Box) | Lite (con default forzati) / Core / Pro |
| `/auto-flat/` | [open.py](decompiled_py/components/open.py) | `silicone.flat_auto_box` (Flat Auto Box) | Lite / Core / Pro |
| `/channels-deposit/` | [channels_deposit.py](decompiled_py/components/channels_deposit.py) | Chiamato da `build_box_operator` → `silicone.build_box` | Core / Pro |
| `/confirm-silicone-mold/` | [confirm_mold.py](decompiled_py/components/confirm_mold.py) | `silicone.confirm` | Core / Pro |
| `/inner-core/` | [inner_core.py](decompiled_py/components/inner_core.py) | usato quando `pro_inner_cavity = True` | **Pro** |

Base URL configurato in `environment.py` (`server.moldboxer.com` produzione, `devserver.moldboxer.com` dev — vedi [constants.py](decompiled_py/constants.py)).

I parametri inviati a `/auto-box/` sono: `box_voxel_size, channel_width, n_splits, channel_depth, adjust_to_contour, larger_back, add_funneler, add_pins` ([auto_box.py:30](decompiled_py/components/auto_box.py:30)).

---

## 4. Inventario funzionalità ↔ codice ↔ piano

Tutte le voci sono nel pannello **N-panel View3D > "Moldboxer Silicone"**.

### 4.1 Pannello "Account" — `SILICONE_PT_account`

| Voce UI | Operatore | Cosa fa | Tier |
|---|---|---|---|
| "Login with Google" | `silicone.login_google` | OAuth device code → `oauth.moldboxer.com/google/start` → apre browser → polling | Tutti |
| "Login with Patreon" | `silicone.login_patreon` | Idem ma con provider Patreon | Tutti |
| "Get Membership" | `wm.url_open` → `moldboxer.com` | Sito di acquisto | Tutti |
| "Update Available" / "Update" | `silicone.open_extension_updates` | Apre la finestra Extensions di Blender per aggiornare | Tutti |
| "Cancel Login" / "Logout" | `silicone.logout` | Svuota token e pending state | Loggato |
| Status "Logged in - Lite/Core/Pro/Free Trial" | (label) | Da `get_login_status_text` | Loggato |
| "Free Trial Exports Remaining: N" | (label, solo in AddonPreferences draw) | Solo se `FREE_BASIC_GOOGLE` | Free Trial |

> Video [00:00-00:43]: "First, after installing Moldboxer, you need to log in. There are multiple options. If you purchased your license from our website, log in with Google here. If you subscribe through our Patreon membership, use this option instead."

### 4.2 Pannello "Mold" — `SILICONE_PT_mold`

| Voce UI | Operatore | Tier | Note |
|---|---|---|---|
| **New** | `silicone.new_project` | Tutti | Rimuove **tutti** gli oggetti dalla scena |
| **Restart** | `silicone.restart` | Tutti | Rimuove tutto **eccetto** `patron`; ricentra |
| **Import** | `silicone.import_model` | Tutti | Importa STL o OBJ; se max dimensione < 10mm propone scale-up 10× ([operators.py:600+](moldboxer_silicone/operators.py)) |
| **Export** | `silicone.export_stl` | Core / Pro / Free-Trial-residuo | Esporta `patron_<volume>ml.stl` + ogni `silicone_*` + ogni altra mesh come `<name>.stl` |
| **Resolution** (dropdown) | `master_quality` (scene prop) | Tutti (Lite forzato a `MID`) | Master voxel detail: FAST / MID / HIGH / ULTRA. Applicato **solo** se il master non è manifold e va riparato |
| **Automatic Box** | `silicone.auto_box` | Lite/Core/Pro | Lite forza defaults e rimuove text volume |
| **Flat Automatic Box** | `silicone.flat_auto_box` | Lite/Core/Pro | Mold a 1 pezzo con top aperto + grip |
| **1. Build Box** | `silicone.build_box` | **Core** / Pro | Advanced mode step 1 |
| **2. Confirm** | `silicone.confirm` | **Core** / Pro | Advanced mode step 2 |

> Video [00:50-01:18]: "First, import the model you want to create the mold from… After confirming, it will appear in the center of the scene. Here you'll see the resolution setting… This setting only applies if the model mesh is not manifold and needs to be repaired".

> Video [01:40-01:58]: "If you've just started using Moldboxer, you'll probably want to stick to these two buttons, automatic box and flat automatic box. These will generate the mold box automatically with optimal settings for most cases."

**Componenti generati dall'Automatic Box** (3 oggetti visibili in scena):
1. `patron` — il modello master originale a sinistra.
2. il **mold system** — box rigido che conterrà il silicone.
3. `silicone_mold` — anteprima del volume di silicone risultante.

> Video [02:13-02:36]: "Once the generation is complete, you'll see three items on the screen. On the left, you have the original model… In the center, you'll see the mold system, and the third item is the final silicone preview".

**Split axis** = asse Y (verde di Blender). L'utente ruota/sposta il modello per controllare dove cade il taglio tra le due metà.

> Video [03:01-03:34]: "If you notice, the split is aligned with this green line, which represents the Y axis… To control this, you need to align your model with the green axis".

### 4.3 Pannello "Settings" — `SILICONE_PT_settings`

> Tutto il pannello: `col.enabled = not lite_tier`. Per i Lite mostra il bottone "Unlock with Core". Quando un Lite tenta di modificare, il guard updater reimposta il default Lite e mostra `silicone.basic_required_dialog`.

#### 4.3.1 Box / Geometry

| Voce UI | Property | Default (free) | Default (Lite forzato) | Cosa fa |
|---|---|---|---|---|
| **Silicone Thickness** | `box_gap` (FloatProperty) | 4.5 | 6.0 | Distanza tra master e box (mm) |
| **Fixed Master** | `wing_join_patron` (Bool) | True | True | True: master fuso alla base; False: master separato con key di assemblaggio |
| **Funneler** | `funneler` (Bool) | True | True | Inlet cilindrico per colata silicone in cima al box |
| **Clamp Pins** | `clamp_pins` (Bool) | True | True | Pin di allineamento tra le due metà del box |
| **Detail** | `box_quality` (Enum) | MID | FAST | Risoluzione voxel del box generato. FAST/MID/HIGH/ULTRA |
| **Safe Mode Box** | `build_from_sphere` (Bool) | False | False | Costruisce dalla sfera ammazza-gap. "You'll probably never use it" (video) |
| **Clear Extraction** | `clear_extraction` (Bool) | True | True | Apre un percorso nella direzione di split per evitare undercut bloccanti |
| **Master-base Pin** | `master_base_pin` (Bool) | True | True | Aggiunge un pin sulla base che si inserisce nel master (solo se Fixed Master è OFF) |

> Video [05:36-06:01]: "Here you'll find the most important parameter… silicone thickness… defines the distance between the model and the mold box".

> Video [06:01-07:00]: "Fixed master option. This determines whether the master model is attached to the base as a single piece."

> Video [07:55-08:14]: "If you've already created your master model… the base pin may prevent you from placing it correctly… you can disable the master base pin setting."

> Video [10:09-10:51]: "Clear extraction… The system clears a path along the extraction direction… so the mold can be opened without getting stuck."

#### 4.3.2 Channels

| Voce UI | Property | Default (free) | Default (Lite forzato) | Cosa fa |
|---|---|---|---|---|
| **Width** | `channel_width` (Float) | 5.0 | 5.0 | Larghezza dei canali strutturali sul box |
| **Depth** | `channel_depth` (Float) | 6.0 | 6.0 | Distanza dalla cima del canale alla superficie esterna del box |
| **Countour Adapted** *(sic)* | `channel_adjust_to_contour` (Bool) | True | True | Se True, canali seguono il profilo del modello |
| **Larger Back** | `channel_back_larger` (Bool) | True | True | Canale posteriore più largo per facilitare clamping post-taglio |

> Video [11:15-13:50]: Triplice funzione canali: 1) supporto/stabilità a mold capovolto, 2) rinforzo silicone sottile, 3) miglior flusso del silicone in viscosità alte.

**Note tecniche dal video** (riferimento utili per UX/marketing):
- Spessori usabili: 2 mm con silicone ~3000 cps, 6 mm+ con silicone ~20000 cps.
- "Channels improve the silicone flow during pouring" (importante per silicon ad alta viscosità).

### 4.4 Pannello "Pro Tools" — `SILICONE_PT_pro_settings`

> ⚠️ La trascrizione video Part 1 NON copre Pro Tools (rimandata a Part 2). Le descrizioni qui sotto vengono dal codice e dai tooltip Python.

> Per i Lite o Core mostra "Unlock with Pro" (`OpenUpgradeLicense` con `license_target='PRO'`). I controlli pro sono `col.enabled = pro_access` dove `pro_access = has_cached_pro_access(context)` ([panels.py:58](moldboxer_silicone/panels.py:58)).

#### 4.4.1 Inner Cavity

| Voce UI | Property | Default | Tooltip |
|---|---|---|---|
| **Inner cavity** | `pro_inner_cavity` (Bool con getter/setter custom) | False | "Create inner pot-style cavity filler geometry to reduce silicone usage" |
| **Power** | `pro_inner_cavity_sensitivity` (Enum) | "3" | Aggressive (1) = trova più cavità; Balanced (3) = smussa le piccole |
| **Snap Tolerance** | `pro_inner_cavity_snap_tolerance` (Float) | 0.05 | "Tolerance used when generating the inner cavity box snap fit" |

Quando attivo: `AutoBox` non chiama il flusso standard ma esegue `bpy.ops.silicone.build_box()` + `bpy.ops.silicone.confirm()` ([operators.py:318-320](moldboxer_silicone/operators.py)), che internamente passa per `inner_core` (`/inner-core/` server).

#### 4.4.2 Two-Part Silicone

| Voce UI | Property | Default | Tooltip |
|---|---|---|---|
| **2-Part Silicone** | `pro_two_part_silicone` (Bool) | False | "Create a mold system for producing separate 2-part silicone molds" |
| **Open base** | `pro_open_base` (Bool) | True | "Keep the two-parts mold base open below the selected object's minimum Z" |
| **Casting Feet** | `pro_casting_feet` (Bool) | True | "Enable casting feet for two-parts molds" |
| **Key Size** | `pro_key_size` (Float) | 10.0 | "Cube size used to build one key at each two-parts circle vertex" |
| **Key Tolearnce** *(sic)* | `pro_key_tolearnce` (Float) | 0.5 | "Size reduction applied to the male keys on each axis" |

Quando attivo: `AutoBox` chiama `build_two_parts_box(context)` + `confirm_two_parts(context)` ([two_parts.py](decompiled_py/components/two_parts.py)).

### 4.5 Pannello "Utils" — `SILICONE_PT_utils`

#### 4.5.1 General

| Voce UI | Operatore | Property collegata | Tier | Cosa fa |
|---|---|---|---|---|
| **Scale Z (cm)** | `silicone.scale_height` | `scale_height` (cm) | Tutti | Ridimensiona il master all'altezza specificata. UI in cm, internamente convertita in mm (`*10`) |
| **Center** | `silicone.center_obj` | — | Tutti | `bpy.ops.object.origin_set(type='GEOMETRY_ORIGIN', center='BOUNDS')` + porta su Z=0 |
| **Heal** | `silicone.heal_patron` | — | Tutti | Applica modificatore voxel remesh per riparare non-manifold |
| **Decimate** | `silicone.decimate` | `decimate_factor` | Tutti | Modificatore Decimate Collapse |

> Video [18:30-19:35]: tutte le quattro utility coperte.

#### 4.5.2 Clean / Cut

| Voce UI | Operatore | Property | Tier | Cosa fa |
|---|---|---|---|---|
| **Height** | (input) | `cut_clean_height` | — | Altezza di riferimento per le 4 operazioni sotto |
| **Clean All Top** | `silicone.clean_all_top` | — | Tutti | Pulisce tutto sopra (altezza - 0.1) — appiattisce completamente la cima |
| **Cut Bot** | `silicone.cut_bot` | — | Tutti | Taglio piano `cut_plane` a `min_z + cut_clean_height` |
| **Clean Top** | `silicone.clean_top` | — | Tutti | Pulisce sopra all'altezza specificata |
| **Clean Bot** | `silicone.clean_bot` | — | Tutti | Pulisce sotto l'altezza, estrudendo verso il basso |

> Video [16:30-18:25]: spiegazione completa con esempio ornamenti / cocker spaniel.

#### 4.5.3 Grid

| Voce UI | Operatore | Property | Tier | Cosa fa |
|---|---|---|---|---|
| **Grid** | `silicone.grid` | `grid_rows`, `grid_columns`, `grid_distance` | **Core** / Pro | Duplica il master in array NxM con spacing dato |

> Video [19:35-21:00]: esempio fiori 3x3 e 2x4.

> Codice ([operators.py:566-580](moldboxer_silicone/operators.py)): gate `has_basic_server_access()` → richiede Core.

#### 4.5.4 Casting Input

| Voce UI | Operatore | Property | Tier | Cosa fa |
|---|---|---|---|---|
| **H** | (input) | `casting_input_h` | — | Mezza altezza del cilindro di colata (lunghezza totale 2×H) |
| **D** | (input) | `casting_input_diameter` | — | Diametro |
| **Face** | (dropdown) | `casting_input_axis` | — | Asse +/-X, +/-Y, +/-Z su cui posizionare il cilindro |
| **Add Casting Input** | `silicone.add_casting_input` | — | Tutti | Aggiunge un cilindro al mesh selezionato |

Non guardato in panels.py rispetto al tier. Probabilmente è una utility ausiliaria principalmente per Pro (workflow two-part molds).

#### 4.5.5 Dev (visibile solo se `dev_mode = True` nelle AddonPreferences)

| Voce UI | Operatore | Cosa fa |
|---|---|---|
| **Dev Repo Path** | (input) | Percorso locale repo di sviluppo |
| **Reload From Repo** | `silicone.reload_from_repo` | Ricarica i moduli dal repo locale (hot reload) |
| **Test Operator** | `silicone.test_mode_operator` | Operatore segnaposto/test |

Hidden behind `addon.preferences.dev_mode` flag — non visibile agli utenti finali.

### 4.6 Operatori esistenti ma NON visibili in UI

Questi sono in `CLASSES` di `__init__.py` ma i pannelli che li mostravano sono **commentati** in `panels.py`:

| Operatore | Cosa fa | Dove era |
|---|---|---|
| `silicone.build_grip` | Costruisce un grip stand-alone | PT_utils (sezione "Grip", commentata) |
| `silicone.add_grip` | Aggiunge grip a mesh esistente | PT_utils (sezione "Grip", commentata) |
| `silicone.split_with_connector` | Taglia mesh a metà + aggiunge connettore cilindrico 5×10mm | PT_utils (sezione "Split Connector", commentata) |

Probabilmente feature rimosse dalla UI in v1.4.9 ma codice ancora presente.

---

## 5. Flusso completo "Automatic Box" (riferimento per debugging)

Quando l'utente clicca "Automatic Box" con default Core/Pro:

```
silicone.auto_box (AutoBox.execute)
  ├── SelectedMoldboxerOperator.execute
  │     ├── MoldboxerOperator.execute → has_active_server_access (gate)
  │     └── preprocess_patron(center=False) + configure_metric_millimeter_units
  ├── apply_lite_access_defaults (forza defaults se T0)
  │
  ├── IF pro_two_part_silicone:
  │     build_two_parts_box(context)   ← due_parts.py
  │     confirm_two_parts(context)
  │
  ├── ELIF pro_inner_cavity:
  │     bpy.ops.silicone.build_box()   → build_box_operator → server /channels-deposit/
  │     bpy.ops.silicone.confirm()     → confirm() → server /inner-core/ + /confirm-silicone-mold/
  │
  └── ELSE (standard):
        build_box(context)             ← crea wrapper locale
        request_auto_box(context)      → POST /auto-box/ (zip PLY 'box') ← QUI VA AL SERVER
        sub_patron(get_box_voxel_size(box_quality))
        silicone_mold = Object('silicone_mold')
        context.scene.volume = silicone_mold.volume
        add_basing_to_system(volume, wing_join_patron, master_base_pin)
        split(int(n_splits))           ← splitter.py
        IF NOT is_lite_tier:
            write_volume()             ← mostra testo "Xml" sul box
        ELSE:
            rimuovi Text1
        space_mold_system()            ← distanzia i 3 oggetti in scena
        refresh_generated_object_materials()
        set_viewport_material_preview()
```

Per il **Flat Automatic Box** (`silicone.flat_auto_box`):

```
silicone.flat_auto_box (FlatAutoBox.execute)
  ├── SelectedMoldboxerOperator.execute → has_active_server_access (gate)
  ├── apply_lite_access_defaults
  ├── auto_flat(context)               ← open.py / auto_flat.py → POST /auto-flat/
  ├── refresh_generated_object_materials
  └── set_viewport_material_preview
```

Per **Advanced Mode** (separato in 2 step):

```
1. silicone.build_box (BuildBox.execute)  ← gate Core
     build_box_operator(context)   → POST /channels-deposit/
     → in scena compaiono:
        - "wrapper" (in oro): il box che segue il contorno
        - "channels" (in blu): le colonne sui lati
        - "deposit" (in verde-acqua): l'inlet di colata
     ↪ utente può scalare/spostare/duplicare ogni componente

2. silicone.confirm (Confirm.execute)     ← gate Core
     confirm(context)              → POST /confirm-silicone-mold/
     → calcola silicone, split, scrive volume, finalizza
```

> Video [14:05-15:40]: "This mode divides the mold generation process into steps… In gold, the box wrapper that follows the shape of the model. In blue, the channels, in this case, not contour adapted. And in a more greenish tone, the deposit."

---

## 6. Trial / Free Trial — dettagli tecnici

- Status `auth_stripe_status == "FREE_BASIC_GOOGLE"` ← assegnato server-side quando un utente Google fa login senza aver mai acquistato.
- Contatore client-side: `auth_trial_exports_remaining`, default 2, persistito in `userpref.blend`.
- `consume_trial_export(prefs)` decrementa il contatore. Chiamato in `ExportSTL.execute` ([operators.py:716](moldboxer_silicone/operators.py:716)) solo se stato = FREE_BASIC_GOOGLE.
- Il contatore è **legato alla email**: cambiando account Google il counter si resetta a 2 (logica in `initialize_trial_export_counter`, [auth.py:109](decompiled_py/components/auth.py:109)).
- La frase del video "the trial will start automatically… one-day free trial" suggerisce che il server **scada il refresh_token a 24h** per i FREE_BASIC_GOOGLE (logica server-side, non osservabile dal client).
- A esaurimento, `has_export_access()` ritorna False → `silicone.export_license_required_dialog` ([operator_access.py](decompiled_py/operator_access.py)).

---

## 7. Cose nominate nel video ma NON ancora implementate / future

Citazioni dirette dalla trascrizione segnano roadmap:

- **"This will be updated soon. Instead, this area will display the casting volume"** [05:36] — attualmente il flat mold mostra il **silicone volume** nel grip; in futuro mostrerà il **casting volume** (volume del pezzo finale, non del silicone).
- **"We'll also include an automatic hole generation feature"** [08:00] — quando `master_base_pin` è disabilitato, in futuro una funzione genererà automaticamente i fori sul master per allinearlo.
- **"more parts, which we'll be adding soon"** [10:51] — più di 2 metà per il box (oggi `n_splits` è limitato a 0 o 2 — vedi enum in [properties.py:173](moldboxer_silicone/properties.py:173)).

---

## 8. Cose nel codice non coperte dal video

Funzionalità presenti nel codice non spiegate nel Part 1:

1. **`SplitWithConnector`** ([operators.py:771](moldboxer_silicone/operators.py:771)) — taglia una mesh in due metà aggiungendo un connettore cilindrico 5×10mm. UI commentata in panels.py → potrebbe essere reintrodotta.
2. **`BuildGrip` / `AddGrip`** ([operators.py:536-557](moldboxer_silicone/operators.py)) — costruzione/aggiunta grip indipendente dal box. UI commentata.
3. **`AddCastingInput`** ([operators.py:429-453](moldboxer_silicone/operators.py)) — non spiegato esplicitamente, probabilmente coperto in Part 2 (workflow 2-part molds).
4. **Tier T1** — esiste in `is_core_tier` ma `get_login_status_text` non lo etichetta esplicitamente. Possibile tier nascosto/legacy.
5. **Dev mode** — `dev_mode`, `test_mode`, `dev_repo_path`, `silicone.reload_from_repo`, `silicone.test_mode_operator`. Solo per sviluppatori interni.
6. **`silicone.reset_background_color`** — esiste in CLASSES ma riga commentata in panels.py utils (era in PT_utils).
7. **Window branding** ([window_branding.py](decompiled_py/window_branding.py)) — cambia AppUserModelID Windows (taskbar usa mbx.ico), aggiunge overlay logo + dimensioni nel viewport. Trasparente all'utente.

---

## 9. Cose nel video non coperte dal codice (controllo di copertura)

Ho ri-pettinato la trascrizione cercando elementi UI / parametri non mappati al codice. **Nessuna omissione trovata**: ogni feature menzionata nel video è presente in operators/properties/components.

Casi al limite verificati:
- "Rotate / Move / Scale tool" [03:50-04:25]: questi sono i **transform tool nativi di Blender** (G/R/S), non operatori Moldboxer. Niente da aggiungere lato Moldboxer.
- "Silicone preview" object: è chiamato `silicone_mold` lato codice (vedi `space_mold_system` in [confirm_mold.py:63](decompiled_py/components/confirm_mold.py:63)).
- "Mold system" / "the third item": è il box dopo `confirm`. Composto da più oggetti generati (`box_bridged`, `attacher_*`, `silicone_mold`, `patron` se Fixed Master, ecc.).
