# 04 — Protocollo di test misurabile: clear coat su PLA

Protocollo pratico replicabile in casa per **misurare** (non solo "sentire") la differenza tra clear coat su PLA verniciato. Riferito ai punti 22-25 di `02_painting_and_primers/_next_questions.md` e punto 1/5 di `04_sealing_presentation/_next_questions.md`.

> Obiettivo: in **~6 settimane** ottenere dati quantitativi su tape adhesion, scratch, yellowing UV, water bead, heat sag, per **5 trattamenti** comparativi. Output: tabella vincitori/perdenti + raccomandazione operativa.

---

## 1. Provini — stampa

### Geometria
- **Rettangolo piatto 20 × 40 × 3 mm**.
- Top surface: orientato verso l'alto in stampa, layer height 0.16 mm (riferimento commerciale tipico).
- 1 superficie "verniciata" (top), 1 "naturale" (bottom, da non toccare per riferimento).
- File CAD: 1 STL parametrico, una passata di stampa.

### Filamento
- **Bambu PLA Basic White (10100)** o **Polymaker PolyLite PLA White** — bianco puro per visibilità yellowing.

### Quantità
- **30 provini** identici.
- 6 trattamenti × 5 repliche (necessario per significatività statistica minima).

### Tempo stampa
- ~4 ore totali su A1 (provini stampati 6 per piatto, 5 piatti).
- Costo filamento: ~2-3 €.

---

## 2. Trattamenti (6 condizioni)

| ID | Trattamento | Note |
|---|---|---|
| **T0** | PLA nudo, nessuna vernice (controllo negativo) | Baseline degradazione PLA |
| **T1** | Primer Tamiya White + bianco Tamiya TS-26 (controllo positivo, no clear coat) | Mostra cosa fa la vernice da sola |
| **T2** | T1 + Mr. Super Clear UV Cut Flat (2 mani) | Riferimento hobby UV |
| **T3** | T1 + Krylon UV-Resistant Clear Gloss (2 mani) | Alternativa consumer |
| **T4** | T1 + SprayMax 2K Clear Glamour Gloss (3 mani, mist-medium-wet) | Premium 2K |
| **T5** | T1 + Pledge Floor Care (3 mani pennello / dip) | Controllo "economico" |

Stesso primer, stesso bianco, stesso operatore, stessa giornata di applicazione, stessa T/umidità (registrare).

### Tempo cura prima dei test
- **7 giorni** (168 h) a 20-22 °C, 40-60 % RH, **al buio**. Sufficiente per cura primaria di tutti i prodotti (2K incluso); il 2K continua per settimane, ma 7 gg è la soglia di "spedibilità" reale.

---

## 3. Test #1 — Tape adhesion (ASTM D3359 Method B / ISO 2409)

### Equipaggiamento
- **Cross-hatch cutter** dedicato (Elcometer 107, ~70 €) OPPURE **bisturi + righello + dima** (3 mm spacing per spessori <50 µm). DIY rispetta ASTM se la dima è precisa.
- **Nastro adesivo standard ASTM**: 3M 250 / Permacel P-99 / Tesa 4651. **Critico**: il nastro deve avere adesione nota (1.7-2.5 N/cm). Tesa 4651 disponibile in IT.
- Lente d'ingrandimento 10x.

### Procedura
1. Effettuare 6 tagli paralleli + 6 tagli perpendicolari (griglia 5 × 5 mm con 6 linee → 25 quadrati di 1 mm² se spacing 1 mm; per coating spessi 50-125 µm usare 2 mm spacing → 16 quadrati).
2. Spazzolare via i frammenti con pennello morbido.
3. Applicare striscia di nastro 75 mm sopra la griglia, premere con dito per 90 secondi.
4. Strappare a **180°** in 0.5-1 secondo.
5. Esaminare con lente: contare quanti quadrati si sono staccati.

### Score ASTM D3359
| Score | Descrizione |
|---|---|
| 5B | 0 % staccato — adesione perfetta |
| 4B | <5 % staccato |
| 3B | 5-15 % staccato |
| 2B | 15-35 % staccato |
| 1B | 35-65 % staccato |
| 0B | >65 % staccato — fail |

### Output atteso
- T0: N/A (nessuna vernice).
- T1-T3: 4B-5B atteso.
- T4: 5B atteso.
- T5: 3B-4B atteso (Pledge è poco adesivo).

**Costo strumenti**: ~70-100 € (cutter + nastro) o ~10 € (bisturi + nastro Tesa).
**Tempo**: 30 min per 5 repliche × 6 trattamenti = 3 h test totale.

---

## 4. Test #2 — Scratch test (casa, semi-quantitativo)

### Equipaggiamento
- **Mohs hardness pencil set** (Hodax, Mitutoyo): 5-30 € set base. Punte da 2H a 9H pencil hardness ASTM D3363.
- **Alternative low-cost**:
  - Unghia (Mohs ~2.5).
  - Moneta in rame (Mohs ~3).
  - Lama acciaio (Mohs ~5.5).
  - Chiave acciaio (Mohs ~6).
  - Vetro (Mohs ~6.5).
  - Lima diamantata economica (Mohs ~9-10).

### Procedura ASTM D3363 (pencil hardness)
1. Affilare matita HB → punta cilindrica piatta (no cono, sì cilindro carta vetro 400).
2. Tenere matita a 45° sulla superficie, premere con forza fissa (~7.5 N) e spingere 6 mm.
3. Esaminare graffio: se la matita HB **non lascia segno**, salire a F, H, 2H, 3H...
4. La hardness è il **valore più alto che NON lascia segno** (gouge resistance) o **non lascia segno permanente dopo gomma** (scratch resistance).

### Output atteso
| Trattamento | Hardness attesa |
|---|---|
| T0 PLA nudo | ~F-HB |
| T1 vernice Tamiya | ~F |
| T2 Mr. Super Clear | ~F-H |
| T3 Krylon | ~HB-F |
| T4 SprayMax 2K | ~2H-3H |
| T5 Pledge | ~HB |

**Costo**: 5-30 €.
**Tempo**: 1 h totale.

---

## 5. Test #3 — UV cabinet artificiale (yellowing delta-E)

### Equipaggiamento minimo
- **Lampada UV 365 nm** (Wood-style): 15-30 € (LED 50 W tipo Amazon).
- **Lampada UV-A nail tech** (per gel manicure, 48 W LED): 25-50 € — più uniforme, copertura migliore.
- **Box di cartone foderato di alluminio** (DIY) per concentrare emissione.
- **Smartphone Pro RAW** + **ColorChecker Passport Mini** (~80-100 €) o **app gratuita "Color Grab" / "Color Picker"** (meno precisa).
- **Cartoncino X-Rite ColorChecker** (riferimento bianco/grigio): ~80 €.

### Procedura
1. Scattare foto di partenza (T=0 h) sotto luce stabile: provini + ColorChecker affiancati, distanza fissa, esposizione manuale.
2. Estrarre RAW, processare in Lightroom con **calibrazione ColorChecker** (genera profilo color).
3. Misurare valore **L\*a\*b\*** del centro di ogni provino (eyedropper Lightroom o Photoshop).
4. Esporre provini in box UV: **100 ore continue a ~5 cm dalla lampada**. Equivalenza approssimativa: 100 h UV-A 365 nm ≈ 6-12 mesi luce solare indoor [stima, **da verificare** con curva specifica della lampada].
5. Ripetere foto + misura L*a*b* ogni 20 h (T=20, 40, 60, 80, 100).
6. Calcolare **ΔE\*ab** (formula CIE 1976):
   `ΔE = sqrt((L1-L0)² + (a1-a0)² + (b1-b0)²)`

### Interpretazione ΔE
- ΔE < 1 → invisibile a occhio.
- ΔE 1-2 → visibile a confronto diretto.
- ΔE 2-5 → chiaramente visibile.
- ΔE > 5 → cambio colore evidente.

### Output atteso
| Trattamento | ΔE @ 100 h |
|---|---|
| T0 PLA nudo | 5-15 (ingiallimento forte) |
| T1 vernice senza clear | 3-8 (la vernice protegge in parte) |
| T2 Mr. Super Clear UV Cut | 1-3 |
| T3 Krylon UV-Resistant | 1-4 |
| T4 SprayMax 2K | <1-2 |
| T5 Pledge | 3-7 (no UV protection) |

**Costo**: 100-150 € (lampada + ColorChecker se non si ha).
**Tempo**: 100 h calendario (4 giorni 24/24) + 1 h fotografia + 2 h analisi.

---

## 6. Test #4 — Water bead angle / idrofobicità

### Equipaggiamento
- **Smartphone con macro mode** o **clip macro 10x** (10-20 €).
- **Pipetta micropipetta** o **siringa insulina** (gocce ~5-10 µl).
- **Goniometro digitale gratuito**: app "Protractor" o software desktop **ImageJ** (https://imagej.net) gratuito.
- **Treppiede smartphone** per stabilità (15-30 €).

### Procedura
1. Provino orizzontale su tavolo piano.
2. Depositare goccia 5 µl acqua deionizzata al centro.
3. Fotografare di profilo (smartphone all'altezza del piano) entro 5 secondi.
4. Importare immagine in ImageJ, plugin "Drop Shape Analyzer" (DSA).
5. Misura angolo di contatto.

### Interpretazione
- < 30° = idrofilo (acqua si spande)
- 30-90° = parzialmente idrofobo
- 90-120° = idrofobo
- > 120° = superidrofobo

### Output atteso
- T0 PLA nudo: 70-80°
- T1 vernice: 75-90°
- T2-T3 lacca: 80-95°
- T4 SprayMax 2K: 90-105° (PU naturalmente idrofobo)
- T5 Pledge: 70-85°

**Costo**: 30-50 € (treppiede + clip macro).
**Tempo**: 1 h totale.

---

## 7. Test #5 — Heat resistance (auto d'estate)

### Equipaggiamento
- **Termometro digitale con sonda K-type** (10-25 €).
- **Auto al sole** estate (cruscotto, scuro, parcheggiato 4 ore in pieno sole) — temperatura ambiente realistica 50-70 °C.
- **Alternativa controllata**: **forno cucina** termoregolato (verifica con termometro: forno casa è precisione ±10 °C) a 50 °C e 60 °C, 4 h.

### Procedura
1. Misurare planarità iniziale provino (riga + sentirne deflessione, oppure proiettore laser su piano).
2. Esporre 4 h a 50 °C, 4 h a 60 °C (giorni separati per evitare cumulazione).
3. Ispezionare:
   - Deflessione visibile? (PLA Tg 60 °C → bordi piegano)
   - Cambio finish (matte → satin per softening superficiale)?
   - Imprinting (appoggiato su qualcosa lascia segno)?
   - Tackiness (appiccicaticcio)?
4. Dopo raffreddamento, ripetere test scratch.

### Output atteso
- T0/T1: deformazione a 60 °C, fingerprint imprinting facile.
- T2/T3/T5: il clear coat aiuta marginalmente, ma è il PLA il limite (Tg 60).
- T4 SprayMax 2K: il clear ha Tg ~75-85 °C, **resiste meglio in superficie ma il PLA sotto cede comunque**. Conferma il punto chiave: **il 2K non rende il PLA indistruttibile termicamente**.

**Costo**: 25 € (termometro).
**Tempo**: 2 giorni reali.

---

## 8. Test #6 — Chemical resistance (opzionale)

### Equipaggiamento
- Cotone fioc + cronometro + solventi:
  - Acqua, IPA 70 %, etanolo 96 %, benzina (litri carburante), olio motore, detergente casa.

### Procedura
1. Cotton swab impregnato → posato 30 sec → ruotato 10 colpi → rimosso → asciugato.
2. Ispezione visiva: opacità, lifting, lifting completo.

### Output atteso
- T2/T3 lacca: alcol e benzina opacizzano sensibilmente.
- T4 2K: resiste a tutto eccetto solventi clorurati (non testati a casa).
- T5 Pledge: si scioglie con acqua calda.

**Costo**: ~5 € (materiali già in casa).
**Tempo**: 30 min.

---

## 9. Tempistica complessiva

| Fase | Tempo calendario | Tempo attivo |
|---|---|---|
| Stampa provini | 1 giorno | 30 min |
| Applicazione trattamenti | 1 giorno | 4 h |
| Cura 7 giorni | 7 giorni | 0 |
| Test adhesion + scratch | 1 giorno | 4 h |
| Test UV cabinet | 4-5 giorni continui | 3 h |
| Test water bead | 1 giorno | 1 h |
| Test heat | 2 giorni | 1 h |
| Test chimico | 0.5 giorni | 30 min |
| Analisi + tabella | 2 giorni | 4 h |
| **TOTALE** | **~20-25 giorni** | **~17-18 h attive** |

---

## 10. Bill of materials

| Voce | Costo (€) | Note |
|---|---|---|
| Filamento PLA bianco | 3 | Bambu/Polymaker |
| Primer Tamiya White | 12 | 1 bomboletta |
| Bianco Tamiya TS-26 | 10 | 1 bomboletta |
| Mr. Super Clear UV Cut Flat | 16 | 1 bomboletta |
| Krylon UV-Resistant Clear | 12 | 1 bomboletta |
| SprayMax 2K Clear | 25 | 1 bomboletta |
| Pledge Floor Care | 10 | 1 bottiglia |
| Cross-hatch cutter Elcometer | 70 | Opz. → 10 € bisturi+Tesa |
| Nastro Tesa 4651 | 8 | |
| Mohs pencil set | 25 | Opz. → unghie/monete |
| Lampada UV 365 nm 50 W | 25 | |
| ColorChecker Passport Mini | 90 | Opz. → app gratuita |
| Clip macro smartphone | 15 | |
| Termometro sonda K | 15 | |
| ImageJ software | 0 | Free |
| **TOTALE realistico (full kit)** | **~340 €** | |
| **TOTALE minimo (DIY low-cost)** | **~120 €** | senza Elcometer/ColorChecker/Mohs |

Output atteso: una **tabella 6 × 5** (trattamenti × test) che permette decisione informata su quale clear coat usare per quale caso d'uso, con dati propri. Materiale ottimo per **content marketing** del brand (blog post, IG carousel "I tested 5 clear coats on PLA").

---

## 11. Fonti e standard

- ASTM D3359 Tape Adhesion: https://www.astm.org/d3359-23.html
- ASTM D3363 Pencil Hardness: https://www.astm.org/d3363-22.html
- ISO 2409 Cross-cut test: https://www.iso.org/standard/72524.html
- CIE Delta E 1976/2000: https://en.wikipedia.org/wiki/Color_difference
- ImageJ Drop Shape Analysis plugin: https://imagej.net/plugins/dropsnake
- Elcometer test instruments: https://www.elcometer.com
- ColorChecker Passport Mini: https://calibrite.com/product/colorchecker-passport-photo-2/
- Test protocol references — Reddit r/coatings, r/Detailing test threads.
- YouTube channel "Project Farm" — protocollo casalingo di test comparativi, ottima ispirazione metodologica.
