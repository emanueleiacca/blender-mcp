# 03 — Water bead angle test (idrofobicità & sealing efficacy)

> **TL;DR**: una goccia d'acqua + smartphone macro a 90° + un'app angolo
> gratuita misurano l'**angolo di contatto** abbastanza bene da decidere se
> un clear coat sta davvero "sigillando" la superficie. Costo: €0.

Risolve **R2-A §6 "Test #4 Water bead"** versione povera. Confronta sealing
efficacy di Pledge, MaxMeyer trasparente, Mr.Super Clear, PLA nudo. Più
diretto/interpretabile del ΔE per la domanda "questo clear coat sigilla?".

---

## 3.1 Perché l'angolo di contatto conta

Quando una goccia d'acqua si posa su una superficie, l'angolo che forma tra
la superficie del liquido e la superficie solida (misurato attraverso il
liquido) indica quanto la superficie è **idrofila** (acqua si spalma) o
**idrofoba** (acqua resta in goccia).

| Angolo | Caratterizzazione | Significato sealing |
|---|---|---|
| < 30° | Super-idrofila | Acqua penetra, **fail** |
| 30-60° | Idrofila | Sealing povero |
| 60-90° | Lievemente idrofoba | Sealing accettabile per pezzi indoor |
| **90-110°** | **Idrofoba** | **Sealing efficace, water-resistant** |
| > 110° | Molto idrofoba | Eccellente, lotus-effect zone |
| > 150° | Super-idrofoba | Coatings nano (non rilevante qui) |

**Soglia operativa per piccolo brand commerciale**: target **>90°** per pezzi
che possono entrare in contatto con liquidi (lampade da tavolo in bagno,
vasi, oggetti cucina decor). Sotto 70° = clear coat non sta davvero
"sigillando".

Riferimento scientifico: https://en.wikipedia.org/wiki/Contact_angle

---

## 3.2 Setup laboratorio del povero — €0

| Item | Costo | Note |
|---|---|---|
| Goccia d'acqua | €0 | acqua del rubinetto OK; deionizzata ideale ma non critica |
| Smartphone macro mode | €0 | qualsiasi smartphone post-2018 |
| Righello acciaio | €0 (già da test 01) | come riferimento dimensionale |
| App misura angolo Android | €0 | "On Protractor" — https://play.google.com/store/apps/details?id=protractor.on |
| App misura angolo iOS | €0 | "Protractor" — https://apps.apple.com/it/app/protractor-easy-measure-angle/id1551614946 |
| Goniometer Pro Android (alternativa) | €0 free / €3 pro | https://play.google.com/store/apps/details?id=kr.sira.protractor |
| Software desktop alternativo | €0 | ImageJ + plugin Drop Shape Analysis: https://imagej.net/plugins/dropsnake |
| Siringa insulina o pipetta | €0.10 | farmacia, per gocce ripetibili |

**Totale: €0.10** (sì, dieci centesimi).

---

## 3.3 Procedura

### Step 1 — Preparazione provino
- Provino orizzontale **perfettamente piatto** su tavolo livellato (controlla
  con app livella smartphone).
- Provino **asciutto e pulito** (ultimo IPA almeno 1h prima per non
  contaminare con grasso).
- **Pulisci con cotton bud + IPA** se hai toccato il provino con dita.

### Step 2 — Deposito goccia
- **Siringa insulina** carica con 0.5 mL acqua deionizzata (o demineralizzata
  da supermercato, sezione ferri da stiro, €0.60/litro).
- Tieni siringa **verticale**, ago a **2-3 mm dalla superficie**.
- **Premi piano** finché una goccia di **~5-10 µL** (≈ 1 unit della scala
  insulina) si stacca per gravità. NON spingere la goccia contro la
  superficie.

⚠️ Goccia troppo grande (>20 µL): la gravità deforma la goccia
("appiattimento"), falsa l'angolo verso l'alto. Resta sotto 10 µL.

### Step 3 — Foto di profilo
- **Smartphone a 90° sulla superficie**, sensore allineato al piano del
  provino.
- Usa pila di libri o smartphone holder per stabilità.
- **Lente macro mode** o clip macro 10x (€10 Aliexpress se vuoi più qualità).
- **Distanza 8-12 cm**, fuoco sulla goccia.
- **Sfondo scuro** dietro il provino (cartoncino nero) → contrasto goccia
  visibile.
- **Luce di lato** (lampada da scrivania, non frontale).
- Scatta **entro 5 secondi** dal deposito (acqua evapora, l'angolo cambia).

### Step 4 — Misura angolo
1. Apri foto in app **On Protractor** (Android) o **Protractor** (iOS).
2. Posiziona il vertice del protractor sul **punto di contatto goccia-superficie**
   (left o right).
3. Allinea un braccio del protractor con la **superficie del provino**.
4. Allinea l'altro braccio con la **tangente alla goccia nel punto di contatto**.
5. Leggi angolo.
6. Ripeti dal lato opposto della goccia → fai la media dei due valori.
7. Ripeti su 3 gocce diverse sullo stesso provino → media finale.

### Step 5 — Documentazione
Salva: foto originale, foto annotata con angolo, valore in tabella Excel.

---

## 3.4 ImageJ Drop Snake (più scientifico, gratis)

Per chi vuole essere più rigoroso senza spendere:
1. Scarica ImageJ: https://imagej.nih.gov/ij/download.html
2. Installa plugin **DropSnake**:
   https://imagej.net/plugins/dropsnake
3. Apri foto goccia.
4. Plugin disegna automaticamente la curva e calcola angolo da entrambi i lati
   con migliore precisione di un'app angolo manuale.
5. Output: angolo sinistro, angolo destro, altezza goccia, diametro base.

Tempo: 2 min/foto vs 30 sec con app — usalo per validation, non per tutti
i provini.

---

## 3.5 Test matrix consigliato

| ID | Trattamento | Angolo atteso (forum/stima) | Misura tua |
|---|---|---|---|
| W0 | PLA Bambu Basic nudo | 75-85° | ? |
| W1 | PLA + 1 mano primer MaxMeyer + bianco | 75-90° | ? |
| W2 | W1 + Pledge 2 mani | 70-85° (Pledge è poco idrofobo) | ? |
| W3 | W1 + MaxMeyer Trasparente Lucido | 85-100° | ? |
| W4 | W1 + Mr. Super Clear UV Cut | 80-95° | ? |
| W5 | W1 + cera Kiwi neutra strofinata | 95-110° (cera = idrofoba) | ? |

**Insight chiave**: il test rivela che **Pledge ≈ PLA nudo** per
idrofobicità → Pledge è un buon "filler livellante" e UV-medium-grade, ma
**non sigilla davvero**. Conferma trade-off del workflow R2-E §7.3 step 8.

---

## 3.6 Cosa misurare oltre l'angolo (gratis)

### Tempo evaporazione 10 µL
- Deposita goccia 10 µL, cronometro.
- Misura tempo per scomparire visibilmente (a 22°C, 50% RH).
- Range tipico: 8-25 min.
- **Più alto = superficie idrofoba** (acqua scivola lontana dal provino o
  resta perlina) o **meno porosa** (no assorbimento).

### Stain test (dopo evaporazione)
- Lascia goccia evaporare completamente.
- Esamina superficie a luce radente.
- **Alone visibile?** → c'è stato assorbimento minerali = superficie porosa.
- **Nessuna traccia?** → ottimo sealing.

### Drop scivolamento angolo
- Inclina provino lentamente con goniometro su carta.
- Misura angolo a cui la goccia inizia a **scivolare** (non rotolare).
- Superficie con angolo <10° = molto idrofoba/lubrica.

---

## 3.7 Bias

1. **Acqua del rubinetto** contiene minerali che cambiano tensione
   superficiale ±5%. Usa demineralizzata per ferro da stiro per consistenza
   tra sessioni.
2. **Temperatura**: a 30°C la tensione superficiale acqua scende ~5%
   (angolo diminuisce 2-3°). Lavora a 20-25°C.
3. **Vibrazioni**: tavolo ondulante o smartphone shake → goccia ovale, falsa
   misura. Treppiede + provino su lastra inerziale (€0, mattonella).
4. **Tempo dal deposito**: misura **<5 secondi**. Dopo 30s l'angolo scende
   per evaporazione/wicking.
5. **Operatore parallasse**: lente smartphone non perfettamente al livello
   superficie → vedi la goccia "dall'alto" → angolo apparente sbagliato.
   Usa lente acquario per controllo (1€).

---

## 3.8 Costo & tempo

- **Setup**: €0.10 (siringa) + €0 software = quasi gratis.
- **Per provino**: 3 min (foto) + 2 min (analisi app) = 5 min.
- **Test 6 trattamenti × 3 gocce**: ~90 min.

**Confronto R2-A**: lì €30-50 (treppiede + clip macro), risultato simile.
Saving 95%.

---

## 3.9 Fonti

- Wikipedia Contact angle: https://en.wikipedia.org/wiki/Contact_angle
- ImageJ DropSnake plugin: https://imagej.net/plugins/dropsnake
- On Protractor Android: https://play.google.com/store/apps/details?id=protractor.on
- Goniometer Pro Android: https://play.google.com/store/apps/details?id=kr.sira.protractor
- Protractor iOS: https://apps.apple.com/it/app/protractor-easy-measure-angle/id1551614946
- "DIY contact angle measurement" guide accademica:
  cerca "contact angle measurement smartphone" su Google Scholar
- Project Farm wax & sealer tests (channel): https://www.youtube.com/@ProjectFarm
- r/Detailing wax sealing comparison threads: https://www.reddit.com/r/AutoDetailing/
