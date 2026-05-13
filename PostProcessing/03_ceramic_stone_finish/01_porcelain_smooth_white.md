# 01 — Porcellana liscia bianca lucida su PLA (Bambu A1)

> Obiettivo: superficie tipo **statuetta porcellana bianca**, perfettamente liscia, riflesso satinato/lucido controllato, **layer lines invisibili**. Tutto **cold-cure** (PLA Tg ~55-60 °C: niente calore, niente forno).

---

## 1. Constraint critico: PLA non si cuoce
- **Tg PLA ≈ 60-65 °C** → sotto carico inizia a deformare già a 45-50 °C ([Makershop](https://makershop.co/what-temperature-can-pla-withstand/)).
- **NO**: forno, kiln, heat gun ravvicinato, lampada infrarossi vicina, asciugatura al sole estivo.
- **SI**: stufa di casa lontana, ventilazione forzata fredda, deumidificatore, UV (se UV-only LED, freddi).
- Epoxy resin che cura: scegliere formule **slow-cure / low-exotherm** (XTC-3D è formulato per PLA proprio per questo). Vedere `04_glazed_glossy_finish.md`.

---

## 2. La gerarchia del "porcelain effect"
Esistono 3 vie distinte:

| Via | Look | Difficoltà | Costo | Resistenza |
|-----|------|------------|-------|------------|
| **A. Filler primer + sanding + satin white + clear satin** | Porcellana realistica | Media | Basso (€15-30) | Ottima |
| **B. Gesso multistrato + sanding + acrilico bianco + Pledge** | Eggshell porcellanato, opaco-lucido | Bassa | Bassissimo (€10-20) | Media (Pledge protegge) |
| **C. XTC-3D / epoxy coat + sanding + bianco + 2K clear** | Vetroso, "glazed porcelain" | Alta | Alto (€40-80) | Eccellente |

La **via A** è il workflow di riferimento per FDM. La **B** è la "scorciatoia da pittore" (gesso = bianco di partenza). La **C** scivola verso "glazed" — vedere `04_glazed_glossy_finish.md`.

---

## 3. Workflow A — Filler primer pro (RECIPE RACCOMANDATA)

### Materiali
| Step | Prodotto | Marca/Modello | Dove |
|------|----------|---------------|------|
| Sanding | Carta abrasiva 220/400/600/800/1000 wet&dry | 3M / Mirka | Brico, Amazon IT |
| Primer/filler | Filler Primer Grey 400ml | **Rust-Oleum Filler Primer** (ATO-50) | Leroy Merlin, Amazon IT (€10-14) |
| Primer alt. EU | Plastic Primer | **U-POL Power Can High Build** | Amazon IT |
| Sealer fine | Surface Primer White 17ml/200ml | **Vallejo / AK Interactive** | Hobbyshop |
| White base | Satin White spray | **Montana Gold Shock White Pure** o **Tamiya TS-26** | Amazon, hobby |
| Clear coat | Acrylic Satin Varnish | **Mr. Hobby Premium Topcoat Semi-Gloss** o **Vallejo Mecha Satin Varnish** | Hobbyshop |

### Step-by-step (totale ~2-3 giorni con asciugature)

1. **Sand raw print 220 → 400 → 600** a secco, leggera pressione. Rimuove i picchi delle layer lines senza scavare valli.
2. **Filler primer coat #1**: 2-3 mani leggere (cross-coat), distanza 25-30 cm, 10 min tra mani. Sec touch ~30 min.
3. **Wet sand 400** dopo 2 h. La polvere grigia evidenzia immediatamente le imperfezioni residue. Continuare finché la superficie non è omogenea.
4. **Filler primer coat #2** (di solito sufficiente). Wet sand 600.
5. **Eventuale coat #3** localizzato sui difetti. Sand 800.
6. **Primer fine bianco** (Vallejo Surface Primer airbrush, o Tamiya Fine White spray) — 1 mano sottile. Questo è lo strato che restituisce "uniformità bianca pura".
7. **Sand 1000 a umido** SOLO per togliere puntini di polvere. Non andare sotto al primer.
8. **White satin** — 2-3 mani sottili, distanza 25 cm, 15 min tra mani. Tamiya TS-26 è la classica "porcellana finta" del modellismo statico.
9. **Clear satin coat** — Mr. Hobby Premium Topcoat Semi-Gloss (in lattina) è lo standard pro per "porcellana satinata". 2 mani molto leggere.
10. **Cura 24-48 h** prima di toccare/maneggiare. Polvere durante la cura = nemico assoluto.

### Tip pro
- **Cross-coating obbligatorio**: ogni mano in direzione perpendicolare alla precedente.
- **Mai una mano pesante**: il filler primer cola facilmente sui dettagli.
- **Test del polpastrello**: dopo wet-sanding, passare delicatamente il dito. Deve sembrare "guscio d'uovo levigato".
- **Bianco freddo vs caldo**: Tamiya TS-26 è leggermente caldo (avorio porcellanato). Per "bone china" molto bianco freddo usa **Mr. Color C62 Flat White + 5% C1 White** airbrush.

Fonti: [Tangible Day primers](https://tangibleday.com/best-primer-for-3d-prints-recommendation-and-tips/), [All3DP painting](https://all3dp.com/2/beginner-s-guide-to-painting-3d-prints-pla-abs/), [Rust-Oleum TDS ATO-50](https://www.rustoleum.com/~/media/digitalencyclopedia/documents/rustoleumusa/tds/english/cbg/automotive/ato-50_filler_primer_tds.ashx).

---

## 4. Workflow B — Gesso multistrato (low-budget porcelain)

Il gesso acrilico **è già bianco e opaco**: copre e leviga in un solo prodotto. Liquitex e Golden sono lo standard. Il limite: si applica a pennello/airbrush, non spray, quindi richiede mano.

### Materiali
| Step | Prodotto | Note |
|------|----------|------|
| Base | **Liquitex Basics Gesso** o **Liquitex Professional Gesso** | 473ml ~€18 Amazon IT |
| Smoothing mix | **Liquitex Modeling Paste** + Gesso 1:3 | Per pre-fill grossi gap |
| White top | **Liquitex Soft Body Titanium White** o **Vallejo Model Color Dead White 70.992** | |
| Sealer | **Pledge Floor Care / Pledge Revive It** (ex Future) | Walmart/Amazon US, in EU cercare "Pledge multi-surface gloss" |

### Procedura
1. Sand 320 raw print.
2. Pennellata di gesso #1, **dilato 10-15% con acqua**. Pennellate incrociate. Asciugatura 1 h.
3. Sand 400 leggero a secco — il gesso "frigge via" e leviga.
4. Coat gesso #2, ancora più diluito. Sand 600.
5. Coat #3 NON diluito, applicato con pennello piatto morbido o airbrush → 3 mani sottili.
6. Sand 800/1000 wet. La superficie ora è **eggshell**: matte bianco, soft-touch.
7. (Opz.) **Top coat Pledge Floor Care**: 1 mano pennellata → asciuga in self-leveling 30 min. Restituisce il "lucido porcellana" iconico dei miniaturisti.

### Vantaggi
- Costa <€20 totale.
- Si lavora a pennello su pezzi piccoli.
- Pledge dà un riflesso "ceramica satinata" molto convincente e si toglie con ammoniaca se sbagli.

Fonti: [Make: Gesso 3D prints](https://makezine.com/article/digital-fabrication/3d-printing-workshop/using-gesso-to-prime-your-parts-cheaply/), [Pledge floor care trick](https://miniaturewargaming.com/blog/future-floor-wax-now-pledge-floor-care/), [Just Paint acrylics](https://justpaint.org/hand-painting-3d-prints-with-acrylics/).

---

## 5. Trick avanzato: "kaolin slurry" / porcelain-effect paint

Esistono pitture che asciugando lasciano **micro-cristalli che simulano la glassa porcellana**:

- **Pebeo Porcelaine 150** ([Amazon](https://www.amazon.com/Pebeo-Porcelaine-150-Ceramic-Paint/dp/B004O7A8VG)) — water-based, lucida, formulata per imitare smalto ceramico. **Problema**: normalmente richiede cottura a 150 °C → **NON usabile su PLA**. Si può applicare senza cottura ma perde resistenza meccanica (rimane decorativa).
- **Pebeo Ceramic enamel effect** ([Amazon](https://www.amazon.com/PEBEO-Ceramic-Enamel-Effect-Bottle/dp/B0096MR4NE)) — oil-based alkyd, **air-dry**, finitura smaltata high-gloss. Compatibile PLA. 45 ml ~€7.
- **Pebeo Fantasy Moon** — pearlescent texture, more "marbled porcelain" che bianco puro.

**Workflow con Pebeo Ceramic enamel (air-dry)**:
1. Filler primer + sand 800 (come workflow A).
2. Mano sottile bianca acrilica (Vallejo).
3. **Pebeo Ceramic White** a pennello, in 2 mani sottili, 24 h asciugatura tra mani.
4. Cura totale 8 giorni a temperatura ambiente (no UV diretto).
5. NO clear coat sopra — il Pebeo è già self-leveling con finitura smaltata.

Limite: Pebeo air-dry non resiste a graffi profondi né a lavaggio frequente. Buono per **pezzi estetici da display**.

Fonti: [Pebeo product line](https://www.amazon.com/pebeo-ceramic-paint/s?k=pebeo+ceramic+paint).

---

## 6. Tabella confronto bianchi
| Prodotto | Tono | Finitura raw | Costo | Resistenza |
|----------|------|--------------|-------|------------|
| Tamiya TS-26 Pure White | Bianco neutro | Gloss | €10/spray | Buona, classico modellismo |
| Montana Gold Shock White Pure | Bianco freddo | Satin | €6/spray | Media |
| Vallejo Surface Primer White 73.600 | Bianco neutro | Matte | €8/200ml | Buona (airbrush) |
| Liquitex Gesso white | Avorio caldo | Matte ruvido | €18/473ml | Solo come base |
| Pebeo Ceramic White | Bianco-avorio | High gloss smaltato | €7/45ml | Decorativa |
| Mr. Hobby C62 Flat White | Bianco puro | Matte profondo | €4/10ml | Eccellente (con clear) |

---

## 7. Cosa evitare assolutamente
- **Smalti a olio** spessi → non aderiscono bene a PLA non primerizzato, restano gommosi.
- **Pittura "lavabile" da pareti** → film troppo elastico, screpola sugli spigoli.
- **Primer rosso/grigio scuro** senza coprire con bianco abbondante: trapela come tono "sporco" sotto il bianco e ammazza l'effetto porcellana.
- **Una mano sola pesante di filler primer**: cola, riempie i dettagli, restituisce un look "plastica fusa".
- **Saltare il wet-sanding intermedio**: senza quello le layer lines vincono.

---

## 8. Esempio realistico tempi (pezzo 10x10x15 cm)
| Giorno | Operazione | Tempo attivo | Asciugatura |
|--------|------------|--------------|-------------|
| 1 mattina | Sand 220-600 | 30 min | — |
| 1 mattina | Filler primer #1 (3 mani) | 15 min | 2 h |
| 1 pomeriggio | Wet sand 400 + filler #2 | 30 min | overnight |
| 2 mattina | Wet sand 600 + filler #3 spot | 25 min | 2 h |
| 2 pomeriggio | Wet sand 800 + primer bianco fine | 25 min | overnight |
| 3 mattina | Sand 1000 leggero + white satin x2 | 20 min | 4 h |
| 3 pomeriggio | Clear satin x2 | 10 min | 48 h cura |

Totale attivo: ~2 h 35 min. Calendario: ~3-4 giorni.