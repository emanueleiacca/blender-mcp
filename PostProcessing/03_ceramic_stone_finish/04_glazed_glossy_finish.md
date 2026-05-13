# 04 — Effetto smaltato lucido (Glazed / Glossy ceramic)

> Obiettivo: superficie tipo **ceramica smaltata**, lucido vetroso, riflesso profondo, percezione "wet". Imita l'effetto della glassa cotta in forno — su PLA si ottiene con **coatings cold-cure**.

---

## 1. La triade glaze
| Approccio | Spessore tipico | Look | Difficoltà | Costo per pezzo |
|-----------|-----------------|------|------------|-----------------|
| **A. Multi-clear-coat spray** | 50-150 µm | Lucido satinato a vetroso | Media | €3-5 |
| **B. Epoxy coat (XTC-3D, generic)** | 200-500 µm | Vetroso, deep glaze | Media-alta | €5-15 |
| **C. UV resin clear coat brushed** | 100-300 µm | Vetroso, high control | Alta | €4-10 |
| **D. 2K automotive clear coat** | 100-200 µm | Premium glass-like | Alta (DPI necessari) | €10-20 |
| **E. Pledge Floor Care** | 20-40 µm | "Wet ceramic" satinato | Bassissima | €0.20 |

---

## 2. Workflow A — Multi clear-coat spray (RECIPE STANDARD)

> Reference workflow per "porcellana smaltata bianca" su PLA.

### Step
1. Eseguire workflow porcellana liscia (file 01) fino al passo white base.
2. **Clear coat #1 gloss**: Tamiya TS-13 Clear o Mr. Hobby B-503 Premium Gloss, 1 mano sottile. Asciuga 1 h.
3. **Wet sand 1500** se ci sono polverine. Solo polverine, non scavare.
4. **Clear coat #2 gloss**: mano più piena, leggermente bagnata (= "wet coat"). 2 h asciugatura.
5. **Clear coat #3 gloss** opzionale, wet coat finale.
6. Cura **72 h** in ambiente senza polvere.
7. **Optional polish**: Tamiya Polishing Compound Fine + microfibra → eleva il riflesso a "specchio".

### Spray clear coats consigliati
| Prodotto | Tipo | Look | Prezzo |
|----------|------|------|--------|
| **Mr. Hobby B-513 Premium Topcoat Gloss** | Lacquer | Top, vetroso | €15/lattina |
| **Tamiya TS-13 Clear** | Lacquer | Classico, lucido pieno | €10 |
| **Vallejo Gloss Varnish 26.517** | Acrylic | Buono, meno aggressivo | €10 |
| **Rust-Oleum 2X Clear Gloss** | Enamel | Economico, buon riflesso | €8 |
| **Montana Varnish Gloss UV** | Acrylic | Sicuro PLA, UV-protect | €13 |

Fonti: [Siraya clear coat 3D prints](https://siraya.tech/blogs/news/clear-coat-for-3d-prints), [3D Printerly polish](https://3dprinterly.com/6-ways-how-to-polish-pla-3d-prints-smooth-shiny-glossy-finish/).

---

## 3. Workflow B — Epoxy coat (XTC-3D & alternative)

> **Smooth-On XTC-3D**: formulato specificamente per 3D printing, **basso exotherm** (PLA-safe). 

- **XTC-3D Coat** ([Smooth-On](https://www.smooth-on.com/products/xtc-3d/)) — 2 component 2:1 ratio, cura 2-3.5 h, self-leveling.
- **Resin Pro 3D-Finish Fast Coating** ([Resin Pro](https://resinpro.co.uk/product/3d-finish-fast-coating-for-3d-prints/)) — 4 h cure, alternativa EU.
- **HTA3D 3D-Smoother** ([HTA3D](https://www.hta3d.com/en/3d-smoother-epoxy-coating-for-3d-prints-similar-to-xtc-3d)) — clone economico EU.
- **Generic 2-part epoxy** (Pebeo Gedeo, Mont Marte, Resinpal): può funzionare ma **rischio surriscaldamento** se mescolato in massa >50 g.

### Step XTC-3D
1. Sand 320 raw print (la grana media è OK, l'epoxy livella).
2. Asciuga, pulisci da polvere (aria compressa).
3. Mix 2:1 by volume A:B. Mescolare 1 minuto in cup small.
4. **Stendere a pennello morbido o cotton tip**. Stendere TUTTO il pezzo entro 10 min (pot life).
5. Self-leveling fa il lavoro: in 30 min trovi una superficie liscia.
6. (Opz.) **Ruotare il pezzo** ogni 5 min per i primi 20 min — evita drip points.
7. Cura 2-3 h primo touch, 24 h cura piena.
8. Sand opzionale 1500-2000 wet + secondo coat per assoluto glass-like.
9. Eventuale color coat dopo (Vallejo aderisce a epoxy curato).

### Pro/contro XTC-3D
- ✓ Riempie layer lines fino a 0.3 mm.
- ✓ Aggiunge resistenza meccanica al pezzo.
- ✓ Self-leveling = niente brushstrokes.
- ✗ Costoso: kit 644 g ~€45.
- ✗ Pot life corto: pezzi grandi richiedono mix multipli.
- ✗ Esotermico: NO masse >50 g di mix in una volta su PLA.

Fonti: [MatterHackers XTC-3D guide](https://www.matterhackers.com/articles/how-to-smooth-and-finish-3d-prints-with-xtc-3d), [Smooth-On product info](https://www.smooth-on.com/product-line/xtc-3d/), [Xometry XTC-3D guide](https://www.xometry.com/resources/3d-printing/xtc-3d/).

---

## 4. Workflow C — UV resin clear coat

> UV resin cura **freddo** (LED 405 nm) e in **30-60 sec** = ZERO rischio termico su PLA.

### Prodotti
- **Anycubic Clear UV Resin** — €25/1kg, classico
- **Siraya Tech Tenacious Clear** — più resistente
- **Bondic / Lazerbond** — UV glue, pratico per ritocchi locali

### Step
1. Sand 600 raw.
2. Pennellare UV resin sottile, evitando bolle (pennello "trascinato" lungo la layer line).
3. **UV LED 405 nm 30-60 sec** (lampada manicure, €15).
4. Sand 1000 wet (la superficie è dura ma sandabile).
5. Secondo coat se servono ulteriori riempimenti.
6. Coat finale sottile **non sandato** → si auto-livella vetroso.

### Pro/contro
- ✓ Velocissimo (cura UV in secondi).
- ✓ Zero calore.
- ✓ Resistenza e durezza eccellenti.
- ✗ Pennellate visibili se non lavori con calma — l'UV cura prima del self-leveling.
- ✗ Resina non curata = irritante; usare guanti nitrile.

Reference: [Hackaday UV resin smoothing](https://hackaday.com/2018/03/08/3d-printering-print-smoothing-tests-with-uv-resin/).

---

## 5. Workflow D — 2K clear coat automotive

> Quando vuoi qualità "auto da concorso" sul pezzo PLA.

- **SprayMax 2K Glamour Clear** (aerosol con attivatore integrato) — €25/spray. La lattina ha un pulsante che rompe il setto del catalizzatore: una volta attivata, va usata entro 24-48 h.
- Look risultante: vetroso profondo da concorso, resistenza UV/chimica top.
- Tossico in nebulizzazione: **maschera A2-P3 obbligatoria**, ventilazione forzata.

### Step
1. Workflow porcellana A (file 01) completo fino a clear coat #2.
2. Sand 2000 wet + asciuga.
3. Attivare SprayMax (premere pulsante sotto).
4. 3 mani: la prima light, le due successive medie.
5. Distanza 20 cm, ambiente >18 °C.
6. Asciugatura 24 h indoor.

### Considerazioni
- Vetroso davvero "automotive".
- Costa €25 a lattina = €5-8 per pezzo.
- **Solo per pezzi premium**.

---

## 6. Workflow E — Pledge Floor Care (trick miniaturisti)

> Il segreto dei modellisti scala da 20 anni. Acrylic floor polish che self-leveling restituisce un riflesso "ceramica satinata" eccezionale.

- **Prodotto USA**: Pledge Revive It Floor Gloss (ex Future, ex Floor Care Multi-Surface Finish).
- **Prodotto EU/IT**: cercare "Pledge One Go Multi-Surface Gloss" o equivalenti generic "lucidante pavimenti acrilico autolivellante". Marche italiane: **Bripi Cera lucidante autolucidante**, **Mafra Acrilico Lucido**.

### Step
1. Pezzo dopo porcelain workflow (file 01) — bianco satinato finito.
2. **Una mano pennellata leggera** di Pledge (pennello morbido pulito, no diluizione).
3. Self-leveling 30 min.
4. Asciuga 4-6 h. Mano #2 se vuoi più profondità.
5. Cura overnight.

### Pro/contro
- ✓ Costo: €0.20 per pezzo.
- ✓ Self-leveling perfetto.
- ✓ Reversibile (si toglie con ammoniaca).
- ✓ Compatibile con pittura acrilica sotto.
- ✗ Sensibile all'acqua (non è impermeabile vero).
- ✗ Look "ceramic satin", non "glass". Non è la finitura top per chi vuole specchio vetroso.

Fonti: [Pledge Floor Wax → Pledge Floor Care rename](https://miniaturewargaming.com/blog/future-floor-wax-now-pledge-floor-care/), [paizo.com Future Floor Polish thread](https://paizo.com/threads/rzs2othj), [FineScale Modeler](https://finescale.com/how-to/tips/2018/05/reader-tips-pledge-future-gloss-has-a-new-name).

---

## 7. Color-glazed (ceramica colorata smaltata)

Per "smaltato colorato" (es. ceramica blu cobalto, verde celadon):

1. Porcelain workflow A fino a white base.
2. **Base color**: usare **Vallejo Mecha Color** o **Mr. Color** acrilici in tonalità desiderata (es. C5 Blue + 20% C1 White per cobalto pallido).
3. 2-3 mani sottili.
4. **Gloss clear** sopra come al punto 2 di questo file.

Per finitura **"glazed crackle"** (smaltato con micro-crepe) → vedi file 05.

---

## 8. Confronto sintetico

| Workflow | Look finale | Tempo (active) | Tempo (calendar) | Costo per pezzo | Skill |
|----------|-------------|----------------|------------------|-----------------|-------|
| A. Multi clear spray | Lucido satinato pieno | 20 min | 4-5 giorni | €4 | Base |
| B. XTC-3D | Vetroso, deep | 30 min | 2 giorni | €10 | Medio |
| C. UV resin | Vetroso, controllabile | 25 min | 4 h | €5 | Medio |
| D. 2K SprayMax | Glass auto-grade | 15 min | 2 giorni | €8 | Avanzato (DPI) |
| E. Pledge | Ceramic satin elegante | 5 min | 1 giorno | €0.20 | Trivial |

**Recipe più promettente per "porcellana smaltata bianca"**: workflow A (file 01) + 2 mani Mr. Hobby Premium Topcoat Gloss + finish con polish Tamiya. Compromesso ottimo qualità/sforzo.