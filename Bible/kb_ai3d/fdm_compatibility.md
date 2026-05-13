# FDM Compatibility — rework Blender per ciascun tool

Per ogni tool 3D, lista dei difetti tipici dell'output e check-list di rework in Blender prima di Bambu Studio + A1. Si appoggia al KB Blender già presente in `Blender for 3d print documentation/` (vedi `Blender for 3d print documentation/INDEX.md`).

---

## Pre-flight comune (tutti i tool)

Indipendentemente dal tool, ogni mesh esce dalla generazione AI con almeno **alcuni** di questi problemi:

1. **Scala arbitraria** — il tool non sa quanto è grande l'oggetto reale
2. **Asse Z mal allineato** — il "su" del modello potrebbe non essere il "su" stampabile
3. **Base spuria o inclinata** — riflessi e ombre nella foto generano basi piatte fittizie
4. **Polycount eccessivo** per le esigenze FDM (lo slicer triangola comunque)
5. **Eventuali non-manifold edges/vertici** — invisibili in render, fatali per slicing

**Check-list pre-flight obbligatoria** prima di lavorare su qualsiasi tool-specific issue:

```
[ ] Import STL in Blender
[ ] Object → Apply → Scale (anche se sembra OK)
[ ] N-panel → Item → verifica dimensioni cm/mm
[ ] Edit Mode → Select All by Trait → Non Manifold → quanti?
[ ] Mesh → Clean Up → Merge by Distance (default 0.0001 m)
[ ] Verifica orientamento: l'asse Z corrisponde al "su" stampabile?
[ ] Spianamento base se necessario
```

Riferimenti KB Blender:
- `Blender for 3d print documentation/docs/scale_detection.md` — calcolare scala vera
- `Blender for 3d print documentation/docs/scripting_guide.md` — gotchas API
- `Blender for 3d print documentation/docs/fdm_printing_constraints.md` — vincoli A1

---

## Per tool

### Tripo 3.1

**Difetti tipici**:
- Triangle soup con vertici fusi e facce sovrapposte
- ~1 generazione su 10 client-ready as-is
- Basi piatte spurie sotto al soggetto (eredità delle ombre nella foto)
- Asimmetrie sul retro (single-image)
- Polycount alto in HD (500k) — utile ridurre

**Rework specifico**:
1. Pre-flight comune
2. Mesh → Clean Up → **Decimate Geometry** se polycount > 300k (target 150-200k)
3. Mesh → Clean Up → **Merge by Distance** (0.001 m, più aggressivo del default — risolve i vertici fusi)
4. Edit Mode → check facce duplicate: Select → All by Trait → **Faces Overlapping**
5. Spiana la base spuria: seleziona ring inferiore, scale Z=0, snap a Z=0
6. Se hai usato Multi View Tripo: verifica simmetria visiva (mirroring eventuale solo se necessario)

**Tempo medio rework**: 5-15 min

---

### Hi3D 2.1 — ENGINE PRIMARIO ⭐

**Sezione estesa** (engine primario del workflow, decisione utente 2026-05-13).

**Difetti tipici**:
- Triangle soup molto densa (1536³ Pro = ~2M poly!)
- STL pesanti, lenti da aprire in Blender (>30 sec import)
- Seam di proiezione su retro non visto (single-view)
- **Membrane intrinseche** dove decorazione fitta si fonde con parete (Vaso limoni 2026-05-08)
- Base spuria con base inclinata (riflessi/ombre della foto interpretate come geometria)

**Rework completo H3.1 (10-step protocol)**:

1. **PRIMA del pre-flight (CRITICO se >1M poly)**: Blender lagga catastroficamente con 2M poly. Decimate Geometry **ratio 0.25-0.40** (target ~500k tri) PRIMA di qualunque altra operazione

2. **Pre-flight comune**: Apply Scale, Merge by Distance 0.0001m, Select All by Trait → Non Manifold (conta)

3. **MCP `analyze_mesh_for_print`** (Bambu KB integration):
   ```
   - polycount
   - non_manifold_edges
   - non_manifold_verts
   - holes
   - overhang_45_pct
   - quasi_flat_ceiling_pct  ← KEY metric per membrane intrinseche
   - pca_thickness_ratio
   - contact_points_count
   ```

4. **Se `quasi_flat_ceiling_pct > 5%`**: membrane intrinseche presenti
   - Strategia A: PyMeshLab Ambient Occlusion → eliminare facce con AO < 0.15 (Regola 37 TESTING_LOG)
   - Strategia B: BVHTree Fibonacci hemisphere raycast (Regola 38)
   - Vedi `Bible/Blender for 3d print documentation/docs/membrane_removal.md`
   - **Fallback (Regola 31)**: dopo 2 tentativi falliti, propose Meshmixer alternative — non insistere

5. **Verifica seam posteriore**: Edit Mode → view from back → search discontinuità verticali → Mesh → Clean Up → **Fill Holes** (max edges 4)

6. **Plane-fit SVD su contact points** (Regola 29, per soggetti multi-foot):
   - Se `contact_points_count >= 3`: usare SVD plane fit sui contact points
   - Allineare Z=0 al piano di stampa
   - Verificare con MCP `check_pre_export`

7. **Bisect base spuria** (Regola 34 KISS):
   - Se la base è inclinata o ha geometria spuria sotto: bisect Z=epsilon (es. 4.98mm sotto il bottom dei feet) → keep upper portion → fill flat
   - **Non tentare snap vertices** (peggiora la geometria circolare — confermato su vaso limoni)

8. **`check_pre_export` MCP** (Regola 36 OBBLIGATORIA):
   - `bbox_z_min == 0` (no clipping)
   - `contact_points_count > 0` (stampabile)
   - `non_manifold_edges == 0` (slicer-ready)
   - `holes == 0` (watertight)
   - Se uno qualunque fallisce: NON esportare, fix prima

9. **HIRES validation** (Regola 30 OBBLIGATORIA):
   - `render_hires_multiview` MCP a 1920×1440 (4 viste: front/right/top/iso)
   - Visualizzare i 4 PNG e validare: silhouette, presenza dettagli, base piatta, no buchi visibili
   - **Mai dichiarare success su low-res screenshot** (storia delle allucinazioni 2026-05-04/08)

10. **Decimate finale** a target ~150-200k tri (Bambu Studio non ha bisogno di più, slicer triangola comunque)

**Tempo medio rework H3.1**: 10-25 min (più dei concorrenti per il polycount + step membrane se serve).

**Casi noti dal campo (Hi3D 2.1)**:
- ✅ **Vaso limoni 2026-05-08**: unico tool che ha prodotto un mesh lavorabile su soggetto "strutturalmente occluso". Rework: bisect Z=4.98mm, fill_islands=1 (Regola 35 indicator)
- ⚠️ **Albero corallo 2026-05-XX**: membrane intrinseche post-Hi3D non rimuovibili automaticamente. Workflow: 2 attempt → escalate a Meshmixer (Regola 31)

---

### Hunyuan 3D 3.1

**Difetti tipici**:
- Mesh **watertight** out-of-the-box (vantaggio significativo)
- Smoothing eccessivo: dettagli ornamentali fini possono essere già spariti — meno rework, ma potenziale rifare la generazione
- Volti deformati (se hai ignorato il decision tree e hai usato Hunyuan su volti)

**Rework specifico**:
1. Pre-flight comune (probabilmente nessun non-manifold da fixare!)
2. Verifica visiva dettagli ornamentali: se troppo lisci, **scartare e cambiare tool** (non c'è cleanup Blender che recupera dettagli persi)
3. Decimate solo se polycount > 500k (raro)
4. Quad topology: irrilevante per FDM (slicer triangola), ma **non triangolare manualmente** — gli slicer moderni gestiscono quad

**Tempo medio rework**: 3-8 min (il più rapido se la generazione è buona)

---

### Meshy 6

**Difetti tipici**:
- Smoothing aggressivo ai polycount default — dettagli persi
- Single-mesh con elementi sospesi non manifold
- Quad remesh può lisciare bordi

**Rework specifico**:
1. Pre-flight comune (attenzione ai non-manifold sospesi)
2. Verifica visiva dettagli — Meshy è quello che più probabilmente delude su ornamenti fini → rigenera con polycount alto se possibile
3. Edit Mode → Select → All by Trait → **Loose** → elimina geometria isolata
4. Decimate a 100-150k se serve

**Tempo medio rework**: 5-12 min

---

### Rodin Gen 2

**Difetti tipici**:
- Mesh non sempre print-ready: report di non-manifold da repair
- Cavità profonde tendenzialmente riempite (sottosquadri stretti persi)
- Ottimizzato per rendering, non stampa

**Rework specifico**:
1. Pre-flight comune con **attenzione speciale** ai non-manifold (più frequenti che altrove)
2. Mesh → Clean Up → **Make Manifold** (operatore robusto, accettare i piccoli cambiamenti che introduce)
3. Verifica sottosquadri: se il soggetto reale ha cavità che il mesh ha riempito, **non puoi recuperare** → ridurre la quality tier o cambiare tool. Stampa stessa la versione "piena" se accettabile
4. Decimate a 200-300k (Rodin va alto come Hi3D, ma topologia migliore)

**Tempo medio rework**: 8-20 min

---

## Tabella di sintesi

| Tool | Watertight? | Non-manifold | Smoothing | Gen. MakerWorld | Rework Blender | Verdetto FDM |
|------|-------------|--------------|-----------|-----------------|----------------|--------------|
| Tripo 3.1 | A volte | Frequente | Moderato | **~2.5 min** | 5-15 min | Solido default, ottimo per iterare |
| Hi3D 2.1 | Spesso | Raro | Minimo | **~7 min** | 10-25 min | Top qualità, pesante da gestire in Blender |
| Hunyuan 3.1 | **Sempre** | **Raro** | Aggressivo | **~3 min** | 3-8 min | Velocissimo se la gen è buona |
| Meshy 6 | A volte | Occasionale | **Aggressivo** | **~4 min** | 5-12 min | Verificare smoothing empiricamente |
| Rodin Gen 2 | A volte | **Frequente** | Minimo | **~3 min** | 8-20 min | Top qualità ma rework Blender alto |

---

---

## Ranking empirico per soggetti complessi (dati reali)

**Caso di test**: vaso decorativo con limoni scolpiti che coprono 100% della parete esterna (oggetto strutturalmente occluso). Fonte: gesso. Input: foto Gemini-processata laterale bassa.

| Tool | Struttura contenitore | Fondo | Dettaglio limoni | Usabilità |
|------|-----------------------|-------|------------------|-----------|
| Tripo 3.1 | ❌ blob informe | ❌ bucato | ❌ | ❌ Scartare |
| Rodin Gen-2 | ❌ blob informe | ❌ bucato | ⚠️ parziale | ❌ Scartare |
| Meshy 6 | ❌ blob informe | ✅ chiuso | ⚠️ fronte ok / retro no | ⚠️ Lavorabile con rework pesante |
| Hi3D 2.1 | ❌ blob informe | ✅ chiuso | ✅ migliore | ✅ Migliore punto di partenza per rework |

**Conclusione**: su soggetti con decorazione che oclude completamente la struttura, **Hi3D 2.1 è il solo tool che produce un output lavorabile**. I 7 minuti valgono. Non usare Tripo o Rodin su questa categoria di oggetti.

**"Fondo bucato" — causa**: il tool non vede il fondo dell'oggetto nella foto → genera una mesh senza base definita. Non è legato all'apertura superiore del contenitore. Fix in Blender: seleziona edge loop inferiore → Fill → scale Z=0 → snap a Z=0.

## Aggiornamenti dal campo

Questa pagina deve essere **aggiornata empiricamente**. Dopo ogni stampa:
- Quanto tempo è servito davvero?
- Quali difetti sono comparsi che non sono in questa lista?
- Quale operatore Blender ha funzionato meglio?

Annota in `Blender for 3d print documentation/FIELD_NOTES.md` e poi consolida qui i pattern ricorrenti.

---

## Asset naming convention (estende Regola 41 TESTING_LOG)

Pattern community (Patreon/Cults3D/MyMiniFactory) per nomenclatura asset stampabili. Estende la convenzione `relief|wall_art|2.5D|plaque|medallion|lithophane` della Regola 41.

### Pattern completo

```
{collection}_{piece}_{variant}_{state}_{scale}_{target}_v{NNN}.{ext}
```

### Componenti

| Componente | Esempi | Note |
|---|---|---|
| `{collection}` | `caltagirone`, `pulcinella`, `albero_corallo` | Raccolta o serie |
| `{piece}` | `pignaCono`, `testaDiMoro`, `vasoLimoni` | camelCase per pezzo specifico |
| `{variant}` | `blu`, `oro`, `monocromo`, `multicolor`, `M4`, `S`, `L` | Variante stilistica o scala |
| `{state}` | `raw`, `clean`, `hollow`, `supported`, `split`, `keyed` | Stato del file STL |
| `{scale}` | `28mm`, `120mm`, `S`, `M`, `L` | Dimensione fisica target |
| `{target}` | `FDM`, `resin`, `a1`, `x1c`, `mini`, `bust` | Stampante target o use case |
| `v{NNN}` | `v001`, `v002`, `v015` | Versione (zero-padded) |

### Suffissi di stato (`{state}`)

- `_raw` — appena uscito dal generator (Hi3D, Tripo, ecc.)
- `_clean` — post-Blender cleanup (non-manifold fix, decimate)
- `_hollow` — svuotato per Spiral Vase o riduzione filamento
- `_supported` — supporti già modellati (tree o standard)
- `_split` — diviso in N pezzi assemblabili
- `_keyed` — con pin/dovetail per assemblaggio post-stampa
- `_relief` / `_wall_art` / `_2.5D` / `_plaque` / `_medallion` / `_lithophane` — tela intenzionale (Regola 41)

### Esempi

```
caltagirone_pignaCono_blu_raw_120mm_a1_v001.stl   ← appena generato Hi3D
caltagirone_pignaCono_blu_clean_120mm_a1_v002.stl ← post-Blender
caltagirone_pignaCono_blu_hollow_120mm_a1_v003.stl ← svuotato Spiral Vase

pulcinella_testaDiMoro_oro_clean_S_a1_v001.stl    ← variante piccola, oro
pulcinella_testaDiMoro_oro_clean_L_x1c_v001.stl   ← variante L per X1C

albero_corallo_membrana_clean_M_a1_v005.stl       ← 5 iterazioni di membrane removal

vaso_limoni_monocromo_bisect_L_a1_v002.stl        ← post-bisect Z=4.98
```

### Folder structure consigliata

```
output_stl/
├── caltagirone/
│   ├── pignaCono/
│   │   ├── source/                   ← foto originali
│   │   ├── gemini/                   ← output Gemini
│   │   ├── raw/                      ← STL grezzi dei vari tool
│   │   │   ├── _hi3d.stl
│   │   │   ├── _tripo.stl
│   │   │   └── _meshy.stl
│   │   ├── caltagirone_pignaCono_blu_clean_120mm_a1_v002.stl  ← final
│   │   └── notes.md                  ← prompt usato, settings, problemi
```

### Cross-reference

- **Regola 41 TESTING_LOG** — nomenclatura `relief|wall_art|2.5D|plaque|medallion|lithophane`
- **Loot Studios convention** — pre-supported/separate variants (rifermimento community)
- **Cults3D / MyMiniFactory upload guidelines** — bundle structure ufficiale
