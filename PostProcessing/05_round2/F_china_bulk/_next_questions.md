# Next questions — F_china_bulk

Spunti emersi durante la ricerca, per round 3 o approfondimenti dedicati.

---

## A. Approfondimenti per round 3

### A.1 Agente di sourcing specifico — caso studio reale

- Contattare 2-3 agenti (Yansourcing, Easy China, Jing Sourcing) con specifica RFQ per pacchetto multi-categoria del brand (packaging + filamento + tools + pigmenti).
- Confrontare quote effettive vs DIY Alibaba.
- Verificare:
  - Quale fee reale applicano (5%, 8%, 10%, fissa o variabile).
  - Lead time aggiunto vs guadagno prezzo.
  - QC photo report incluso?
  - Possono sdoganare DDP a IT con fattura italiana valida per P.IVA?
  - Quale forwarder usano in Italia (Savino, etc.)?

### A.2 Test reale "Aliexpress small batch" → KPI documentati

Comprare oggi un **primo ordine €100-150** come da `10_master_china_shopping_list.md` sezione B.1 e tenere log dettagliato:
- Data ordine, data tracking attivato, data delivery.
- Costo dichiarato vs effettivo (IVA, handling).
- % scarto su lotto ricevuto.
- Qualità soggettiva 1-10 per ciascun item.
→ Aggiungere come `11_test_order_journal.md` futuro.

### A.3 Filamento: test comparativo eSun vs Sunlu vs Bambu vs Eryone su Bambu A1

- Stessa STL (mini sculpt 5cm con detail medio).
- Stesso profilo Bambu Studio (modificato per ogni brand).
- Misura: deviazione dimensionale (calibro), peso, finitura visiva ortografica (camera + microscopio), tempo stampa, % scarto support residue, costo per pezzo finito.
→ Per round 3 dedicato "best filament for commercial post-processing 2026".

### A.4 Test acrilico waterborne CN — protocollo PLA compatibility

- Comprare 3 acrilici waterborne 1 L diversi (Alibaba RFQ).
- Provini PLA Bambu identici.
- Test: adesione (cross-cut ASTM D3359), copertura (mani), tempo asciugatura, finitura visiva, resistenza graffio.
- Pubblicare risultato come tabella → `12_acrilico_china_test_results.md`.

### A.5 Packaging design + Alibaba RFQ workflow concreto

- Brand già ha logo? Se sì, preparare dieline tecnica (Adobe Illustrator + EPS export).
- Definire 5 fornitori shortlist con criteri specifici Q/P/Q (years experience, sample policy, customer review).
- Documentare lo scambio RFQ standard (template messaggio inglese che lavora bene con CN).
- → Cartella `13_alibaba_packaging_rfq_template/`.

### A.6 Forwarder IT contatti diretti

- Mappare 3-5 forwarder IT che lavorano con piccoli volumi LCL dalla Cina:
  - Savino del Bene (HQ Prato) — branch Genova, Milano.
  - Bertola Logistica (Torino).
  - Spedizionieri minori zona Genova/La Spezia.
- Richiedere preventivi standard per LCL 0.5 m³ / 80 kg da Shenzhen.
- Confrontare vs DHL Express per stessi pesi.

---

## B. Validazione fatti da verificare

1. **Aliexpress IOSS validità 2026**: confermare che il regime sia ancora attivo (era stato proposto un possibile aumento soglia a €350 a livello UE, monitorare).
2. **Dazio coatings 6.5%**: alcuni codici TARIC sono leggermente diversi a fine 2025 / 2026 (rivedere annualmente).
3. **REACH SVHC list aggiornata**: pigmenti banditi → verificare candidate list ECHA dell'anno corrente.
4. **Costi LCL Shenzhen-Genova 2026**: shipping rates si sono normalizzati post-2022 ma fluttuano stagionalmente. Quotare reale.
5. **Trade Assurance**: continua a essere offerto efficacemente nel 2026, ma le dispute resolution policies cambiano. Verificare T&C aggiornati.

---

## C. Connessioni con altre cartelle KB

- `D_pipeline_industrial/05_pricing_model.md` → integrare costi unitari realistici post-bulk Cina.
- `D_pipeline_industrial/04_batch_processing_strategies.md` → l'arrivo di bulk packaging cambia logica batch (deve essere pronta scorta per evadere ordini in 24-48h).
- `C_italia_sourcing/05_heat_set_inserts_packaging.md` → questo file aggiunge alternativa CN credibile da comparare.
- `A_2k_clearcoat/` → 2K aerosol da Cina **non** raccomandato; questa cartella conferma. Restare su SprayMax DE.

---

## D. Idee di prodotti / categorie non coperte qui

- **Resina UV 3D print bulk Cina** (DLP/SLA) — Anycubic, Elegoo, eSun. Se brand passa da FDM a SLA in futuro, ricerca dedicata.
- **Bambu Lab compatible spools rifill** — alternative third-party brand su Aliexpress che funzionano con AMS.
- **Stampaggio injection mold piccolo lotto** (per custom plinth/base in plastica) — Cina è regina, ma scala 100-1000 pcs è il sweet spot.
- **Laser cutting / engraving custom name plate metal/wood** — Alibaba ha fornitori interessanti per piccoli batch nameplate brandizzati su pezzi premium.
- **Vetrinette display / clochette / acrylic boxes custom** per esposizione prodotto fiera o vetrina shop fisico — Alibaba molto competitiva 50+ pcs.

---

## E. Domande all'utente per indirizzare round 3

1. Quale fase di crescita: garage hobby <50 pezzi/anno, micro-brand 50-300/anno, brand 500-2000/anno?
2. Hai già P.IVA / codice EORI? (cambia drasticamente workflow doganale)
3. Volume packaging attuale (quanti pacchi/mese spediti)?
4. Design brand già definito o in evoluzione? (impacta su quando ordinare custom packaging)
5. Budget primo investimento Cina: €100, €500, €2000, €5000?
6. Hai un commercialista per import/export? Disponibile a investire €600-1500/anno se ROI evidente?
7. Velocità o costo: preferisci ordini rapidi Aliexpress IOSS o pazienza per LCL bulk reale?
8. Cosa stai pensando di sviluppare nei prossimi 12 mesi (nuovi prodotti, nuovi mercati)?
