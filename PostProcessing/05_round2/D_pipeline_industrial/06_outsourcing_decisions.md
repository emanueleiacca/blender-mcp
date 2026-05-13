# 06 — Quando outsourcing conviene

Domanda chiave: per quale fase del pipeline e a quale volume conviene
**comprare il servizio invece di farlo in casa**?

Framework: outsource quando **cost_outsource < cost_internal_full_burden**
(includendo time-opportunity cost dell'utente).

---

## 1. Fasi candidate all'outsourcing

| Fase | Outsourceable? | Service tipico | Quando |
|---|---|---|---|
| Modellazione CAD | Sì | Freelancer Fiverr/Upwork, modellisti dedicati | Per modelli complessi una tantum |
| Stampa 3D | Sì | JLCPCB, Craftcloud, Hubs, PCBWay, Treatstock | Lotto > 50 pezzi o stampe complesse PA/resin |
| Sanding | No (low-skill, alto labor, basso valore aggiunto in market) | — | Quasi mai praticabile |
| Painting | Sì | Painters Etsy, mini-painters servizio, contract paint shops | Quando pezzo richiede dettagli che richiedono ore |
| Heat-set / assembly | No | — | Quasi sempre in-house, fase rapida |
| Base/plinth | Sì | Falegnami locali, laser cut services, Etsy "custom wood base" | Sempre conveniente sopra 10 pezzi se base non triviale |
| Nameplate inciso | Sì | Trotec, Vistaprint, Etsy laser shops | Sempre conveniente |
| Packaging stampato | Sì | Packhelp, Noissue, Sticker Mule, PrintFul | Sopra 50 unità anno |
| Foto prodotto | Sì (forse) | Fotografi locali, servizi "product photography" online | Quando lo styling diventa il vincolo |
| Fulfillment | Sì | Shipbob, Etsy POD partners | Sopra 100 pezzi/mese o spedizioni internazionali frequenti |

---

## 2. Printing on demand (POD) — analisi

### 2.1 Servizi consigliati 2025

| Service | URL | Note |
|---|---|---|
| **JLCPCB 3D Printing** | https://jlc3dp.com | Cinese, prezzi imbattibili, qualità FDM/SLA buona, lead time 5-10 gg + shipping |
| **Craftcloud** (by All3DP) | https://craftcloud3d.com | Aggregator, confronta prezzi da multiple manifatture EU/US/CN |
| **Hubs** (ex 3D Hubs, ora Protolabs Network) | https://www.hubs.com | Pro/industrial, qualità alta, prezzo alto |
| **PCBWay 3D Printing** | https://www.pcbway.com/rapid-prototyping/3d-printing/ | Simile JLC, alternativa |
| **Treatstock** | https://www.treatstock.com | Marketplace makers EU |
| **Sculpteo** | https://www.sculpteo.com | Francia, qualità premium, prezzo premium |
| **i.materialise** | https://i.materialise.com | Belgio, focus arte/design |

### 2.2 Cost comparison (FDM PLA, 100 g, statuetta)

| Service | Cost stimato/pezzo (FDM PLA 100 g) | Lead time | Note |
|---|---:|---|---|
| JLCPCB | 4-6 € | 7-14 gg | Mai testato qualità su statuette estetiche; controllare sample |
| Craftcloud | 6-10 € | 7-21 gg | Depende dal partner |
| Hubs | 12-18 € | 5-10 gg | Quality assured |
| Sculpteo | 15-25 € | 5-10 gg | Premium |
| **In-house Bambu A1** | **2 € (PLA only)** + 0.30 € energy = **~2.30 €** | 4-5 h + supervision | Stampa propria sempre più economica per FDM puro |

**Conclusione**: per stampa FDM PLA da Bambu A1, **outsourcing non conviene
mai** in puro costo. Conviene solo se:
- Si esaurisce capacità (50+ pezzi a settimana sostenuti).
- Si vuole resin SLA/MJF per finitura super-liscia (diverso processo).
- Si vuole nylon/CF per parti funzionali (diverso materiale).

---

## 3. Painting outsource — analisi

### 3.1 Servizi mini painting

Mini-painters professionali offrono painting su Etsy/IG. Tariffe 2024-2025:

| Category | Costo per pezzo (12 cm decor) |
|---|---:|
| Tabletop standard | 15-30 € |
| Display/showcase quality | 40-80 € |
| Display+ / pro level | 80-200 € |

Search Etsy: "miniature painting service", "commission painting".

### 3.2 Tipping point

Cost interno painting (lotto 10) da `04_batch_processing_strategies.md`:
- Filler + primer + color + gloss + polish: ~24 min/pezzo × 15 €/h = **6 €/pezzo**
  in labor + ~5 € materiali = **~11 €/pezzo full burden**.

Outsource standard: ~20-30 €/pezzo.

**Outsource painting non conviene** per finitura porcellana semplice. Conviene
solo per:
- Pezzi che richiedono **detail painting alto** (volti, occhi, gradient): in
  questi casi il labor interno esplode a 1-2 h/pezzo → 25-30 € labor → outsource
  competitive.
- Quando l'utente vuole **liberare tempo** per CAD/marketing/listing.

---

## 4. Base/plinth outsource — analisi

### 4.1 Servizi

| Service | Costo base 60×60×15 mm noce | Note |
|---|---:|---|
| Falegnameria locale (taglio + finitura olio) | 8-15 € | Quality variable, ottimo per piccoli lotti |
| Laser cut service (Sculpteo, Ponoko, Snijlab.nl) | 5-12 € + setup | Eccellente per multistrato betulla, MDF |
| Etsy "custom wood base" shops | 6-15 € | Search "wood display base custom", quality variable |
| **In-house** (compra blocchetti grezzi, finitura olio) | 4-7 € | Time ~20 min/pezzo |

Tipping point: a 10-30 pezzi/lotto, **outsource al laser cutter** per
multistrato betulla è competitive. Per noce pieno, in-house resta meglio per
1-2 €/pezzo.

### 4.2 Nameplate

| Service | Cost stimato per targhetta 40×15 mm |
|---|---:|
| Trotec / Vistaprint laser engrave alluminio | 3-8 € (MOQ 10-25) |
| Etsy laser shops (search "custom nameplate brass") | 5-12 € |
| **In-house** (richiede laser engraver) | 0.50 € + CAPEX 300-3000 € |

Tipping point: **sempre outsource sotto 200 pezzi/anno**. CAPEX laser non
ripaga.

---

## 5. Packaging outsource — analisi

Da Round 1 `04_sealing_presentation/05_packaging_brand_experience.md` (se
disponibile). Servizi:

| Service | URL | MOQ | Cost/unit |
|---|---|---:|---:|
| Packhelp | https://packhelp.com | 30-100 | 2-8 € (custom box) |
| Noissue | https://noissue.co | 50-100 | 1-5 € (tissue + sticker) |
| Sticker Mule | https://www.stickermule.com | 10-50 | 0.5-2 € (sticker) |
| The Boxery / Uline | varies | 100+ | 0.30-1.50 € (boxes plain) |

Tipping point packaging brandato: **sopra 50 unità/anno** sì, sotto fare con
scatole generiche + sticker custom.

---

## 6. Foto prodotto outsource

### 6.1 Fotografi locali

- Tariffa pro: 100-300 € per sessione (multi-pezzo).
- Output: 6-shot per pezzo, edit, deliverable web-ready.
- Conviene se ≥ 5 pezzi/sessione e produzione regolare.

### 6.2 Servizi online

- **Soona** (https://soona.co) e simili: 39 $/photo + setup. Spedire pezzi.
- **Pulpix** o agenzie locali: ~50 €/foto per pezzo.

### 6.3 Tipping point

Foto in-house in batch costa ~8-10 min/pezzo + 3 min editing = **~13 min/pezzo
× 15 €/h = ~3 €/pezzo**.

Outsource: ~30-50 €/foto.

**Foto outsource non conviene** per il prosumer hobby. Conviene solo per:
- Foto "hero" lifestyle ad alto budget per campagne IG/Etsy front page.
- Quando il setup foto in casa è impossibile (spazio, luce).
- Quando si vuole un look che richiede skill (high-end editorial, food-style).

---

## 7. Decision matrix riassuntiva

| Volume annuale | Outsource? |
|---|---|
| < 20 pezzi/anno | Tutto in-house. Outsource solo nameplate. |
| 20-100 pezzi/anno | Outsource: nameplate, packaging (sopra 50). |
| 100-500 pezzi/anno | + Base/plinth (laser cut), painting per pezzi complessi, foto pro 1 sessione/quarter. |
| 500+ pezzi/anno | + Stampa parziale (overflow), painting da contractor, fulfillment 3PL. |

---

## 8. Red flags outsourcing

1. **Qualità irriproducibile**: il contractor non garantisce QC → il maker
   rischia di vendere lotto sotto-spec.
2. **Lead time imprevedibili**: JLCPCB può variare 7-30 gg → impossibile fare
   "drop release".
3. **Comunicazione asincrona**: contractor estero, time zone → un revisione
   richiede 24-48h.
4. **Lock-in**: contractor che cambia prezzi dopo 1 anno → margini erosi.
5. **Diluizione brand**: outsource del finishing rende il prodotto
   indistinguibile da quello di altri sellers che usano lo stesso contractor.

---

## 9. Quando in-house è una scelta strategica (non solo economica)

- **Brand artigianale**: parte del valore percepito è "fatto a mano". Outsource
  rompe il claim.
- **Iterazione veloce**: nuovi SKU testabili in 24h senza contratti contractor.
- **Skill building**: ogni lotto migliora la finitura interna; outsource non
  cresce competenza.
- **Margine alto**: in-house cap il cost più basso, possibile fare campagne
  "drop" a basso prezzo o promo.

---

## 10. Fonti

- All3DP Craftcloud comparison: https://all3dp.com/1/3d-printing-service/
- JLCPCB 3D Printing FAQ: https://jlc3dp.com/help/topic/3d-printing
- Hubs Manufacturing Trend Report: https://www.hubs.com/get/trends/ (annual)
- Punished Props YouTube: pricing/outsourcing decisions
- "Should you sell your 3D prints" — Maker's Muse:
  https://www.youtube.com/c/MakersMuse
- Reddit r/3Dprinting "outsourcing finishing":
  https://www.reddit.com/r/3Dprinting/search/?q=outsourcing+finishing
- Packhelp blog "MOQ for small makers":
  https://packhelp.com/blog/
