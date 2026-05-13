# Meshy-6

## 1. Cos'è e quando usarlo

Meshy-6 (rilascio 18 gennaio 2026) è il modello image-to-3D di Meshy, integrato in MakerLab di MakerWorld accanto a Hunyuan 3.1 e Tripo. Sweet spot storico: **asset game-ready** con **quad topology** e PBR puliti, pensati per pipeline real-time. La v6 ha migliorato la **geometria organica** (volti, anatomia) e gli **edge hard-surface**, ma rimane orientata a output con **polycount contenuto e silhouette pulite**, non alla cattura di micro-dettaglio scolpito.

## 2. Capacità tecniche

- **Topology**: scelta esplicita tra `quad` (quad-dominant) e `triangle` (mesh decimata triangolare)
- **Polycount**: parametro `target_polycount` configurabile da **100 a 300.000**, default **30.000**. Esiste anche `model_type: lowpoly` per real-time
- **Remesh**: `should_remesh` (default false su Meshy-6 → mesh nativa già triangolare prima del remesh quad opzionale). Salvabile la versione pre-remesh
- **Symmetry**: `off` / `auto` / `on` ← utilissimo per soggetti assialmente simmetrici (vasi, teste)
- **Risoluzione dettagli**: ottima per silhouette e proporzioni; dettagli ornamentali fini (squame, intrecci) tendono ad ammorbidirsi a polycount default
- **Format export**: GLB, OBJ, FBX, **STL**, USDZ, **3MF**
- **Multi-view**: NON supportato in image-to-3D di v6 (input singola immagine)
- **Pose**: A-pose / T-pose (irrilevante per ceramiche)

## 3. Input ideale

- **Sfondo completamente neutro/bianco**, soggetto isolato — fattore primario di qualità
- **Vista frontale piena**, soggetto centrato, illuminazione diffusa senza ombre dure
- **Risoluzione**: foto nitida, soggetto che riempie il frame; sotto ~1024px degrada
- **Cosa rovina**: sfondi complessi, riflessi/lucidatura forte (tipica delle ceramiche smaltate — Meshy interpreta highlight come geometria), prospettive estreme, ombre proiettate

## 4. Limiti noti

- **Smoothing aggressivo**: geometria ripulita e regolarizzata, perdendo micro-rilievi e linee di texture scolpita
- A `target_polycount` default (30k) i dettagli ornamentali ripetitivi (squame della pigna, capelli intrecciati) appaiono **fusi/morbidi**
- **Quad remesh** ottimo per topologia, ma può "lisciare" ulteriormente bordi taglienti
- Su MakerLab l'export costa **2 crediti per file**
- Output single-mesh, talvolta con elementi sospesi non manifold che richiedono cleanup

## 5. Adatto al nostro caso d'uso?

**Parzialmente adatto.**

**Pro**:
- Simmetria assiale forzabile (perfetta per pigne/vasi)
- Silhouette pulite, base solida per teste di moro stilizzate
- Output STL/3MF diretto

**Contro**:
- Quad topology **inutile per FDM** (slicer triangola comunque)
- Smoothing tipico **impoverisce i dettagli ornamentali scolpiti** che caratterizzano queste ceramiche

**Da preferire SOLO se**:
- Polycount alto (≥150k)
- Remesh **disattivato** (`should_remesh=false`, `topology=triangle`)
- `symmetry=on` su soggetti assiali

⚠️ I parametri fini (target_polycount, topology, symmetry, model_type) **non sono esposti direttamente** nell'UI MakerLab — sono preselezionati dalla pipeline. Per controllo completo serve l'API/web app Meshy diretta.

## 6. Tempo di generazione (MakerWorld)

**~4 minuti** (confermato da UI MakerWorld, maggio 2026). MakerWorld lo descrive come "Sculpting-level 3D modeling" — descrizione più ambiziosa di quanto emerso dalla ricerca esterna. **Da verificare empiricamente** se questa claim si traduce in dettagli ornamentali migliori del previsto.

## 7. Settings/parametri MakerWorld

⚠️ **Confermato da test reale (2026-05-08)**: nell'UI MakerLab si seleziona **SOLO l'engine** (Meshy 6). Non esistono controlli per target_polycount, topology (quad/triangle), symmetry o should_remesh nell'interfaccia MakerLab. Questi parametri esistono solo nelle API Meshy dirette.

- MakerLab: seleziona **Meshy 6**
- Export STL/3MF disponibile dopo la generazione
- I parametri avanzati richiedono la web app/API Meshy diretta

## 7. Fonti

- https://www.meshy.ai/blog/meshy-6-launch
- https://docs.meshy.ai/en/api/image-to-3d
- https://fal.ai/models/fal-ai/meshy/v6/image-to-3d
- https://www.toolworthy.ai/tool/meshy-ai-v6
- https://3dprintingindustry.com/news/meshy-and-makerworld-team-up-to-put-ai-3d-model-generation-in-bambu-lab-users-hands-250281/
- https://www.fabbaloo.com/news/bambu-lab-integrates-meshy-6-into-makerlab-expanding-ai-image-to-3d-capabilities
- https://forum.bambulab.com/t/new-makerlab-tool-image-to-3d-model/76805
- https://3dshoes.com/news/image-to-3d-print-workflow-meshy-makerworld/
