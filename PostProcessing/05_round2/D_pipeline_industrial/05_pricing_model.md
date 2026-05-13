# 05 — Pricing model: cost-plus + perceived value

Obiettivo: definire un metodo replicabile per pricing di prodotto stampato 3D
finitura premium, in modo da non vendere in perdita e da indovinare il
posizionamento sul mercato Etsy / IG / DTC.

> Non si inventano numeri di prezzo finale: il pricing dipende da nicchia,
> brand, geo. Si fornisce il **framework** e si citano **benchmark pubblici**
> verificabili.

---

## 1. Componenti di costo (cost-plus base)

### 1.1 Costi diretti per pezzo

Dalla tabella in `03_end_to_end_timeline.md`, pezzo "porcellana 12 cm":

| Voce | Pezzo singolo | Lotto 10 | Lotto 50 |
|---|---:|---:|---:|
| PLA filamento (100 g × 20 €/kg) | 2.00 | 2.00 | 1.80 (sconto volume) |
| Filler primer + primer fine | 2.10 | 1.80 | 1.50 |
| Color + gloss + polish | 2.40 | 2.00 | 1.70 |
| Heat-set + hardware | 0.30 | 0.30 | 0.25 |
| Base/plinth | 5.00 | 4.50 | 4.00 |
| Packaging (scatola + foam + tissue) | 3.50 | 3.00 | 2.50 |
| Sundries (IPA, masking, sandpaper) | 0.50 | 0.40 | 0.35 |
| **Subtotale materiali** | **15.80** | **14.00** | **12.10** |

### 1.2 Labor

Da `04_batch_processing_strategies.md`:
- Pezzo singolo: ~4 h
- Lotto 10: ~86 min/pezzo
- Lotto 50: ~51 min/pezzo

Tariffa labor da applicare:
- **Hobbysta-prosumer**: 12-18 €/h (tariffa pari a part-time qualificato).
- **Pro full-time**: 25-40 €/h (deve coprire tasse e contributi su tariffa lorda).

Per esempio "prosumer 15 €/h":

| Lotto | Labor/pezzo |
|---|---:|
| Singolo (240 min) | 60 € |
| 10 pz (86 min) | 21.50 € |
| 50 pz (51 min) | 12.75 € |

### 1.3 Overhead

- Energia stampante: ~0.30 €/pezzo (4-5 h × 100 W × 0.30 €/kWh).
- Energia ventilazione + luci: ~0.10 €/pezzo.
- Ammortamento setup CAPEX (1300 € / 200 pezzi previsti anno 1): ~6.50 €/pezzo
  → si normalizza nel tempo a ~1-2 €/pezzo dopo break-even.
- Quota fissa Etsy listing (0.20 $/listing, 4 mesi durata) + 6.5% transaction
  fee + payment processing 3% + 4% Etsy ads (se attivo).

**Approssimazione Etsy commissions su 80 € retail**:
- Listing: trascurabile.
- Transaction: 80 × 6.5% = 5.20
- Payment processing: 80 × 3% + 0.30 = 2.70
- Etsy ads (se opt-in): ~4%
- Total Etsy commission ~10-14% del retail → **~10 €/pezzo a 80 € retail**.

### 1.4 Failure / yield

Da `04_batch_processing_strategies.md`: yield realistico 85%. → moltiplicatore
costo **/0.85 = +18%** per coprire scarti.

### 1.5 Cost totale (full burden)

Lotto 50, esempio:

| Voce | € |
|---|---:|
| Materiali | 12.10 |
| Labor (51 min × 15 €/h) | 12.75 |
| Overhead energia | 0.40 |
| Ammortamento setup | 2.00 |
| Etsy commission @ 80 € retail | 10.00 |
| Spedizione netta (assumendo cliente paga shipping) | 0 |
| Subtotale | **37.25** |
| × yield correction (1.18) | **43.95** |
| **Cost totale per pezzo venduto** | **~44 €** |

### 1.6 Markup minimo

Su 44 € cost full burden:
- **Break-even**: 44 € retail (impossibile vendere senza margine).
- **Markup 2× (hobby sostenibile)**: 88 € retail.
- **Markup 2.5× (pro standard)**: 110 € retail.
- **Markup 3× (handmade premium)**: 132 € retail.

Range realistico **80-130 €** retail per posizionamento "decor premium artigianale".

---

## 2. Pricing per perceived value

Cost-plus dà la **soglia minima** sotto cui non scendere. Sopra, si lavora con
**perceived value**.

### 2.1 Leve di perceived value (additivo)

Da letteratura e case study DTC:

| Leva | Effetto stimato sul retail accettato |
|---|---|
| Brand/storytelling (about, processo) | +15-30% |
| Edizione limitata numerata | +20-50% |
| Base/plinth premium (noce + nameplate inciso) | +30-60% |
| Packaging unboxing (scatola brandata, tissue, COA) | +15-25% |
| Foto prodotto pro (vs smartphone improvvisato) | +20-40% (impatto su conversion, non su prezzo richiesto, ma traduce a +€ effettivo per visit) |
| Signature/COA cartaceo firmato | +10-20% |
| Drop scarcity (release windowed) | +20-50% (Instagram model) |

### 2.2 Tipping point: quando posizionare alto

Sotto **~50 €** retail il cliente Etsy compara con merch generico → guerra di
prezzo. Sopra **~100 €** retail il cliente compara con arte, regali premium,
collectibles → leve di brand contano molto più del costo materiali.

**Sweet spot identificato dai case study (vedi sotto)**: posizionamento
**80-150 €** per pezzo handmade 10-15 cm con storytelling, in Etsy categoria
"3D printed home decor" / "art object" / "collectible figurine".

---

## 3. Benchmark pubblici (case study)

### 3.1 Punished Props Academy (Bill Doran)

Video "How to Price Your Work" — formula esplicita:
**Retail = (Materials + Labor + Overhead) × 2** for wholesale, **×3-4** for retail.
Bill Doran lavora prop replica 30-80 cm a 200-1500 $.
https://www.youtube.com/watch?v=mzGcvxCt4yY (cercare il video aggiornato).

### 3.2 Beneath the Bunker

Maker UK su YouTube, blog post pricing:
- Statuette 15 cm painted: cost ~£15-20, retail £60-90.
- Markup ~3-4×.
- Edizioni limitate 25-50 pz, sell-through ~80%.

https://www.youtube.com/@BeneathTheBunker

### 3.3 Lost in Tech

Tabletop terrain printed + painted:
- Pieces 5-10 cm: 8-20 € retail.
- Bundle 5-10 pezzi: 40-80 €.
- Markup ~2.5-3×.

https://www.youtube.com/@LostInTech

### 3.4 Etsy Top Sellers — categoria "3D printed home decor"

Tool Marmalead / eRank (https://marmalead.com, https://erank.com) permette di
scansionare top sellers per nicchia. Per "3d printed sculpture 12 cm decor"
range 2024:
- Median listing: 25-65 € (basso effort painted).
- Top 10% listing: 80-150 € (premium finishing + branding).
- Premium outliers: 200-500 € (artisti riconosciuti, edizioni limitate).

### 3.5 Etsy success stories pubblicate (caveat: cherry-picked)

- **r/Etsy** thread "How I priced my prints" 2023-2024 (search):
  https://www.reddit.com/r/Etsy/search/?q=3d+printed+pricing
- **Tested.com** episodi su sellers/maker income (Adam Savage interviste).
- **Maker's Muse** "Should you sell your 3D prints" 2022 + update:
  https://www.youtube.com/c/MakersMuse

Take-away ricorrente: **non vendere sotto 3× materiali** mai. La maggior parte
dei maker hobby vende sotto 2× per "fare girare", poi smette dopo 6 mesi per
burnout. Solo chi mantiene markup 3-4× sopravvive.

---

## 4. Pricing tabella riassuntiva per il prodotto utente

Assunzioni: statuetta 12 cm porcellana lucida bianca, base noce, edizione
limitata 25, lotto produzione 25 unità.

| Posizionamento | Retail target | Margine assoluto | Margine % | Probabilità sell-through 6 mesi |
|---|---:|---:|---:|---:|
| Sotto costo (errore comune) | 35 € | -9 € | -25% | 100% (e perdi soldi) |
| Break-even | 44 € | 0 € | 0% | 80% |
| Hobby sustainable | 70 € | 26 € | 37% | 50-70% |
| **Pro markup target** | **100-130 €** | **56-86 €** | **56-66%** | **30-50%** |
| Premium positioning | 180 € | 136 € | 76% | 15-25% |
| Art collectible (signed, COA) | 280 € | 236 € | 84% | 5-15% |

**Raccomandazione**: lanciare a **110 €** retail con edizione 25, foto pro,
packaging brandato. Se sell-through < 30% in 6 mesi, ridurre a 90 €. Se >70%,
alzare a 130-150 € sulla prossima edizione.

---

## 5. Errori di pricing da evitare

1. **Sottocostare il labor** ("è il mio hobby"): il tempo costa anche se non si
   è impiegati. Includere sempre almeno 12 €/h.
2. **Ignorare Etsy fees**: 10-14% del retail sparisce in commissioni.
3. **Pricing sotto compete**: la guerra di prezzo si perde sempre contro il
   maker cinese stampato in massa.
4. **Non includere yield 85%**: 15% degli sforzi è scarto, va in cost.
5. **Dimenticare il setup CAPEX**: stampante, attrezzi vanno ammortizzati.
6. **Spedizione "gratis" senza calcolare**: o si include nel retail o si
   addebita esplicitamente. Buchi neri tipici.
7. **Sconti aggressivi per "lanciare"**: la prima vendita imposta l'aspettativa
   di prezzo. Si lancia alto, si sconta se serve, mai il contrario.

---

## 6. Modello in Excel/Sheet (suggerimento implementativo)

Colonne: SKU, peso (g), tempo print (h), tempo umano (min), num inserti, base
type, complessità finitura (1-5), lotto size.

Output (calcolato): materiali €, labor €, overhead €, yield-corrected cost,
markup 2x / 2.5x / 3x retail, margine % a ogni livello.

Template pubblico simile: "3D printing pricing calculator" — esempi:
- https://www.3dprintingbusiness.directory/pricing-calculator/
- https://obehave.com/3d-printing-cost-calculator/ (focus business)

Adattare con righe per le voci specifiche del workflow porcellana.
