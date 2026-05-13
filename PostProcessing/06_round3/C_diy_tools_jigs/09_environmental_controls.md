# 09 — Controlli ambientali: hygrometer + termometro (€3-15)

> Obiettivo: monitorare **T e RH** del garage/spazio di spruzzo per
> evitare failure mode noti delle vernici (blooming, runs, cure issue,
> orange peel). Investimento minimo, ROI altissimo nei mesi umidi.

---

## 9.1 BOM

| Item | Source | Cost € | Note |
|---|---|---|---|
| **Hygrometer + termometro digitale** | Aliexpress / Amazon / Lidl | 3-8 | LCD piccolo, batterie AAA |
| Hygrometer + display tempo storico (max/min) | Amazon | 8-15 | utile per trend giorni |
| Igrometro Xiaomi MiHome | Aliexpress | 12-18 | con app + storico mese |
| Wired probe (sonda esterna) | Amazon | 10-15 | per misurare zona spruzzo separata |
| **Setup minimo** | | **€3-5** | sufficiente |

URL:
- https://it.aliexpress.com/wholesale?SearchText=digital+hygrometer+thermometer
- https://www.amazon.it/s?k=igrometro+digitale

---

## 9.2 Soglie operative per workflow R2 PLA

### Range "safe" generale

| Parametro | Range OK | Range marginale | Range NOK |
|---|---|---|---|
| Temperatura ambiente | **18-25 °C** | 15-18 / 25-28 | <15 / >28 |
| Umidità relativa (RH) | **40-60%** | 30-40 / 60-70 | <30 / >70 |
| Differenza T pezzo vs aria | <3 °C | 3-5 °C | >5 °C (condensa) |
| Velocità aria zona spruzzo | 0.1-0.3 m/s | 0.3-0.8 | >0.8 (overspray + cura non uniforme) |

### Specifico per fase workflow

| Fase | T target | RH target | Problemi fuori range |
|---|---|---|---|
| **Sgrasso IPA** | 18-25 °C | <70% | Lento evaporazione IPA, residui |
| **Carteggio wet 800-2000** | qualsiasi | qualsiasi | — |
| **Primer Maximum/MaxMeyer** | 20-25 °C | 40-60% | **<10 °C**: primer non bagna, polvere; **>70% RH**: blooming bianco |
| **Acrilico airbrush** | 20-25 °C | 40-65% | Tip dry (RH bassa), orange peel (T bassa) |
| **Pledge clear** | 18-25 °C | 40-60% | RH alta = "blush" lattiginoso |
| **Mr. Super Clear UV Cut** | 20-25 °C | <60% | RH alta: blooming biancastro grave |
| **SprayMax 2K** | 18-25 °C | 50-70% | T <15°C = no cura |
| **Heat-set inserts** | 18-25 °C | qualsiasi | Pezzo freddo dopo stampa = condensa nel foro |

### Failure mode noti

- **Blooming (velo bianco)**: clear coat spruzzato con RH >65% raffredda
  per evaporazione solvente sotto dew point → condensa microscopica.
  Visibile come opacità lattiginosa. **Fix**: aspetta giorno meno umido o
  riscalda zona spruzzo a 22-24 °C.
- **Runs (gocce)**: T bassa = solvente non evapora velocemente, vernice
  scorre per gravità. **Fix**: alza T, mani più sottili.
- **Orange peel**: troppi solidi + T alta + RH bassa = vernice "schiena
  d'arancia". **Fix**: diluisci 10-15% airbrush, aumenta passate
  riducendo deposito.
- **Dust nibs**: aria mossa porta polvere. **Fix**: ventola in modalità
  bassa durante spruzzo, alta solo dopo.

---

## 9.3 Posizionamento sensori

- **1 sensore in zona spruzzo** (sopra cabina/banco, a 30-50 cm dal
  pezzo).
- **1 sensore in deposito vernici** (cassetto/scaffale dove stocchi
  bombolette/primer). Le bombolette conservate a T <5 °C hanno cattiva
  atomizzazione; quelle a T >40 °C rischio scoppio.
- **Sensore appena fuori cabina** (per confronto: differenza T interna
  vs esterna → indica capacità climatizzazione spazio).

---

## 9.4 Trick economy "Pre-warm bomboletta"

Le bombolette spray (Maximum, MaxMeyer, Pledge spray) sono molto
sensibili a T:
- <15 °C: pressione interna bassa, atomizzazione fine non parte (gocce
  grosse).
- 15-25 °C: range nominale.
- >40 °C: pressione alta, atomizzazione troppo aggressiva, rischio.

**Pre-warm**:
- Bagnetto acqua tiepida (max 35 °C, MAI acqua calda > 40 °C) per 5-10 min
  prima di spruzzare. Eleva T contenuto a ~25 °C.
- **MAI**: forno, microonde, fiamma diretta, asciugacapelli vicino
  (rischio scoppio/incendio).
- Sicurezza: leggi etichetta CLP del prodotto.

---

## 9.5 Deumidificatore DIY/economy

Se vivi in zona umida (es. costa, scantinato, garage piano terra) e
rilevi RH >70% costante:

| Soluzione | Costo | Capacità | Note |
|---|---|---|---|
| Sale grosso da cucina in barattolo aperto | €1 / kg | 50-100 g acqua/giorno per kg | per piccolo armadio attrezzi |
| Cloruro di calcio "Idrosec" | €5 / kg Brico | 300-500 g/giorno | armadio/cabina |
| Deumidificatore portatile Peltier (12V/220V) | €30-50 | 200-500 ml/giorno | piccola stanza |
| Deumidificatore compressore 12 L/giorno | €150-250 | 12 L/giorno | garage 20-30 m² |
| Aria condizionata domestica | esistente | variabile | deumidifica come effetto laterale |

**Trick maker community**: bidone graniglia silice (gel di silice
ricaricabile) €15 → 5 kg di silica gel = deumidifica una zona 1 m²
spruzzo per ~1 settimana fra rigenerazioni in forno 100 °C × 2 h.

---

## 9.6 Riscaldamento DIY in inverno

Garage in inverno = T spesso 5-15 °C → fuori range workflow.

| Soluzione | Costo | Note |
|---|---|---|
| Termoventilatore Lidl/Brico 2000 W | €15-25 | 30 min pre-riscaldo zona spruzzo |
| Pannello radiante elettrico 500 W | €30-50 | bassa convezione = NO polvere mossa, ideale |
| Lampada infrarossa 250 W (calore radiante) | €15-25 | per spot heating pezzo dopo spruzzo |
| Tubo riscaldante terrari/rettilari (12V/220V) | €15-20 | per cabina chiusa piccola |

**Trick zero spesa**: 2 ore prima della sessione, sposta cabina vicino
al termosifone domestico (se garage comunica con casa) o accendi
illuminazione LED panel intensa per riscaldare zona.

---

## 9.7 Riferimenti

- r/airbrush "humidity temperature problems":
  https://www.reddit.com/r/airbrush/search?q=humidity
- Don's Airbrush Tips environmental:
  http://www.donsairbrushtips.com/
- Wikipedia psychrometric chart (T/RH/dew point):
  https://en.wikipedia.org/wiki/Psychrometrics
- Forum auto-restorers "spray paint humidity":
  https://www.autobody101.com/forums/
- Pellet stove forum "garage humidity control":
  https://forum.pelletfuel.com/

---

## 9.8 Quick reference card (stampa e appendi in cabina)

```
   ┌───────────────────────────────────────┐
   │  CHECK PRE-SPRAY                      │
   │                                       │
   │  T zona = .... °C                     │
   │  RH zona = .... %                     │
   │                                       │
   │  T target: 18-25 °C                   │
   │  RH target: 40-60 %                   │
   │                                       │
   │  Bomboletta a temperatura?  □         │
   │  Pezzo asciutto e in temperatura? □   │
   │  Ventola estrazione ON?  □            │
   │  Maschera ABEK1 indossata? □          │
   │  Guanti nitrile? □                    │
   │                                       │
   │  Se RH > 65%: NO clear coat oggi      │
   │  Se T < 15°C: NO 2K, pre-warm tutto   │
   └───────────────────────────────────────┘
```
