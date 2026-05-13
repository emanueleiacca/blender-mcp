# 02 — Pricing psychology: anchoring, decoy, bundling, scarcity

**Obiettivo**: applicare leve di psicologia dei prezzi documentate (studi accademici + consensus DTC) per ottenere **AOV +30–70%** e **prezzo accettato +15–40%** senza alzare il costo di produzione.

> ⚠️ Tutti gli "uplift" sono **stime ragionate** da letteratura o consensus indie maker. Marcati [stima da verificare] quando non riconducibili a uno studio specifico. La verifica reale è il **lotto pilota A/B** (vedi `08_ab_testing_analytics_diy.md`).

---

## 1. Cost-plus vs perceived-value: dove sta la soglia

Da R2-D `05_pricing_model.md`: cost full burden per pezzo "porcellana 12 cm" ≈ **44 €** (lotto 50). Markup standard handmade:

- 2× = **88 €** (hobby sustainable)
- 2.5× = **110 €** (pro standard)
- 3× = **132 €** (premium handmade)
- 4× = **176 €** (art collectible)

**Bill Doran / Punished Props formula** (consensus indie maker):
> Retail = (Materials + Labor + Overhead) × 2 wholesale, × 3–4 retail.

https://www.youtube.com/watch?v=mzGcvxCt4yY

**Domanda chiave**: dove posizionare? Risposta: **cost-plus dà il pavimento**, le leve sotto ti dicono **quanto sopra il pavimento puoi spingere**.

---

## 2. Anchoring (effetto ancora)

### 2.1 Studio fondante

**Tversky & Kahneman (1974)**, *Judgment under Uncertainty*, Science 185:1124. L'esposizione a un numero arbitrario influenza stime successive del 30–40%.

**Ariely, Loewenstein, Prelec (2003)**, *Coherent Arbitrariness*, Quarterly J. Economics 118(1). Test "ultime 2 cifre SSN" → bid asta varia del 60–120% sui prezzi finali. https://web.mit.edu/ariely/www/MIT/Papers/CoherentArbitrariness.pdf

### 2.2 Applicazione per indie maker

**Tactic catalogo "decoy alto"**: posizionare in cima al catalogo Etsy/Shopify **1 pezzo top a €180–250** (anche se vende 0 unità). Tutti gli altri pezzi €60–120 sembrano "il prezzo ragionevole".

| Posizione catalogo | Prezzo | Vendite attese | Funzione |
|---|---:|---:|---|
| Pezzo "flagship" (edizione 1/5, base noce + COA) | 220 € | 0–1/anno | **Ancora alta** |
| Premium edition | 130 € | 5/anno | Margine alto, vetrina |
| **Standard edition** (target principale) | 75 € | 30/anno | **Volume reale** |
| Mini / desk version | 35 € | 50/anno | Entry-level, traffic |

**Effetto**: senza il flagship a 220 €, i 75 € sembrano "caro per stampa 3D". Con il flagship, sembrano "accessibili".

**Tactic prezzo barrato**: mostrare "€90 ~~€120~~" trigger anchor sul prezzo barrato. Etsy supporta sconti nativi.
- Studio: Anderson & Simester (2003), *Effects of $9 Price Endings*, QME 1(1). Sconti percepiti = +20–50% conversion su prodotti commodity.

### 2.3 Tabella effort/cost/uplift

| Tactic | Effort setup | Costo | Uplift atteso* |
|---|---|---|---|
| Pezzo flagship €200+ | 1× produzione | costo materiali 1 pezzo (~50 €) | +15–30% retail accettato altri SKU |
| Prezzo barrato sconto -25% | 5 min listing | 0 | +20–40% conversion [stima] |
| Catalogo ordinato per prezzo decrescente | 10 min | 0 | +10–15% AOV [stima] |

*Stime da consensus DTC + studi citati. Da verificare con A/B reale.

---

## 3. Charm pricing (€39 vs €40)

### 3.1 Studi accademici

- **Anderson & Simester (2003)**, MIT Sloan, *$9 endings*: vendite +24% testando $34 vs $39 vs $44 su catalogo donne. https://www.mit.edu/~simester/papers.htm
- **Thomas & Morwitz (2005)**, *Penny Wise and Pound Foolish*, J. Consumer Research 32: "left-digit effect" — il cervello processa la prima cifra. €3.99 vs €4.00 = percepito "3 qualcosa" vs "4".
- **Schindler & Kibarian (1996)**, *Increased Consumer Sales Response*, J. Retailing 72(2): test campo, .99 endings = +8% revenue su catalogo apparel.

### 3.2 Quando funziona / non funziona

| Categoria prodotto | Charm pricing efficace? | Endings consigliato |
|---|---|---|
| Mass-market commodity | Sì, forte | .99 (€39.99) |
| Decor mid-range | Sì, moderato | .95 / .99 (€89.95) |
| **Handmade premium / arte** | **No, controproducente** | **Round (€90, €120)** |
| Luxury / collectible | Round o "art price" | €180, €250, $1.200 |

**Consensus indie maker** (r/Etsy thread "psychology pricing"): per handmade sopra 50 €, .99 sembra "tecnologico/discount" e abbassa la perceived value. Sotto 30 € (mini, accessori), .99 può aiutare.

### 3.3 Decisione operativa

Per il tuo brand:
- **Mini decor 15–35 €**: prova €19.99, €24.99, €29.99.
- **Standard 50–130 €**: round numbers (€75, €90, €110, €130).
- **Premium 150+ €**: round (€180, €220, €280).

---

## 4. Decoy effect (effetto esca)

### 4.1 Studio fondante

**Huber, Payne, Puto (1982)**, *Adding Asymmetrically Dominated Alternatives*, J. Consumer Research 9: introdotta un'opzione "esca" che è inferiore a una sola delle due alternative → spinge la scelta verso quella dominante.

**Dan Ariely** (2008), *Predictably Irrational*, cap. 1: replicato con The Economist subscription:
- Online $59 (16%)
- Print $125 (0%)
- **Online + Print $125 (84%)** ← decoy "print only" rende "online+print" affare evidente.

https://www.youtube.com/watch?v=xOhb4LwAaJk (TED talk Ariely)

### 4.2 Applicazione 3-tier handmade

| Versione | Prezzo | Cosa cambia | Funzione |
|---|---:|---|---|
| **Standard** | 60 € | Pezzo nudo + scatola | Entry, attira |
| **Plus** ← target | 80 € | + base noce + thank-you card scritta a mano | **Punto di vendita reale** |
| Premium | 140 € | + COA firmato + edizione numerata + packaging custom | Decoy alto |

**Effetto**: il cliente vede Premium 140 €, valuta cosa contiene Plus 80 €, decide "Plus è ottimo affare" → conversione su Plus +40–70%. **[stima — da verificare A/B]**

### 4.3 Asymmetric dominance: la regola

Decoy efficace = inferiore SOLO a una opzione, paragonabile all'altra. Esempio decoy male formulato (NON funziona):

| Versione | Prezzo | Problema |
|---|---:|---|
| A | 60 € | |
| B | 80 € | Migliore di A su tutto |
| C (decoy mal fatto) | 70 € | Peggiore di A E di B → ignorato, no effetto |

Decoy ben formulato:

| Versione | Prezzo | Contenuto |
|---|---:|---|
| A | 60 € | Decor 12 cm |
| B (target) | 80 € | Decor 12 cm + base |
| C (decoy) | 95 € | Decor 12 cm + base + COA (rapporto qualità/prezzo peggiore di B) → B sembra ottimo |

### 4.4 Etsy listing variants

Etsy permette **variants** nello stesso listing. Usa:
- Variant 1: "Standard – €60"
- Variant 2: **"With wooden base – €80 ⭐ Most popular"** (target)
- Variant 3: "Numbered edition (limited 25) – €140"

Il tag "Most popular" è permesso e funziona come **social proof + decoy navigator**.

---

## 5. Bundling

### 5.1 Studio fondante

- **Adams & Yellen (1976)**, *Commodity Bundling and the Burden of Monopoly*, QJE 90(3): bundling estrae più surplus quando le valutazioni sono **correlate negativamente** tra prodotti.
- **Stremersch & Tellis (2002)**, *Strategic Bundling*, J. Marketing 66(1): mixed bundling (bundle + opzione singola) supera pure bundling.

### 5.2 Tattiche per 3D printed home decor

| Bundle | Composizione | Prezzo bundle | Prezzo singolo equivalente | Sconto apparente | AOV uplift |
|---|---|---:|---:|---|---|
| **Pair** | 2 pezzi coordinati | 130 € | 80 × 2 = 160 € | -19% | **+62%** vs 80 € |
| **Trio set** | 3 pezzi (H 8/12/16 cm) | 180 € | 50+80+110 = 240 € | -25% | **+125%** vs 80 € |
| **Room set** | 3 decor + 1 lampshade | 250 € | 320 € | -22% | **+212%** |
| Gift bundle | 1 pezzo + packaging gift premium + card scritta | 95 € | 80 € + 5 (packaging) | nessuno (premium bundle) | **+19%** |

**Insight**: il bundling per **AOV (Average Order Value) è la leva singola più potente** per piccolo brand Etsy, perché:
- 1 spedizione invece di 2 (margin saving).
- 1 commissione Etsy (~10% una volta).
- Cliente attivato per un solo acquisto, lifetime value più alto.

### 5.3 Mixed bundling (consigliato)

Offrire **sempre** la versione singola **E** il bundle. **Non forzare** il bundle. Il cliente che vuole un pezzo solo ti compra comunque, chi vuole più → upgrading naturale.

---

## 6. Edizioni limitate numerate vs open edition

### 6.1 Effetto scarcity in letteratura

- **Cialdini (1984)**, *Influence*, cap. 7: scarcity → urgenza → desiderabilità.
- **Lynn (1991)**, *Scarcity Effects on Value*, Psychology & Marketing 8: prodotti "limitati" percepiti come +15–25% più desiderabili a parità di altre variabili.

### 6.2 Numerazione fisica (case study)

| Brand | Pratica | Effetto pricing |
|---|---|---|
| **Squidmar Miniatures** | Limited print runs YouTube collabs, 50–100 pezzi numerati a mano | +50–100% vs open edition stesso brand |
| **Sideshow Collectibles** "Premium Format" | Edizione 750 / 1500 / 3000 globale, numero stampato su targhetta | Markup 5× vs Hot Toys "regular" |
| **Prime 1 Studio** | Limited 300–600, signed by designer | Sell-through 60–80% a $2.000–4.000/pezzo |
| **Studio Trousdell** (indie sculptor Etsy) | Edizioni 25 pz numerate, COA firmato | Retail 80–250 €, sell-through ~70% |

### 6.3 Edizioni open vs limited per il tuo caso

| Modello | Pro | Contro | Per chi |
|---|---|---|---|
| Open edition | Stampa on-demand, no rischio | Niente scarcity, prezzo basso | Brand giovane, traffic basso |
| **Limited 25/50** | Scarcity, premium accettato | Devi produrre tutto, magazzino | **Sweet spot piccolo brand commerciale** |
| Limited 5/10 | Massima scarcity | Numeri troppo bassi → vendi 5 pezzi totali | Solo se pezzo top €200+ |

**Tactic operativa**: produrre lotto 25 a numerazione manuale. Markup target 3×. Sell-through 6 mesi target 50–70%. Se >70% prima di 4 mesi → alza prezzo prossima edizione +20%. Se <30% → riposiziona/sconto.

### 6.4 COA (Certificate of Authenticity)

- Carta cotone 300 g stampata Pixartprinting: **~30 €/100 pezzi** (https://www.pixartprinting.it/).
- Numerazione a mano (numeratore stamp Aliexpress €8).
- Firma originale + data.
- Costo unitario: ~0.30 € + 30 sec.
- **Effetto**: +10–20% retail accettato [stima consensus indie maker].

---

## 7. Scarcity FOMO operativa (Etsy/Shopify)

| Tactic | Piattaforma | Setup |
|---|---|---|
| "Only N left" badge | Etsy nativo se quantity ≤ 10 | Imposta quantità reale del lotto |
| Countdown sconto | Shopify (app Hurrify, Klaviyo email) | 48–72 h timed offer |
| "Last 3 pieces of edition 25" | Etsy description manuale | Aggiorna manualmente |
| Email "almost sold out" alla lista | Mailchimp/ConvertKit | Trigger a 80% sell-through |
| Drop calendarizzato (es. ogni primo del mese) | IG stories + email | Crea aspettativa ricorrente |

**Consensus DTC** (Sideshow newsletter pattern): drop programmati funzionano meglio di disponibilità continua per brand "collectible".

---

## 8. Free shipping threshold

- Studio NRF (National Retail Federation) 2023: 75% consumatori USA aggiunge a carrello per raggiungere free shipping. https://nrf.com/research/consumer-view
- Threshold ottimale = **~1.3× AOV medio** (consensus Shopify blog).

Esempio: AOV medio 75 € → free shipping a **€95**. Cliente con singolo pezzo 75 € spesso aggiunge mini-piece 20 € per evitare 8 € spedizione.

---

## 9. Tabella riassuntiva ROI delle leve

| Leva | Effort | Costo monetario | Uplift atteso* | Difficoltà reversibile |
|---|---|---|---|---|
| Anchoring (flagship €200) | Medio (1 produzione) | ~50 € (costo flagship) | +15–30% altri SKU | Bassa |
| Charm pricing (.99 entry) | Basso (5 min) | 0 | +5–15% conversion fascia bassa | Basso |
| Decoy 3-tier | Medio (3 versioni) | 0 incrementale | +30–60% mix-shift verso target | Basso |
| Bundling pair | Basso (1 listing extra) | 0 | +60% AOV su bundle | Basso |
| Edizione limitata 25 numerata | Medio (COA + numerazione) | 0.30 €/pezzo | +20–50% retail | Alto (non reversibile per quel lotto) |
| Scarcity "last N" | Bassissimo | 0 | +10–20% urgenza | Basso |
| Free shipping threshold | Basso | -8 €/ordine break-even | +15–25% AOV | Basso |

*Uplift atteso = **stima ragionata** da letteratura + consensus DTC. Marcati come tali. **[da verificare con A/B reale]**.

---

## 10. Decisione operativa per il tuo brand

Setup raccomandato lancio mese 1:

1. **3 SKU iniziali** uno per "tier": Mini 29 € / Standard 75 € / Premium 130 €.
2. **1 flagship "ancora" 220 €** edizione 5 numerata.
3. **1 bundle pair** a 130 € (vs 75×2 = 150).
4. **Free shipping > 90 €**.
5. **Round pricing** sopra 50 €, charm pricing sotto.
6. **Limited edition 25** sui top 2 SKU.

Target conversione 12 mesi: AOV medio **95–110 €** (vs 75 € senza leve = +30%).

---

## 11. Fonti

- Tversky & Kahneman (1974), *Judgment under Uncertainty*, Science.
- Ariely, Loewenstein, Prelec (2003), *Coherent Arbitrariness*, QJE.
- Anderson & Simester (2003), *Effects of $9 Endings*, QME.
- Thomas & Morwitz (2005), *Penny Wise and Pound Foolish*, JCR.
- Huber, Payne, Puto (1982), *Asymmetrically Dominated Alternatives*, JCR.
- Cialdini, *Influence*, 1984.
- Ariely, *Predictably Irrational*, 2008.
- Bill Doran (Punished Props), "How to Price Your Work": https://www.youtube.com/watch?v=mzGcvxCt4yY
- Shopify Blog, *Bundle Pricing Strategy*: https://www.shopify.com/blog/bundle-pricing
- r/Etsy thread "pricing psychology": https://www.reddit.com/r/Etsy/search/?q=pricing+psychology
- NRF Consumer View: https://nrf.com/research/consumer-view
