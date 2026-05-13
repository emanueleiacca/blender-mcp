# KB AI 3D — Indice

Knowledge base per il workflow **foto → mesh 3D → stampa FDM** usando i 5 engine image-to-3D disponibili su MakerLab di MakerWorld. Dominio specifico: **prodotti decorativi artigianali** (ceramiche, terracotta, legno intagliato, metallo sbalzato) stampati mono-colore su Bambu A1.

Questa è la **pagina d'ingresso**. Carica questo file all'inizio di ogni sessione che riguarda image-to-3D.

---

## Mappa dei file

```
kb_ai3d/
├── INDEX.md                        ← sei qui
├── workflow.md                     ← step-by-step manuale completo (8 step)
├── decision_tree.md                ← quale tool 3D per quale foto (5 domande)
├── fdm_compatibility.md            ← rework Blender per ciascun tool
├── tools/
│   ├── tripo-3.1.md
│   ├── hitem3d-2.1.md              (Hi3D 2.1)
│   ├── hunyuan-3d-3.1.md
│   ├── meshy-6.md
│   └── rodin-gen-2.md
├── gemini_prompts/
│   ├── README.md                   ← guida d'uso dei prompt
│   ├── master_template.md          ← template base parametrizzato
│   ├── single_photo_cleanup.md     ← prompt completo per 1 foto
│   ├── multi_photo_canonical.md    ← prompt completo per N foto → 1 vista canonica
│   ├── delight_aggressive.md       ← block: per smalti/lucidi
│   ├── detail_preservation.md      ← block: per micro-rilievi fitti
│   └── perspective_correction.md   ← block: per foto storte/grandangolari
└── examples/                       ← (vuoto, da popolare con casi reali)
```

---

## Workflow in una riga

> Foto cellulare → **Gemini cleanup** (1 immagine pulita) → **MakerLab** (mesh STL) → **Blender** (rework FDM) → **Bambu Studio** → A1

Dettaglio completo in [`workflow.md`](workflow.md).

---

## I 5 tool image-to-3D disponibili

| Tool | Sweet spot | File |
|------|-----------|------|
| **Tripo 3.1** | Default solido, ornamenti fini, MakerLab nativo | [`tools/tripo-3.1.md`](tools/tripo-3.1.md) |
| **Hi3D 2.1** | Massimo dettaglio (1536³ Pro), Delight slider per smalti | [`tools/hitem3d-2.1.md`](tools/hitem3d-2.1.md) |
| **Hunyuan 3D 3.1** | Mesh watertight, simmetrie pulite, niente volti | [`tools/hunyuan-3d-3.1.md`](tools/hunyuan-3d-3.1.md) |
| **Meshy 6** | Veloce per soggetti semplici; smussa dettagli fini | [`tools/meshy-6.md`](tools/meshy-6.md) |
| **Rodin Gen 2** | Top qualità scultorea, perfetto per volti e ornamenti densi | [`tools/rodin-gen-2.md`](tools/rodin-gen-2.md) |

Tutti e 5 sono integrati nativamente su MakerLab (`makerworld.com/makerlab/imageTo3d`). Vedi [`decision_tree.md`](decision_tree.md) per la logica di scelta.

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

## Stato della KB (13 maggio 2026)

**Aggiornamenti recenti**:
- ✅ 5 tool documentati con specifiche tecniche e fonti
- ✅ Decision tree basato su 6 dimensioni (apertura/cavità, densità dettaglio, simmetria, n. foto, finish, volti, colori AMS)
- ✅ 9 file di prompt Gemini (modulari e componibili) — include `photo_fidelity_lock.md` post-fallimento allucinazione Gemini
- ✅ FDM compatibility per ciascun tool con tempi medi rework + ranking empirico per soggetti complessi
- ✅ 1 esempio loggato (`vaso_limoni_2026-05-08.md`)

**Da fare**:
- ⚠️ `examples/` da popolare con i casi di SESSION 002-004 (limone bassorilievo, asino multi-zampe, farfalla PCA, albero corallo membrana intrinseca, vaso limoni bisect definitivo)
- ⚠️ MakerLab è in evoluzione (Hi3D e Rodin aggiunti recentemente, possibili nuovi engine 2026) — verificare periodicamente che i settings descritti siano ancora correnti

**Lezioni cross-KB da SESSION 002-004** (rilevanti anche per kb_ai3d):
- Regola 25 TESTING_LOG: PRIMA di consigliare "Support: Off" calcolare overhang area — vale anche su mesh STL appena uscite da AI generator
- Regola 31 TESTING_LOG: membrane intrinseche di asset sculpt NON sono automatizzabili → preferire tool che producono mesh con minor membrana (Hunyuan watertight > Hi3D, vedi `fdm_compatibility.md`)
- Regola 36 TESTING_LOG: pre-export check OBBLIGATORIO (bbox_z_min=0, contact_points_count) — applicabile anche dopo rework su mesh AI
- Regola 41 TESTING_LOG: nomenclatura asset (relief|wall_art|2.5D|plaque|medallion|lithophane) indica tela intenzionale — utile anche per nominare correttamente gli STL uscenti da MakerLab

---

## Field notes

Quando una sessione produce scoperte pratiche (un prompt Gemini che funziona meglio di altri, un settings MakerLab non documentato, un difetto ricorrente di un tool su un certo tipo di soggetto), aggiungere una entry in `Blender for 3d print documentation/FIELD_NOTES.md` (file condiviso di field notes del progetto) e/o un esempio strutturato in `kb_ai3d/examples/`.
