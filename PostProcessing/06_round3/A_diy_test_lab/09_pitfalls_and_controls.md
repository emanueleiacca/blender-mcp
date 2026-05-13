# 09 — Pitfalls & controlli per laboratorio del povero

> **TL;DR**: 12 modi in cui un test casalingo restituisce numeri **plausibili
> ma sbagliati**, e come evitarli. Costo controlli: €10-15.

Sez. ispirata alle "10 cose che ho imparato a sbagliare" tipiche di Project
Farm + folklore makers. Da leggere PRIMA di Day 1 del protocollo 14gg.

---

## 9.1 Variabilità umidità tra applicazioni

### Problema
Spray applicato a 30% RH cura diverso da spray a 70% RH. Differenza visibile
in:
- **Adesione** (umidità intrappolata → 1-2 punti cross-hatch).
- **Yellowing** baseline (umidità nei polimeri).
- **Finish** (orange peel a bassa RH, soft a alta RH).

### Controllo
- **Igrometro digitale Aliexpress** €5: cerca "digital hygrometer thermometer mini".
  https://www.aliexpress.com/wholesale?SearchText=digital+hygrometer+thermometer
- **Registra T/RH** all'inizio E alla fine di ogni applicazione.
- **Target**: 18-25°C, 40-60% RH.
- **Se fuori range**: rimanda di 1-2h o usa stanza diversa.
- **Annota** comunque su Excel colonna "note ambient".

---

## 9.2 Camera smartphone auto WB

### Problema
Smartphone auto white balance "corregge" la foto in base alla luce ambientale.
Risultato: due foto della stessa scena in due momenti diversi hanno WB
diverso → ΔE artefatto fino a 5-10 unità (più del segnale di yellowing
reale).

### Controllo
- Usa modalità **Pro / RAW / Manual** dello smartphone (Samsung Pro Mode,
  iPhone "ProRAW" o app Halide / Open Camera).
- **WB fisso 5500K** (Daylight).
- **Esposizione fissa** (no Auto ISO).
- **Lente fissa** (non zoom).
- **Sempre stessa lampada** in stesso angolo.

### Hack se non hai modalità pro
- App **Open Camera Android** (free): https://opencamera.org.uk/
  Permette WB e exposure manuali su qualunque Android.

---

## 9.3 Inconsistenza pressione cross-hatch

### Problema
La pressione lametta varia tra tagli → alcuni tagliano solo coating, altri
affondano nel PLA → falsi positivi 0B.

### Controllo
- **Dima stampata** con scanalature 0.5mm profonde — guida la lametta a
  profondità costante.
- **Grammino calibrato**: poggia un peso noto (50-100g, una moneta 2€ +
  bullone M6) sopra la lametta mentre tagli. Pressione costante.
- **Pratica su provino sacrificio** prima di ogni sessione (5 tagli di warmup).

---

## 9.4 Cura insufficiente

### Problema
"Test a 24h dall'applicazione" → coating ancora plastico, adesione e
hardness inferiori al valore finale 7-30 gg.

### Controllo
- **Aspetta 7 giorni minimo** per tutti i test (R2-A standard).
- **Cura al buio** per evitare yellowing pre-test.
- **Cura a 20-22°C**: temperature più basse rallentano la polimerizzazione.

### Test "double check"
Ripeti i test a 30 giorni se hai dubbi sulla cura completa di alcuni
trattamenti (Pledge, polyurethane). Il delta 7gg vs 30gg dovrebbe essere
piccolo per acrilici 1K, può essere significativo per 2K e polyurethane.

---

## 9.5 Substrato non uniforme

### Problema
Provini stampati in lotti diversi, layer height diversa, o orientamento
diverso → top surface texture diversa → coating si comporta diverso.

### Controllo
- **STAMPA TUTTI I PROVINI IN UN SOLO PLATE**, stesso filamento spool,
  stesso giorno, stessa T temperature stampa.
- **Stesso sand 320** su tutti prima del primer (un solo pezzo di carta vetrata,
  passate uguali).
- Marca provino bottom (lato non testato) per orientamento.

---

## 9.6 Lampada UV decay

### Problema
LED UV-A 365nm Aliexpress economici perdono potenza nel tempo (3-6 mesi).
Sessioni successive con stessa lampada possono dare differenti irraggiamenti.

### Controllo
- **Tutti i provini in una sola sessione UV** continuativa.
- Misura **un provino di riferimento** ogni N test (es. un provino tutto
  Maximum BricoIO) → se ΔE del riferimento varia tra sessioni, c'è decay.
- Tieni un **"provino archive"** non esposto, usalo come zero ogni volta.

---

## 9.7 ColorChecker DIY degradazione

### Problema
Inkjet su carta fotografica sbiadisce sotto luce ambiente → calibrazione
WB drifta.

### Controllo
- **Conserva ColorChecker DIY in busta nera** o cassetto chiuso.
- **Sostituisci ogni 3 mesi** (€0.50 stampa).
- Usa **patch carta bianca Fabriano** come riferimento "no inchiostro" stabile,
  per controllare il drift del ColorChecker stesso.

---

## 9.8 Bias operatore (single-blind)

### Problema
Sai quale provino è quale → involontariamente sei più "morbido" col
trattamento che speri vinca.

### Controllo
- **Numerazione random** sotto i provini.
- Foglio Excel **separato** (`trattamenti.txt`) che mappa numero ↔
  trattamento, **non aprilo durante i test**.
- Solo dopo aver compilato l'Excel test, decodifica.

### Validation cross-operatore
Per test soggettivi (thumb roll, tactile), **fai eseguire i test da una
seconda persona ignara dei trattamenti**. Confronta i ranking.

---

## 9.9 Replica insufficiente

### Problema
1 provino per trattamento → singolo dato, alta varianza, conclusioni traballi.

### Controllo
- **2 repliche minimo** per trattamento (R2-A consigliava 5 per significatività
  statistica vera). 2 è il compromesso "DIY pragmatic": ti dà un'idea
  di varianza, non significatività statistica formale.
- Se due repliche dello stesso trattamento divergono molto (es. cross-hatch
  3B vs 5B) → **ripeti il trattamento**, hai un problema di applicazione.

---

## 9.10 Tape rotolo aperto da troppo tempo

### Problema
Scotch Magic conservato in cassetto polveroso 6 mesi → adesione degradata
20-30%. Risultato: tutti i cross-hatch sembrano 4B-5B (falsi positivi).

### Controllo
- **Rotolo nuovo dedicato test** (€1.20).
- Scarta primi 30 cm del rotolo (potenzialmente contaminati).
- Usa entro 1 mese dall'apertura.

---

## 9.11 Acqua dura test water bead

### Problema
Acqua rubinetto con tante TDS (calcio, magnesio) ha tensione superficiale
diversa da acqua deionizzata.

### Controllo
- **Acqua demineralizzata da supermercato** (sezione ferri da stiro), €0.60/L.
- Stesso lotto di acqua per tutti i provini di una sessione.

---

## 9.12 Trazione tape velocità diversa

### Problema
Strappo lento (>2 sec) → falsi 5B. Strappo troppo veloce (<0.3 sec) → falsi 0B.

### Controllo
- **Conta "uno-due"** durante strappo → ~1 sec è il target.
- Per riproducibilità: **peso 500g attaccato** al tape, fallo cadere dal
  bordo del tavolo. Gravità + peso = velocità ripetibile.

---

## 9.13 Tabella "cosa annotare nel campo note Excel"

Per ogni provino, per ogni test, annota:
- T °C ambiente.
- RH %.
- Ora del giorno.
- Operatore.
- Lotto bomboletta/prodotto (es. "MaxMeyer batch 2024-03").
- Anomalie visive (bolle, cola, polvere).
- "Note free" libera per intuizioni.

Questi metadata salvano analysi quando un risultato sembra strano dopo settimane.

---

## 9.14 Quando rifare il test

Segnali che invalidano la sessione:
1. RH fuori 30-70% durante applicazione.
2. T fuori 15-30°C.
3. Lampada UV ha avuto sbalzi (timer fallito, blackout).
4. Provini caduti o manipolati durante cura.
5. Foto T=0h e Tn con luce diversa (visibile a occhio nudo).
6. >50% varianza tra repliche di stesso trattamento.

In questi casi: **scarta sessione, ripeti**. Meglio rifare 1 giorno di test
che basare decisioni produttive su dati corrotti.

---

## 9.15 Fonti

- ASTM general "Good Practice for Coatings Test":
  https://www.astm.org/standardization-news/?q=coatings-testing
- Project Farm "How I test" descriptions (varie video descrizioni):
  https://www.youtube.com/@ProjectFarm
- Reddit r/coatings DIY mistakes thread:
  https://www.reddit.com/r/coatings/
- "Why your DIY paint test is wrong" blog post di restoration forums.
- Hygrometer Aliexpress: https://www.aliexpress.com/wholesale?SearchText=hygrometer+thermometer+digital
- Open Camera Android: https://opencamera.org.uk/
