# 01 — Cross-hatch tape test (ASTM D3359 versione povera)

> **TL;DR**: lametta + righello + nastro Scotch Magic = stessa informazione
> qualitativa che ti darebbe il kit Elcometer 107 (€70) + Tesa 4651 (€8/rotolo)
> nel **90% dei casi che ti interessano** come prop maker / piccolo brand.
> Project Farm style: "is it close enough for what you're doing? Yes."

Risolve **direttamente** la riga "Test cross-hatch ASTM*" in
`05_round2/E_diy_budget/02_brico_lidl_paints.md` (sezione 2.1) — i valori
3B/4B oggi sono **stime forum**, non test propri. Dopo questo test, hai dati
**tuoi** su Maximum BricoIO vs MaxMeyer vs Plasti-kote.

---

## 1.1 Cos'è davvero il cross-hatch test

ASTM D3359 (Method B, "X-cut" e "lattice") misura **l'adesione di un coating
al substrato** facendo una griglia di tagli, applicando un nastro adesivo
calibrato, strappandolo a 180°, e contando quanti quadrati si staccano.

Scala 0B-5B:
| Score | Quadrati staccati | Significato pratico |
|---|---|---|
| 5B | 0 % | Adesione perfetta. Coating si comporta come "pelle". |
| 4B | <5 % | Molto buona. Solo bordi taglio sfilacciati. |
| 3B | 5-15 % | Accettabile per uso decorativo. Sotto stress meccanico potrebbe perdere. |
| 2B | 15-35 % | Marginale. Va bene per pezzi che non si toccano. |
| 1B | 35-65 % | Insufficiente per qualsiasi uso commerciale. |
| 0B | >65 % | Fail totale. Coating si stacca a fogli. |

Spec ufficiale: https://www.astm.org/d3359-23.html

---

## 1.2 Setup laboratorio del povero — €2.50 totali

| Item | Prezzo € | Dove | Note |
|---|---|---|---|
| Lametta nuova doppio filo (Astra Superior) | 0.30 (1 lametta da pack 5 da €1.50) | farmacia, supermercato | mai usata, sterile, taglio netto |
| Righello acciaio inox 15 cm | 1.00 | Lidl, cartolibreria | acciaio rigido, NON plastica |
| Nastro Scotch Magic 19mm | 1.20 (per rotolo, dura 50+ test) | qualunque negozio | tape "trasparente opaco" classico |
| Pennello morbido (capello) | gratis | qualunque | per rimuovere polvere taglio |
| Smartphone | già hai | — | per foto macro |

**Totale netto per il test: €0.50** (lametta usa-getta + 1 striscia tape).

### Perché Scotch Magic 19mm e non altro
- **Adesione ~1.8-2.2 N/cm** (range pubblicato da 3M tech sheet) → **rientra
  nello spec ASTM 1.7-2.5 N/cm**. È letteralmente quasi un drop-in replacement
  di Tesa 4651, costa 1/6.
- **Trasparente opaco**: vedi i quadrati staccati attraverso il nastro.
- **Non è "Crystal Clear"**: quello è più aggressivo, falsa il test verso 0B.
- Tech sheet 3M Scotch Magic: cerca "3M Scotch Magic 810 TDS" su google.

⚠️ **NON usare**: nastro carta da imbianchino (adesione troppo bassa, falsi
positivi 5B), nastro pacchi marrone (troppo aggressivo), nastro elettrico
(adesivo gommoso che lascia residui).

---

## 1.3 Pattern di taglio: 6×6 quadrati 1mm

### Geometria
- **Provino**: piastrina 25×25mm o 20×40mm (vedi `08_14_day_protocol.md` per
  STL standard).
- **Griglia**: 6 tagli orizzontali + 6 verticali, spaziati **1 mm** → 25
  quadrati 1×1 mm (la cornice esterna non si conta).
- Per coating **>50 µm** (es. primer + vernice + clear coat = ~80-120 µm
  totale), ASTM richiede spacing 2 mm → 16 quadrati. Per coperture sottili
  (solo Pledge a pennello, ~20 µm) usa 1 mm.

### Dima fai-da-te
Stampa in PLA una **dima 25×25mm con 7 scanalature parallele 1mm spacing,
profondità 0.5mm**. Tempo stampa: 5 min. Usala per guidare la lametta:
1 passaggio in scanalatura → 1 taglio dritto a profondità controllata.

Disegno descritto:
```
   ┌────────────────────┐
   │ ╱ ╱ ╱ ╱ ╱ ╱ ╱      │  ← scanalature 1mm
   │                    │
   │  area di taglio    │
   │  con righello +    │
   │  lametta           │
   └────────────────────┘
```

Per la seconda serie di tagli **ruoti la dima di 90°** e ripeti.

### Procedura mani
1. Provino fermo su tavolo (nastro biadesivo sotto, NON sul coating).
2. Dima sopra, allineata al margine.
3. Lametta perpendicolare al provino, **angolo 90°**, pressione *quel tanto*
   che senti il taglio attraversare il coating senza affondare nel PLA (con
   un po' di pratica diventa muscle memory; pratica su provino "sacrificio"
   prima).
4. **6 tagli in una direzione**, poi ruota 90° e fai altri 6.
5. Spazzola via la polvere con pennello morbido (NON soffia → umidità).

---

## 1.4 Applicazione tape: 60 secondi, strappo 180°

1. Strappa una striscia di Scotch Magic **lunga ~75 mm**.
2. Centra sopra la griglia, lascia ~25 mm di "linguetta" che sporge.
3. **Premi col polpastrello pollice** sopra l'intera griglia per **60 secondi**,
   pressione costante "ferma ma non bianca delle nocche". ASTM dice "press
   firmly" — uno standard meglio è **usare il retro di una matita** facendo
   3 passate avanti-indietro.
4. Aspetta altri **30 secondi** (i polimeri adesivi devono "flow" e
   massimizzare contatto).
5. **Strappo a 180°**: prendi la linguetta, piegala indietro sopra sé stessa
   parallela al provino, **strappa in 0.5-1 secondo con un movimento netto**.
   - NON tirare a 90°: falsa il test verso 5B.
   - NON tirare lento: falsa verso 0B.

### Calibrazione "pressione strappo"
Se vuoi essere più scientifico: lega un peso di **500 g** (bottiglia acqua
0.5L) al capo del nastro, lascia cadere dal bordo del tavolo. Il peso fa
il pull a velocità riproducibile. Costo extra: €0.

---

## 1.5 Scoring: foto + griglia overlay

### Documentazione foto
1. **Smartphone macro mode**, distanza 8-10 cm.
2. **Luce radente** da una lampada da scrivania a 45° (rivela imperfezioni
   meglio della luce frontale).
3. **WB manuale**: imposta "Daylight 5500K" o usa modalità Pro RAW (vedi
   `09_pitfalls_and_controls.md` § WB).
4. Includi sempre un **riferimento dimensionale** nel frame (righello o coin).

### Conta quadrati staccati
Apri foto in Photoshop / GIMP / smartphone Photos app, **overlay griglia**
6×6 sopra l'immagine. Conta i quadrati che hanno >50% di coating mancante.

Score:
```
% staccato = (quadrati persi / 25) × 100
0 %       → 5B
< 5 %     → 4B (max 1 quadrato)
5-15 %    → 3B (2-4 quadrati)
15-35 %   → 2B (4-9 quadrati)
35-65 %   → 1B (9-16 quadrati)
> 65 %    → 0B (> 16 quadrati)
```

---

## 1.6 Confronto con "vero" ASTM

| Aspetto | ASTM ufficiale | Versione povera | Delta |
|---|---|---|---|
| Cutter | Elcometer 107 €70 | Lametta + dima €1.30 | Lametta meno costante ma OK con pratica |
| Tape | Tesa 4651 €8/rotolo | Scotch Magic €1.20 | Adesione 1.8 vs 2.0 N/cm (~entrambi in range) |
| Pressione applicazione | "press firmly" (soggettivo anche in ASTM) | retro matita ×3 | Equivalente |
| Strappo | manuale o tester | manuale | Equivalente |
| Lente | 10x | smartphone macro 5x + zoom digitale | Sufficiente per quadrati 1mm |
| Risultato | score 0B-5B | score 0B-5B | **stessa risoluzione decisionale** |

**Verdetto**: il vero costo del cross-hatch ASTM ufficiale non è il
risultato in più — è la **riproducibilità tra laboratori** (certificazione
ISO 17025). Per uso interno comparativo, la versione povera dà gli stessi
ranking.

---

## 1.7 Esempio test matrix (vai a `07_excel_template_radar.md`)

| Trattamento | Score atteso |
|---|---|
| PLA nudo + Pledge | 1B-2B (Pledge non aderisce a PLA non primerizzato) |
| Maximum BricoIO solo | 2B-3B (atteso da R2-E) |
| MaxMeyer Primer + Maximum | 4B (atteso da R2-E) |
| MaxMeyer Primer + MaxMeyer Acrilico | 4B-5B (atteso) |
| Plasti-kote Super Primer + Maximum | 4B-5B (atteso) |
| Saratoga water-based + Pledge | 3B (atteso) |

Numeri "attesi" sono ipotesi da R2-E forum-derived: **lo scopo del test è
verificarli o smentirli**.

---

## 1.8 Bias e limiti (sii onesto)

1. **Pressione lametta non calibrata**: pratica 5-10 tagli su provino
   sacrificio prima. Senti la "soglia" giusta.
2. **Curvature**: il test funziona solo su superfici piatte. Per pezzi
   curvi, stampa **un provino piatto applicando lo stesso trattamento dello
   stesso lotto**.
3. **Temperatura coating**: testa a 20-22°C. A 10°C molti acrilici sono
   più fragili → falsi 1B.
4. **Tempo cura**: 7 giorni minimo. Pledge a 3 giorni dà 2B; a 14 giorni
   dà 4B (cura continua).
5. **Operatore**: lo stesso operatore in una sessione. Il "tuo" 4B può
   essere il "mio" 3B. Per validation cross-operator → fai testare a un
   amico cieco rispetto ai trattamenti.

---

## 1.9 Tempo & costo riassunto

- **Setup**: 10 min (stampa dima + raccolta materiali).
- **Per provino**: 5 min taglio + 90 sec applicazione tape + 30 sec strappo
  + 2 min foto = **~9 min/provino**.
- **6 trattamenti × 2 repliche**: ~110 min totali.
- **Costo materiali test**: €2.50.

**Confronto R2-A protocollo**: €70-100 strumenti, stessa info. **Saving:
97%**. Stessa decisione finale.

---

## 1.10 Fonti

- ASTM D3359-23: https://www.astm.org/d3359-23.html (spec ufficiale, $50 ma
  riassunti pubblici su molti blog vernici).
- ISO 2409 equivalente EU: https://www.iso.org/standard/72524.html
- 3M Scotch Magic Tape 810 TDS: https://multimedia.3m.com/mws/media/66235O/3m-scotch-magic-tape-810.pdf
- Project Farm "Best Spray Paint" methodology: https://www.youtube.com/@ProjectFarm
- Reddit r/coatings cross-hatch DIY thread: https://www.reddit.com/r/coatings/
- Forum prop maker IT, cross-hatch fai-da-te: https://www.modellismopiu.net/
