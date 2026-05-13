# Next Deepsearch — programmazione round successivo

> **Scopo**: questo file documenta cosa è rimasto **non coperto** dal round di deepsearch 2026-05-13 e cosa sarebbe utile esplorare nei round successivi. Da consultare prima di lanciare nuove ricerche parallele.

**Ultima compilazione**: 2026-05-13
**Stato KB post-round 1**: vedi `INDEX.md` § Stato della KB

---

## Lacune identificate post-round 1

### Lacuna 1 — Hi3D 2.1 settings empirici reali

**Cosa manca**: il file `tools/hitem3d-2.1.md` ha ricetta operativa basata su documentazione ufficiale Math Magic e benchmark indipendenti. Mancano **dati empirici raccolti dal workflow utente reale** su:

- **Delight slider sweet spot per ceramica siciliana specifica** (testa di moro vs pigna vs vaso limoni)
- Quando il Portrait mode (1536 dedicated face model) supera quello standard
- Quanto il `Mesh Repair` toggle on/off cambia il rework Blender downstream
- Performance reale del **ComfyUI plugin** (stabilità, VRAM richiesta, qualità vs cloud)

**Per il prossimo round**:
- Deepsearch su review community Hi3D ComfyUI plugin (Reddit, Discord Math Magic, GitHub issues)
- Test empirico utente di 3-4 settings combinations su stesso soggetto

### Lacuna 2 — Workflow batch processing

**Cosa manca**: la KB descrive il workflow **single-asset**. Non c'è guidance per chi vuole processare **N asset in batch** (es. 20 ceramiche da catalogare).

**Per il prossimo round**:
- Workflow batch via Hi3D ComfyUI plugin
- Scripting Bambu Studio per slice multipli automatici
- Quality control automatizzato post-batch (analyze_mesh_for_print su N STL)
- Reference: come fanno i pro su Patreon (drop mensile di 20+ asset)

### Lacuna 3 — Materials e finish post-stampa per look ceramica autentica

**Cosa manca**: `ceramic_filaments.md` documenta i filamenti, ma manca il **finish post-stampa** per look autentico:

- Tecniche sanding/polishing
- Vernici/smalti consigliate per look ceramica (Citadel, Vallejo, Liquitex)
- Patina techniques (washes, dry brushing per look "vissuto")
- Cottura/seal per durability

**Per il prossimo round**:
- Deepsearch tutorial finish ceramica look (YouTube, Patreon, IG)
- Riferimento workflow Garland (Conservation ceramics)

### Lacuna 4 — Quality control / validation oggettiva

**Cosa manca**: la KB ha checklist soggettive ("ti sembra ok?"). Servono metriche **oggettive** per:

- Quality score automatico post-Hi3D (silhouette diff vs source image)
- Print-readiness score (composto di non-manifold, overhang, thickness)
- Comparison metric tra tool su stesso soggetto

**Per il prossimo round**:
- Deepsearch su quality metrics per AI-generated 3D (IoU 3D, Chamfer distance, mesh quality scores)
- Tencent HY3D-Bench methodology (252K watertight meshes — di cosa misura)
- Tool per silhouette comparison (Blender script che renderizza mesh e confronta con foto)

### Lacuna 5 — Edge case validation empirica

**Cosa manca**: i **7 nuovi prompt block edge case** (transparency, fibrous, articulated, ecc.) sono basati su ricerca + ragionamento. Manca validation empirica.

**Per il prossimo round**:
- Test utente di ognuno dei 7 block su soggetto reale
- Documentare in `examples/` ognuno dei casi che funziona/fallisce
- Refinement dei block in base a feedback

### Lacuna 6 — Integration MakerLab roadmap

**Cosa manca**: MakerLab evolve velocemente (Tripo P1.0 introdotto Mar 2026, Hi3D added Q1 2026, Meshy 6 added 17 Mar 2026). Manca:

- Roadmap MakerLab pubblica (se esiste)
- Quale engine arriverà dopo (rumor TRELLIS.2 cloud? Hunyuan 3.5 cloud?)
- Quali parametri verranno esposti in MakerLab UI nel prossimo trimestre

**Per il prossimo round**:
- Deepsearch su forum.bambulab.com + Discord MakerWorld per signals
- Verifica periodica (ogni 3 mesi) della UI MakerLab per nuovi engine

### Lacuna 7 — Mobile/iPad workflow

**Cosa manca**: il workflow attuale assume **desktop** (Blender, MakerLab in browser). Esiste un workflow **iPad-only** o **mobile-first**?

- Nomad Sculpt cresce iPad — vale per ceramica?
- KIRI Engine mobile per photogrammetry da iPhone
- Workflow integrato iPad → Bambu Studio mobile app

**Per il prossimo round**:
- Deepsearch su Patreon iPad sculptors (Apple Pencil + Nomad)
- Test empirico workflow iPad → STL → A1

### Lacuna 8 — Multicolore AMS empirico

**Cosa manca**: la KB documenta `color_simplification.md` block per stampe AMS. Mancano:

- Test empirico dei colori che sopravvivono al pipeline (Gemini → Meshy 6 → 3MF → Bambu Studio → AMS A1)
- Quanti colori effettivamente recuperabili (4 dichiarati AMS, ma in pratica?)
- Workflow per assignare colori in Bambu Studio se 3MF perde l'info

**Per il prossimo round**:
- Deepsearch su forum Bambu community per workflow AMS + AI
- Test utente con soggetto multi-color tipico (es. testa di moro bianca + nera + oro)

### Lacuna 9 — Failure case studies estesi

**Cosa manca**: examples/ ora ha 6 casi (1 originale + 5 nuovi). Servono **più failure cases** documentati:

- Casi dove Hi3D ha fallito anche con setting corretti
- Casi dove Bambu Studio auto-orient ha sbagliato
- Casi dove la stampa è venuta male per ragioni non previste

**Per il prossimo round**:
- Logging più aggressivo dei fallimenti (anche quelli "embarrassing")
- Sezione "common failure modes" derivata da N casi

### Lacuna 10 — Cross-pollination con altre KB

**Cosa manca**: la KB kb_ai3d ha cross-reference solide con TESTING_LOG e Blender KB, ma poca con **Bambu Wiki documentation**. Esempi:

- Quale layer height per Hi3D-decimated mesh a 200k tri?
- Quale tree support density per soggetti AI-generated tipici?
- Auto-orient settings ottimali per categoria asset

**Per il prossimo round**:
- Audit cross-reference tra kb_ai3d e Bambu Wiki documentation
- Aggiungere section in WORKFLOW_END_TO_END sulla mapping kb_ai3d → Bambu Wiki

---

## Strategie deepsearch raccomandate per round 2

### Strategia A — Validazione empirica vs Strategia B — Discovery

**Round 1 (2026-05-13)** è stata **discovery-driven** (cosa esiste, cosa è cambiato 2026). Per round 2 considerare:

**Round 2A — Validation-driven** (test empirici):
- Test settings combinations Hi3D
- Test 7 edge case blocks
- Test workflow batch
- Documentare in `examples/`

**Round 2B — Discovery continuation**:
- ZBrush 2026 photogrammetry pipeline
- Nuovi paper arXiv image-to-3D Q3 2026
- Update MakerLab post-summer 2026

### Strategia C — Vertical deep-dive

Invece di 4 ricerche parallele "wide", **una ricerca verticale profonda** su:

- **Hi3D 2.1 expert deep-dive**: tutti i parametri, tutti i sweet spot, tutti i tradeoff, comparison granulare con concorrenti
- **Ceramica siciliana specifica**: ogni categoria (testa di moro, pigna, vaso limoni, asino, frutta) con workflow ottimale per ognuna

---

## Cosa NON cercare nel prossimo round

Lessons learned dal round 1:

- **Non duplicare** ricerca su engine che non useremo (TripoSR, InstantMesh — già consolidati in legacy)
- **Non investire** in tool con setup proibitivo (PartCrafter sperimentale, ORGAN GAN niche)
- **Non chiedere** "best AI tool 2026" generale — la KB ha già la risposta filtrata per il dominio
- **Non re-investigare** Meshy 4 (deprecated confirmed)

---

## Output structure raccomandata per round 2

Quando si lancia round 2, chiedere ai 4 agenti deepsearch di restituire **diff** rispetto allo stato attuale della KB, non report standalone:

```
For each finding:
- File path da modificare (se esistente) o da creare (se nuovo)
- Specific edit suggerito (Edit block o Write content)
- Source citation (URL + data)
- Priority P0-P3 (impact × effort)
```

Questo format è già stato applicato a `RESEARCH_2026-05-13.md` § E — replicare.

---

## Manutenzione di questo doc

Aggiornare `NEXT_DEEPSEARCH.md` quando:
- Si chiude un round (segnare lacune coperte ✅)
- Si scopre una nuova lacuna mentre si fa workflow normale
- Si decide di non investigare più una lacuna (segnare ❌ con motivazione)
