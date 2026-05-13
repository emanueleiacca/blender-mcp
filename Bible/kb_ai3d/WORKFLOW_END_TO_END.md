# Workflow End-to-End — Foto reale → Stampa Bambu A1

Pipeline operativa unificata che attraversa le 3 sub-KB del progetto. Documenta i passi MANUALI dell'utente e i passi AUTOMATICI di Claude (via MCP `blender-mcp`).

---

## Diagramma alto livello

```
┌────────────────────────────────────────────────────────────────┐
│  STADIO 1: FOTO → STL grezzo                                   │
│  ────────────────────────────────────────                      │
│  [USER] Scatta foto cellulare ──────┐                          │
│                                     ▼                          │
│  [USER + CLAUDE] decision_tree.md → tool + prompt Gemini       │
│                                     │                          │
│  [USER] Apre Gemini, applica prompt suggerito                  │
│                                     │                          │
│  [USER] Verifica output (CHECKLIST in workflow.md step 4)      │
│                                     │                          │
│  [USER] Carica immagine pulita su MakerLab → engine 3D         │
│                                     │                          │
│  [USER] Download STL/3MF                                       │
└─────────────────────────────────┬───────────────────────────────┘
                                  │
┌─────────────────────────────────▼───────────────────────────────┐
│  STADIO 2: STL grezzo → STL print-ready                        │
│  ────────────────────────────────────────                      │
│  [USER] Import STL in Blender + dice "fatto" a Claude          │
│                                     │                          │
│  [CLAUDE via MCP] workflow consolidato 41 regole TESTING_LOG:  │
│      - analyze_mesh_for_print → diagnosi 17 metriche           │
│      - kb_route → routing rule attivata (R001..R016)           │
│      - Esecuzione playbook appropriato (repair_basic etc.)     │
│      - HIRES render multi-vista (R30) per validazione visiva   │
│      - analyze_overhang (R25)                                  │
│      - check_pre_export (R36) PRIMA di export                  │
│      - export_stl con suffisso _stl.stl (R23)                  │
└─────────────────────────────────┬───────────────────────────────┘
                                  │
┌─────────────────────────────────▼───────────────────────────────┐
│  STADIO 3: STL print-ready → Stampa fisica                     │
│  ────────────────────────────────────────                      │
│  [USER] Import STL in Bambu Studio                             │
│  [CLAUDE consulente] Settings da Bambu Wiki + analyze_overhang │
│  [USER] Slice + invio ad A1                                    │
│  [USER] Stampa + verifica fisica                               │
│  [USER + CLAUDE] Loop: cosa è andato bene/male → log session   │
└─────────────────────────────────────────────────────────────────┘
```

---

## STADIO 1 — Foto → STL (manuale assistito)

### 1.1 — Scatto foto
**Ruolo**: Utente solo.
**Output**: 1-4 foto cellulare ben illuminate, soggetto al 70-80% frame.
**Reference**: `kb_ai3d/workflow.md` §Step 1.

### 1.2 — Condivisione con Claude
**Ruolo**: Utente condivide foto + chiede "che fare?".
**Claude legge**:
1. `kb_ai3d/decision_tree.md` — 6 domande (apertura/cavità, densità dettaglio, simmetria, n foto, finish, volti, colori AMS)
2. `kb_ai3d/tools/<tool_scelto>.md` — settings MakerLab
3. `kb_ai3d/gemini_prompts/master_template.md` + i block specifici

**Claude restituisce**:
- Tool 3D consigliato (Tripo/Hi3D/Hunyuan/Meshy/Rodin)
- Prompt Gemini completo, pronto da copiare
- Settings MakerLab specifici per il tool
- Note attenzione (apertura/cavità? casting defects? delight?)

### 1.3 — Esecuzione Gemini
**Ruolo**: Utente esegue app Gemini con prompt + foto, ottiene immagine pulita.
**Verifica**: checklist in `kb_ai3d/workflow.md` §Step 4 (sfondo bianco, no riflessi, no ombre, silhouette fedele).

### 1.4 — MakerLab generazione mesh
**Ruolo**: Utente carica immagine su `makerworld.com/makerlab/imageTo3d`, seleziona engine, scarica STL.
**Tempo tipico**: 2.5-7 min secondo tool (vedi `decision_tree.md` tabella tempi).

### 1.5 — Download e nominazione STL
**Ruolo**: Utente.
**Convenzione naming**: `<soggetto>_<tool>_<data>.stl` (es. `pigna_siciliana_tripo31_2026-05-13.stl`).
**Salvare anche**: foto originali + immagine Gemini per tracciabilità (vedi `workflow.md` §Note di tracciabilità).

---

## STADIO 2 — STL grezzo → STL print-ready (AUTOMATIZZATO via Claude MCP)

### 2.1 — Apertura in Blender
**Ruolo**: Utente apre `addon.py` (Blender MCP), connette server, importa STL.
**Segnala a Claude**: "STL aperto, è disponibile come `<object_name>`".

### 2.2 — Diagnostica iniziale (Claude automatico)
**Tool MCP da chiamare**: `analyze_mesh_for_print(object_name)`.

**Output JSON con 17 metriche** (le 13 storiche + 4 nuove di P2.G2):
- Topologia: vertex_count, non_manifold_edges, boundary_loops, disconnected_shells, degenerate_faces, watertight
- Dimensioni: dimensions_mm, surface_area_mm2, center_of_mass_mm
- Qualità: aspect_ratio_p95, dihedral_angle_p90_deg, bottom_contact_area_mm2, convex_hull_volume_ratio, wall_thickness_*, inverted_face_pct
- **NUOVE (P2.G2)**: overhang_45_pct (R25), quasi_flat_ceiling_pct (R25), pca_thickness_ratio (R27), contact_points_count (R29)

### 2.3 — Routing decision
**Tool MCP**: `kb_route(analysis_json)` (server `blender-kb`).
**Output**: una delle 16 regole R001-R016 attivata + topic + playbook + expected_after.

### 2.4 — Esecuzione playbook
**Tool MCP**: `kb_get_playbook(playbook_id)` + `execute_blender_code(...)` per ogni step.

**Playbook disponibili (Bible/playbooks/)**:
- `repair_basic` — primo cleanup (merge by distance + fill holes + recalc normals)
- `repair_aggressive` — voxel remesh fallback per buchi grossi
- `recalc_normals` — solo normali
- `decimate_to_target` — polycount target
- `post_decimate_cleanup` — sliver triangles cleanup
- `quadriflow_preserve_edges` — re-topology pulita
- `remove_internal_membrane_ao` — **NEW** PyMeshLab AO per membrane intrinseche (R37)
- `remove_internal_faces_bvhtree` — **NEW** BVHTree raycast hemisphere (R38)
- `select_linked_flat` — **NEW** flood-fill BFS edge-per-edge (R39)

### 2.5 — Validazione HIRES (R30 obbligatoria)
**Tool MCP**: `render_hires_multiview(object_name, views="TOP,BOTTOM,FRONT", resolution_x=1920, resolution_y=1440)`.
**Mai dichiarare "operazione completata" senza inspezionare i PNG salvati.**

### 2.6 — Iterazione fino a `ready_to_slice=True`
**Loop**: `analyze_mesh_for_print` → `kb_route` → playbook → `analyze_mesh_for_print`.
**Stop rules** (R-vari del TESTING_LOG):
- 2 tentativi falliti membrana → R31 stop, proponi Meshmixer manuale
- Asset diventa tubolare/frammentato → Undo (R31)
- holes_fill restituisce 0 facce → R33 fan triangolare
- Utente dice "ancora vedo problema" 2× → R30 HIRES check obbligatorio

### 2.7 — Orientamento + multi-foot alignment (R29)
**Per asset con contact_points_count >= 3**: routing rule R016 → `orientation_strategy/multi_foot_plane_fit`.
Plane-fit SVD sui N punti di appoggio per parallelizzare al bed prima di Z=0.

### 2.8 — Pre-export check (R36 obbligatorio)
**Tool MCP**: `check_pre_export(object_name, expected_contact_points=N)`.
**Block se ready_to_export=False**.

### 2.9 — Export STL finale
**Tool MCP**: `export_stl(object_name, filepath, apply_modifiers=True)`.
**Naming**: `<oggetto>_<tag>_stl.stl` (R23).

---

## STADIO 3 — STL → Stampa fisica (manuale assistito)

### 3.1 — Import in Bambu Studio
**Ruolo**: Utente.

### 3.2 — Settings (Claude consulente)
**Claude legge**:
1. Output `analyze_overhang(object_name)` precedente → support_decision
2. `Bambu Wiki documentation/docs/bambu_studio_settings.md` (preset per profili)
3. `Bambu Wiki documentation/docs/tree_support_tuning.md` (Tree Hybrid)
4. **TESTING_LOG.md** SESSION 004 sintesi settings per tipologia asset (2.5D, 3D, multi-isole)

**Claude restituisce**: tabella "delta vs default" con N modifiche specifiche.

### 3.3 — Slice + invio
**Ruolo**: Utente.

### 3.4 — Stampa + verifica fisica
**Ruolo**: Utente.

### 3.5 — Loop feedback (impara)
Cosa è andato bene/male sulla stampa fisica?
- Bene → log in `kb_ai3d/examples/` come esempio strutturato
- Male → analisi: prompt Gemini? engine? rework Blender? settings Bambu?
- Nuove scoperte → aggiunta come regola/nota in TESTING_LOG.md + FIELD_NOTES.md

---

## Punti di contatto critici tra gli stadi

### STADIO 1 → 2: nominazione asset
Convenzione `<soggetto>_<tool>_<data>.stl` aiuta Claude a riconoscere:
- Asset proveniente da AI generator → applicare `kb_ai3d/fdm_compatibility.md` tool-specific
- Pattern nomenclatura (R41): `relief|wall_art|2.5D|plaque|medallion|lithophane` → tela intenzionale, NON tentare rimozione

### STADIO 2 → 3: passaggio metriche
L'output di `analyze_overhang` + `check_pre_export` del stadio 2 viene RIUSATO al stadio 3 per le settings Bambu Studio:
- `support_decision` → diretto su Bambu Studio Tree Hybrid
- `contact_points_count` + `bbox` → decisione brim

### STADIO 1 → 3 (skip 2?): NO, mai
Mai esportare STL da MakerLab direttamente a Bambu Studio senza passare per Stadio 2. Le mesh AI hanno problemi documentati (`fdm_compatibility.md` tabella) che lo slicer non gestisce.

---

## Stop rules cross-stadio

Quando applicare lo STOP del workflow:

| Trigger | Stadio | Azione |
|---|---|---|
| 3 generazioni MakerLab tutte inutilizzabili | 1 | Riconsiderare prompt Gemini, riscattare foto |
| Output Gemini è "AI render" e non "edit della foto" | 1 | Aggiungere `photo_fidelity_lock.md` al prompt |
| Asset categorizzato "strutturalmente occluso" (decoro copre 100%) | 1 | Usare direttamente Hi3D 2.1, niente Tripo/Rodin |
| Membrana intrinseca + 2 tentativi falliti | 2 | R31 stop, proponi Meshmixer manuale o accetta |
| Asset diventa frammentato dopo delete | 2 | Undo + ripensa criterio filtro |
| Stampa fallita per warping/adesione | 3 | Aumentare brim, verificare contact_points_count (R29/R36) |
| Stampa fallita per support marks visibili sul fronte | 3 | Riorientare l'asset (R29) o cambiare strategia "Block/Enforce" supports |

---

## Templates per messaggi tipici

### "Ti mando foto, dimmi che fare"
Claude risponde con:
1. Analisi foto: cosa vedo, materiale, apertura, simmetria
2. Decision tree applicato: tool consigliato + perché
3. Prompt Gemini pronto (testo da copiare)
4. Settings MakerLab specifici
5. Cose da verificare nell'output Gemini prima di MakerLab

### "STL aperto in Blender, procedi"
Claude esegue automaticamente:
1. `analyze_mesh_for_print` → diagnosi
2. `kb_route` → playbook
3. Esegue playbook
4. `render_hires_multiview` → mostra render
5. `analyze_overhang` → strategy supporti
6. `check_pre_export` → block export se non ready
7. Propone settings Bambu Studio in tabella

### "Stampa fatta, ecco com'è venuta [+ foto del print]"
Claude:
1. Confronta foto stampa vs foto originale soggetto
2. Identifica difetti (warping, layer shift, support marks, dimensioni)
3. Risale al stadio responsabile (gen AI? rework? settings?)
4. Propone fix per la prossima iterazione
5. Logga la sessione in `kb_ai3d/examples/<nome>_<data>.md` se è un caso formativo

---

## Riferimenti incrociati

- **kb_ai3d (questo)**: `INDEX.md`, `decision_tree.md`, `workflow.md`, `fdm_compatibility.md`, `tools/`, `gemini_prompts/`, `examples/`
- **Blender for 3d print documentation**: `INDEX.md` (56 topic), `routing_rules.yaml` (16 rules), `playbooks/` (9 playbook), `docs/membrane_removal.md`, FIELD_NOTES.md
- **Bambu Wiki documentation**: `INDEX.md` + 20 doc su Bambu Studio settings, materiali, supporti, ecc.
- **Workflow/TESTING_LOG.md**: 41 regole operative + 5 sessioni storiche (livello root del repo, FUORI da Bible/)

---

## Manutenzione di questo doc

Aggiornare WORKFLOW_END_TO_END.md quando:
- Nuovi tool MCP aggiunti al server `blender-mcp` → aggiornare elenco endpoint stadio 2
- Nuovi playbook aggiunti → aggiornare elenco stadio 2.4
- Nuove sub-KB aggiunte → aggiungere stadio o reference
- Nuovi pattern emergono dall'esperienza → aggiungere stop rule o template messaggio
