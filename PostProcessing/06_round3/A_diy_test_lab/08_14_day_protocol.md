# 08 — Protocollo 14 giorni: dalla stampa alla decisione

> **TL;DR**: in 14 giorni di calendario, con ~14 ore lavoro attivo totali e
> **<€50 di BOM**, esci con dati propri su 6 trattamenti × 7 test e una
> decisione informata su quale workflow scegliere. Versione povera del
> protocollo R2-A (€120-340, 25 giorni).

Sostituisce/affianca `05_round2/A_2k_clearcoat/04_measurable_test_protocol.md`
per chi vuole risultati **velocemente, gratis, decisione next-week**.

---

## 8.1 Calendario alto-livello

| Giorno | Cosa fai | Tempo attivo |
|---|---|---|
| Day 1 | Stampa 12 provini PLA Bambu Basic identici | 30 min setup + 4h stampa unattended |
| Day 2 | Sand uniforme 320 → applica primer (6 trattamenti × 2 repliche) | 2h |
| Day 3 | Applica color base | 1.5h |
| Day 4-9 | Cura completa (no test, no manipolazione) | 0 |
| Day 10 | Setup laboratorio (lampada UV, ColorChecker, dima cross-hatch) | 1.5h |
| Day 11 | Test 01 cross-hatch + Test 04 scratch + Test 06 thumb roll | 2h |
| Day 11-12 | Test 02 ΔE: foto T=0h, lampada UV ON | 30 min + unattended |
| Day 13 | Test 02 fine 48-100h, foto Tn | 30 min |
| Day 13 | Test 03 water bead + Test 05 drop + Test 06 tactile | 2h |
| Day 14 | Data entry Excel + grafico radar + decisione | 2h |
| **TOTALE** | | **~14h attivo** |

Note: Day 11-12 il test UV non è 100h pieno per stare in 14 giorni — è 48-72h
(test "accelerato del test accelerato"). Per data più robusto, estendere a
21 giorni e 100h UV.

---

## 8.2 Day 1 — Stampa provini

### STL provino standard
**Piastrina 25 × 25 × 3 mm**, top surface piatta orientata verso l'alto in
stampa. 1 angolo smussato 45°×2mm per orientamento (marca "alto").

Creabile in 5 min in TinkerCAD: https://www.tinkercad.com/

### Parametri stampa Bambu A1
- Filamento: **Bambu PLA Basic White** (10100). Bianco puro per visibilità
  yellowing (test 02).
- Layer height: **0.16mm** (riferimento commerciale tipico).
- Infill: 50% gyroid (poco rilevante per test superficie).
- 12 provini su 1 piatto in ~1h (stampa parallela).

### Numerazione
Marca ogni provino sulla **superficie bottom non testata** con numero
permanente (sharpie). Mantieni mapping numero ↔ trattamento in un foglio
"trattamenti.txt" SEPARATO dal foglio Excel test (blinding).

### Costo
~30 cents di filamento totale.

---

## 8.3 Day 2 — Sand + primer

### Sand 320 uniforme
- Carta vetrata 320 wet, **passata uguale per tutti** in direzione random.
- Sciacqua, asciuga 10 min.
- **Stesso operatore stesso giorno** = baseline uniforme.

### Trattamenti
6 condizioni × 2 repliche = 12 provini (corrisponde alla stampa Day 1).

| ID | Trattamento |
|---|---|
| T0 | PLA nudo (no primer no color no clear) — controllo negativo |
| T1 | Maximum BricoIO spray bianco diretto (no primer) |
| T2 | MaxMeyer Primer Filler + Maximum bianco |
| T3 | MaxMeyer Primer + Maximum + Pledge 2 mani |
| T4 | MaxMeyer Primer + Maximum + Mr. Super Clear UV Cut |
| T5 | Plasti-kote Primer + Maximum + Mr. Super Clear |

Applicazione:
- Bomboletta 25-30 cm distanza, 2 mani sottili perpendicolari.
- Asciugatura 30 min tra mani.
- T/RH stessa giornata. Registrare con hygrometer (vedi
  `09_pitfalls_and_controls.md`).

Tempo totale Day 2: ~2h.

---

## 8.4 Day 3 — Color base e prima parte clear

- Color base white (Maximum BricoIO per T1-T5 dove applicabile).
- Pledge per T3, lascia curare overnight prima del clear coat su T4/T5.
- Mr.Super Clear su T4, T5.

Tempo Day 3: ~1.5h.

---

## 8.5 Day 4-9 — Cura

**Non toccare. Non testare. Non spostare.**

7 giorni minimo di cura per:
- Pledge (cura completa ~5-7 gg).
- Acrilici 1K (cura primaria 24h, completa 7-14 gg).
- Mr.Super Clear (cura ~3 gg).

Tenere provini a:
- 20-22°C.
- 40-60% RH (igrometro €5).
- **BUIO** (cassetto chiuso) → no UV pre-test che falsa baseline.

Tempo attivo: 0.

---

## 8.6 Day 10 — Setup laboratorio

Cose da preparare:
- **Dima cross-hatch** stampata (1mm scanalature).
- **Lametta nuova** dal pack.
- **Scotch Magic** rotolo nuovo.
- **Lampada UV-A 365nm** (arrivo Aliexpress giorno 1 → giorno 10 OK
  con corriere standard).
- **Box di cartone con alluminio interno** per UV.
- **ColorChecker DIY stampato** + foglio fotografico extra di scorta.
- **App scaricate sullo smartphone**: Color Grab, On Protractor.
- **Excel/Sheet aperto** con template §7.

Tempo: 1.5h.

---

## 8.7 Day 11 — Test "fast": adesione + scratch + thumb roll

Test rapidi che non richiedono tempo di esposizione.

### Test 01 cross-hatch (45 min totali)
12 provini × 5 min = 60 min teorici. Stima realistica con foto: ~75 min.
NB: per T0 (PLA nudo) il cross-hatch non ha senso → skip, score N/A.

### Test 04 scratch (30 min totali)
12 provini × 5 tester × 30 sec = ~30 min reali.

### Test 06 thumb roll (15 min)
Veloce, brutale, una passata.

### Foto T=0h per Test 02
Subito dopo gli altri test (i test sopra non sono distruttivi sul colore).
12 provini su sfondo grigio con ColorChecker DIY, smartphone Pro RAW manuale.

Tempo Day 11: ~2.5h.

### Avvio UV
Sera Day 11: provini in box UV, lampada accesa con timer.

---

## 8.8 Day 11-13 — Test 02 UV in unattended

Lampada accesa 48-72 ore (~h21 Day 11 → h21 Day 13 = 48h, prolungare a
Day 14 mattino per 72h).

Snapshot intermedi: opzionali se vuoi curva ΔE vs ore. Per la versione
"decisione veloce", basta T=0h e T=72h.

Hands-off durante UV. Controlla T del box ogni 24h (apri 30s, lascia
raffreddare).

---

## 8.9 Day 13 — Test rimanenti

### Test 02 fine UV
- Spegni lampada.
- Lascia 30 min raffreddare provini a T ambiente.
- Foto T=72h stessa scena Day 11.
- Misura L*a*b* con Color Grab.
- Calcola ΔE.

### Test 03 water bead (30 min)
6 trattamenti × 2 repliche × 3 gocce / replica = 36 misure. Veloce con app
On Protractor: 30 sec/misura = 18 min + 12 min foto.

### Test 05 drop impact (30 min)
6 trattamenti × 2 repliche distrutte progressivamente. Soglia trovata in
3-5 altezze ciascuna.

### Test 06 tactile rank (30 min)
5 testers (familia/amici), ranking 12 provini. 6 min/tester. Coordina con
WhatsApp + photo dei provini.

Tempo Day 13: ~2h.

---

## 8.10 Day 14 — Data entry + decisione

1. Apri Excel/Sheet template (§7).
2. Inserisci dati di tutti i test.
3. Verifica formule normalizzazione.
4. Genera grafico radar.
5. Genera scatter cost-vs-performance.
6. **Decisione**:
   - Trattamento score più alto? È sopra il tuo budget tempo/€?
   - Sweet spot Pareto (score alto, costo basso)?
   - Quale trattamento elimini dal workflow attuale?

Tempo: 2h (con calma + screenshot per documentazione).

### Output decisionale
Una **slide o nota** con:
- Vincitore comparativo (T_X) e perché.
- Costo/pezzo del vincitore.
- Tempo aggiunto al workflow R2-E §7.3.
- Limitazioni del test (campione piccolo, UV 72h non 12 mesi, etc.).
- Prossimo test da fare (vedi `_next_questions.md`).

---

## 8.11 BOM completa <€50

| Item | Prezzo € | Note |
|---|---|---|
| Filamento PLA Bambu Basic White (parte di kg già a casa) | 0.50 | ~30g totale |
| Maximum BricoIO bianco 400ml | 5.00 | parte di bomboletta già usata in produzione → costo allocato |
| MaxMeyer Primer Filler 400ml | 10.00 | id |
| Pledge 750ml | 4.00 | id |
| Mr. Super Clear UV Cut Flat 170ml (Amazon IT) | 16.00 | la spesa maggiore |
| Plasti-kote Super Primer (opz, se vuoi T5) | 8.00 | |
| **Materiali coatings** | **43.50** | parzialmente già a casa |
| Lametta Astra pack 5 | 1.50 | |
| Righello acciaio | 1.00 | |
| Scotch Magic 19mm | 1.20 | |
| Stampante ColorChecker DIY su carta foto (1 foglio) | 0.50 | |
| Lampada UV-A 365nm 50W Aliexpress | 18.00 | (€15-22) |
| Timer presa Aliexpress | 4.00 | |
| Igrometro digitale Aliexpress | 5.00 | |
| Bilancia da cucina (se non hai) | 8.00 | Lidl, Brico |
| Siringa insulina farmacia | 0.10 | |
| **Tooling** | **~39** | |
| **Totale solo materiali extra (escl. coatings parzialmente in casa)** | **~€45** | |
| **Totale teorico full purchase** | **~€80** | molti già in casa |

**Pulizia mentale**: i coatings sono già parte del workflow R2-E quotidiano,
spesa per il test = solo tooling (~€39). Bilancia/igrometro restano utili
per produzione successiva. **Net spesa marginale ~€20**.

---

## 8.12 Versione MEGA-BUDGET (€10 totali)

Se proprio non vuoi spendere:
- Skip Mr.Super Clear (no test ΔE per quel trattamento) — score limitato a
  5 trattamenti invece di 6.
- Skip lampada UV → test 02 sostituito con esposizione finestra Sud 7 giorni
  (più variabile ma gratis).
- Skip Plasti-kote (T5) → score 4 trattamenti.
- Salta bilancia (usa "feeling").

BOM <€10 (solo lametta + tape + carta + siringa).

Trade-off: meno trattamenti, dati UV meno controllati, test scratch più rumoroso.
**Ma**: hai un risultato comunque, hai dato un primo segnale, sai dove
investire €40 il mese prossimo.

---

## 8.13 Cosa fare DOPO Day 14

1. **Aggiorna `INDEX.md`** con la decisione presa e il nuovo workflow consigliato.
2. **Stampa 10-20 pezzi reali** col workflow vincitore, traccia tempo con
   stopwatch (validazione R2-D pipeline).
3. **Foto prodotto e listing** con il nuovo workflow → ascolta feedback cliente.
4. **Pianifica round 4 test** per i gap rimasti (vedi `_next_questions.md`).

---

## 8.14 Fonti

- Bambu PLA Basic TDS: https://us.store.bambulab.com/products/pla-basic-filament
- TinkerCAD per STL provino: https://www.tinkercad.com/
- Cura PLA timing (forum): https://www.reddit.com/r/3Dprinting/
- Acrilici cura times (vedi 05_round2/E_diy_budget): coatings_pratici
- Project Farm "long term test methodology": https://www.youtube.com/@ProjectFarm
- Lampada UV-A Aliexpress search: https://www.aliexpress.com/wholesale?SearchText=uv+365nm+50w+led
