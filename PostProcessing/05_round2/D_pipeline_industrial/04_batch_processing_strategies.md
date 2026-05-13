# 04 — Batch processing strategies (10/50/100 pezzi)

Scalare il pezzo singolo di `03_end_to_end_timeline.md` (~4 h umano) a un lotto.
Obiettivo: portare il tempo umano per pezzo sotto **2 h** a 10 pezzi, sotto
**1 h** a 50 pezzi, sotto **45 min** a 100 pezzi (limite asintotico per pezzo
con finitura porcellana premium senza outsourcing).

---

## 1. Principio: cosa parallelizza e cosa no

| Operazione | Tipo | Note |
|---|---|---|
| Stampa | **Sequenziale per stampante** | Bambu A1 = 1 pezzo alla volta o N piccoli su plate condiviso |
| Cura primer/color/gloss | **Parallela illimitata** (dipende da spazio drying) | Cura 1 h × 10 pezzi = 1 h, non 10 h |
| Sanding | **Sequenziale umano** | Un paio di mani, una superficie alla volta |
| Spray | **Semi-parallela** | Una mano spray copre 3-5 pezzi piccoli in 1 minuto |
| Foto | **Parallela con costruzione setup** | Setup persistente = 30 s/pezzo dopo il primo |
| Packaging | **Sequenziale** | Ma kit pre-assemblato riduce a 3-4 min/pezzo |
| Heat-set insert | **Sequenziale**, ma 10 s/pezzo | Trascurabile |

**Insight #1**: tutte le fasi di **cura** scalano ~gratis (l'unico costo è
spazio drying). Le fasi **labor-bound** scalano via setup ottimizzato.

---

## 2. Strategia per lotto da 10 pezzi (small batch tipico Etsy)

### 2.1 Print

- Bambu A1 plate 256×256 mm. Statuetta 12 cm: footprint ~50×50 mm → **9-12
  pezzi/plate** se la geometria lo consente.
- Tempo print plate completo: ~20-30 h (300-500 g). Print overnight + giorno.
- **Trick**: usare "by object" sequential print solo se i pezzi sono alti e
  rischio collisione testa. Altrimenti "by layer" è più efficiente.

### 2.2 Sanding batch

- Rack stampato 3D con slot per pezzi (PETG). Pezzi in fila, sanding una mano
  alla volta in sequenza.
- Tempo: 10 pezzi × 25 min sanding singolo = 250 min se sequenziale puro.
- **Ottimizzazione "stazione"**: si passa carta 220 su tutti i 10 pezzi in
  fila, poi 400, poi 600. Ridotto **~30-40%** per riduzione context-switch
  carta/strumento → ~160 min totali = 16 min/pezzo.

### 2.3 Spray station

- Cardboard box 60×60 cm come spray booth, lazy susan da cucina come turntable.
- 10 pezzi disposti su pannello cartone, ogni pezzo su tappo bottiglia
  (rotazione facile).
- Filler primer: una passata copre 5 pezzi in 30 s → 2 passate = 60 s totali +
  pre/post = **5 min per applicazione su tutti**.
- 3 mani filler primer × 5 min = 15 min totali (vs 45 min per 10 pezzi singoli).
- Cura: 30 min × 3 cycle = 1h30 (gratis, parallela).
- **Saving netto sanding+filler per lotto 10**: da ~450 min totali (45×10) a
  ~180 min = **-60%**.

### 2.4 Foto + listing

- Setup foto permanente (vedi `03_end_to_end_timeline.md`).
- Template Etsy con campi `[product_name]`, `[edition_number]`, foto sostituite.
- Foto 6-shot: 10 min per pezzo (10 × 6 = 60 shot) → batch 100 min totali =
  **10 min/pezzo**.
- Editing Lightroom: 1 preset applicato a tutti, batch export → **3 min/pezzo**.
- Listing: copy-paste da template + foto upload → **5 min/pezzo**.

### 2.5 Totale 10 pezzi

| Fase | Tempo umano totale | Per pezzo |
|---|---:|---:|
| Slicing + setup | 30 min | 3 min |
| Print supervision | 30 min | 3 min |
| Rimozione + cleanup | 60 min | 6 min |
| Sanding (in batch station) | 160 min | 16 min |
| Filler + sanding intermedio | 80 min | 8 min |
| Primer fine + color + gloss | 60 min (spray batch) | 6 min |
| Polish | 100 min | 10 min |
| Heat-set + base assembly | 100 min | 10 min |
| Foto batch | 100 min | 10 min |
| Editing + listing | 80 min | 8 min |
| Packaging batch | 60 min | 6 min |
| **TOTALE** | **860 min ≈ 14h20** | **~86 min/pezzo** |

**Da 4 h/pezzo singolo a 1h26/pezzo a 10 pezzi → -64%.**

---

## 3. Strategia per lotto da 50 pezzi

A 50 pezzi entrano nuove ottimizzazioni:

### 3.1 Print farm (anche minima)

- 1 Bambu A1: ~24h × 5 batch da 10 = 5 giorni continui.
- 2 Bambu A1: dimezza a 2-3 giorni.
- Outsource printing JLCPCB / Craftcloud per lotto pilota:
  ~3-5 €/pezzo printed only, vedi `06_outsourcing_decisions.md`.

### 3.2 Drying/curing rack verticale

- Costruire scaffale 5 livelli per cura primer/color. 50 pezzi in batch
  contemporaneamente.
- Costo: ~80 € (scaffale Ikea Ivar 80×80×180) + cartone.

### 3.3 Spray booth con extractor

- Cardboard spray booth con ventola PC + filtro carbone, dehumidifier vicino.
- Permette mani spray in sequenza rapida senza aspettare ricircolo aria.

### 3.4 Time stimato lotto 50 pezzi

| Fase | Tempo per pezzo | Totale 50 pz |
|---|---:|---:|
| Setup + slicing | 1 min | 50 min |
| Print supervision | 2 min | 100 min |
| Sanding batch | 12 min | 600 min (10 h) |
| Filler + spray | 5 min | 250 min |
| Primer + color + gloss + polish | 12 min | 600 min |
| Heat-set + base | 7 min | 350 min |
| Foto + listing | 8 min | 400 min |
| Packaging | 4 min | 200 min |
| **TOTALE** | **~51 min/pezzo** | **~42 h** |

**A 50 pezzi: ~51 min/pezzo umano**.

---

## 4. Strategia per lotto da 100 pezzi (limite asintotico hobby)

A 100 pezzi senza outsourcing finishing si tocca un soffitto: il **labor umano
diventa il collo di bottiglia**. Saving marginali:

- Stencil/mascherature riusabili per dettagli.
- Airbrush invece di bombolette per consistency su dettagli.
- Heat-set insert con jig CNC-positioned (non a mano libera).
- Packaging: scatole pre-stampate con brand, custom foam inserts CNC-cut.

A questo punto la decisione è economica:
- Continuare in-house → tempo umano ~45 min/pezzo asintotico.
- Outsource finishing (paint contractor): 8-15 €/pezzo, tempo umano ~10 min/pezzo
  per QC e packaging.

Vedi `06_outsourcing_decisions.md`.

---

## 5. I "3 trick di batch" che salvano > 30%

### Trick 1 — Stazioni dedicate (no context-switching)

Una zona per sanding, una per spray, una per assembly, una per foto. Tool e
materiali sempre nello stesso punto. Saving stimato: **30-40%** sul totale
labor [CONS, principio LEAN manufacturing, vedi 5S].

### Trick 2 — Cura parallela su rack

Tutti i pezzi del lotto curano insieme. La cura è **tempo gratis**: 1 h cura
serve uguale per 1 o 50 pezzi. Sposta tutto il drying time da "lineare nel
numero di pezzi" a "costante". Saving su lotto 50: **da 50 × 1 h = 50 h a 1 h
totale** sui tempi cura primer.

### Trick 3 — Template + preset + jig

- Lightroom preset = -80% tempo editing.
- Etsy template = -75% tempo listing.
- Heat-set jig = -60% tempo per inserto + drop failure rate.
- Stencil mascheratura = -90% tempo dettagli ripetitivi.

Investimento setup iniziale: ~6-10 h. Ripaga in ~20 pezzi.

---

## 6. Failure rate batch e QC

Su lotto 50, attendersi:
- Print failures: 2-5% (1-3 pezzi) → re-print, ~30 min/pezzo cost.
- Finishing failures (run, dust, scratch): 5-10% (3-5 pezzi) → strip & re-finish
  o scarto.
- Heat-set failures: 1-2% (vedi `01_heat_set_inserts_protocol.md`).

**Yield realistico lotto 50: ~85%** = 42-43 pezzi vendibili. Considerare nel
pricing (vedi `05_pricing_model.md`).

QC step formalizzato a fine batch (10 min totali su 50 pz):
- Visual check sotto lampada radente (3000 K e 6500 K, layer lines e color shift).
- Funzionale: heat-set + vite a campione (1 su 10).
- Pesatura per identificare under-printed (sotto 95% peso atteso).

---

## 7. Investimento setup (one-time CAPEX)

| Item | Costo (€) | Ripaga in |
|---|---:|---|
| 2× Bambu A1 (se non già) | 700 | 50 pezzi |
| Spray booth DIY (cardboard + extractor PC + filtro) | 60 | 20 pezzi |
| Drying rack Ikea Ivar | 80 | 30 pezzi |
| Saldatore + punte heat-set | 100 | 50 pezzi |
| Light tent 60 cm + 2 luci LED + ColorChecker | 150 | 30 pezzi |
| Lazy susan + jig PETG sanding | 30 | 20 pezzi |
| Tripod + smartphone holder + remote | 50 | 20 pezzi |
| Lightroom subscription (1 anno) | 120 | sempre |
| **Totale setup** | **~1300 €** | **~100-150 pezzi venduti** |

A 80 €/pezzo retail e ~30 € margine netto: ripaga in 50-60 pezzi (~6 mesi
operatività moderata).
