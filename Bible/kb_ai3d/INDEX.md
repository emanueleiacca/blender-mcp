# KB AI 3D — Indice

Knowledge base per il workflow **foto → mesh 3D → stampa FDM** usando i 5 engine image-to-3D disponibili su MakerLab di MakerWorld. Dominio specifico: **prodotti decorativi artigianali** (ceramiche, terracotta, legno intagliato, metallo sbalzato) stampati mono-colore su Bambu A1.

Questa è la **pagina d'ingresso**. Carica questo file all'inizio di ogni sessione che riguarda image-to-3D.

---

## Mappa dei file

```
kb_ai3d/
├── INDEX.md                        ← sei qui
├── workflow.md                     ← step-by-step manuale completo (8 step)
├── decision_tree.md                ← quale tool 3D per quale foto (15+ domande)
├── fdm_compatibility.md            ← rework Blender per ciascun tool + naming
├── WORKFLOW_END_TO_END.md          ← pipeline integrata cross-KB + marketing/licensing
├── RESEARCH_2026-05-13.md          ← sintesi deepsearches (reference)
├── NEXT_DEEPSEARCH.md              ← cosa programmare nel prossimo round
├── birefnet_workflow.md            ← workflow ibrido BiRefNet pre-pass
├── ceramic_filaments.md            ← filamenti per look ceramica A1
├── tools/
│   ├── tripo-3.1.md                ← engine MakerLab
│   ├── hitem3d-2.1.md ⭐           ← H3.1 ENGINE PRIMARIO (vedi anche tools/tripo-p1-h3-1.md per Tripo)
│   ├── hunyuan-3d-3.1.md           ← engine MakerLab
│   ├── meshy-6.md                  ← engine MakerLab (97% slicer pass)
│   ├── rodin-gen-2.md              ← engine MakerLab (top per volti)
│   ├── trellis-2.md                ← OSS local primary (MIT, GPU)
│   ├── hunyuan3d-2-1-oss.md        ← OSS local secondary (Tencent)
│   ├── sam-3d.md                   ← Meta SAM 3D Objects (niche, scene-level)
│   └── tripo-p1-h3-1.md            ← Tripo enterprise dual-track (NUOVO 2026)
├── gemini_prompts/
│   ├── README.md                   ← guida d'uso + iteration protocol + Gemini versions
│   ├── photo_fidelity_lock.md      ← ⚠️ sempre prima sezione
│   ├── master_template.md          ← template base (affirmative framing 2026)
│   ├── proportion_anchor_block.md  ← safety net drift proporzioni
│   ├── single_photo_cleanup.md
│   ├── multi_photo_canonical.md
│   ├── casting_defects.md          ← block: gesso (bolle, linee stampo)
│   ├── delight_aggressive.md       ← block: smalti/lucidi
│   ├── detail_preservation.md      ← block: micro-rilievi
│   ├── perspective_correction.md   ← block: foto storte
│   ├── color_simplification.md     ← block: multicolore AMS
│   ├── transparency_reflective.md  ← block edge D7: vetro/cromo
│   ├── fibrous_subject.md          ← block edge D8: pelo/fibre
│   ├── articulated_multipart.md    ← block edge D9: multi-pezzo
│   ├── severe_undercuts.md         ← block edge D12: sottosquadri
│   ├── engraved_text_lt_2mm.md     ← block edge D11: testo fine
│   ├── archaeological_restoration.md ← block edge D14: frammenti
│   └── video_only_input.md         ← block edge D15: solo video
└── examples/
    ├── limone_bassorilievo_2026-05-01.md     ← wall art success
    ├── asino_4_zampe_2026-05-03.md           ← multi-foot SVD Regola 29
    ├── farfalla_PCA_2026-05-04.md            ← PCA orient Regola 28
    ├── albero_corallo_failed_2026-05-05.md   ← membrane FAILED Regola 31
    ├── vaso_limoni_2026-05-08.md             ← occluded subject saga giorno 1
    └── vaso_limoni_bisect_definitivo_2026-05-09.md ← KISS bisect Regola 34
```

---

## Workflow in una riga

> Foto cellulare → **Gemini cleanup** (1 immagine pulita) → **MakerLab** (mesh STL) → **Blender** (rework FDM) → **Bambu Studio** → A1

Dettaglio completo in [`workflow.md`](workflow.md).

---

## Tool image-to-3D — engine primario e fallback

### 🎯 Engine primario (default)

| Tool | Sweet spot | File |
|------|-----------|------|
| **Hi3D 2.1** ⭐ | **Engine primario** — soggetti decorati, ornamenti fitti, ceramica smaltata (Delight slider) | [`tools/hitem3d-2.1.md`](tools/hitem3d-2.1.md) |

### MakerLab fallback / casi specifici

| Tool | Sweet spot | File |
|------|-----------|------|
| **Tripo 3.1** | Smoke test rapidi su soggetti semplici (~2.5 min) | [`tools/tripo-3.1.md`](tools/tripo-3.1.md) |
| **Hunyuan 3D 3.1** | Mesh watertight, simmetrie pulite, niente volti | [`tools/hunyuan-3d-3.1.md`](tools/hunyuan-3d-3.1.md) |
| **Meshy 6** | 97% slicer pass rate, AMS multi-color | [`tools/meshy-6.md`](tools/meshy-6.md) |
| **Rodin Gen 2** | Top qualità scultorea per volti | [`tools/rodin-gen-2.md`](tools/rodin-gen-2.md) |
| **Tripo P1.0 / H3.1** | Tripo enterprise dual-track (NUOVO 2026) | [`tools/tripo-p1-h3-1.md`](tools/tripo-p1-h3-1.md) |

### Open-source local (per chi ha GPU)

| Tool | Sweet spot | File |
|------|-----------|------|
| **TRELLIS.2** | OSS primary, MIT, watertight scripts | [`tools/trellis-2.md`](tools/trellis-2.md) |
| **Hunyuan3D 2.1 OSS** | OSS secondary, più accessibile (8GB VRAM) | [`tools/hunyuan3d-2-1-oss.md`](tools/hunyuan3d-2-1-oss.md) |

### Niche

| Tool | Sweet spot | File |
|------|-----------|------|
| **Meta SAM 3D** | Scene-level segmentation (foto in contesto) | [`tools/sam-3d.md`](tools/sam-3d.md) |

Tutti e 5 gli engine MakerLab sono integrati nativamente su `makerworld.com/makerlab/imageTo3d`. Vedi [`decision_tree.md`](decision_tree.md) per la logica di scelta.

---

## Come usare la KB in una sessione tipo

**Setup iniziale (una volta per sessione)**:
1. Carica `INDEX.md` (questo file)
2. Carica `workflow.md`
3. Carica `decision_tree.md`

**Per ogni nuovo soggetto**:
1. Utente mostra foto/foto del soggetto
2. Claude: leggi `decision_tree.md` → decidi tool 3D + tipo prompt Gemini
3. Claude: leggi il `tools/<tool>.md` scelto per i settings MakerLab
4. Claude: leggi i `gemini_prompts/` necessari (master + eventuali block) → componi prompt finale per l'utente
5. Utente esegue Gemini → MakerLab → download STL
6. Claude: leggi `fdm_compatibility.md` → guida l'utente nel rework Blender

**Doc da NON caricare preventivamente**: i singoli `tools/*.md` e i prompt-block specifici. Si caricano on-demand.

---

## Knowledge base correlate

- [`Blender for 3d print documentation/INDEX.md`](../Blender%20for%203d%20print%20documentation/INDEX.md) — KB Blender (41 regole operative + 56 topic + 9 playbook + 16 routing rules)
- [`Bambu Wiki documentation/INDEX.md`](../Bambu%20Wiki%20documentation/INDEX.md) — KB Bambu Lab (specs A1, materiali, Bambu Studio)

I tre KB sono complementari, ognuno copre uno stadio della pipeline end-to-end:
- **kb_ai3d** (questa): foto → STL grezzo (uso manuale + reference per Claude)
- **Blender for 3d print documentation**: STL grezzo → STL print-ready (usato via MCP `blender-mcp`)
- **Bambu Wiki documentation**: STL print-ready → stampa fisica

## Modalità d'uso (NON via MCP)

Questa KB **non è esposta come tool MCP**. È documentazione di reference per:
- L'**utente**: guida step-by-step per la pipeline foto → STL
- **Claude**: docs da consultare quando l'utente condivide foto e chiede assistenza nella scelta tool/prompt

Differenza con `Blender for 3d print documentation` (che invece è KB MCP completa con tool `kb_get_topic`, `kb_route`, ecc.).

---

## Stato della KB (13 maggio 2026 — major update)

**Aggiornamenti 2026-05-13** (post-deepsearch):
- ⭐ **H3.1 dichiarato engine primario** del workflow (decisione utente)
- ✅ `hitem3d-2.1.md` ESTESO con ComfyUI 2026, Fast Texture, ricetta workflow completa, edge cases
- ✅ `meshy-6.md` UPDATE con benchmark 97% slicer pass + AMS multi-color
- ✅ `decision_tree.md` esteso con **D7-D15** (9 nuove domande edge case)
- ✅ `master_template.md` riformulato con **affirmative framing** (best practice Gemini 2026)
- ✅ **NEW** `proportion_anchor_block.md` (safety net drift proporzioni)
- ✅ `gemini_prompts/README.md` esteso con iteration protocol + Gemini version recommendations + alternative AI tools
- ✅ **NEW 7 edge case blocks**: transparency, fibrous, articulated, undercuts, engraved_text, archaeological, video_only
- ✅ **NEW** `tools/trellis-2.md` (OSS local primary)
- ✅ **NEW** `tools/hunyuan3d-2-1-oss.md` (OSS local secondary)
- ✅ **NEW** `tools/sam-3d.md` (Meta SAM 3D niche)
- ✅ **NEW** `tools/tripo-p1-h3-1.md` (Tripo dual-track enterprise)
- ✅ **NEW** `birefnet_workflow.md` (pre-pass BG removal)
- ✅ **NEW** `ceramic_filaments.md` (filamenti per look ceramica A1)
- ✅ `fdm_compatibility.md` H3.1 ESTESO con 10-step protocol + asset naming convention community
- ✅ `WORKFLOW_END_TO_END.md` esteso con workflow professionali community + marketing/licensing
- ✅ **5 nuovi esempi loggati**: limone_bassorilievo, asino_4_zampe, farfalla_PCA, albero_corallo_failed, vaso_limoni_bisect_definitivo
- ✅ Riferimenti Meshy 4 **rimossi** (API discontinued)
- ✅ **NEW** `NEXT_DEEPSEARCH.md` — programmazione round successivo

**Aggiornamenti precedenti (8 maggio 2026)**:
- 5 tool documentati con specifiche tecniche e fonti
- Decision tree basato su 6 dimensioni (apertura/cavità, densità dettaglio, simmetria, n. foto, finish, volti, colori AMS)
- 9 file di prompt Gemini (modulari e componibili)
- 1 esempio loggato (`vaso_limoni_2026-05-08.md`)

**Da fare (vedi NEXT_DEEPSEARCH.md per dettagli)**:
- ⚠️ Test empirici dei tool OSS local (TRELLIS.2, Hunyuan3D 2.1 OSS) sul workflow utente
- ⚠️ Validazione dei 7 edge case blocks su soggetti reali
- ⚠️ MakerLab in evoluzione — verificare periodicamente engine label e timings

**Lezioni cross-KB da SESSION 002-004** (rilevanti anche per kb_ai3d):
- Regola 25 TESTING_LOG: PRIMA di consigliare "Support: Off" calcolare overhang area — vale anche su mesh STL appena uscite da AI generator
- Regola 31 TESTING_LOG: membrane intrinseche di asset sculpt NON sono automatizzabili → preferire tool che producono mesh con minor membrana (Hunyuan watertight > Hi3D, vedi `fdm_compatibility.md`)
- Regola 36 TESTING_LOG: pre-export check OBBLIGATORIO (bbox_z_min=0, contact_points_count) — applicabile anche dopo rework su mesh AI
- Regola 41 TESTING_LOG: nomenclatura asset (relief|wall_art|2.5D|plaque|medallion|lithophane) indica tela intenzionale — utile anche per nominare correttamente gli STL uscenti da MakerLab

---

## Field notes

Quando una sessione produce scoperte pratiche (un prompt Gemini che funziona meglio di altri, un settings MakerLab non documentato, un difetto ricorrente di un tool su un certo tipo di soggetto), aggiungere una entry in `Blender for 3d print documentation/FIELD_NOTES.md` (file condiviso di field notes del progetto) e/o un esempio strutturato in `kb_ai3d/examples/`.
