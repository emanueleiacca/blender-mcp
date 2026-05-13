# 04 — Coin scratch hardness test (Mohs casalingo)

> **TL;DR**: una sequenza di oggetti casalinghi di durezza nota — unghia,
> moneta rame, chiave, vetro, lima — ti dà una scala 1-5 di durezza superficie
> abbastanza informativa per decidere se un clear coat resiste ai graffi
> d'uso quotidiano. Sostituisce il **Mohs pencil set (€25)** del R2-A §4.

Risolve **R2-A §4 "Test #2 Scratch test"** in versione gratis. Decisione:
"questa pasta morde con l'unghia? Allora è troppo morbida per essere
toccata".

---

## 4.1 La scala Mohs

Scala di durezza minerale (Friedrich Mohs, 1812). Va da 1 (talco) a 10
(diamante). Un materiale "più duro" graffia un materiale "più morbido".

Per pittura/coating siamo nel range 2-7. Riferimento:
https://en.wikipedia.org/wiki/Mohs_scale_of_mineral_hardness

### Materiali di riferimento casalinghi
| Materiale | Mohs | Note |
|---|---|---|
| Unghia umana | 2.5 | varia 2.3-2.7 per persona |
| Moneta rame puro | 3.0 | 1 cent USA pre-1982; in EU monete da 1/2/5 cent sono **rame placcato acciaio**, Mohs ~4 effettivo |
| Moneta nichel | 4.0 | 50 cent / 1€ / 2€ EU (lega rame-nichel) |
| Punta coltello acciaio | 5.5 | coltello cucina classico |
| Chiave casa | 5.5-6.0 | acciaio nichelato |
| Vetro window | 5.5-6.0 | bottiglia birra, finestra |
| Punta lima acciaio | 6.5-7.0 | lima per fai-da-te Brico |
| Carta vetrata grit 1000 | 7+ | corindone sintetico |

### Sequenza "gentile→aggressiva" consigliata
Unghia (2.5) → moneta 1€ rame placcato (≈4) → chiave (5.5) → vetro (6) →
punta lima (6.5).

Engineering Toolbox per Mohs vs materiali comuni:
https://www.engineeringtoolbox.com/mohs-scale-d_1623.html

---

## 4.2 Procedura standardizzata

### Setup
- Provino piano sul tavolo, fissato con biadesivo sotto.
- Lampada da scrivania luce **radente 30° dall'orizzontale** → graffi si vedono come riflessi.
- Smartphone in macro mode pronto.

### Per ogni "tester" (materiale di prova)
1. Tieni il tester a **45° rispetto alla superficie**.
2. Premi con pressione **"come scriveresti su un foglio"** (~3-5 N, prova
   prima su carta vetrata per calibrare il "sentiment").
3. Tira il tester per **5 cm**, ripeti **5 passate** parallele nello stesso
   punto (zona ~10×10mm).
4. Pulisci la polvere con pennello morbido o soffio.
5. Foto macro luce radente.
6. Score:
   - **Graffio visibile e tangibile (puoi sentirlo passando l'unghia)**: il
     coating ha durezza **inferiore** a quel tester.
   - **Solo segno superficiale (sparisce con dita strofinate)**: durezza
     simile.
   - **Nessun segno**: durezza superiore.

### Scoring "scala casalinga 1-5"
| Score casa | Significato | Mohs approx |
|---|---|---|
| **1** | Si graffia con unghia | ≤2.5 |
| **2** | Resiste unghia, si graffia con moneta 1€ | 2.5-4 |
| **3** | Resiste moneta, si graffia con chiave | 4-5.5 |
| **4** | Resiste chiave, si graffia con vetro/lima | 5.5-6.5 |
| **5** | Resiste tutto in casa | >6.5 (raro per acrilici) |

### Sensibilità unghia
**Soglia critica**: se il coating fa **score 1** → inservibile per pezzi
commerciali. Cliente passa il dito e li graffia. **Score ≥ 2 minimo** per
oggetti commerciali; **score ≥ 3** per oggetti "manipolati" (giochi,
miniature da gioco, oggetti da scrivania).

---

## 4.3 Test matrix consigliato

| ID | Trattamento | Score atteso |
|---|---|---|
| H0 | PLA Bambu Basic nudo | 2-3 (PLA Mohs ~3) |
| H1 | + Pledge 2 mani | 1-2 (Pledge è cera, morbida) |
| H2 | + MaxMeyer Trasparente Lucido | 2-3 |
| H3 | + Plasti-kote spray clear | 2-3 |
| H4 | + Mr. Super Clear UV Cut | 2-3 |
| H5 | + SprayMax 2K Glamour (riferimento alto-end R2-A) | 3-4 |

**Insight chiave**: pratica della scala mostra che **acrilici 1K stanno tutti
nel range 2-3**, il vero salto è 2K (3-4). Conferma trade-off R2-A:
2K dà +1-2 punti hardness, ma a costo di PPE/complessità.

---

## 4.4 Pencil hardness ASTM D3363 (variante più precisa, €5)

Se vuoi ancora più rigore: compra **set matite Faber-Castell o Staedtler
da 6B a 6H** (€5 cartolibreria).

### Procedura
1. Affila matita 6H, poi appoggia la punta su carta vetrata grit 400,
   sfrega per appiattire la punta a **cilindro piatto 1mm diametro**.
2. Tieni matita a **45°**, premi con **7.5 N** (~750g — usa bilancia da
   cucina premendo la matita sopra finché legge 750g).
3. Sposta matita di **6 mm** sopra il provino.
4. Esamina:
   - **Gouge** (incisione nel coating): durezza inferiore alla matita.
   - **Scratch** (solo segno, no incisione): durezza pari.
   - **No mark**: durezza superiore.
5. **Pencil hardness = la matita più dura che NON lascia gouge**.

Scala matite (più morbide → più dure):
`6B - 5B - 4B - 3B - 2B - B - HB - F - H - 2H - 3H - 4H - 5H - 6H`

Note: ASTM D3363 spec: https://www.astm.org/d3363-22.html
Conversione Mohs ↔ pencil:
- 6B-2B ≈ Mohs 1-2 (coating morbidissimo)
- B-F ≈ Mohs 2-3
- H-2H ≈ Mohs 3-4
- 3H-4H ≈ Mohs 4-5
- 5H-6H ≈ Mohs 5-6

---

## 4.5 Documentazione foto

Setup standard luce radente → confronti pre/post sequenza.

Esempio diagramma:
```
Prima            Dopo unghia      Dopo 1€         Dopo chiave
[liscio]   →    [liscio]    →    [liscio]   →    [graffio visibile]
                                                   ← Score 3 (resiste 1€, cede chiave)
```

---

## 4.6 Bias e controlli

1. **Cura coating**: testa a **7 giorni minimo** post-applicazione. A 24h
   tutti i coating sembrano molli. A 30 giorni alcuni continuano a
   indurire (2K, polyurethane).
2. **Temperatura**: a 10°C i polimeri sono più fragili (fratturano), a
   30°C più morbidi (graffio profondo). Testa a 20-25°C.
3. **Pressione operatore**: variabilità ±30% tra mani. Soluzione:
   peso fisso (vedi §4.4 pencil 750g) o **stesso operatore stessa
   sessione**.
4. **Oxidazione moneta rame**: monete vecchie hanno strato ossido che
   smorza il test. Usa monete relativamente nuove o lucida con dentifricio.
5. **Vetro non sempre 6 Mohs**: vetro temperato finestra ≈ 7. Soda-lime
   bottiglia ≈ 5.5-6. Sii consistente: stesso oggetto in tutti i test.

---

## 4.7 Tempo & costo

- **Setup**: €0 (oggetti casa) + €5 opzionale (pencil set).
- **Per provino**: 2 min per tester × 5 tester = 10 min.
- **Test 6 trattamenti**: ~60 min.

Confronto R2-A: lì €5-30 (Mohs pencil set). **Saving 100% se usi solo casa**.

---

## 4.8 Fonti

- Mohs scale wiki: https://en.wikipedia.org/wiki/Mohs_scale_of_mineral_hardness
- ASTM D3363 Pencil Hardness: https://www.astm.org/d3363-22.html
- Engineering Toolbox Mohs reference:
  https://www.engineeringtoolbox.com/mohs-scale-d_1623.html
- Project Farm "Toughest Floor Finish" methodology (channel):
  https://www.youtube.com/@ProjectFarm
- AvE channel "skookum test" methodology (philosophical inspiration):
  https://www.youtube.com/@arduinoversusevil2025
- r/Coatings DIY hardness threads: https://www.reddit.com/r/coatings/
