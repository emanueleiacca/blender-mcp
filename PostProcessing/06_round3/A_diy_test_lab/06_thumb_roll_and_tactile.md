# 06 — Thumb roll & tactile rank tests (folklore prop maker)

> **TL;DR**: due test "brutali" non-ASTM ma **stranamente predittivi** nelle
> esperienze prop maker: il **thumb roll test** (correlato a cross-hatch
> adhesion in pratica) e il **tactile ranking** (sostituto del profilometro
> €5000 per rugosità superficiale). Costo: €0.

Risolve i gap "non posso comprare cutter ASTM oggi" e "profilometro per
rugosità è fuori budget" — fa decisioni informate stasera senza ordini Aliexpress.

---

## 6.1 Thumb roll test (folklore)

### Origine
Tradizione prop maker / autocarrozzeria / restauratore mobili: si valuta
un coating ruotando il **pollice carico** sopra la superficie 360° con
pressione costante. Se il coating "rolls off" — viene via — l'adesione è
fail.

NON è ASTM. Non c'è spec ufficiale. Ma **in 50 anni di pratica auto/prop
maker correla bene con cross-hatch ≤3B** secondo aneddoti di settore (vedi
forum r/AutoBody, r/Modelmakers, ASCI restoration forums).

### Procedura
1. Coating curato 24-72h.
2. Premi il **pollice** sopra il coating con **pressione "pollice in su
   forte"** (~30-40 N, prova prima su bilancia da cucina premendo finché
   leggi 3-4 kg).
3. **Ruota il pollice 360° mantenendo pressione**. Una rotazione completa,
   ~2 secondi.
4. Solleva, esamina con luce radente:
   - **Nessun segno, nessun residuo sul pollice**: pass, OK.
   - **Leggero residuo (sembra polvere chiara sul pollice)**: borderline.
   - **Visibile chip / area di coating mancante sul provino**: fail.
   - **Coating "rolls up" sul pollice come pellicola**: fail catastrofico.

### Score 1-3
| Score | Risultato | Equivalente ASTM cross-hatch |
|---|---|---|
| 3 | No segni, no residuo | ~4B-5B |
| 2 | Residuo lieve sul pollice, no chip | ~3B |
| 1 | Chip visibile o lifting | ≤2B |

### Quando usarlo
- **Test "stasera"** prima di setup completo cross-hatch.
- **Screening rapido** tra molti trattamenti: scarta i fail in 30 sec
  ciascuno, poi cross-hatch solo sui sopravvissuti.
- **Validazione di lotto** in produzione: ogni 10 pezzi finiti, thumb roll
  test su un punto nascosto.

### Bias enormi
- **Pressione operatore** varia ±50%. Stesso operatore stessa sessione.
- **Sudorazione dita** lubrica → falsi pass.
- **Pollice secco vs umido** → diversi attriti.
- **Non quantifica**: solo pass/fail/borderline.

---

## 6.2 Variante: pencil eraser test

Stessa logica, più riproducibile:
1. Usa una **gomma matita rosa standard** (Staedtler Mars Plastic, Faber-Castell).
2. Sfrega 10 volte avanti-indietro con pressione "come cancelli matita".
3. Esamina: graffio visibile? Coating viene via?

Più consistente del pollice perché la gomma ha attrito definito. Stesso
scoring 1-3.

---

## 6.3 Tactile ranking (sostituto profilometro)

### Cos'è un profilometro
Strumento che misura la rugosità superficiale (Ra, Rz) in micron passando
una punta diamantata sul materiale. Costo €1000-10000. Output: numero
Ra in µm.

### Versione tattile
Il dito umano sente differenze di rugosità **giù a ~10 µm** (più sensibile
di quanto la gente pensi). Letteratura tribologia conferma:
https://www.science.org/doi/10.1126/science.1238288 (Skedung et al. 2013,
"Feeling small: exploring the tactile perception limits").

### Procedura
1. **Stampa o prepara N provini** con trattamenti diversi (es. PLA grezzo,
   sand 320, sand 600, sand 1000, sand 1500+Pledge, sand 2000+Pledge+polish).
2. **Numera provini** su lato nascosto (1-N).
3. **Reclutta 5-10 testers** (amici, famiglia — non devono essere esperti):
   - Bendati o "concentrati sul tatto, occhi chiusi".
   - Gli dai i provini in **ordine random**.
   - Devono ordinarli da **più ruvido a più liscio**.
4. **Registra l'ordine** di ciascun tester.
5. **Calcola rank medio**:
   - Ogni provino riceve un rank 1-N da ciascun tester.
   - Media i rank → rank finale "consensus".
6. **Provini con rank simile** = **rugosità percepita simile**.

### Esempio matrice (fittizio dimostrativo)
| Provino | Tester1 | Tester2 | Tester3 | Tester4 | Tester5 | Avg rank |
|---|---|---|---|---|---|---|
| A: PLA grezzo | 1 | 1 | 1 | 1 | 2 | **1.2** |
| B: sand 320 | 2 | 2 | 3 | 2 | 1 | **2.0** |
| C: sand 600 | 3 | 4 | 2 | 3 | 3 | **3.0** |
| D: sand 1000 | 4 | 3 | 4 | 4 | 4 | **3.8** |
| E: + Pledge | 5 | 5 | 5 | 5 | 5 | **5.0** |

→ Ranking finale: A < B < C < D < E (dal più ruvido al più liscio).
Tester3 fa "swap" tra B e C (notano la differenza con difficoltà — implica
che B e C sono **vicini come rugosità**).

### Valore decisionale
Se 5 testers ordinano A < B < C **identicamente**, la differenza è chiara.
Se i ranking sono "noisy" tra B e C, **non vale la pena passare da 320 a
600** — il cliente non sente la differenza.

Questo test risolve direttamente: "posso saltare lo step sand 600 in R2-E
§7.3?" Risposta empirica basata sui tuoi clienti tipo (i testers).

### Reverse test — "trovami quello diverso"
Variante: 5 provini, 4 identici + 1 leggermente diverso. Tester deve
trovare l'outlier. Se nessuno lo trova → la differenza è impercettibile,
non vale lo sforzo produttivo.

---

## 6.4 Bias

### Thumb roll
1. Sudorazione operatore (lubrifica): asciuga dita prima di ogni test.
2. Forza variabile: pratica su bilancia cucina.
3. Pelle callosa vs liscia: stesso operatore.

### Tactile ranking
1. **Effetto temperatura provino**: se tieni un provino in mano 30 sec, si
   scalda — sembra diverso dagli altri. Mantieni tutti a stessa T (cassetto
   chiuso prima del test).
2. **Effetto polso**: provini umidi vs secchi → diverse percezioni. Asciugali
   tutti uguale.
3. **Effetto sequenza**: il primo provino tastato è il riferimento mentale.
   **Randomizza ordine per ogni tester**.
4. **Selezione testers**: musicista (mani sensibili) ≠ idraulico (mani
   calose). Mix realistico dei tuoi clienti target.

---

## 6.5 Costo & tempo

- **Setup**: €0 (gomma matita opzionale €1).
- **Thumb roll per provino**: 30 sec.
- **Tactile ranking 5 provini × 5 testers**: ~25 min totali (5 min/tester).

**Confronto profilometro**: €1000-10000. **Saving: 99.9%**. Trade-off: non
hai valore Ra in µm, ma **rank ordering perceptual**, che è ciò che conta
per scelta produttiva.

---

## 6.6 Quando NON fidarti di questi test

- **Prima decisione di vita**: thumb roll è "screening", non "qualifica".
  Per scegliere il clear coat finale di produzione, fai anche cross-hatch.
- **Comunicazione con cliente B2B**: nessun acquirente serio accetta "ho
  fatto il thumb roll test e va bene". Per quello servono dati misurati.
- **Variability between sessions**: questi test sono in-sessione. Non
  confrontare il thumb roll di lunedì col venerdì.

---

## 6.7 Fonti

- Skedung et al. 2013 Scientific Reports — limiti tattili dito umano:
  https://www.nature.com/articles/srep02617
- r/AutoBody "thumbnail test for paint" thread (folklore):
  https://www.reddit.com/r/AutoBody/
- r/Modelmakers cure check tradition: https://www.reddit.com/r/modelmakers/
- "Thumbnail hardness test" wiki:
  https://en.wikipedia.org/wiki/Thumbnail_test
- Project Farm sandpaper grit test methodology:
  https://www.youtube.com/@ProjectFarm
- ASTM does NOT have a thumb roll standard — è puro folklore di settore.
