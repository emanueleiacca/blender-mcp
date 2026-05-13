# 99 — Connections: come questo round 3 risolve le decisioni R1+R2

> **TL;DR**: ogni test di questo lab risolve un set specifico di domande
> sospese in Round 1+2. Questo file è la **mappa di causalità inversa**:
> partendo dalla decisione che devi prendere, sai quale test fare.

---

## 99.1 Decisioni che hai "in sospeso" dopo R1+R2

| # | Decisione sospesa | File R1/R2 | Test R3 che risolve |
|---|---|---|---|
| D1 | Quale primer comprare di routine: Maximum BricoIO vs MaxMeyer Primer Filler vs Plasti-kote? | `05_round2/E_diy_budget/02_brico_lidl_paints.md` §2.1 (tutto basato su "claim user community") | **Test 01 cross-hatch** + **Test 06 thumb roll** |
| D2 | Pledge è davvero abbastanza per clear coat default, o serve Mr. Super Clear UV Cut? | `05_round2/E_diy_budget/07_workflow_recommended.md` step 8 + `INDEX.md` gap #2 | **Test 02 ΔE UV** + **Test 03 water bead** |
| D3 | Quando salire al 2K (SprayMax)? | `05_round2/A_2k_clearcoat/04_measurable_test_protocol.md` esiste, ma costa €120-340 | Tutto il pacchetto R3 con T6 opzionale SprayMax (€22 extra) |
| D4 | Vale la pena passare da sand 320 a sand 600+800 nel workflow R2-E? | `05_round2/E_diy_budget/07_workflow_recommended.md` step 2 e 4 | **Test 06 tactile rank** |
| D5 | Quale clear coat per pezzi che entrano in contatto con acqua/umidità (lampade bagno, vasi)? | `05_round2/E_diy_budget/06_premium_vs_budget_comparison.md` (manca dato water-resistance) | **Test 03 water bead** |
| D6 | Pezzi commerciali Etsy resistono al trasporto / cliente che fa cadere? | `05_round2/D_pipeline_industrial/` (pricing) → influenza politica reso | **Test 05 drop impact** |
| D7 | Lidl Crelando acrilici sono davvero "Vallejo Studio per fornitore comune"? | `_next_questions.md` E_diy_budget #18 | **Test 01 + 02 + 04** parallel con Crelando come trattamento extra |
| D8 | Pledge spruzzato con Preval sprayer = Mr. Hobby Premium Gloss a 1/30 costo? | `_next_questions.md` E_diy_budget #5 | **Test 02 + 03** con T_Preval come variante |

---

## 99.2 Per ogni test, quale file R1/R2 viene "validato"

### Test 01 — Cross-hatch
**Cita esplicitamente**:
- `05_round2/E_diy_budget/02_brico_lidl_paints.md` §2.1 (tabella "Aderenza
  a PLA — claims hobby vs test misurato") — i valori 3B/4B sono **stime
  forum**, non test. Cross-hatch sostituisce questi con dati propri.
- `05_round2/A_2k_clearcoat/04_measurable_test_protocol.md` §3 — questo
  R3 è la versione "povera" (€2.50 vs €70-100) del Test #1 di R2-A.
- `02_painting_and_primers/_next_questions.md` punti 22-25 — gap originale
  R1 su adesione primer.
- Decide: **Maximum BricoIO va usato con primer o no?** (tabella R2-E §2.1
  dice "con primer", il test te lo conferma con tuoi dati).

### Test 02 — ΔE UV
**Cita esplicitamente**:
- `INDEX.md` gap #2 "Yellowing 12 mesi Δ-E di 5 clear coat".
- `04_sealing_presentation/_next_questions.md` punti 1 e 5 (gap originale R1
  su yellowing).
- `05_round2/E_diy_budget/06_premium_vs_budget_comparison.md` — confronta
  Pledge vs UV cut premium. Il test ti dice il **vero** delta yellowing,
  non quello "atteso".
- `05_round2/E_diy_budget/_next_questions.md` #2 e #5 (Pledge + Preval
  alternative).
- Decide: **Pledge è abbastanza per default, o devi pagare Mr.Super Clear
  per pezzi premium?**

### Test 03 — Water bead
**Cita esplicitamente**:
- `05_round2/A_2k_clearcoat/04_measurable_test_protocol.md` §6 Test #4
  versione povera.
- `04_sealing_presentation/01_glossy_matte_sealers.md` (R1, generico) — il
  test ti dice quale "sigilla davvero" tra i tuoi candidati.
- `_next_questions.md` E_diy_budget #12 (food-contact safe Pledge) — il test
  water bead aiuta a capire se Pledge crea barriera o no.
- Decide: **per pezzi bagno/cucina decor, quale clear coat è giusto?**

### Test 04 — Coin scratch
**Cita esplicitamente**:
- `05_round2/A_2k_clearcoat/04_measurable_test_protocol.md` §4 Test #2
  versione casalinga gratuita (vs €5-30 Mohs pencil set).
- `02_painting_and_primers/04_durability.md` (R1, se esiste) — il test ti
  dice quale finish resiste graffio quotidiano del cliente.
- Decide: **per pezzi "manipolati" (miniature, giochi da scrivania), il
  workflow R2-E §7.3 è abbastanza, o serve durezza superiore (2K)?**

### Test 05 — Drop impact
**Cita esplicitamente**:
- Gap implicito di tutto R2: nessuno ha mai testato robustezza meccanica
  del pezzo finito.
- `05_round2/D_pipeline_industrial/05_packaging_diy.md` (se esiste in R2-E
  packaging) — il drop test ti dice **quanto packaging serve davvero**.
- Decide: **packaging mailer kraft + bubble wrap è abbastanza per Etsy, o
  serve scatola rigida + foam?**

### Test 06 — Thumb roll + tactile
**Cita esplicitamente**:
- `05_round2/E_diy_budget/07_workflow_recommended.md` step 2 e 4
  (sand 320 → 600 → 800). Tactile rank ti dice se il cliente sente la
  differenza tra 600 e 800.
- Decide: **posso skippare lo step sand 800 e risparmiare 3 min/pezzo
  senza degradare l'esperienza cliente?**
- Folklore prop maker (thumb roll) → conferma rapida prima di setup
  completo cross-hatch.

### Test 07 — Excel template radar
**Cita esplicitamente**:
- Aggregatore: rende leggibili gli output dei test 01-06.
- Usa pesi del file `05_round2/E_diy_budget/06_premium_vs_budget_comparison.md`
  (peso prezzo vs qualità per piccolo brand commerciale).

### Test 08 — Protocollo 14gg
**Cita esplicitamente**:
- Versione "DIY budget" del protocollo R2-A `04_measurable_test_protocol.md`
  (€120-340, 25gg).
- Stesse decisioni risolte, costo 1/3, tempo 60%.

### Test 09 — Pitfalls
**Cita esplicitamente**:
- `_sources.md` di tutti i round per riferimenti metodologici.
- Errori comuni che invaliderebbero gli output dei test 01-06.

---

## 99.3 Vincitori R2 da CONFERMARE con i tuoi dati R3

Da `05_round2/E_diy_budget/02_brico_lidl_paints.md` §2.1 e workflow R2-E §7.3:

### Claim R2 da validare con R3
| Claim R2 | Pagina | Test R3 conferma/smentisce |
|---|---|---|
| "MaxMeyer Primer Filler vincitore Q/P" | R2-E §2.1 | Test 01 cross-hatch |
| "Maximum BricoIO funziona solo con primer prima" | R2-E §2.1 verdetto | Test 01 cross-hatch su 2 condizioni |
| "Pledge clear coat OK per 85-90% percezione cliente" | R2-E §7 filosofia | Test 02 ΔE + Test 03 water bead + Test 06 thumb roll |
| "Mr. Super Clear UV Cut step su pezzi >€40" | R2-A two-tier strategy | Test 02 ΔE quantifica il delta vs Pledge |
| "Plasti-kote = Rust-Oleum solido" | R2-E §2.1 | Test 01 cross-hatch |
| "Saratoga effetto pietra ≈ Montana GRANIT" | R2-E §2.1 | (fuori scope: test estetico soggettivo, non in R3-A) |

### Workflow #7 R2-E "Porcellana economy" — convalida operativa
Dopo il 14gg, dovresti poter rispondere "SÌ confermato" o "NO, sostituire X con Y"
per ogni step del workflow:
- Step 3 primer: vincitore di Test 01.
- Step 5 color: già testato in R2-E (Maxi Color, Maximum) → R3 non testa colore base ma compatibilità clear sopra.
- Step 8 clear coat: vincitore di Test 02 + 03.

---

## 99.4 Cose che R3 NON copre (gap residui per round 4+)

Da `_sources.md` e `_next_questions.md` ancora aperti dopo R3:
- A/B pricing Etsy reale (R2-D + INDEX gap #5).
- Test journal primo ordine Aliexpress (INDEX gap #6).
- Marmorino veneziano su PLA primerizzato (INDEX gap #7).
- Vase mode multi-perimeter Orca su Bambu A1 (INDEX gap #8).
- Foto prodotto A/B testing (R2-D ROI marginale highest).

Vedi `_next_questions.md` di R3 per la lista completa di gap residui post-R3.

---

## 99.5 Decisione finale dopo 14gg: come dovresti procedere

1. **Conferma o sostituisci** ogni elemento del workflow R2-E §7.3.
2. **Aggiorna `INDEX.md`** con il "workflow validato R3" che sostituisce
   quello atteso/intuito di R1+R2.
3. **Pubblica il blog/IG post** "I tested 6 budget coatings on PLA — here's
   the winner" (content marketing R2-A §10 "Output atteso").
4. Investi nel **round 4** sui gap residui prioritari (vedi `_next_questions.md`).
