# Rodin Gen 2 (Hyper3D / Deemos)

> **⚠️ Disponibilità su MakerWorld**: Rodin **non risulta tra gli engine selezionabili nativamente** in MakerLab (al momento delle ricerche, MakerLab espone Meshy 6, Hunyuan 3.1, Tripo). Da verificare direttamente sull'interfaccia. Se assente, l'accesso a Rodin richiede **hyper3d.ai** diretto, fal.ai o WaveSpeedAI (fuori dal workflow MakerWorld).

## 1. Cos'è e quando usarlo

Rodin Gen-2 (rilascio agosto 2025, upgrade novembre 2025) è il modello image-to-3D di punta di Deemos/Hyper3D, basato su un'architettura **BANG da 10 miliardi di parametri** con generazione ricorsiva part-based. Sweet spot: **statue, busti, personaggi, ornamenti scolpiti ad alta densità di dettaglio** — considerato attualmente top-tier per qualità geometrica scultorea.

## 2. Capacità tecniche

- **Topology**: output **quad-dominante nativo** (raro tra i tool AI), disponibile in 4k / 8k / 18k / 50k quad. Alternativa raw triangle: 2k / 20k / 250k / **500k tris**
- **Polycount**: massima densità del mercato (fino a 500k tri o 50k quad)
- **Risoluzione dettagli**: dichiarato **4× miglioramento mesh quality vs Gen-1**; recensioni indipendenti lo classificano "undisputed leader in quality" (8.5–9.5/10)
- **Format export**: GLB, USDZ, FBX, OBJ, **STL** (nativo, utile per FDM)
- **Multi-view**: sì, supporto multi-immagine nativo (switch automatico se carichi più foto)
- **Extra**: bake high-poly→low-poly con normal map, T/A pose forzato, "Use Original Alpha" per silhouette pulite

## 3. Input ideale

- **Sfondo**: pulito/uniforme o con alpha trasparente (toggle "Use Original Alpha" lo sfrutta)
- **Angolazione**: 3/4 frontale per soggetto singolo; per multi-view fornisci front + side + back coerenti
- **Illuminazione**: diffusa, neutra, **senza ombre dure proiettate** (interpretate come geometria)
- **Risoluzione**: alta (≥1024px lato lungo), soggetto centrato e ben staccato dallo sfondo
- **Cosa rovina**: occlusioni, riflessi su superfici lucide (ceramiche smaltate fotografate male), prospettive estreme, dettagli ornamentali in zona d'ombra

## 4. Limiti noti

- **Mesh non sempre print-ready**: report indipendenti segnalano che gli STL Rodin richiedono **repair per non-manifold edges** — ottimizzazione orientata al rendering, non alla stampa
- Cavità profonde tendono a essere riempite (es. trigger di armi nei test): possibile **perdita di sottosquadri stretti**
- Non sostituisce un artista per modelli a tolleranze dimensionali strette
- Seam/texture artifacts della Gen-1 dichiarati risolti; geometria pulita ma da ispezionare

## 5. Adatto al nostro caso d'uso?

**Adatto (probabilmente top-tier qualitativo)** — Rodin è progettato proprio per soggetti scolpiti densi (statue, busti, ornamenti), che è esattamente il profilo di teste di moro siciliane, pigne e figurine partenopee. Il quad output a 18k/50k face cattura squame, capelli intrecciati e foglie meglio di Tripo/Hunyuan in benchmark indipendenti.

**Caveat operativi**:
1. **Non in MakerWorld** (probabile) → workflow due-step con piattaforma esterna
2. Mettere in conto un passaggio di **repair non-manifold in Blender** prima di Bambu Studio

## 6. Tempo di generazione (MakerWorld)

**~3 minuti** (confermato da UI MakerWorld, maggio 2026). MakerWorld lo descrive come "Well-balanced in speed and quality" — conferma il suo posizionamento come alternativa rapida a Hi3D per qualità scultorea. Stesso tempo di Hunyuan ma output qualitativo generalmente superiore per soggetti ornamentali.

## 7. Settings/parametri MakerWorld

⚠️ **Confermato da test reale (2026-05-08)**: nell'UI MakerLab si seleziona **SOLO l'engine** (Rodin Gen-2). Non esistono controlli per quality tier, mesh type, T/A pose o Use Original Alpha nell'interfaccia MakerLab.

- MakerLab: seleziona **Rodin Gen-2**
- Export STL disponibile dopo la generazione
- Parametri avanzati disponibili solo su `hyper3d.ai` diretto

## 7. Fonti

- https://developer.hyper3d.ai/api-specification/rodin-generation-gen2
- https://hyper3d.ai/
- https://wavespeed.ai/blog/posts/introducing-hyper3d-rodin-v2-image-to-3d-on-wavespeedai/
- https://help.scenario.com/en/articles/rodin-hyper3d-models-the-essentials/
- https://gaga.art/blog/rodin-gen-2-review/
- https://www.3daistudio.com/blog/best-3d-model-generation-apis-2026
- https://ideate.xyz/blogs/posts/ai-3d-model-comparison-trellis-tripo-meshy-rodin-hunyuan
- https://cyber-fox.net/blog/ai-3d-generators-review-in-2025/
- https://makerworld.com/en/makerlab/imageTo3d
- https://pixeldojo.ai/industry-news/hyper3ds-rodin-gen-2-revolutionizing-3d-model-generation-for-professional-creators
