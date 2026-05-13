# Hitem3D 2.1 (Hi3D v2.1) — ENGINE PRIMARIO

> **🎯 H3.1 è l'engine principale di questo workflow** (decisione utente, 13 maggio 2026).
> Questo file è il riferimento più dettagliato della KB. Aggiornato con findings deepsearch 2026-05-13.

> **Nota nomenclatura**: il prodotto era "Hitem3D" fino al rebrand di aprile 2026, ora ufficialmente **Hi3D v2.1**. Dominio invariato (`hitem3d.ai`). Sviluppato da Math Magic, basato sul modello proprietario **Sparc3D**.

> **⚠️ Disponibilità su MakerWorld**: Hi3D 2.1 **è integrato in MakerLab** come engine ufficiale dal Q1 2026 (etichetta "NEW", confermato da UI maggio 2026). Tempo generazione ~7 min. Per parametri avanzati (Delight slider, View-Aligned vs Canonical Pose, face count) → web app diretta `hitem3d.ai`.

---

## 1. Cos'è e quando usarlo

Generatore image-to-3D **specializzato in mesh ad altissima risoluzione volumetrica** (fino a 1536³ Pro), pensato esplicitamente per stampa 3D e miniature ad alto dettaglio. Sweet spot: oggetti scultorei densi di dettagli fini (volti, ornamenti, micro-rilievi) dove la concorrenza a 1024³ "spalmaccia" la superficie.

**Verdetto empirico (2026-05-08, vaso limoni)**: **unico tool fra i 5 che produce un output lavorabile su soggetti "strutturalmente occlusi"** (decoro che copre 100% della parete esterna, struttura del contenitore nascosta). I 7 minuti di generazione valgono la pena rispetto ai 2.5-4 min dei concorrenti se l'oggetto non è banale.

**Quando preferirlo**:
- Ceramica decorata con ornamento fitto (testa di moro, pigna siciliana, vaso a sbalzo)
- Soggetti dove micro-rilievo è il valore primario (squame, intrecci, foglie scolpite, lineamenti facciali)
- Ceramica smaltata lucida (Delight slider dedicato)
- Soggetti dove i concorrenti producono "blob informe" (Tripo, Rodin, Meshy hanno fallito storicamente su decoro che oclude completamente la forma)

**Quando NON preferirlo**:
- Iterazioni rapide di test (7 min è troppo lento — per smoke test usa Tripo 3.1 a 2.5 min)
- Soggetti banali a bassa densità ornamentale (Hunyuan watertight è più rapido e altrettanto buono)
- Quando serve quad topology pulita per sculpting downstream (Hi3D produce triangle soup)

---

## 2. Capacità tecniche

### 2.1 Architettura

- **Modello base**: Sparc3D (proprietario, Math Magic) — modello generativo volumetrico
- **Topology**: triangle soup ad alta densità (non quad, non topology-aware)
- **v2.1 Advanced Mode**: face-count personalizzabile + mesh repair integrato

### 2.2 Risoluzione volumetrica

Tier disponibili (in ordine crescente):
- **512³** — fast preview, dettagli grossolani persi
- **1024³** — qualità "standard" dei concorrenti
- **1536³** — **target consigliato** per ceramica decorata
- **1536³ Pro** — top di categoria, fino a ~2M poligoni
- **Portrait mode** — modello dedicato a teste/volti scolpiti a 1536

### 2.3 Aggiornamenti v2.1 (vs v2.0)

- Geometria **>60% più veloce** (sotto i 2 minuti a 1536 nella web app diretta)
- Modalità **View-Aligned** (massima fedeltà all'immagine) vs **Canonical Pose** (struttura più consistente)
- Slider **Delight 0-1** per rimuovere ombre dipinte → **utile per ceramica smaltata** (vedi §5)
- **Fast Texture Mode** (<2 min) per generazione texture PBR (irrilevante per FDM mono-colore)
- **ComfyUI plugin** integrato (2026) — workflow scriptable per chi ha GPU locale

### 2.4 Export

- **Formati**: STL, OBJ, FBX, GLB
- **Polycount tipico al tier 1536³ Pro**: ~2M triangoli — i file STL sono pesanti (decine di MB)
- **Multi-view input**: supportato sulla web app diretta (l'integrazione MakerWorld espone solo single-view)

---

## 3. Input ideale

### 3.1 Foto sorgente (per single-view)

- **Sfondo**: pulito, isolato, alto contrasto (white/grey seamless)
- **Illuminazione**: **diffusa e uniforme** — ombre dure e luce laterale forte degradano la stima di forma. Outdoor coperto o softbox
- **Angolazione**: 3/4 frontale leggermente dall'alto è il default robusto
- **Cavità/contenitori aperti**: usare **angolazione laterale bassa** (< 10° sopra il bordo) — vedi `decision_tree.md` Domanda 0
- **Risoluzione**: alta, JPG/PNG/WebP, max 20 MB
- **Cosa rovina i risultati**:
  - ombre proiettate dipinte sul soggetto (Delight slider compensa parzialmente)
  - sfondo "rumoroso"
  - soggetto tagliato dal frame
  - riflessi speculari forti su ceramica lucida (Delight slider obbligatorio in questo caso)

### 3.2 Multi-view (solo web app)

- 2-4 foto da angolazioni distinte (front, 3/4 dx, 3/4 sx, retro)
- Stesso illuminamento tra le foto (CRITICO — altrimenti Sparc3D fa fatica a fondere)
- Stessa scala/distanza fotografica
- Per soggetti assialmente simmetrici (vasi, pigne): front + retro è sufficiente

### 3.3 Workflow Gemini pre-cleanup (raccomandato)

1. **BiRefNet** (opzionale, se sfondo complesso) → alpha PNG pulito
2. **Gemini 2.5 Flash** → delight + perspective correction
3. **Gemini 3 Pro** (Nano Banana Pro) → canonical view se multi-foto critica
4. → **Hi3D 2.1** (MakerLab o web app)

---

## 4. Limiti noti

- Mesh **non topology-clean**: triangoli densi e disordinati, inadatti a sculpting/rigging downstream senza retopo (irrilevante per FDM)
- Polycount molto alti = STL pesanti; Blender import lento (>30 sec a 2M poly)
- Storicamente seam di proiezione sul retro non visto in single-view; v2.0/2.1 hanno migliorato ma non azzerato
- "Free trial" limitato; uso intensivo sulla web app diretta richiede crediti a pagamento (su MakerLab: 2 crediti per export STL)
- **Membrane intrinseche**: come tutti i generative model, può produrre mesh con facce interne dove la decorazione si fonde con la parete (vedi `Blender for 3d print documentation/docs/membrane_removal.md` per il fix — Regola 31/37/38 di TESTING_LOG)

---

## 5. Adatto al nostro caso d'uso? — VERDETTO H3.1 = PRIMARY

**SÌ — engine primario del workflow** per ceramiche siciliane / italiane decorate.

### 5.1 Motivazione tecnica

- Teste di moro, pigne, figurine partenopee vivono di **micro-dettaglio scolpito** (squame, capelli intrecciati, foglie, lineamenti) — esattamente ciò per cui i 1536³ Pro sono pensati
- Texture/PBR irrilevanti per FDM mono-colore → **paghiamo solo per ciò che ci serve: geometria**
- **Delight slider a 0.7-1.0** rimuove l'ombreggiatura dipinta dalle foto di ceramica reale, evitando che finti chiaroscuri diventino rilievi falsi nella mesh — **vantaggio specifico vs Tripo/Hunyuan**
- **Unica vittoria empirica su soggetti strutturalmente occlusi** (vaso limoni 2026-05-08): Tripo, Rodin, Meshy 6 hanno tutti fallito; Hi3D ha prodotto un blob informe per la struttura ma con dettaglio decorativo corretto, da rifinire in Blender

### 5.2 Costi e tradeoff

| Aspetto | Hi3D 2.1 | Concorrenti |
|---|---|---|
| Tempo generazione MakerLab | ~7 min | Tripo 2.5 / Hunyuan 3 / Meshy 4 / Rodin 3 |
| Tempo generazione web app | <2 min (Fast Texture skip) | n/a |
| Polycount tipico | 1-2M | 100k-500k |
| Mesh topology cleanness | Bassa (triangle soup) | Hunyuan: alta (watertight) |
| Delight slider | ✅ presente | ❌ assente nei concorrenti |
| Multi-view input | ✅ web app | Tripo Multi View / Hunyuan / Rodin |
| Verdict su occlusione strutturale | ✅ unico funzionante | ❌ falliscono |

**Conclusione**: i 5 min di tempo extra rispetto a Hunyuan/Rodin sono **completamente compensati** dal fatto che H3.1 è l'unico che funziona su soggetti complessi. Su soggetti banali, usa Hunyuan/Tripo per velocità.

---

## 6. Tempo di generazione

### 6.1 MakerWorld (MakerLab UI)

**~7 minuti** (confermato da UI MakerWorld, maggio 2026 — etichettato "NEW"). Il più lento tra i 5 engine MakerLab.

### 6.2 Web app diretta (`hitem3d.ai`)

- **<2 minuti** a 1536³ (Geometry only, Fast Texture skip)
- ~3-4 minuti a 1536³ Pro (~2M poly)
- ~5-7 minuti se generi anche le texture PBR (irrilevante per FDM mono-colore)

**Strategia**: per iterare rapidamente, usa la web app diretta con Fast Texture mode. Per workflow lineare con un singolo soggetto, MakerLab è più semplice.

---

## 7. Settings/parametri

### 7.1 MakerLab UI (interface limitata)

⚠️ **Confermato da test reale (2026-05-08)**: nell'UI MakerLab si seleziona **SOLO l'engine** (Hitem3D 2.1). Non esistono controlli per:
- Tier risoluzione (512/1024/1536/Pro)
- Geometry Type (View-Aligned / Canonical Pose)
- Delight slider (0-1)
- Face count
- Mesh repair toggle
- Multi-view input

I parametri avanzati sono disponibili **solo sulla web app diretta** `hitem3d.ai`.

### 7.2 Web app diretta (parametri completi)

Settings raccomandati per ceramica decorata:

| Parametro | Valore consigliato | Note |
|---|---|---|
| **Resolution tier** | **1536³** (o 1536³ Pro per ornament density top) | 1024 perde squame/intrecci fini |
| **Mode** | **View-Aligned** | Più fedele alla foto. Canonical Pose solo se serve A-pose forzata |
| **Delight slider** | **0.7-1.0** se ceramica smaltata; **0.0-0.3** se gesso/terracotta opaca | Vedi §5.1 e `gemini_prompts/delight_aggressive.md` |
| **Face count target** | **300k-500k** (FDM) | 2M è eccessivo per A1; Blender decimerà comunque |
| **Mesh repair** | **ON** | Riempie holes e fixa non-manifold elementari |
| **Multi-view** | ON se hai 2-4 foto coerenti | OFF se single-view (Gemini canonical) |
| **Generate texture** | **OFF** (Fast Texture skip) | Irrilevante per FDM mono-colore. Risparmia 3-5 minuti |

### 7.3 ComfyUI integration (Q1 2026)

Per chi ha GPU locale (12GB+ VRAM), il plugin ComfyUI permette di scriptare il workflow:

```
Image Load → BiRefNet (BG removal) → Hi3D 2.1 Node (1536³, Delight 0.8) → Mesh Repair → Export STL
```

**Vantaggi**: batch processing, reproducibility, no costo per generazione.
**Svantaggi**: setup ComfyUI non banale, richiede VRAM significativa, no Bambu integration diretta.

⚠️ **Status**: integrazione ComfyUI ufficiale è in beta — la stabilità del workflow on-prem dipende dalla versione Sparc3D che Math Magic decide di esporre. Verificare release notes su `hitem3d.ai/blog` prima di basare un workflow produttivo su questo.

---

## 8. Rework Blender post-Hi3D

Vedi `fdm_compatibility.md` § Hi3D 2.1 per la check-list completa. In sintesi:

1. **PRIMA del pre-flight**: se polycount > 1M, fare un Decimate Geometry con ratio 0.3-0.5 PRIMA di tutto il resto, altrimenti Blender lagga
2. Pre-flight comune (Apply Scale, non-manifold check, Merge by Distance)
3. **Verifica seam posteriore**: Edit Mode → vista da retro → cerca discontinuità verticali → fixale con Mesh → Clean Up → Fill Holes (max edges 4)
4. **Membrane intrinseche** (se decorazione fitta): controlla con `analyze_mesh_for_print` (MCP `blender-mcp`) → metric `quasi_flat_ceiling_pct`. Se > 5%, valuta PyMeshLab AO o BVHTree raycast (vedi `Bible/Blender for 3d print documentation/docs/membrane_removal.md`)
5. **Decimate finale** a target 150-300k tri (Bambu Studio non ha bisogno di più)

**Tempo medio rework post-Hi3D**: 10-25 min (più dei concorrenti per il polycount).

---

## 9. Workflow ricetta — H3.1 per ceramica siciliana decorata

### 9.1 Setup foto

1. Soggetto su sfondo bianco/grigio neutro
2. Luce diffusa (giorno coperto, vicino finestra senza sole diretto)
3. 1-3 foto da angolazioni laterali basse (per contenitori aperti)
4. JPG/PNG, soggetto al 70-80% del frame

### 9.2 Gemini cleanup

1. **Photo fidelity lock** sempre come prima sezione
2. `master_template.md` come base
3. **Block aggiuntivi** in ordine:
   - `casting_defects.md` se gesso, oppure `delight_aggressive.md` se ceramica smaltata
   - `detail_preservation.md` per micro-rilievi fitti
   - `perspective_correction.md` solo se foto storta
4. Output: 1 PNG 2048×2048 con sfondo bianco puro, delight applicato

### 9.3 Generazione Hi3D

**Opzione A — MakerLab** (semplice):
- `makerworld.com/makerlab/imageTo3d`
- Engine: Hitem3D 2.1
- Upload immagine Gemini → genera (7 min) → export STL

**Opzione B — Web app diretta** (controllo completo):
- `hitem3d.ai` → upload
- Resolution: **1536³**
- Mode: **View-Aligned**
- Delight: **0.8** (ceramica) o **0.2** (gesso)
- Face count: **300k**
- Mesh repair: **ON**
- Generate texture: **OFF**
- Genera (~2 min) → download STL

### 9.4 Validazione pre-Blender

Prima di aprire Blender, in Hi3D web app o MakerLab:
- Ruota la preview a 360° — la silhouette è fedele alla foto?
- I dettagli ornamentali sono visibili?
- Il fondo del soggetto è chiuso (non bucato)?
- La base appare piatta o inclinata?

Se 2 o più punti falliscono → rigenera con setting diversi (es. Delight più basso se i dettagli sono spariti). Massimo 3 tentativi prima di tornare alla foto sorgente o cambiare strategia.

### 9.5 Pipeline downstream

Hi3D STL → Blender (MCP `blender-mcp`) → analyze_mesh_for_print → fix non-manifold + membrane se serve → export → Bambu Studio → A1.

Vedi `WORKFLOW_END_TO_END.md` per il workflow integrato cross-KB completo.

---

## 10. Edge cases noti per Hi3D 2.1

### 10.1 Soggetto cavo (vaso/ciotola)

- **Foto laterale bassa obbligatoria** (vedi `decision_tree.md` Domanda 0)
- Hi3D produce comunque blob nella struttura interna ma con dettaglio decorativo corretto
- Rework Blender: bisect Z=top_rim_z per aprire la cavità (vedi Regola 34 TESTING_LOG)

### 10.2 Volti scolpiti

- Usare **Portrait mode** se disponibile sulla web app (modello specializzato)
- Se non disponibile: 1536³ Pro standard funziona, ma Rodin Gen 2 è marginalmente migliore sui volti

### 10.3 Membrane intrinseche post-generazione

- Sintomo: `analyze_mesh_for_print` reporta `quasi_flat_ceiling_pct > 5%`
- Fix: vedi `Bible/Blender for 3d print documentation/docs/membrane_removal.md`
- Strategia raccomandata: PyMeshLab AO (Regola 37) o BVHTree raycast (Regola 38)
- Se entrambe falliscono: rigenera con Delight diverso o cambia angolazione foto

### 10.4 Asset multi-foot (statue, animali con zampe)

- Hi3D produce talvolta basi inclinate o zampe non a Z=0
- Fix: usa MCP tool `analyze_overhang` + `check_pre_export` (Regole 29/36 TESTING_LOG)
- Allinea le N zampe via plane-fit SVD prima di esportare

---

## 11. Fonti

### Documentazione ufficiale

- https://www.hitem3d.ai/blog/Hi3D-v2-1-is-Live-Faster-More-Stable-More-Controllable/
- https://www.hitem3d.ai/blog/en-Hi3D-Updates/
- https://www.hitem3d.ai/3dprinting/use-case
- https://www.hitem3d.ai/blog/en-From-Image-to-Physical-Object-A-Complete-AI-to-3D-Printing-Workflow-Guide/
- https://www.hitem3d.ai/blog/Introducing-Hitem3D-2-0/

### Confronti e benchmark

- https://trellis2.app/blog/best-ai-3d-model-generator
- https://www.3daistudio.com/3d-generator-ai-comparison-alternatives-guide/hitem3d-alternative
- https://www.fabbaloo.com/news/hitem3d-releases-version-2-0-with-integrated-texture-generation-for-higher-fidelity-3d-models
- https://www.meshy.ai/blog/best-ai-tools-for-3d-printing
- https://3dprintingindustry.com/news/bambu-lab-launches-new-ai-3d-model-generator-233736/

### KB cross-reference

- `WORKFLOW_END_TO_END.md` — pipeline integrata
- `fdm_compatibility.md` § Hi3D 2.1 — rework Blender
- `decision_tree.md` — quando preferire Hi3D
- `Bible/Blender for 3d print documentation/docs/membrane_removal.md` — fix membrane intrinseche
- `Workflow/TESTING_LOG.md` Regole 25/31/36 — vincoli FDM post-AI

---

## Changelog

- **2026-05-13**: file esteso a engine primario del workflow. Aggiunto §2.3 ComfyUI, §7.3, §9 ricetta H3.1, §10 edge cases, §11 fonti. Cross-reference TESTING_LOG e membrane_removal.
- **2026-05-08**: confermato verdict empirico unico tool funzionante su "structurally occluded subjects".
- **2026-04**: rebrand Hitem3D → Hi3D v2.1.
