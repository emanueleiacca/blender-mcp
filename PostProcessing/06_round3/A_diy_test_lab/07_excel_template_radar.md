# 07 — Template Excel/Sheet con scoring e grafico radar

> **TL;DR**: una sola griglia Excel + grafico radar fa convergere 7 test
> diversi in **una decisione visuale**. Costo: €0 (Google Sheets gratis).

Questo file descrive la struttura del foglio. Puoi ricrearla in 15 min su
Google Sheets o LibreOffice Calc. Esempio compilato con **dati fittizi**
serve solo a mostrare come si legge — **non sono test reali**.

---

## 7.1 Struttura foglio "Test Matrix"

### Layout colonne
| Col | Header | Tipo | Range/scala |
|---|---|---|---|
| A | Trattamento ID | testo | T0...T5 |
| B | Descrizione trattamento | testo | libera |
| C | Costo €/pezzo | numero | €/pezzo materiali |
| D | Tempo lavoro min/pezzo | numero | minuti |
| E | Cross-hatch (test 01) | scala 0-5 | 0B=0, 5B=5 |
| F | ΔE @ 100h UV (test 02) | numero | basso = meglio |
| G | Water bead angle ° (test 03) | numero | alto = meglio (target >90°) |
| H | Scratch score (test 04) | scala 1-5 | alto = meglio |
| I | Drop threshold cm (test 05) | numero | alto = meglio |
| J | Thumb roll (test 06) | scala 1-3 | alto = meglio |
| K | Tactile rank (test 06) | scala 1-N | basso = più liscio |
| L | Score normalizzato 0-100 | formula | media pesata |

### Normalizzazione (riga 2 onwards)
Per confrontare metriche con scale diverse, **normalizza tutto su 0-100**
dove 100 = meglio.

```
Cross-hatch normal     = E2 / 5 * 100
ΔE normal              = MAX(0, 100 - F2*10)        ;  ΔE 0=100, ΔE 10=0
Water bead normal      = MIN(100, MAX(0, (G2-30)/(120-30)*100))
Scratch normal         = H2 / 5 * 100
Drop normal            = MIN(100, I2 / 80 * 100)    ; 80cm = 100
Thumb roll normal      = J2 / 3 * 100
Tactile normal         = (1 - (K2-1)/(N_max-1)) * 100
```

### Peso decisionale (per piccolo brand commerciale)
| Test | Peso |
|---|---|
| Cross-hatch (E) | 25% |
| ΔE UV (F) | 20% |
| Water bead (G) | 10% |
| Scratch (H) | 15% |
| Drop (I) | 15% |
| Thumb roll (J) | 5% |
| Tactile (K) | 10% |

**Formula score finale colonna L**:
```
=SUMPRODUCT({0.25,0.20,0.10,0.15,0.15,0.05,0.10}, {E_norm,F_norm,G_norm,H_norm,I_norm,J_norm,K_norm})
```

Pesi modificabili: se stai facendo lampade da bagno, dai più peso a water
bead (umidità). Se fai miniature da gioco, più peso a scratch e thumb roll.

---

## 7.2 Esempio compilato (FITTIZIO — non sono dati reali)

| ID | Trattamento | €/pz | min | CH | ΔE | WB | SC | DR | TR | TC | SCORE |
|---|---|---|---|---|---|---|---|---|---|---|---|
| T0 | PLA nudo (controllo) | 0.00 | 0 | 0 | 14.9 | 78° | 2 | 30 | 1 | 1 | **18** |
| T1 | Maximum BricoIO solo | 0.20 | 5 | 2 | 8.5 | 82° | 2 | 35 | 2 | 2 | **38** |
| T2 | MaxMeyer Primer + Maximum + Pledge | 0.45 | 12 | 4 | 7.2 | 84° | 3 | 40 | 3 | 4 | **65** |
| T3 | MaxMeyer Primer + Maximum + MaxMeyer Trasp | 0.65 | 13 | 4 | 4.1 | 92° | 3 | 38 | 3 | 4 | **71** |
| T4 | MaxMeyer Primer + Maximum + Mr.Super Clear UV | 0.85 | 13 | 4 | 1.8 | 88° | 3 | 38 | 3 | 4 | **77** |
| T5 | Plasti-kote Primer + Maximum + Mr.Super Clear | 1.10 | 14 | 5 | 1.5 | 89° | 4 | 42 | 3 | 4 | **82** |
| T6 | SprayMax 2K (riferimento high-end R2-A) | 2.20 | 18 | 5 | 0.9 | 102° | 4 | 65 | 3 | 5 | **94** |

(**ESEMPIO FITTIZIO** per illustrare struttura. Non basare decisioni su questi numeri.)

### Lettura della tabella esempio
- **T0** controllo: tutto basso, conferma PLA nudo è inadeguato commerciale.
- **T1** Maximum solo: marginal, costo bassissimo ma score 38.
- **T2-T4** stratificati con primer: score 65-77, costo €0.45-0.85.
- **T5** Plasti-kote+Maximum+SC: score 82, vicino al 2K a 1/2 del costo.
- **T6** 2K: score 94 ma costo €2.20 e 18 min lavoro + PPE.

**Decisione esempio**: T4 (€0.85, 13 min, score 77) è "sweet spot" per
piccolo brand. T5 se vuoi 5 punti score extra a +30% costo.

---

## 7.3 Grafico radar

### Google Sheets
1. Seleziona colonne ID + Cross-hatch_norm + ΔE_norm + ... + Tactile_norm.
2. Insert → Chart → Chart type = **Radar Chart**.
3. Series = ogni trattamento, Categories = nomi test.
4. Output: grafico ragnatela 7-assi con poligono per trattamento.

### LibreOffice Calc
1. Stessa selezione.
2. Insert → Chart → Net (= radar in LibreOffice).
3. Stesso risultato.

### Interpretazione visuale
Poligono più grande/regolare = trattamento migliore.
Poligono "schiacciato" = un test passa, altri falliscono → trattamento
sbilanciato (es. T1 con score adesione basso ma good scratch).

### Esempio interpretazione esempio fittizio
- **T6 (2K)**: poligono quasi al limite esterno, molto regolare.
- **T4**: poligono inscritto in T6, leggermente più piccolo ma molto vicino.
- **T0**: stella collassata al centro.

---

## 7.4 Foglio "Cost vs Performance"

Aggiungi grafico scatter:
- X axis: Costo €/pz (colonna C)
- Y axis: Score finale (colonna L)
- Punti: ogni trattamento.

Trade-off "Pareto frontier" diventa visivo: il **sweet spot** è il punto
in alto-sinistra (basso costo, alto score). I trattamenti in alto-destra
(alto costo, alto score) sono "premium". I trattamenti in basso (basso
score qualsiasi costo) si scartano.

---

## 7.5 Foglio "Time tracking" per produzione

Quando passi alla produzione, l'Excel diventa un **time tracker**:
- Colonna: pezzi prodotti.
- Riga: ogni step del workflow.
- Cella: minuti registrati con stopwatch.

Output: profilo medio tempo per pezzo, identifica colli di bottiglia.
Connessione diretta con R2-D `pricing_pipeline` per validare il pricing
basato su tempo reale, non stimato.

---

## 7.6 Template Google Sheets pubblico

Non posso linkare un foglio reale (non posso creare URL pubblici). Ma in
2 minuti puoi:
1. Creare nuovo Google Sheet.
2. Copia/incolla la tabella di §7.2 come point di partenza.
3. Aggiungi formule normalizzazione e score finale.
4. Insert chart radar.

Tempo setup: 20 min. Riusabile per ogni test futuro.

---

## 7.7 Best practice per data entry

1. **Una scheda per sessione test**: data, T/RH, operatore, batch coating.
2. **NON modificare dati passati** — se serve correzione, aggiungi colonna
   "note correzione" con motivazione.
3. **Versiona** mensilmente (Sheet → File → Make a copy).
4. **Backup** colonna O con timestamp data.
5. **Foto**: link in colonna P alle foto Google Drive corrispondenti
   (`HYPERLINK("url", "foto")`).

---

## 7.8 Connessione con altri file

- I valori inseriti vengono da: test 01-06 (file `01_*.md` - `06_*.md`).
- Il file `99_connections.md` ti dice **quali decisioni il foglio risolve**.
- Il file `08_14_day_protocol.md` ti dice **quando compilare il foglio**.
- Il file `09_pitfalls_and_controls.md` ti dice **cosa annotare in "note"**.

---

## 7.9 Fonti

- Google Sheets radar chart docs:
  https://support.google.com/docs/answer/9146100
- LibreOffice Calc net chart:
  https://help.libreoffice.org/latest/en-US/text/schart/01/wiz_chart_type.html
- Pareto frontier concept:
  https://en.wikipedia.org/wiki/Pareto_efficiency
- ColourScience radar visualization examples:
  https://www.colour-science.org/
- Project Farm spreadsheet methodology (vedi descrizioni video):
  https://www.youtube.com/@ProjectFarm
