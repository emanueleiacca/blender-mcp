# Hunyuan 3D 3.1 (Tencent)

## 1. Cos'è e quando usarlo

Hunyuan 3D 3.1 è il modello image/text-to-3D open-source di Tencent. Pipeline a due stadi: **Hunyuan3D-DiT** (diffusion transformer flow-matching su latente VAE) per la geometria + **Hunyuan3D-Paint** per le texture PBR. Sweet spot: **geometria pulita e watertight** su soggetti scultorei e hard-surface, con topologia "quad-dominant". Storicamente forte su personaggi stilizzati e oggetti simmetrici, meno su volti realistici e dettagli minuti.

## 2. Capacità tecniche

- **Topology**: quad-dominant (uno dei pochi tool a fare quad reali, non triangulated mesh), edge-flow ottimizzato su giunture
- **Polycount**: configurabile **40k - 1.5M tri/poly**, **mesh watertight** (zero buchi, zero non-manifold)
- **Risoluzione dettagli**: alta su forme primarie e superfici lisce, **media su micro-dettagli ornamentali**
- **Export**: GLB, OBJ, **STL**, FBX, USDZ, PLY (STL diretto utile per FDM)
- **Multi-view**: sì, fino a **8 viste** (front, back, left, right + top, bottom, left_front, right_front)
- **Architettura**: Hunyuan3D-ShapeVAE + DiT flow-matching dual/single-stream (ispirato a FLUX); 3.1 evoluzione iterativa della famiglia 2.x con topologia migliorata
- **Tempi**: Rapid 2-3 min, Pro 3-6 min

## 3. Input ideale

- **Sfondo**: bianco/neutro pulito, soggetto nettamente staccato (essenziale per il segmenter interno)
- **Angolazione**: 3/4 frontale è lo standard; per ceramiche assialmente simmetriche **multi-view fortemente consigliato** (front + side + back)
- **Illuminazione**: diffusa, no ombre dure, no controluce — ombre dure ricostruite come geometria
- **Risoluzione**: 1024×1024+, immagini ad alta nitidezza con soggetto centrato
- **Cosa rovina**: sfondi complessi, riflessi speculari forti su ceramica smaltata (bumps spuri), prospettive estreme, foto sfocate

## 4. Limiti noti

- **Volti e mani**: tendenza documentata a deformarli o appiattirli ("warped, out-of-proportion") → **critico per teste di moro**
- **Dettagli fini**: post-processing pesante (probabile discretizzazione voxel a livello VAE) **liscia via micro-dettagli** ripetitivi (squame di pigna, capelli intrecciati, decori a basso rilievo)
- **Stilizzazione**: rispetto a Meshy preserva meglio l'estetica cartoon, ma a costo di "semplificazione" delle texture in rilievo
- **Smoothing eccessivo** su superfici organiche: ottimo per ceramica smaltata uniforme, problematico per dettagli scolpiti

## 5. Adatto al nostro caso d'uso?

**Parzialmente adatto**, esito polarizzato per soggetto:

| Soggetto | Verdetto | Motivo |
|----------|----------|--------|
| Pigne siciliane / vasi semplici | **Adatto** | simmetria assiale + geometria primaria pulita; watertight = zero rework Blender |
| Teste di moro | **Rischioso** | volto stilizzato ma scultoreo cade nella zona di deformazione; capelli/turbante intrecciati saranno smussati |
| Figurine partenopee ornate | **Sconsigliato se i decori sono il focus**; adatto se silhouette > rilievi |

Per FDM mono-colore è un buon match perché butti via le PBR comunque e tieni solo la geometria quad/watertight, che è il suo output migliore.

## 6. Tempo di generazione (MakerWorld)

**~3 minuti** (confermato da UI MakerWorld, maggio 2026). Veloce, stesso ordine di Rodin. Buon punto di partenza se il soggetto è assialmente simmetrico e senza volti.

## 7. Settings/parametri MakerWorld

⚠️ **Confermato da test reale (2026-05-08)**: nell'UI MakerLab si seleziona **SOLO l'engine** (Hunyuan 3D 3.1). Non esistono controlli per Rapid/Pro, polycount, simmetria o rimozione sfondo manuale nell'interfaccia MakerLab.

- MakerLab: seleziona **Hunyuan 3D 3.1**
- Export STL disponibile dopo la generazione
- Multi-view: da verificare se MakerLab espone l'upload di più immagini per Hunyuan

## 7. Fonti

- https://replicate.com/tencent/hunyuan-3d-3.1
- https://www.3daistudio.com/Models/Hunyuan3D-3-1
- https://github.com/Tencent-Hunyuan/Hunyuan3D-2.1
- https://arxiv.org/html/2506.15442v1
- https://arxiv.org/abs/2501.12202
- https://forum.bambulab.com/t/new-makerlab-tool-image-to-3d-model/76805
- https://medium.com/@Glassenberg/head-to-head-ai-image-to-3d-comparison-hunyuan-vs-meshy-vs-f99cb38faa39
- https://ideate.xyz/blogs/posts/ai-3d-model-comparison-trellis-tripo-meshy-rodin-hunyuan
- https://news.aibase.com/news/23640
- https://3druck.com/en/programs/tencent-launches-hunyuan-3d-engine-worldwide-with-ai-tools-for-3d-models-15152065/
