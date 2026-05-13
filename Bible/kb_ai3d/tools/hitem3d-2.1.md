# Hitem3D 2.1 (Hi3D v2.1)

> **Nota nomenclatura**: il prodotto era "Hitem3D" fino al rebrand di aprile 2026, ora ufficialmente **Hi3D v2.1**. Dominio invariato (`hitem3d.ai`). Sviluppato da Math Magic, basato sul modello proprietario **Sparc3D**.

> **⚠️ Disponibilità su MakerWorld**: Hi3D **non risulta integrato come engine ufficiale** in MakerLab (a maggio 2026 MakerLab espone Meshy 6, Hunyuan 3.1, Tripo). Workflow attuale: web app `hitem3d.ai` → download STL → upload manuale in Bambu Studio. Da verificare se cambia.

## 1. Cos'è e quando usarlo

Generatore image-to-3D **specializzato in mesh ad altissima risoluzione volumetrica** (fino a 1536³ Pro), pensato esplicitamente per stampa 3D e miniature ad alto dettaglio. Sweet spot: oggetti scultorei densi di dettagli fini (volti, ornamenti, micro-rilievi) dove la concorrenza a 1024³ "spalmaccia" la superficie.

## 2. Capacità tecniche

- **Topology**: triangle soup ad alta densità (non quad, non topology-aware). v2.1 aggiunge in Advanced Mode **face-count personalizzabile** e **mesh repair** integrato
- **Polycount**: fino a **~2M poligoni** al tier 1536³ Pro (top di categoria fra i tool consumer)
- **Risoluzione tier**: 512 / 1024 / 1536 / **1536 Pro** (volumetrica). Esiste modello **Portrait** ottimizzato per teste/volti a 1536
- **Format export**: STL, OBJ, FBX, GLB
- **Multi-view**: supportato (anche se l'integrazione MakerWorld — quando arriverà — esporrà tipicamente solo single-view)
- **v2.1 specifiche**:
  - geometria **>60% più veloce** (sotto i 2 minuti tipici a 1536)
  - modalità **View-Aligned** (massima fedeltà all'immagine) vs **Canonical Pose** (struttura più consistente)
  - slider **Delight 0-1** per rimuovere ombre dipinte → **utile per noi** (vedi §5)

## 3. Input ideale

- **Sfondo**: pulito, isolato, alto contrasto (white/grey seamless)
- **Illuminazione**: **diffusa e uniforme** — ombre dure e luce laterale forte degradano la stima di forma. Outdoor coperto o softbox
- **Angolazione**: 3/4 frontale leggermente dall'alto è il default robusto; per soggetti a simmetria assiale (pigne, vasi) frontale ortogonale + lato aiutano in multi-view
- **Risoluzione**: alta, JPG/PNG/WebP, max 20 MB
- **Cosa rovina i risultati**: ombre proiettate dipinte sul soggetto, sfondo "rumoroso", soggetto tagliato dal frame, riflessi speculari forti su ceramica lucida

## 4. Limiti noti

- Mesh **non topology-clean**: triangoli densi e disordinati, inadatti a sculpting/rigging downstream senza retopo
- Polycount molto alti = STL pesanti; Bambu Studio gestisce, ma import in Blender lento
- Storicamente seam di proiezione e cuciture sui retro non visti; v2.0/2.1 hanno migliorato ma non azzerato
- "Free trial" limitato; uso intensivo richiede crediti a pagamento

## 5. Adatto al nostro caso d'uso?

**Adatto (probabile top scelta tecnica)** per ceramiche italiane. Motivazione:

- Teste di moro, pigne, figurine partenopee vivono di **micro-dettaglio scolpito** (squame, capelli intrecciati, foglie, lineamenti) — esattamente ciò per cui i 1536³ Pro sono pensati
- Texture/PBR irrilevanti per FDM mono-colore → **paghiamo solo per ciò che ci serve: geometria**
- **Delight slider a 1** rimuove l'ombreggiatura dipinta dalle foto di ceramica reale, evitando che finti chiaroscuri diventino rilievi falsi nella mesh — **vantaggio specifico vs Tripo/Hunyuan**
- Limite: mesh "triangle soup" andrà ripulita in Blender (decimate + remesh) prima della stampa, ma è gestibile con il KB Blender già esistente

**Caveat workflow**: se MakerWorld non integra Hi3D, il workflow è due-step (Hi3D web → download STL → Bambu Studio) invece che un solo step in MakerLab.

## 6. Tempo di generazione (MakerWorld)

**~7 minuti** (confermato da UI MakerWorld, maggio 2026 — etichettato "NEW"). Il più lento tra i 5. Sceglierlo solo quando la qualità conta più della velocità di iterazione. Non adatto per test rapidi.

## 7. Settings/parametri MakerWorld

⚠️ **Confermato da test reale (2026-05-08)**: nell'UI MakerLab si seleziona **SOLO l'engine** (Hitem3D 2.1). Non esistono controlli per tier risoluzione, Geometry Type, Delight, face count o mesh repair nell'interfaccia MakerLab.

I parametri avanzati (Delight slider, 1536³ Pro, View-Aligned/Canonical Pose) sono disponibili **solo sulla web app diretta** `hitem3d.ai`, non su MakerLab. Se questi parametri sono critici per il tuo soggetto, usa la web app Hi3D direttamente e importa lo STL in Bambu Studio a mano.

- MakerLab: seleziona **Hitem3D 2.1**
- Web app diretta: tier risoluzione, Delight 0-1 (metti 0.7-1.0 per ceramica), View-Aligned vs Canonical Pose, face count, mesh repair, multi-view

## 7. Fonti

- https://www.hitem3d.ai/blog/Hi3D-v2-1-is-Live-Faster-More-Stable-More-Controllable/
- https://www.hitem3d.ai/blog/en-Hi3D-Updates/
- https://www.hitem3d.ai/3dprinting/use-case
- https://www.hitem3d.ai/blog/en-From-Image-to-Physical-Object-A-Complete-AI-to-3D-Printing-Workflow-Guide/
- https://www.hitem3d.ai/blog/Introducing-Hitem3D-2-0/
- https://trellis2.app/blog/best-ai-3d-model-generator
- https://www.3daistudio.com/3d-generator-ai-comparison-alternatives-guide/hitem3d-alternative
- https://www.fabbaloo.com/news/hitem3d-releases-version-2-0-with-integrated-texture-generation-for-higher-fidelity-3d-models
- https://www.meshy.ai/blog/best-ai-tools-for-3d-printing
- https://3dprintingindustry.com/news/bambu-lab-launches-new-ai-3d-model-generator-233736/
