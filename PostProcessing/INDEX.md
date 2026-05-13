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

## 🎯 Raccomandazione operativa (sintesi round 1+2)

### Workflow base "Porcellana economy" — **€0.42-0.55/pezzo materiali, 50 min**
Da `05_round2/E_diy_budget/07_workflow_recommended.md`. Copre **85-90% della
percezione qualità del cliente non-modellista** rispetto al workflow premium €7/pezzo.

```
Sgrasso IPA → PVA+talco filler DIY → sand 320/600 →
Primer MaxMeyer/Maximum BricoIO → sand 800 wet → acrilico Maxi Color →
(opz wash tè + drybrush Giotto) → Pledge clear coat → (opz polish dentifricio)
```

### Setup tool una tantum — **€92 totali** (€198 se solo IT, €100 via Cina)
Da `05_round2/E_diy_budget/04_setup_tools_under_100eur.md` e
`05_round2/F_china_bulk/10_master_china_shopping_list.md`:
- Airbrush 0.3mm + compressore tank 3L Aliexpress: €60-80
- Light tent PULUZ 60cm + LED ring + tripod: €40-50
- Maschera 3M 6200 clone + filtri A1: €15
- Carta vetrata + pennelli + spatole + IPA + guanti: €25 Brico

### Quando salire di tier (two-tier strategy R2-A)
- **Default**: Pledge / Glassex (€0.03/pezzo) o Mr. Super Clear UV Cut (€0.50/pezzo)
- **Solo pezzi >€40 commerciali con touchpoint**: SprayMax 2K (€22-28/bombola, PPE serio)
  Sotto soglia il ROI del 2K non ripaga PPE/complessità/sensibilizzazione cronica.

### Shortcut radicali per geometrie specifiche (R2-B)
| Geometria | Shortcut | €/pezzo | Tempo | Resa |
|-----------|----------|---------|-------|------|
| Vasi/lampshade decor | PLA Silk vase mode + Pledge | €1.60 | 30 min | 7/10 |
| Ciotole biscuit | PLA Matte nudo (no post) | €3.75 | 0 min | 7/10 |
| Ciotole biscuit autentico | Kaolin slurry DIY (PVA+kaolin) | €0.30 | 60 min | 10/10 |
| Stone/granito | ProtoPasta Sandstone nudo* | €10 | 0 min | 8/10 |

*Premium filament — valutare solo se volume giustifica €30+/kg.

### Heat-set inserts protocol (R2-D) — 3 step
1. **CAD**: foro = OD_inserto (M3 Ruthex → 4.0mm), depth × 1.2, chamfer 45°×0.5mm, parete ≥ 2.5× thread.
2. **Heat**: 210°C (mai >230°C), 1-2s preheat, 3-5s pressione perpendicolare, no rotazione.
3. **Jig**: cilindro guida PETG perpendicolare → drop fail rate 3-5×.
Inserts Cina M3 500 pcs €20 vs Ruthex €60-90 (R2-F).

### Fase con ROI marginale più alto: **foto prodotto + listing** (R2-D)
- Da 45min/pezzo → 8min/pezzo con setup permanente
- Light tent + tripod + ColorChecker + Lightroom preset + template Etsy
- Investimento 4h + €150 → ripaga in **10 pezzi**
- Conversion +35-60% Etsy (più impattante di 2h di sanding extra)

### 3 trick "near-free" R2-E
1. **Wash tè nero + goccia detergente piatti** (€0.001/pezzo) = Citadel Agrax Earthshade (€8/24ml)
2. **Pledge/Glassex clear coat a pennello** (€0.03/pezzo) = Mr.Hobby Premium Gloss (€0.50/pezzo) @ 85% resa
3. **Polish dentifricio + carta 2000 wet** (€0.01/pezzo) = Tamiya Polishing Compound

### 3 trick batch-processing R2-D (saving >30%)
1. **Cura parallela su rack verticale**: tutti i pezzi curano insieme, tempi morti O(N)→O(1)
2. **Stazioni LEAN 5S**: zona sanding, spray, assembly, foto — niente context switch
3. **Template + preset + jig**: setup una tantum 6-10h, ripaga in 20 pezzi, taglia 60-80% task ripetitivi

---

## 🛒 Sourcing — strategia di crescita ordini Cina (R2-F)

| Fase | Ordine | Piattaforma | Budget | Obiettivo |
|------|--------|-------------|--------|-----------|
| M1 | Test | Aliexpress IOSS | €100-150 | familiarizzare, validare qualità su prodotti chiave |
| M2 | Espansione | Aliexpress | €350 | airbrush+compressore+filamento |
| M5-6 | Custom | Alibaba Trade Assurance | €1600 | packaging custom 500+, sticker, mailer kraft |
| M8+ | Agente | Yansourcing/EasyChina (fee 5-8%) | spesa annua >€3000 | scaling |

**Top 5 ROI Cina (>50% saving, low risk dogana)**:
1. Heat-set M3 500 pcs (€20 vs €60-90, -65%)
2. Pigmenti mica/pearl 24 colori (€8 vs €50-80, -80%)
3. Compressore AS186 + Fengda BD-130 (€90 vs €280-400, -65%)
4. Sunlu PLA+ 10kg bundle (€100 vs €180-220, -45%)
5. Light tent PULUZ + accessori foto (€100 vs €280-350, -65%)

**NON comprare Cina** (qualità o problemi normativi):
- Cloni Vallejo/Citadel/Tamiya/Mr.Hobby/XTC-3D (qualità inferiore)
- Bombolette spray commerciali (IATA mare obbligatorio, CLP/SDS farlocchi)
- PPE filtri respiratore "certificate" (certificazione EU sospetta)

**Fallback Italia** se non hai tempo Cina (R2-C): starter kit €198 (Saratoga + Tamiya + Mr.Hobby UV Cut + carta + 3M + Vallejo).

---

## 📁 Struttura KB

```
PostProcessing/
  INDEX.md                                  # questo file
  01_layer_lines_smoothing/                 # ROUND 1
  02_painting_and_primers/                  # ROUND 1
  03_ceramic_stone_finish/                  # ROUND 1 — 5 effetti + 10 ricette multi-layer
  04_sealing_presentation/                  # ROUND 1
  05_round2/
    A_2k_clearcoat/                         # tier-above, two-tier strategy
    B_shortcuts_filaments/                  # filamenti speciali + trick consumer
    C_italia_sourcing/                      # mappa shop IT/EU
    D_pipeline_industrial/                  # heat-set + ironing + pricing + batch
    E_diy_budget/                           # ⭐ workflow core <€1/pezzo
    F_china_bulk/                           # Alibaba/1688/Aliexpress
```

Ogni cartella: file numerati + `_sources.md` (URL) + `_next_questions.md` (spunti).

---

## 🔬 Round 3 — gap di conoscenza prioritari (test concreti)

Pattern cross-agent emersi come gap rispetto alla letteratura:

1. **Cross-hatch ASTM D3359 misurato** su PLA Bambu Basic per 5 primer (Maximum BricoIO,
   MaxMeyer, Saratoga, Vallejo, Tamiya). Sostituire stime forum con dati reali.
2. **Yellowing 12 mesi** Δ-E smartphone+ColorChecker di 5 clear coat (Pledge, MaxMeyer,
   Plasti-kote, Vallejo Polyurethane, Aliexpress generic).
3. **Preval sprayer + Pledge decantato** → DIY spray gloss €0.05/pezzo (potenziale replacement Mr.Hobby Premium).
4. **Time-tracking lotto pilota 10 pezzi** reale con stopwatch per validare timeline R2-D.
5. **A/B pricing Etsy reale** (€80 / €110 / €140) → conversion rate effettivo.
6. **Test journal primo ordine Aliexpress** (KPI documentati: tempo, dogana, qualità).
7. **Marmorino veneziano su PLA primerizzato** (claim teorica forte, mai testato).
8. **Vase mode multi-perimeter Orca Slicer** su Bambu A1 (vasi >25cm robusti).

I round 1+2 hanno coperto la dimensione **bibliografica e sourcing**. Il round 3
naturale è **sperimentale**: test casalinghi misurati con protocolli definiti
(`05_round2/A_2k_clearcoat/04_measurable_test_protocol.md` è il template).
