# 03 — End-to-end timeline: statuetta 12 cm "porcellana lucida bianca"

Caso studio reale: una statuetta decorativa, scala 12 cm altezza, ~100 g
filamento, finitura porcellana lucida bianca, vendita Etsy come pezzo singolo.
Workflow basato sulla "Ricetta 1" dell'INDEX (Round 1: porcellana liscia).

> Tutti i tempi sono **stima ragionata** basata sul Round 1 + esperienza
> documentata da maker (vedi `_sources.md`). Non sono misurati direttamente.
> Sostituire con misure reali quando l'utente farà il primo lotto pilota.

---

## 1. Tabella time/cost dettagliata (1 pezzo)

| # | Fase | Tempo macchina/cura | Tempo umano attivo | Costo materiali (€) |
|---|---|---:|---:|---:|
| 1 | Modellazione/edit CAD (riuso modello esistente) | — | 0–30 min | — |
| 2 | Slicing Bambu Studio + ironing setup | — | 10 min | — |
| 3 | Stampa 0.16 mm, ~100 g PLA, ironing top | 4–5 h | 0 (overnight) | 1.50 |
| 4 | Rimozione pezzo da plate + supporti | — | 10–15 min | — |
| 5 | Pulizia IPA + wash detergente | 10 min asciugatura | 5 min | 0.10 |
| 6 | Sanding 220 → 400 (walls) | — | 25 min | 0.30 |
| 7 | Filler primer x3, sand 400 inter-coat | 30 min × 3 = 1h30 cura | 3 × 15 min = 45 min | 1.50 |
| 8 | Sanding finale 600 → 800 (wet) | — | 20 min | 0.30 |
| 9 | Primer fine Vallejo White | 1 h cura | 10 min | 0.60 |
| 10 | Base color Tamiya TS-26 (2 mani) | 1 h cura tra mani | 10 min | 1.20 |
| 11 | Gloss topcoat Mr. Hobby Premium (2 mani) | 1 h cura tra mani + 24 h full | 10 min | 1.00 |
| 12 | Polish Tamiya Fine Compound | — | 15 min | 0.20 |
| 13 | Heat-set insert (1× M3 base mount) | — | 2 min | 0.15 |
| 14 | Base/plinth (noce 60×60×15) + finitura | — | 20 min (assembly) | 5.00 |
| 15 | Foto prodotto (6 shot listing) | — | 30 min | — |
| 16 | Editing Lightroom + export | — | 15 min | — |
| 17 | Packaging (scatola + pluriball + foam) | — | 10 min | 3.50 |
| 18 | Listing admin + spedizione | — | 15 min | — |
| | **TOTALI** | **~8–9 h cura** | **~4 h umano** | **~15.40 €** |

### 1.1 Tempo "calendario" reale (non sovrapponibile)

Per via dei tempi di cura inter-coat (almeno 1 h tra primer/color/gloss, 24 h
full cure prima del polish):
- **Minimo realistico per 1 pezzo**: 2 giorni (Day 1: print overnight + sanding
  + filler primer 3 mani; Day 2: primer fine + color + gloss + polish + assembly + foto).
- **Comfort realistico**: 3-4 giorni con margini per errori e cura full prima
  del polish.

### 1.2 Cost-out aggregato

- Materiale + consumabili: **~15-17 €**
- Lavoro umano: **~4 h** → se valutato a 15 €/h hobbista: **60 €**; a 25 €/h
  pro: **100 €**.
- Overhead (energia stampante, vernici scaduti, supporti falliti): **~10%** = ~1.50 €.
- **Cost stimato (full burden) ≈ 75-115 €** per pezzo singolo, non scalato.

---

## 2. Identificazione delle fasi ad alto ROI marginale

Dove ridurre 1h muove davvero il costo unitario? Analisi:

| Fase | Tempo (min) | Riducibile a (min) | Saving | ROI per ora investita in ottimizzazione |
|---|---:|---:|---:|---|
| 3. Stampa | 270 | 270 (vincolo fisico) | 0 | Basso — già automatica |
| 6+8. Sanding | 45 | 20 (con ironing + filler aggressivo) | -25 min | **ALTO** |
| 7. Filler primer x3 | 45 attivo | 30 (1-2 mani spesse + air dry batch) | -15 min | Alto |
| 11. Gloss topcoat | 10 | 10 | 0 | Già minimo |
| 15. Foto prodotto | 30 | 5 (setup persistente + smartphone preset) | **-25 min** | **MOLTO ALTO** |
| 16. Editing foto | 15 | 3 (Lightroom preset + batch export) | -12 min | **ALTO** |
| 17. Packaging | 10 | 4 (kit pre-assemblato + pre-cut foam) | -6 min | Medio |
| 18. Admin Etsy | 15 | 3 (template listing + label batch) | **-12 min** | **MOLTO ALTO** |

### Top 3 fasi a ROI marginale più alto (1 h investita → ritorno)

1. **Foto prodotto + editing** (45 min → 8 min ottimizzato). Setup luce
   permanente, ColorChecker, Lightroom preset, smartphone su tripod fisso. Un
   investimento di 4 h una tantum (costruzione "fotostudio garage 50×50 cm")
   ripaga in ~10 pezzi.

2. **Listing admin / spedizione** (15 min → 3 min ottimizzato). Template Etsy
   con campi pre-compilati per ogni SKU, etichette stampate in batch da Pirate
   Ship o Shippo, scatole pre-pesate. Setup 2 h ripaga in ~10 pezzi.

3. **Sanding + filler** combinati (45 min → 20 min). Ironing slicer sui top,
   filler primer "high build" Rust-Oleum 2X applicato spesso 1-2 mani invece di
   3 sottili, sanding 600 in un solo pass invece di 400+600. Riduzione di
   qualità accettabile per finiture gloss (il gloss livella).

**Insight chiave**: la maggior parte dei maker hobby investe ore in CAD e
finishing, e spende **30 minuti** per le foto + listing — che sono **il momento
in cui il cliente decide se comprare**. ROI inverso vs intuizione.

---

## 3. Analisi sensitività su variabili chiave

### 3.1 Variazione tempo print (50 g → 200 g)

| Peso pezzo | Print time | Costo PLA | Sanding time | Costo totale materiali |
|---|---:|---:|---:|---:|
| 50 g | 2h30 | 0.75 € | 25 min | 11 € |
| 100 g | 4h30 | 1.50 € | 45 min | 15 € |
| 200 g | 9h | 3.00 € | 70 min | 22 € |
| 400 g | 18h | 6.00 € | 100 min | 32 € |

Nota: costo materiali cresce sublinearmente con il peso perché vernici/primer
sono ~costi fissi finché il pezzo cape in un'unica passata.

### 3.2 Variazione finitura (semplice vs porcellana premium)

| Finitura | Step | Tempo umano | Materiali | Prezzo Etsy stimato |
|---|---|---:|---:|---|
| Raw print + sanding 400 | 6 | 30 min | 5 € | 18-30 € |
| Painted matte unicolor | 11 | 1h30 | 8 € | 30-55 € |
| **Porcellana lucida (questa)** | 18 | 4 h | 15 € | 60-120 € |
| Multi-color + dettagli premium | 22 | 6 h | 20 € | 100-200 € |

---

## 4. Confronto con il "what most people skip"

Errori comuni che gonfiano il tempo:
- **Cure shortcut**: applicare il color prima del primer dry → bubbles → re-do
  intera verniciatura. Costo: +2 h.
- **Sanding senza filler primer**: sanding diretto del PLA non chiude pori,
  primer si attacca male. Costo: +1 h re-sanding.
- **Foto improvvisate**: foto al cellulare senza setup, listing che non vende
  → costo opportunità.
- **Packaging weak**: 1 pezzo su 20 arriva danneggiato in spedizione, refund +
  spedizione gratis = -50 € per evento.

---

## 5. Confronto con benchmark commerciali (case study)

| Maker | Prodotto | Tempo dichiarato | Prezzo | Source |
|---|---|---|---|---|
| Punished Props Academy (Bill Doran) | Prop replica medio (30 cm) | 20-40 h | 200-500 $ | "How to price your work" YouTube https://www.youtube.com/watch?v=mzGcvxCt4yY |
| Beneath the Bunker | Statuette 15 cm painted | 6-8 h dichiarate | 80-150 $ | YouTube channel |
| Tested (Adam Savage) | One Day Builds | 8-12 h | non vendita | https://www.tested.com |
| Lost in Tech | Tabletop terrain painted | 4-6 h | 40-80 € | YouTube |
| Etsy top sellers "3D printed home decor" (ranking Marmalead 2024) | Decor 10-15 cm | non dichiarato | 25-65 € | https://marmalead.com |

**Take-away**: il pezzo "porcellana premium" 12 cm a ~4h umano è **competitivo
ma non eccezionale**. Per posizionamento profittevole serve ridurre a ~2h
umano (via batch processing — vedi `04_batch_processing_strategies.md`) e
salire a **80-120 €** retail con storytelling (numerazione, base nominata,
packaging brandato — vedi Round 1 file 05_packaging_brand_experience.md).

---

## 6. Pricing rapido per il pezzo singolo (preview di `05_pricing_model.md`)

Cost-plus con burden completo:
- Materiali: 15.40 €
- Labor 4 h × 20 €/h: 80 €
- Overhead 15%: 14 €
- Subtotale costo: **~110 €**
- Markup ×2.5 (handmade premium): **~275 €** retail teorico.

Test con benchmark Etsy reali (12 cm decor lucido): retail max sostenibile
~80-150 €. **Conclusione**: a 1 pezzo singolo non scalato, **margine negativo
o nullo**. Serve batch processing per scendere a < 2 h umano per pezzo, oppure
posizionamento "art/collectible" con numero limitato a 150-250 €.
