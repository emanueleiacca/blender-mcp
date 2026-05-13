# Tripo 3.1

## 1. Cos'è e quando usarlo

Tripo 3.1 è il modello image-to-3D di punta di Tripo AI, motore di base anche di MakerWorld. Sweet spot: **soggetti scultorei con dettaglio ornamentale fine** generati in ~10 s da singola immagine, con resa nettamente superiore a v2.5/v3.0 su volti, panneggi e pattern superficiali. Scelta default quando il dettaglio supera la pulizia topologica.

## 2. Capacità tecniche

- **Topology**: triangle soup di default (triangoli "sporchi", vertici fusi, facce sovrapposte segnalati dalla community); opzionale **quad remesh** e **smart low-poly** lato MakerLab/Tripo Studio
- **Polycount**: standard ~100-300k tri; HD/Ultra fino a **500k poly** in MakerWorld, fino a 2M in Tripo Studio Ultra
- **Risoluzione dettagli**: alta — cattura "embedded text, micro-patterns, surface engravings"; community conferma resa di volti e capelli stilizzati
- **Format export**: GLB, OBJ, FBX nativi; **STL e 3MF** disponibili da MakerWorld direttamente
- **Multi-view**: sì, variante **Tripo 3.1 Multi View** ("H3.1") — accetta 2-4 immagini ordinate front/left/back/right (front obbligatoria)

## 3. Input ideale

- **Sfondo**: tinta unita ad alto contrasto col soggetto (bianco, nero o grigio neutro). Sfondi rimossi danno bordi più precisi
- **Angolazione**: 3/4 frontale leggermente dall'alto per single-image; per Multi View le quattro viste ortogonali. Evitare prospettive forti
- **Illuminazione**: diffusa e uniforme, niente ombre dure né specular blow-out (interpretati come geometria). Su multi-view mantenere temperatura/luce coerenti
- **Risoluzione**: ≥ **2048×2048**, max 10 MB; PNG preferito, JPG/WebP accettati
- **Cosa rovina i risultati**: superfici riflettenti/lucide (smalti ceramici!), trasparenze, ombre proiettate sul piano d'appoggio (basi spurie), prospettiva grandangolare, soggetti tagliati dal frame

## 4. Limiti noti

- Topologia "messy" — richiede retopo/cleanup; ~1 generazione su 10 client-ready as-is
- Dettagli **piccoli e ripetitivi** (squame, intrecci) talvolta "ammorbiditi" o fusi a profondità insufficiente
- **Simmetria assiale non garantita** in single-image — Multi View risolve
- Ombre nel piatto della foto generano **basi piatte spurie** o piedistalli incollati
- Output occasionalmente non-watertight: serve check non-manifold prima dello slicing
- ⚠️ **Soggetti con apertura/cavità** (vasi aperti, ciotole, contenitori): il tool vede l'interno dall'immagine 3/4 e può interpretare il soggetto come "una massa di elementi" invece di "un contenitore con rilievi". Risultato: mesh informe, fondo bucato, struttura del contenitore assente. **Confermato empiricamente su vaso limoni (2026-05-08)** — vedi `decision_tree.md` §Soggetti con apertura.

## 5. Adatto al nostro caso d'uso?

**Adatto** — la scelta primaria tra i 5 tool. Resa scultorea + capacità su ornamenti fini + 500k poly + export STL/3MF diretto da MakerWorld lo rendono il candidato ideale per teste di moro, pigne e ceramiche partenopee. Prezzo: triangle soup richiede sempre passaggio Blender (decimate/remesh, fix non-manifold, riallineamento Z, taglio base) prima dello slicing. Per FDM mono-colore i difetti texture sono ininfluenti.

## 6. Tempo di generazione (MakerWorld)

**~2.5 minuti** (confermato da UI MakerWorld, maggio 2026). Il più veloce tra i 5 — ideale per iterazioni rapide e test sul soggetto nuovo prima di passare a tool più lenti.

## 7. Settings/parametri MakerWorld

⚠️ **Confermato da test reale (2026-05-08)**: nell'UI MakerLab si seleziona **SOLO l'engine**. Non esistono controlli per geometry quality, topology, face limit, symmetry o polycount. I parametri esposti nelle documentazioni online si riferiscono alle API dirette di Tripo AI, non all'interfaccia MakerLab.

- Seleziona: **Tripo AI 3.1** oppure **Tripo AI 3.1 Multi View** (se disponibile nel dropdown)
- Export STL/3MF: disponibile dopo la generazione

## 8. Note di affidabilità

- Data rilascio v3.1 non confermata da changelog ufficiale leggibile
- "Triangle soup" segnalata da Neural4D (concorrente — possibile bias); pagina ufficiale Tripo rivendica al contrario "cleaner topology"
- Verdetto pratico: assumere triangle soup come baseline, attivare quad remesh in MakerLab solo se il dettaglio non ne soffre

## 8. Fonti

- https://www.tripo3d.ai/blog/introducing-tripo-new-algorithm3
- https://platform.tripo3d.ai/docs/changelog
- https://www.tripo3d.ai/blog/makerworld-with-tripo
- https://www.tripo3d.ai/tutorials/tripo-ai-image-to-3d-tips
- https://www.tripo3d.ai/tutorials/tripo-ai-image-to-3d-problems
- https://www.scenario.com/blog/tripo-31-multi-view-examples-88ebdd2
- https://wavespeed.ai/models/tripo3d/h3.1/multiview-to-3d
- https://blog.neural4d.com/comparisons/tripo-3-1-model-review/
- https://www.smith3d.com/bambu-lab-makerworld-unlock-ai-3d-model-generation-for-everyday-makers/
