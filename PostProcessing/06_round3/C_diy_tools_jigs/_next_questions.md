# Next questions — R3-C DIY tools & jigs

Spunti per round 4 (sperimentale + iterativo).

---

## A. Test misurati su tool DIY

### A1. Performance spray booth cartone — quantificata

- Misurare con anemometro €15 Aliexpress la **portata aria reale** della
  ventola PC 120 mm @ 12V vs valore dichiarato.
- Test **cattura overspray**: spruzzare 10 ml di acrilico, pesare
  filtro carbone before/after, calcolare % cattura.
- A/B tra: scatola Amazon vs bacinella IKEA vs cabina nuda. Misurare
  overspray sulle pareti circostanti dopo 5 sessioni.

### A2. Durata jig heat-set PETG misurata

- Stampare 5 jig PETG identici, usare ognuno per N sessioni heat-set
  M3 fino a fallimento (foro guida non più ø calibrato).
- Confronto con jig PLA (vita stimata 3-5 sessioni) e ABS (vita stimata
  20-30).
- KPI: numero sessioni prima di sostituzione + tolleranza foro
  misurata con calibro 0.05 mm.

### A3. Failure rate heat-set: jig DIY vs mano libera (R2-D §3.4)

- 50 inserti M3 in PLA standard senza jig, 50 con jig stampato.
- Misurare: % inserti angolo >5° (visivo), pull-out con bilancia molla
  €5 Aliexpress, tempo per inserto.
- Validare claim "failure rate 20→3-5%".

---

## B. Workflow integrato

### B1. Time-tracking lotto pilota 50 pezzi con setup DIY €40

- Cronometrare ogni step del workflow R2-E con tutti i tool R3-C.
- Confronto con timeline teorica R2-D.
- KPI: min/pezzo, € materiali/pezzo, scarto %.
- Output: aggiornare INDEX.md con dati misurati.

### B2. ROI documentato 6 mesi tool DIY

- Setup workshop completo R3-C il giorno X.
- Tracking spesa, ore lavoro, pezzi prodotti, vendite Etsy.
- Calcolare ROI effettivo per ogni tool dopo 100/500/1000 pezzi.

### B3. Reliability lifecycle

- Quale tool DIY fallisce per primo? (ventola PC, motore microonde,
  scatola cartone, jig stampato).
- Documentare MTBF empirico → upgrade order priority.

---

## C. Estensioni DIY non coperte R3

### C1. Compressore airbrush DIY (€10 vs €60-80)

- Recupero compressore frigo dismesso → modificare per airbrush
  (tank + regolatore + water trap).
- Documentato in r/Cosplay broke maker series, ma rischio sicurezza
  (motore frigo non isolato per uso modificato).
- Test: portata in psi/CFM, rumore, sicurezza elettrica.

### C2. Cabina spray con ventola estrattore bagno €15

- Ventola estrattore bagno Brico (200-300 m³/h, IP44, 220V) come
  upgrade economico rispetto a ventola PC 12V.
- Confronto: portata, rumore, costo, installazione.

### C3. Fume extractor portatile per saldatura/heat-set

- Mini fume extractor per evitare di respirare fumi PLA che
  bruciacchia sotto la punta saldatore (anche se a 210°C limitati,
  esposizione cronica VOC noti).
- Build con ventola PC 80mm + filtro carbone piccolo + USB. €5-8.

### C4. Sanding station con aspirazione DIY

- Banco con cassetto aspiratore polveri (riciclo aspirapolvere rotto).
- KPI: cattura polvere PLA fine (PM2.5 da carteggio 1500+ grit).
- Cross-ref con sicurezza polveri R1.

### C5. Forno fai-da-te per cura "warm" PLA (max 50°C)

- Box isolato + lampadina 60W o resistenza ceramica.
- Per cura **rapida** primer/clear coat (riduzione tempi -50%).
- Limiti: Tg PLA 60°C → controllo termostato precision necessaria.
- Vedi anche R2-E §4.7 "forno alimenti ricondizionato".

### C6. Vacuum chamber DIY per degassing resina (cross-effetto PLA)

- Per chi mix resina ricoprente su pezzi PLA (R1 ceramic effect).
- Bombola vetro spessa + pompa vacuum frigo dismesso.
- Sicurezza: implosione possibile, schermo protezione obbligatorio.

---

## D. Documentazione comunità

### D1. Pubblicare STL R3-C su Printables/MakerWorld

- Modelli `04_heat_set_jig`, `02_drying_rack`, `11_photo_turntable`
  parametrici in OpenSCAD → upload con license CC-BY-SA.
- Test community feedback su 3-6 mesi.

### D2. Tutorial video YouTube "setup workshop 3D €40"

- Showcase del workflow R3-C completo in 15-20 min video.
- Beneficio: backlinking SEO per Etsy shop, costruzione brand
  "maker autentico" (cross-ref R3-D storytelling pricing).

### D3. Workshop in fablab/coworking

- Workshop pagato 2-4 h "build your DIY workshop" per altri maker.
- Monetization secondaria sul knowledge stesso.

---

## E. Misurazioni ambientali

### E1. Mapping T/RH garage durante 1 anno

- Hygrometer R3-C-09 con datalogger (Xiaomi MiHome o ESP8266 DIY).
- Identificare finestre/giorni "OK clear coat" vs "OK solo primer".
- Calendario operativo seasonal.

### E2. PM2.5 durante sanding wet vs dry

- Sensor PM2.5 €15 (PMS5003) misurare polveri nel garage durante
  sanding 800/1500/3000.
- KPI: ppm PM2.5, durata necessaria mascherina P2 vs P3.

### E3. VOC monitor durante spruzzo

- Sensor VOC TVOC €15 (CCS811) durante spruzzo primer Maximum,
  acrilico, Pledge.
- Validare efficacia cappa cucina recuperata + filtro carbone DIY.

---

## F. Sicurezza & normative

### F1. Compatibilità setup DIY con assicurazione/normativa IT

- Verifica se workshop home-based con cappa cucina recuperata + 2K
  occasionale è coperto da assicurazione domestica.
- Norme antincendio per stoccaggio bombolette spray al chiuso.

### F2. Disposal scarti R3-C end-of-life

- Filtri carbone saturi: rifiuto pericoloso? Conferimento ecocentro?
- Bombolette decanting: residuo + propellente, normativa.
- PLA scarp triturato: dove conferirlo?

### F3. PPE per setup DIY long-term

- ABEK1 vs ABEK2 cartridge — quando upgradare?
- Esposizione cronica VOC anche con cappa: misurazioni in busta urina
  fenil-acetato? (over-engineering hobby, ma rilevante per pro).

---

## G. Branding & narrative (cross-ref R3-D)

### G1. Storytelling "maker workshop autentico"

- Foto/video del workshop DIY come asset marketing (cf. brand come
  "Patagonia Worn Wear" o "MoonPie").
- A/B test Etsy: listing con "made in DIY workshop Italia" vs listing
  neutro. Conversion delta.

### G2. Aumento prezzi medi grazie a "narrative DIY/sustainable"

- Pricing test (cf. R3-D): pezzo standard €25 vs pezzo "from DIY
  workshop, certified PLA recycled" €40.
- Profitto incrementale vs storytelling effort.

---

## Priorità round 4 suggerite

1. **B1 Time-tracking pilota 50 pezzi** — valida tutti i claim R3-C
   con dati misurati.
2. **A3 Failure rate heat-set** — completa l'R2-D §3.4 con N=100
   test reali.
3. **A1 Performance spray booth cartone** — quantifica per
   raccomandazione safety (booth cartone OK fino a quale uso?).

Tutti gli altri spunti sono incremental e possono essere round 5+.
