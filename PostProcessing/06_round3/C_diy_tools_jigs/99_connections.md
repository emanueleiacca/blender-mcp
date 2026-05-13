# 99 — Connessioni con KB R1+R2

> Mappa esplicita: per ogni tool DIY R3-C, quale step R2-E/D/A/B viene
> abilitato, ottimizzato, sostituito.

---

## 99.1 Mappa rapida (tabellone)

| Tool DIY R3-C | Sostituisce/Abilita | File R2 origine | €/Saving | KPI impatto |
|---|---|---|---|---|
| Spray booth cartone €10 (`01_*`) | sostituisce booth Aliexpress €70 (R2-E #11) | `05_round2/E_diy_budget/04_setup_tools_under_100eur.md` §4.5 | -€60 | abilita spruzzo in spazi marginali |
| Drying rack DIY €5 (`02_*`) | abilita "cura parallela O(N)→O(1)" (R2-D trick #1) | `05_round2/D_pipeline_industrial/` (vedi INDEX §3 trick batch) | -€75 vs Tamiya €80 | -40% tempo morto su batch 50 |
| Light box cartone €5 (`03_*`) | sostituisce PULUZ €40 (R2-E #11) | `05_round2/E_diy_budget/04_setup_tools_under_100eur.md` §4.5 | -€35 | foto Etsy 7/10 vs 8.5/10 |
| Heat-set jig PETG €0.15 (`04_*`) | implementa R2-D §3.4 (jig allineamento) | `05_round2/D_pipeline_industrial/01_heat_set_inserts_protocol.md` §3.4 | -€20 vs Ruthex jig | failure rate 20→3-5% |
| Saldatore Yihua moddato €25 (`05_*`) | sostituisce Hakko €120 (R2-D §3.2) | `05_round2/D_pipeline_industrial/01_heat_set_inserts_protocol.md` §3.2 | -€95 | uguale qualità su batch <500/anno |
| Cappa cucina recuperata €15 (`06_*`) | upgrade R2-E (oltre booth cartone) | `05_round2/E_diy_budget/04_setup_tools_under_100eur.md` §4.7 | -€100 vs cabina pro | abilita 2K saltuario (R2-A) |
| Stencil DIY vinile Lidl €5 (`07_*`) | sostituisce Tamiya masking €15/foglio | (workflow R2-E pittura) | -€10 / batch | abilita branding loghi commerciali |
| Polishing wheel Dremel €20 (`08_*`) | upgrade R2-E "polish dentifricio" da step manuale | `05_round2/E_diy_budget/` (R2-E trick #3) | -€0 (replace tempo manuale 20→3 min/pezzo) | finish mirror 8/10 da 5/10 |
| Hygrometer €5 (`09_*`) | preventiva failure mode primer/clear (R2-E) | `05_round2/E_diy_budget/04_setup_tools_under_100eur.md` (PPE/clima) | n/a | -50% scarti per blooming/runs |
| Storage organizer DIY (`10_*`) | implementa R2-D LEAN 5S | `05_round2/D_pipeline_industrial/` (INDEX §3 trick batch) | -€100 (vs Gridfinity bought) | -30% tempo setup-per-task |
| Photo turntable lazy susan €5 (`11_*`) | sostituisce turntable €25 (R2-D foto) | INDEX §"foto prodotto + listing" | -€20 | abilita 360° reel = +20-40% conversion |
| STL templates (`12_*`) | abilita stampabilità jig/organizer su Bambu A1 | trasversale | n/a (filamento gratis) | enabler tutta R3-C |

---

## 99.2 Setup completo "totalmente DIY" sotto €40

Lista minima per replicare il setup R2-E €92 con tool autocostruiti:

| # | Tool R3-C | Costo € |
|---|---|---|
| 1 | Spray booth cartone + ventola PC | 8 |
| 2 | Drying rack filo+skewer | 5 |
| 3 | Light box cartone + lampada esistente | 3 |
| 4 | Heat-set jig stampato (PETG già in casa) | 0.15 |
| 5 | Yihua 936A clone + punta M3 | 25 |
| 6 | Hygrometer digitale | 4 |
| 7 | Lazy susan IKEA (turntable) | 5 |
| **TOTALE** | | **€50** |

Eliminando il saldatore (se hai già 60W generico R2-E #10):
**€25 totali**.

Se sostituisci anche il saldatore con uno €15 esistente:
**€20 totali**.

**Saving vs R2-E €92**: -€42 ≈ -45%.
**Saving vs R2-C Italia-only €198**: -€158 ≈ -80%.

---

## 99.3 Top 3 connessioni con R2 (cambia metrica)

### 1. Heat-set jig PETG → elimina ~17% scarto del protocollo R2-D

R2-D §3.4 dichiara "failure rate inserto storto >5° = 15-20% senza jig".
Su batch tipico 100 pezzi × 2 inserti = 200 operazioni → **30-40
operazioni difettose** → rilavorazione 15-20 min ciascuna = **+5-7 h
labor** + scarti pezzi non recuperabili.

Con jig DIY (stampa una tantum 30 min PETG €0.15):
- failure rate → 3-5%
- 6-10 operazioni difettose vs 30-40
- **risparmio 4-6 h labor + 80% rilavorazione**

ROI jig: paga in **1 batch di 50 pezzi**.

### 2. Drying rack DIY → abilita batch parallel di R2-D

R2-D trick #1: "cura parallela su rack verticale, tempi morti O(N)→O(1)".
Senza rack fisico, il principio è teorico. Con rack DIY filo+skewer
(€5, 30 min build):
- 50 pezzi simultanei in spazio 60×40 cm
- 1 ciclo primer mattino + 1 colore pomeriggio + 1 sealer notte
- **throughput 3× rispetto a tavolo piano**

Su 1000 pezzi/anno target piccolo brand: **risparmio ~150 ore lavoro
diretto** = €1500 valore.

### 3. Setup foto DIY <€10 → cattura il "ROI marginale più alto" di R2-D

INDEX evidenzia: "fase con ROI marginale più alto = foto prodotto
+ listing, investimento 4h + €150 ripaga in 10 pezzi".

R3-C versione DIY:
- Light box cartone €5 (`03_*`)
- Lazy susan turntable €5 (`11_*`)
- Smartphone + tripod libri €0
- Hygrometer €4 (no, qui non serve)

**Setup foto DIY totale: €10** (vs €150 R2-E).
**Stesso ROI break-even = 10 pezzi**, ma **15× meno capitale** = barrier
to entry sparito per maker che parte con €30 in tasca.

---

## 99.4 Cross-link a R2-A (two-tier strategy 2K)

Il setup R2-A SprayMax 2K richiede **PPE serio + ventilazione adeguata**.
Il tool R3-C che lo abilita: **cappa cucina recuperata €15
(`06_extraction_hood_diy.md`)** + maschera ABEK1 €15 (R2-E #13) +
guanti nitrile (R2-E #14).

**Senza** la cappa cucina recuperata (e con solo booth cartone), il 2K
**non è praticabile** in sicurezza al chiuso. Il file R3-C §06 sblocca
quindi la tier-above R2-A per maker DIY budget.

---

## 99.5 Cross-link a R2-B (filamenti shortcut)

Il `08_polishing_wheel_dremel.md` rende competitivo il **PLA Matte
"biscuit nudo" R2-B**: dopo polish con compound + Dremel, anche un PLA
basic standard può ottenere finish 7/10 senza pagare PLA Matte premium
(€40/kg vs €15/kg basic).

Saving filamento per pezzo medio 50 g: **€1.25** = ripaga Dremel €20 in
**16 pezzi**.

---

## 99.6 Cross-link a R2-F (Cina bulk)

Tutti i tool R3-C hanno componenti acquistabili Cina (`F_china_bulk/`):
- Ventole PC 120 mm: Aliexpress €3-5 (vs €8-12 IT)
- Filtri G3/G4: Aliexpress €1/m² (vs €3-5 IT)
- Punte heat-set: Aliexpress €1 cad (vs €12 Ruthex EU)
- Yihua 936A: Aliexpress €20 (vs €60 Amazon IT)
- Hygrometer: Aliexpress €3 (vs €8 Amazon IT)
- Vinile adesivo: Aliexpress €3 / 5m (vs €5 / 2m Lidl)

**Saving totale R3-C → tutto Cina**: setup DIY scende da **€50 a €30**.

Vedi `05_round2/F_china_bulk/10_master_china_shopping_list.md` per
strategia ordini consolidati.

---

## 99.7 Workflow finale integrato (R1+R2+R3)

```
   STAMPA Bambu A1 (PLA basic, €15/kg)
   │
   ▼
   POST: sgrasso IPA (R1) → filler PVA+talco (R2-E) → sand 320/600 (R2-E)
   │   in: zona 2 sanding workshop (R3-C-10 layout 5S)
   │   tool: carta vetrata Brico €10 (R2-E)
   ▼
   HEAT-SET INSERTS (R2-D protocol)
   │   in: zona 6 assembly
   │   tool: Yihua 936A €25 + punta M3 €1 (R3-C-05)
   │         JIG STAMPATO PETG €0.15 (R3-C-04) ←★ riduce scarto 20%→3%
   ▼
   PRIMER MaxMeyer (R1 + R2-E)
   │   in: zona 4 painting
   │   tool: spray booth cartone €10 (R3-C-01) OR cappa €15 (R3-C-06)
   │         hygrometer €4 (R3-C-09) checked T 20-25, RH <60%
   ▼
   SAND 800 wet + ACRILICO airbrush (R2-E)
   │   in: zona 4 painting
   │   tool: airbrush €30 + compressore €60 (R2-E #8-9)
   ▼
   CURA + WASH + DRYBRUSH (R1)
   │   in: zona 5 cure/drying
   │   tool: DRYING RACK DIY €5 (R3-C-02) ←★ 50 pezzi parallel
   ▼
   PLEDGE CLEAR COAT (R2-E)
   │   in: zona 4
   │
   ▼
   POLISH Dremel + dentifricio (R3-C-08) ←★ finish 8/10 da 5/10
   │
   ▼
   FOTO + LISTING (R2-D ROI marginale)
   │   in: zona 7 photo
   │   tool: light box DIY €5 (R3-C-03) + turntable lazy susan €5 (R3-C-11)
   ▼
   PACKAGING + SHIP (R2-F)
       in: zona 8 shipping
       tool: scatole Amazon recuperate (R3-C-10) + label NIIMBOT €25 (R3-C-10)
```

**Star (★) = tool DIY R3-C che cambiano la metrica**, non solo
sostituiscono un prodotto acquistato.

---

## 99.8 Limiti consapevoli del setup totalmente DIY

| Tool | Quando upgradare a versione acquistata |
|---|---|
| Spray booth cartone | >50 spruzzi/mese → cappa recuperata o cabina pro |
| Drying rack filo | >100 pezzi/lotto → pegboard SKÅDIS o sistema modulare |
| Light box cartone | >100 ordini/mese Etsy → PULUZ + LED panel |
| Heat-set jig PLA | >50 sessioni → PETG dedicato, poi ABS/PA |
| Yihua 936A | >500 inserti/anno → Hakko/Pinecil |
| Cappa recuperata | uso 2K >30 min/settimana → cabina certificata |
| Polishing Dremel clone | >100 pezzi/mese polish → Dremel Bosch originale |
| Hygrometer base €5 | climatizzazione automatica → centralina + deumidificatore |
| Turntable manuale | video 360° quotidiani → motorizzato Arduino o pro |

**Regola**: ogni tool ha una **soglia di volume** oltre cui il
risparmio €/pezzo è eroso dal tempo perso o dalla scarsa affidabilità.
La regola pollice: se un tool fallisce 2 volte in 1 settimana,
upgradalo.
