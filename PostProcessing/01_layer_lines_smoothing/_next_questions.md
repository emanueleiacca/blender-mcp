# Next Research Questions

Spunti emersi durante questa ricerca che meritano un secondo round mirato.

---

### 1. Esistono test misurati (Ra) di sanding manuale step-by-step su PLA?
Tutti i paper trovati misurano Ra ma testano **chimica, ironing, laser** — nessuno fra quelli consultati documenta numericamente "sand 120 → 220 → 400 → 600 → 800 → 2000" su PLA con Ra a ogni step. Sarebbe utilissimo capire **dove si appiattisce la curva** (legge dei rendimenti decrescenti). Cercare: paper su "manual abrasive finishing FDM PLA Ra"; preprint su arXiv; tesi di laurea (theses.fr, Tesionline).

### 2. XTC-3D vs UV resin + baby powder: confronto Ra documentato?
Su Hackaday e blog si trovano molti aneddoti, ma **nessun confronto numerico controllato** Ra dopo identica preparazione. Vale la pena cercare su YouTube (Stefan/CNC Kitchen, Maker's Muse, "Print Smoothing Test Ra") e su pubblicazioni di shop come MatterHackers che a volte commissionano test.

### 3. Etile acetato vapor smoothing su PLA: ricetta ottimale tempo/temperatura?
Le fonti hobbyste consultate dicono "10-30 min", molto vago. Servono dati su: ppm di vapori in camera, temperatura ottimale, % di humidity, **come evitare "blooming" / opacità**. Cercare: r/3Dprinting con flair "Tutorial", thread RepRap forum, eventuali paper su vapor smoothing PLA con EtOAc.

### 4. PolySmooth/Polysher: economia totale rispetto a sanding+primer manuale?
Polysher costa ~300 €, filamento PolySmooth più caro (~30-40 €/kg vs 18-25 € del PLA Bambu). Vale la pena per pezzi estetici prodotti **regolarmente** (>20 pezzi/anno)? Costo per pezzo, tempo risparmiato, qualità reale rispetto a XTC-3D? Cercare: review long-term (1+ anno) su YouTube, Reddit thread con economics.

### 5. Bambu A1 + Textured PEI plate: il "first layer" textured complica il sanding?
Il Bambu A1 viene venduto con textured PEI. Il "lato build plate" del pezzo ha texture pronunciata. Quanto sanding extra serve per livellarla? Vale la pena passare a smooth PEI o cool plate per pezzi estetici? Cercare: Bambu Lab community + Reddit.

### 6. Filler primer Rust-Oleum: differenze Filler vs Auto Primer vs Sandable Primer Filler?
Rust-Oleum vende **almeno 4 prodotti** con nomi simili (Auto Filler Primer, Sandable Filler Primer, 2X Filler Primer, Wood Filler Primer). Quale ha più "high build" reale su PLA? Cercare: Variance Hammer side-by-side, Tangible Day, eventualmente test fai-da-te.

### 7. Bambu A1: ironing in slicer come step alternativo a sanding sul top?
Bambu Studio supporta ironing. Quanto è efficace su PLA Bambu Basic? Ironing temp/speed ideali? Riduce davvero il sanding al solo "lati" del pezzo? Cercare: paper PMC sopra citato fornisce numeri ma non specifico per Bambu; Reddit r/BambuLab.

### 8. Disagreement: alcuni dicono che dopo XTC-3D si perde adesione delle vernici acriliche
Affermazione ricorrente ma non confermata: la superficie di XTC-3D dopo cure sarebbe "troppo liscia" per primer/vernice acrilica, serve scuffing 400 obbligatorio. Verificare con test reale o paper su adesione su epossidiche cure.

### 9. Effetto della temperatura ambiente / umidità sul filler primer
Diversi thread (Goobertown sopra) accennano a "primer blushing" in giornate umide. Quale soglia % RH? Quale temperatura minima? **[da verificare]** con test misurato.

### 10. CA + baking soda: effetto sul colore della verniciatura finale
La baking soda crea una superficie biancastra/grigia. Dopo carteggiatura e primer, si vede una differenza di colore "spotted" sotto vernici chiare/metallic? Cercare: testimonianze prop maker su pezzi con finitura "candy paint" o gloss bianchi.
