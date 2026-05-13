# MoldboxerStudy — Index

Cartella di studio del bundle **Moldboxer Blender 5.0.1 + add-on `moldboxer_silicone` v1.4.9**.
Origine: `C:\Users\emanu\Downloads\MoldboxerBlender\Moldboxer Blender\`.

## Cos'è "Moldboxer"

Un bundle commerciale che:

1. **Distribuisce Blender 5.0.1 vanilla** (binari identici al download ufficiale — verificato `cmp` su `blender.exe`, `blender-launcher.exe`).
2. **Aggiunge un'icona** (`mbx.ico`).
3. **Aggiunge una cartella `portable/`** che sfrutta il *portable mode* di Blender (config e estensioni accanto all'exe invece che in `%APPDATA%`).
4. Dentro `portable/extensions/moldboxer_extensions/moldboxer_silicone/` c'è **l'add-on Python** che è il vero prodotto: un generatore di sistemi di stampi in silicone con UI nel pannello N, sistema di account (Google/Patreon OAuth), tier di licenza (Lite/Core/Pro) e backend server.

## Layout di questa cartella

```
MoldboxerStudy/
├── INDEX.md                 ← questo file
├── CLAUDE.md                ← briefing per LLM (leggi questo per primo)
├── mbx.ico                  ← icona del bundle
├── moldboxer_silicone/      ← l'add-on (sorgente parziale + .pyc)
│   ├── __init__.py          ← entry point, registrazione classi, AddonPreferences
│   ├── blender_manifest.toml
│   ├── operators.py         ← TUTTI gli operatori (UI button → azione)
│   ├── panels.py            ← UI a pannelli N-panel View3D
│   ├── properties.py        ← bpy.types.Scene properties + tier guards
│   └── source/              ← logica core (compilata in .pyc, no .py)
│       ├── bl_utils.pyc
│       ├── constants.pyc
│       ├── devtools.pyc
│       ├── environment.pyc
│       ├── extension_updates.pyc
│       ├── extensions_repo.pyc
│       ├── materials.pyc
│       ├── modifiers.pyc
│       ├── object.pyc       ← wrapper Object (gigante: 800+ righe)
│       ├── operator_access.pyc  ← gate licenza/tier
│       ├── primitives.pyc
│       ├── voxel_size.pyc
│       ├── window_branding.pyc
│       └── components/
│           ├── auth.pyc     ← device-code OAuth (Google + Patreon)
│           ├── auto_box.pyc
│           ├── auto_flat.pyc
│           ├── base.pyc
│           ├── box.pyc
│           ├── channels_deposit.pyc
│           ├── confirm_mold.pyc
│           ├── export.pyc
│           ├── extraction.pyc
│           ├── grip.pyc
│           ├── inner_core.pyc
│           ├── open.pyc
│           ├── preprocess.pyc
│           ├── server.pyc   ← chiamate al backend (autenticate, upload zip, scarica risposta)
│           ├── silicone_mold.pyc
│           ├── split_connector.pyc
│           ├── splitter.pyc
│           ├── two_parts.pyc
│           └── wrapper.pyc
├── decompiled/              ← report markdown per ogni .pyc (shape view)
│   ├── *.md                 ← imports, classi, firme funzioni, stringhe, bytecode
│   └── components/*.md
├── decompiled_py/           ← PSEUDO-PYTHON ricostruito dal bytecode ⭐ usa questo
│   ├── *.py                 ← logica leggibile con label+goto
│   └── components/*.py
├── portable_config/         ← preset Blender preconfigurati nel bundle
│   ├── bookmarks.txt
│   ├── platform_support.txt
│   ├── startup.blend        (binario)
│   └── userpref.blend       (binario)
└── tools/
    ├── pyc_inspect.py       ← dumper bytecode + simboli (stdlib-only)
    └── pyc_to_pseudo.py     ← convertitore bytecode → pseudo-Python (stdlib-only)
```

## File leggibili in chiaro vs compilati

| File | Stato | Cosa contiene |
|---|---|---|
| `__init__.py` | leggibile | `bl_info`, `AddonPreferences`, lista CLASSES, `register()`/`unregister()` |
| `operators.py` | leggibile | ~40 classi `bpy.types.Operator` con `execute()` e dispatch ai componenti |
| `panels.py` | leggibile | 5 pannelli: Account, Mold, Settings, Pro Tools, Utils |
| `properties.py` | leggibile | Tutte le `bpy.types.Scene.*` properties + tier guards |
| `source/*.pyc` | **compilato** | Logica core, NO sorgente. Vedi `decompiled/*.md` per shape |
| `source/components/*.pyc` | **compilato** | Componenti del flusso mold |

Strategia di studio:
- I **comportamenti UI/flusso** → `operators.py`, `panels.py`, `properties.py`.
- L'**implementazione delle operazioni mesh** → `decompiled/*.md` (firme funzioni, stringhe, disassembly bytecode).

## Endpoint server scoperti (da `constants.pyc`)

```
server.moldboxer.com           ← API principale
oauth.moldboxer.com            ← OAuth (Google/Patreon device code)
auth.moldboxer.com             ← validazione token
extension.moldboxer.com        ← updater dell'add-on
devserver.moldboxer.com        ← dev/staging
devoauth.moldboxer.com         ← dev/staging
161.35.206.72                  ← IP (probabile fallback hardcoded — DigitalOcean droplet)
```

## Tier di licenza (da `operator_access.pyc`)

| Codice tier | Significato | Cosa sblocca |
|---|---|---|
| `T0` (LITE_TIER) | **Lite** | Solo flat auto box, scaling, view. Forza default `LITE_LOCKED_BASIC_SCENE_DEFAULTS` |
| `T1`, `T2` | **Core** | Tutte le opzioni "Settings" (gap, qualità, canali, splits, ecc.) |
| `T3` | **Pro** | `pro_inner_cavity`, `pro_two_part_silicone`, casting feet, keys |

Default forzati in modalità Lite (da `operator_access.py`):
```python
LITE_LOCKED_BASIC_SCENE_DEFAULTS = {
    'master_quality': 'MID', 'box_gap': 6.0, 'wing_join_patron': True,
    'funneler': True, 'clamp_pins': True, 'box_quality': 'FAST',
    'build_from_sphere': False, 'clear_extraction': True,
    'master_base_pin': True, 'n_splits': '2',
    'channel_width': 5.0, 'channel_depth': 6.0,
    'channel_adjust_to_contour': True, 'channel_back_larger': True,
}
PRO_SCENE_DEFAULTS = {
    'pro_inner_cavity': False, 'pro_inner_cavity_snap_tolerance': 0.05,
    'pro_inner_cavity_sensitivity': '3', 'pro_two_part_silicone': False,
    'pro_open_base': True, 'pro_casting_feet': True,
    'pro_key_size': 10.0, 'pro_key_tolearnce': 0.5,
}
```

Inoltre lo `auth_stripe_status == "FREE_BASIC_GOOGLE"` attiva il **Free Trial**: limite di 2 export STL (`auth_trial_exports_remaining`, decrementato in `consume_trial_export`).

`has_export_access()` ritorna `True` se loggato (qualsiasi tier non-lite) OPPURE se sei in free-trial con export residui.

## Vedi anche

- [CLAUDE.md](CLAUDE.md) ⭐ — **entry point per LLM**: dove sei, cosa c'è, playbook per task tipici. Leggilo PER PRIMO.
- [NEXT_STEPS.md](NEXT_STEPS.md) ⭐ — stato corrente + backlog prioritizzato. Apri questo per sapere "a che punto siamo".
- [FEATURES.md](FEATURES.md) — inventario completo per piano: ogni feature del video mappata a operatore/property/componente, con tier, endpoint server.
- [RECONSTRUCTION.md](RECONSTRUCTION.md) — teoria/strategia: confine client/server, cosa puoi fare offline oggi, ricette di ricostruzione.
- [moldboxer_lite/](moldboxer_lite) ⭐⭐ — **libreria Python ricostruita** (14 moduli, 2300 righe, smoke test verde):
  - [moldboxer_lite/README.md](moldboxer_lite/README.md) — overview libreria + stato componente.
  - [moldboxer_lite/INTEGRATION.md](moldboxer_lite/INTEGRATION.md) — checklist passo-passo per wirearla nel tuo MCP.
  - [moldboxer_lite/HOWTO.md](moldboxer_lite/HOWTO.md) — 9 ricette per task tipici (test, debug, aggiungere feature, tunare, ecc.).
- [Moldboxer Guide – Part 1 Core Tools.txt](Moldboxer%20Guide%20%E2%80%93%20Part%201%20Core%20Tools.txt) — trascrizione tutorial ufficiale (Part 1, copre Lite + Core).
- [decompiled_py/operator_access.py](decompiled_py/operator_access.py) — la logica di gating dei tier (pseudo-Python leggibile).
- [decompiled_py/components/auth.py](decompiled_py/components/auth.py) — il flusso OAuth device code.
- [decompiled_py/components/server.py](decompiled_py/components/server.py) — il client al backend.
- [decompiled/](decompiled) — disassembly bytecode dettagliato (fallback per quando il pseudo-Python ha errori).
