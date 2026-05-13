# 02 — Δ-E yellowing test con smartphone + ColorChecker DIY

> **TL;DR**: una stampa A4 di ColorChecker su carta fotografica (€0.50) + app
> ColorMeter gratuita + lampada UV-A 365nm Aliexpress (€15-20) replicano
> abbastanza bene la metodologia di una camera UV da €5000 per **rank-ordering**
> di clear coat. NON sostituisce un colorimetro Datacolor in valori assoluti,
> ma **basta per decidere quale clear coat ingiallisce meno**.

Risolve la riga "Yellowing 12 mesi" in `INDEX.md` gap #2 e la riga
"ColorChecker Passport Mini €90" del protocollo R2-A. Decide tra Pledge,
MaxMeyer trasparente, Mr.Super Clear UV Cut, Vallejo Polyurethane, generic
Aliexpress.

---

## 2.1 ColorChecker DIY: stampa & uso

### Cos'è il ColorChecker
24 patch di colore standard X-Rite/Calibrite (originale "Macbeth ColorChecker"
1976). Servono come **riferimento di calibrazione colore**: scatti foto +
ColorChecker nel frame, software usa i valori L*a*b* noti dei 24 patch per
correggere il color profile della tua specifica foto.

### Scarica file
- **PDF/TIFF originale X-Rite 24-patch L*a*b* values**:
  https://xritephoto.com/documents/literature/en/colordata-1p_en.pdf
  (questo è il documento con i valori L*a*b* di riferimento dei 24 patch).
- **Immagine SVG/PNG riproduzione esatta** (community, valori sRGB
  approssimati per stampa):
  https://en.wikipedia.org/wiki/ColorChecker (file "ColorChecker_chart.svg")
- **Babelcolor whitepaper con dati spettrali completi**:
  https://babelcolor.com/index_htm_files/ColorChecker_RGB_and_spectra.xls
- **Repo GitHub "fake" ColorChecker pronto da stampare**:
  cerca "ColorChecker print pdf" su GitHub, varie repo es.
  https://github.com/colour-science/colour (libreria scientifica Python con
  reference)

### Stampa
- **Stampante inkjet con carta fotografica glossy 200 g/m²** (€10/risma 20 fogli
  alla Coop, Esselunga, MediaWorld).
- Impostazioni stampante: **profilo sRGB**, NO "vivid colors", NO "auto
  enhancement". Disattiva qualsiasi profile attivo, usa "match printer".
- Risultato: ColorChecker A4 con 24 patch ~30×30mm ciascuno.

### Limiti onesti del ColorChecker DIY
- **Inchiostri inkjet ≠ pigmenti X-Rite**. Saturazione e gamut diversi.
  → **Non usare per calibrazione assoluta**, ma OK per **differenza relativa
  tra foto T0 e Tn dello stesso pezzo nella stessa scena**.
- **Sbiadisce in luce**: tieni il tuo print in busta scura quando non lo usi.
  Sostituiscilo ogni 3 mesi (€0.50).
- **Aggiungi 1 patch personalizzato**: ritaglia un quadrato di **carta bianca
  ufficio Fabriano Copy** — riferimento "puro" più stabile dell'inkjet
  cromatico.

### Alternative se vuoi spendere un po' di più
| Item | Prezzo | Pro |
|---|---|---|
| Datacolor SpyderCheckr 24 | €60 | Pigmenti veri, dura anni, riferimento accurate |
| Calibrite ColorChecker Passport Mini | €90 | Standard industria foto |
| **ColorChecker DIY inkjet** | €0.50 | "Good enough" per rank-ordering |

---

## 2.2 App di misura colore (smartphone)

### Android
- **Spectrum** (free): https://play.google.com/store/apps/details?id=com.dewinneraar.spectrumlive
  Legge colore al centro di un mirino, restituisce RGB e converte a HSV/HSL.
- **Color Grab** (Loomatix): https://play.google.com/store/apps/details?id=com.loomatix.colorgrab
  Free, legge L*a*b* direttamente. **CONSIGLIATO**.
- **Photochrom Color Picker**: meno preciso ma free.

### iOS
- **ColorMeter Free** (Variable): https://apps.apple.com/it/app/colormeter-free/id539898384
  Free version legge HEX/RGB; pro version (€2) legge L*a*b*.
- **Pantone Connect** (free tier): https://www.pantone.com/connect

### Fallback "no app": Lightroom Mobile + eyedropper
1. **Adobe Lightroom Mobile** (free, account gratuito):
   https://lightroom.adobe.com/
2. Importa foto, usa lo **strumento Color Picker** sopra un patch ColorChecker
   → legge RGB, converti a L*a*b* con formula o web calculator:
   http://colormine.org/convert/rgb-to-lab

### Calibrazione "manuale" delle letture
1. Fotografa ColorChecker DIY in scena fissa.
2. Usa app per misurare il **patch grigio 18%** (riga 4 col 4 del ColorChecker).
3. Confronta con valore atteso L*=50 ±2.
4. **Delta è il tuo "errore di scena"**. Sottrailo da tutte le misure dei
   provini in quella sessione.

---

## 2.3 Protocollo lampada UV-A 365nm

### Hardware
- **Lampada UV-A 365nm 50W LED Aliexpress**: €15-25.
  Esempio: https://it.aliexpress.com/item/1005005xxx — cerca "UV 365nm 50W
  black light LED" (es. brand Lemonbest, Hovermars, ricerca generica).
- **Alternativa**: lampada per gel manicure 48W UV LED (€20-30 Amazon IT).
  Cerca: https://www.amazon.it/s?k=lampada+uv+365nm+led
- **Box DIY**: scatola da scarpe foderata di alluminio (€0, hai in casa).

⚠️ **Sicurezza UV-A**: NON guardare direttamente la lampada, NON tenere
mani sotto >5 min ininterrotti. Occhiali "blue blocker" comuni (€5) o
occhiali da saldatura (€8 Brico) bastano. Coperchio box chiuso = problema
risolto.

### Camera invecchiamento "vera" vs DIY
| Strumento | Costo | Spectrum | Riproducibilità |
|---|---|---|---|
| Atlas Ci4000 Weather-Ometer | €30-50k | xenon arc full spectrum, T/RH controlled | scientifica |
| QUV Q-Lab cabinet | €15-25k | UV-A 340/313 fluorescent | scientifica |
| **Lampada UV-A 365nm Aliexpress + box** | €20 | UV-A puro, T ambiente | qualitativa, **rank-ordering OK** |

**Il DIY non ti dà "100h UV = 6 mesi sole reale"**. Ti dà: dopo X ore tutti i
provini sono nella stessa scena UV, **chi ingiallisce meno vince**.

### Esposizione 100h
- **100 ore continue** ≈ ~4 giorni di notte (lampada accesa h21-h08 in box
  chiuso, off di giorno) + qualche giornata extra. Programma con presa
  timer Aliexpress €5.
- O **100h continue weekend** se hai stanza dedicata.
- Provini a **5 cm dalla lampada** (irradiance max).
- Mantieni **T <30°C** nel box (apri ogni 12h, o ventola PC 12V €3 in
  parallelo). Se la T sale a 50°C, il PLA distorce e perdi il test.

### Snapshot intermedi
T = 0h, 25h, 50h, 75h, 100h → 5 punti dati per provino.

---

## 2.4 Calcolo Δ-E CIE76 (formula manuale)

### Formula
```
ΔE*ab = √[(L₂-L₁)² + (a₂-a₁)² + (b₂-b₁)²]
```

dove:
- L₁, a₁, b₁ = misure a T=0h
- L₂, a₂, b₂ = misure a T=Xh

### Interpretazione percettiva
| ΔE | Visibilità |
|---|---|
| < 1 | Invisibile a occhio non allenato |
| 1-2 | Visibile solo in confronto diretto fianco-a-fianco |
| 2-3.5 | Visibile in osservazione normale |
| 3.5-5 | Ovvio, "il colore è diverso" |
| > 5 | Cambio colore evidente, "è marrone, non bianco" |

Note: CIE76 è la formula "vecchia" — moderna è CIEDE2000, più accurata ma
più complessa. **CIE76 basta per rank-ordering**. Riferimento:
https://en.wikipedia.org/wiki/Color_difference

### Excel template (vedi `07_excel_template_radar.md` per file completo)
```
        L0      a0      b0      L100   a100   b100   ΔE
T_PLA   89.2   -0.5    +2.1    78.4   +1.2   +12.8  14.9
T_Pled  88.7   -0.3    +1.8    82.1   +0.8   +8.5    9.5
T_Max   88.9   -0.4    +1.9    87.5   -0.2   +3.2    1.9
T_SC    89.0   -0.4    +1.8    88.6   -0.3   +2.1    0.6
```
*Esempio fittizio* — numeri inventati per dimostrare il template. **NON usare
come dati reali**.

Formula Excel cella ΔE: `=SQRT((E2-B2)^2+(F2-C2)^2+(G2-D2)^2)`

---

## 2.5 Procedura passo-passo (sessione misura)

### Setup scena foto fissa
1. **Luce stabile**: lampada LED scrivania CRI ≥80 (€15 Ikea Tertial / Lidl),
   sempre stessa posizione e angolo.
2. **Sfondo grigio neutro** (cartoncino A4 Brico €1).
3. **Smartphone fisso** su treppiede o sopra una pila di libri marcata con
   nastro adesivo.
4. **WB manuale**: app Pro RAW / Open Camera (Android free) / Halide (iOS).
   Imposta 5500K, blocca esposizione.
5. **No flash**, no HDR auto, no Night mode.

### Per ogni provino, per ogni snapshot
1. Posa provino + ColorChecker DIY + un "patch bianco" affiancati.
2. Scatta foto in **RAW** se possibile (DNG), altrimenti JPG max quality.
3. Apri foto.
4. Misura con app il **centro del provino** (zona 5×5mm, NON i bordi).
5. Misura il **patch grigio 18% del ColorChecker** → calibrazione (vedi §2.2).
6. Trascrivi L*a*b* in Excel.

### Note importanti
- Stessa **distanza smartphone-provino** ogni volta (segna sul treppiede).
- Stessa **ora del giorno** se hai luce da finestra (preferibile spegnere
  finestre, lavorare di sera).
- **NON spostare il provino sopra ColorChecker**: foto fianco a fianco.

---

## 2.6 Trattamenti consigliati (test matrix)

| ID | Trattamento | Costo/pezzo | Da R2-* |
|---|---|---|---|
| T0 | PLA Bambu Basic White, nudo | €0 | controllo negativo |
| T1 | Pledge / Glassex 2 mani pennello | €0.03 | R2-E §7.3 |
| T2 | MaxMeyer Smalto Trasparente Lucido spray | €0.30 | R2-E §2.1 |
| T3 | Mr. Super Clear UV Cut Flat | €0.50 | R2-A §3 |
| T4 | Plasti-kote spray clear | €0.30 | R2-E §7.5 |
| T5 | Pledge + 1 mano Mr.Super Clear UV Cut top | €0.53 | combo R3 |

**Ipotesi**: T3 e T5 dovrebbero vincere (UV cut additivi). T0 e T1 dovrebbero
ingiallire più velocemente. T2 e T4 in mezzo. **Il test ti dice chi ha
ragione**.

---

## 2.7 Bias riconosciuti

1. **Smartphone camera ≠ colorimetro spettrale**. Errore tipico ±2-3 L*a*b*
   units. **OK per ΔE > 3** (decisione visibile), **noise per ΔE < 1**.
2. **Inchiostri ColorChecker DIY si degradano** insieme ai provini sotto
   UV. Soluzione: ColorChecker fuori dal box UV, usalo solo durante le foto.
3. **Spectrum app legge il display calibrato dello smartphone**, non lo
   spettro reale. Calibra ogni sessione (§2.2).
4. **100h UV-A 365nm ≠ 12 mesi sole reale**. Sole reale include UV-B (più
   distruttivo, filtrato da vetri), IR (riscalda), umidità, ossigeno
   ozonizzato. La tua lampada è SOLO 365nm.
5. **PLA degrada anche al buio** (idrolisi lenta). Tieni T0 controllo
   "buio" + T0 controllo "luce" per stimare baseline shift.

---

## 2.8 Tempo & costo

- **Setup hardware**: €20 (lampada UV) + €0.50 (carta fotografica) + €5 (timer)
  + €1 (cartoncino) = **€26.50** (riusabile per decine di test).
- **Per sessione misura**: 30 min (foto + measure + Excel).
- **Test completo 6 trattamenti × 5 snapshot**: ~150 min misure + 100h calendar.

**Confronto R2-A**: lì ColorChecker Passport Mini €90 + ImageJ. Saving 70%,
**stesso ranking** atteso. Trade-off: precisione assoluta sacrificata, ma
non ne hai bisogno.

---

## 2.9 Fonti

- X-Rite ColorChecker reference values:
  https://xritephoto.com/documents/literature/en/colordata-1p_en.pdf
- BabelColor ColorChecker spectral data:
  http://www.babelcolor.com/colorchecker.htm
- CIE Delta E wiki: https://en.wikipedia.org/wiki/Color_difference
- ColorMine RGB→L*a*b* online calculator: http://colormine.org/convert/rgb-to-lab
- Color Grab Android: https://play.google.com/store/apps/details?id=com.loomatix.colorgrab
- ColorMeter iOS: https://apps.apple.com/it/app/colormeter-free/id539898384
- Adobe Lightroom Mobile: https://lightroom.adobe.com/
- Project Farm UV test method (channel): https://www.youtube.com/@ProjectFarm
- Reddit r/coatings yellowing DIY: https://www.reddit.com/r/coatings/
- ColourScience.com (rigorous foundation): https://www.colour-science.org/
