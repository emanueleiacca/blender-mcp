# PostProcessing — Knowledge Base

KB sul post-processing di stampe estetiche in **PLA basic** su **Bambu A1** per
**piccolo brand commerciale** con vincolo budget. Focus: massimizzare margine
unitario aumentando qualità percepita con DIY + sourcing intelligente (IT/EU/Cina bulk).

**Vincoli operativi confermati**:
- PLA basic (no Silk/Marble/Stoneworks premium, no SLA)
- Tg ~60°C → tutto cold-cure, niente forno
- Garage ventilato disponibile → bombolette OK con PPE
- Warehouse disponibile → bulk ordering Cina realistico
- Scale prodotto miste 3–40 cm
- Uso misto: vendita commerciale + personale
- **Metrica primaria**: €/pezzo + tempo/pezzo, **NON** perfezione assoluta

---

## 🎯 La "pipeline coerente" che emerge dai 3 round

Round 1 ha mappato la bibliografia, Round 2 ha cucito il workflow budget, Round 3
ha aggiunto **artigianalità storica + lab DIY + storytelling**. Convergenza
operativa per il **caso edizione limitata premium**:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  PRODOTTO     →  TECNICA          →  TOOL DIY        →  NARRATIVA  →  PREZZO │
├─────────────────────────────────────────────────────────────────────────────┤
│  Statuetta    →  Marmorino vene-  →  Spray booth     →  "Tradizione →  €80   │
│  18cm PLA     →  ziano (R3-B 02)  →  cartone €8      →  veneziana   →  -120  │
│  basic        →  shellac french   →  + drying rack   →  XVI sec."   →  decoy │
│  €1.50 print  →  polish (R3-B 06) →  filo €5         →  (R3-D 01)   →  R3-D  │
│  Bambu A1     →                   →  light box €3    →                       │
│  (batch 25)   →  Costo ricetta:   →  jig heat-set    →  Edizione    →  Lotto │
│               →  €0.30/pezzo      →  PETG €0.15      →  limitata 25 →  =     │
│               →  (R3-B + R2-E)    →  (R3-C totale    →  numerata    →  Batch │
│               →                   →  €25-50)         →  (scarcity   →  prod  │
│               →                   →                  →   reale!)    →  R2-D  │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Insight chiave**: il batch di produzione R2-D (cura parallela 25 pezzi su
drying rack DIY) **coincide** con l'edizione limitata numerata R3-D → la
scarcity non è marketing fake, è il vincolo fisico di produzione.

---

## 🎯 Raccomandazione operativa per livello

### Tier 1 — "Decor anonimo" (€20-40 retail)
**Workflow base "Porcellana economy" R2-E** — €0.42-0.55/pezzo materiali, 50 min:
```
IPA → PVA+talco DIY filler → sand 320/600 → primer MaxMeyer/BricoIO →
sand 800 wet → acrilico Maxi Color → wash tè (opz) → Pledge clear coat
```
- Setup: €25-50 DIY (R3-C) o €92 acquisto (R2-E) o €100 Cina (R2-F)
- Foto: light box cartone €3 + smartphone (R3-C/R3-D)

### Tier 2 — "Heritage line artigianale" (€60-130 retail)
**Workflow R3-B su base R2-E** — sostituire step finale con ricetta storica:
- **Marmo/pietra**: marmorino veneziano DIY (R3-B 02) — stucco Saratoga + carbonato + pigmenti, lucidato a freddo. Profondità ottica indistinguibile da Calacatta a 30cm.
- **Porcellana profondità**: shellac french polish (R3-B 06) — gommalacca scaglie + alcool denaturato. Mirror finish "pianoforte".
- **Ceramica autentica tatto**: kaolin slurry DIY (R2-B 06) — PVA + kaolin farmacia.
- **Biscuit/terracotta**: casein milk paint (R3-B 05) — ricotta + calce + pigmento, €0.51/pezzo.

Costo incrementale rispetto Tier 1: €0.30-0.80/pezzo + 30-60 min lavoro.
Narrative storica (R3-D 01) giustifica uplift +25-50% retail.

### Tier 3 — "Premium commercial" (€140+ retail)
Solo per pezzi con touchpoint cliente / outdoor display:
- 2K SprayMax sigillatura (R2-A) — PPE serio richiesto
- Scagliola italiana intarsiata (R3-B 03) come medaglione decorativo
- Base/plinth dedicata + nameplate inciso (R1 04-03)
- Heat-set inserts protocol (R2-D 01) con jig DIY (R3-C 04)

---

## 💰 Cost stack riassuntivo

| Voce | Tier 1 economy | Tier 2 heritage | Tier 3 premium |
|------|----------------|-----------------|----------------|
| PLA print 100g | €1.50 | €1.50 | €1.50 |
| Materiali post | €0.45 | €0.75-1.20 | €2-4 |
| Tempo umano | 30-50 min | 60-90 min | 2-3 h |
| Imballaggio | €0.55 | €1-2 | €3-5 |
| **Costo lotto 25** | ~€15-20 | ~€30-50 | ~€80-150 |
| **Retail target** | €20-40 | €60-130 | €140+ |
| **Margine lordo %** | 50-70% | 60-75% | 60-70% |

---

## 🔬 Validare scelte con dati propri (R3-A)

Prima di fissare il workflow definitivo, eseguire **protocollo 14 giorni €39
totale**:
- **Cross-hatch tape test** (R3-A 01) — risolve "Maximum BricoIO o MaxMeyer o Plasti-kote?"
- **ΔE smartphone + ColorChecker DIY** (R3-A 02) — risolve "Pledge basta o serve Mr.Super Clear UV Cut?"
- **Water bead angle** (R3-A 03) — verifica se Pledge sigilla davvero (insight non banale: forse equivale a PLA nudo)

BOM totale: lametta €1.50 + Scotch €1.20 + ColorChecker stampato €0.50 + lampada UV-A €18 + igrometro €5 + bilancia €8 + siringa €0.10 = **€39 misurati**.

Template Excel radar precompilato in `06_round3/A_diy_test_lab/07_excel_template_radar.md`.

---

## 🛒 Sourcing tier strategico

| Tier | Quando | Dove | Esempio acquisto |
|------|--------|------|------------------|
| Test (M1) | Validare qualità | Aliexpress IOSS | Kit €100-150 (heat-set + pigmenti + tools) |
| Operativo (M2-4) | Volume crescente | Aliexpress + Brico IT | €350 setup + bulk Brico/Leroy |
| Custom (M5-6) | Brand experience | Alibaba Trade Assurance | Mailer box+sticker logo €1600 |
| Scaling (M8+) | Spesa annua >€3000 | Agente Yansourcing/EasyChina | Fee 5-8% |

**Top 5 ROI Cina** (R2-F): heat-set €20, pigmenti mica €8, compressore+airbrush €90, PLA+ 10kg €100, light tent €100.
**NON Cina**: cloni Vallejo/Citadel/Tamiya, bombolette spray (IATA), PPE certificato.

---

## 📁 Struttura KB

```
PostProcessing/
  INDEX.md                                  # questo file (operational guide)
  01_layer_lines_smoothing/                 # R1 — sanding, filler, smoothing chimico, epoxy
  02_painting_and_primers/                  # R1 — primer/topcoat/tecniche/effetti/errori
  03_ceramic_stone_finish/                  # R1 — 5 effetti + 10 ricette multi-layer
  04_sealing_presentation/                  # R1 — clear coat, UV, base, foto, packaging
  05_round2/
    A_2k_clearcoat/                         # R2 — tier-above, two-tier strategy
    B_shortcuts_filaments/                  # R2 — vase mode+Pledge, kaolin DIY
    C_italia_sourcing/                      # R2 — mappa shop IT/EU
    D_pipeline_industrial/                  # R2 — heat-set, ironing, pricing, batch
    E_diy_budget/                           # ⭐ R2 — workflow core <€1/pezzo
    F_china_bulk/                           # R2 — Alibaba/1688/Aliexpress
  06_round3/
    A_diy_test_lab/                         # ⭐ R3 — protocollo €39 14gg, decisioni con dati
    B_artisan_recipes/                      # ⭐ R3 — marmorino, shellac, scagliola, casein
    C_diy_tools_jigs/                       # R3 — spray booth cartone, drying rack, light box
    D_storytelling_pricing/                 # R3 — narrative, decoy, foto/video DIY <€30
```

Ogni cartella R3: file numerati + `99_connections.md` (cross-link R1/R2 esplicito) + `_sources.md` + `_next_questions.md`.

---

## 🔗 Cross-links chiave tra round (anti-confusione)

| Decisione/scelta | File primario | Connessioni |
|------------------|---------------|-------------|
| "Quale primer compro?" | R2-E `02_brico_lidl_paints.md` | R3-A `01_cross_hatch` (validare con dato proprio) |
| "Quale clear coat?" | R2-E `03_hi_impact_low_cost_tricks.md` (Pledge) | R3-A `02_delta_e` + `03_water_bead` |
| "Effetto marmo realistico" | R1 `03_ceramic.../06_multilayer_recipes.md` #1 | R3-B `02_marmorino_veneziano` (tier sopra) |
| "Effetto porcellana lucida" | R1 ricetta #3 | R3-B `06_shellac_french_polish` (sostituisce step finale) |
| "Effetto biscuit autentico" | R2-B `06_kaolin_slurry_diy.md` | R3-B `01_gesso_bolognese` (livellante sotto) |
| "Spray senza disperdere vapori" | R2-E setup garage | R3-C `01_spray_booth_cardboard` (cattura overspray) |
| "Heat-set inserts allineati" | R2-D `01_heat_set_inserts_protocol.md` | R3-C `04_heat_set_jig_stl` (fail rate 20%→3-5%) |
| "Foto prodotto livello pro" | R2-D timeline + R2-E setup | R3-C `03_light_box_cardboard` + R3-D `03_photo_indie_premium_diy` |
| "Pricing giusto" | R2-D `05_pricing_model.md` cost-plus | R3-D `02_pricing_psychology` decoy + bundling |
| "Narrative brand" | R1 `04_sealing.../05_packaging_brand` | R3-D `01_storytelling_material_narrative` (per ricetta R3-B) |

---

## 🚀 Round 4 — gap operativi prioritari (test, non più ricerca)

I 3 round bibliografici sono saturi. Round 4 = **passare all'esecuzione misurata**:

1. **Lotto pilota 10-25 pezzi marmorino veneziano con cronometro** — validare empiricamente timeline R2-D + costo R3-B + foto R3-D + pricing R3-D in un singolo ciclo. Sostituire stime con misure.
2. **Esecuzione protocollo R3-A 14 giorni** — produrre dati propri su 5 primer + 5 clear coat. Compilare il radar template. Decidere il workflow definitivo.
3. **A/B pricing Etsy reale 4 settimane** su 1 SKU heritage line: €80 / €100 / €120 → conversion rate effettivo.
4. **Test journal primo ordine Aliexpress €100-150** con KPI documentati (tempi, dogana, qualità) → conferma viability tier-stack sourcing.
5. **Verifica legale-fiscale**: regime forfettario IT a €5k/€20k/€50k anno + obblighi GPSR 2024 per import filamento Cina (R3-D 10).

Tutto il resto è già nella KB — il prossimo passo è **eseguire**, non leggere di più.
