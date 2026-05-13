# 02 — Drying rack DIY per cura parallela (€5)

> Obiettivo: tenere **20-50 pezzi** in cura (primer, vernice, sealer)
> contemporaneamente, senza appoggiarli (che produce print line + adesione
> della vernice fresca al piano). Sblocca la regola batch R2-D:
> "tempi morti O(N) → O(1)".

---

## 2.1 BOM — versione filo di ferro

| Item | Source | Cost € | Time to build | Alternative |
|---|---|---|---|---|
| Fil di ferro plastificato Ø1.5-2 mm rotolo 10 m | Brico/Leroy €2.50 | 2.5 | 0 | filo galvanizzato giardino €3/15m |
| Bastoncini bambù skewer (spiedini) confezione 100 pz | Lidl/supermercato | 1 | 0 | stuzzicadenti €0.50 (per micro-pezzi) |
| Base cartone forato (scatola rovesciata + bucate) | recupero | 0 | 0 | tegola perforata pegboard IKEA SKÅDIS €10 |
| Mollette legno bucato (per pezzi piatti) | Lidl/casa | 1 | 0 | clip carta metallo €1 (Tiger) |
| Nastro biadesivo / colla a caldo | casa | 0 | 0 | colla cianoacrilica €1 |
| **TOTALE** | | **€4-5** | **30 min** | versione pegboard SKÅDIS **€12** |

---

## 2.2 Geometria target

Vuoi:
- **densità**: 50 pezzi in **60 × 40 cm** = 1 pezzo / 48 cm² → spacing 7 cm
- **altezza**: pezzo sospeso 5-8 cm dalla base (evita drip su base)
- **modularità**: rack riposiziona quando il pezzo successivo è di forma diversa

### Configurazioni

**Config A — "Greco-asiatica" (skewer verticali in base bucata)**

```
   ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓       ← pezzi sospesi (puntini = punto di aggancio)
   │ │ │ │ │ │ │ │ │ │       ← skewer bambù verticali 25 cm
   │ │ │ │ │ │ │ │ │ │
═══╧═╧═╧═╧═╧═╧═╧═╧═╧═╧═══    ← base cartone con fori 5 mm grid 5 cm
```

Base 60 × 40 cm con grid 5 × 5 cm → 8 × 5 = **40 spiedini** disponibili.

**Config B — "Chiocciole" (filo a U rovesciato)**

```
    ╱─╲       ╱─╲       ╱─╲       ← filo piegato a U
   /   \     /   \     /   \
  pezzo  pezzo  pezzo
  ▓      ▓      ▓
```

Filo Ø1.5 mm piegato manualmente con pinza. Lunghezza tipica: 15 cm di
filo per ogni U. Su rotolo 10 m → 60+ U.

**Config C — "Linea tendi-panni" (filo orizzontale + mollette)**

```
═══════════════════════════════════  ← filo teso fra due muri / supporti
  ▓  ▓  ▓  ▓  ▓  ▓  ▓  ▓  ▓  ▓     ← mollette + pezzi
```

Buono per pezzi piatti con feature di aggancio (orecchio, anello). Per
batch 50 pezzi serve filo di 3-4 metri lineari → 2-3 linee parallele.

---

## 2.3 Build step-by-step

### Versione skewer verticali (raccomandata, copre 90% dei casi)

1. **Base**: scatola cartone 60 × 40 cm capovolta. Disegna grid 5 cm × 5 cm
   con righello. **Fori Ø5 mm** con punta trapano o chiodo riscaldato. 8 ×
   5 = 40 fori.
2. **Skewer**: spiedino bambù da 25 cm, infilato vertical in ogni foro,
   bloccato con goccia di colla a caldo alla base.
3. **Punto di aggancio sul pezzo**:
   - se il pezzo ha un foro filetto/inserto → infila skewer direttamente;
   - se piatto → mollette legno a U ribaltata su skewer (foglietto carta
     fra molletta e pezzo per non lasciare segno se vernice fresca);
   - se irregolare → un piccolo gancio in filo di ferro (Ø1 mm) avvolto
     attorno allo skewer + uncinato in una concavità del pezzo.
4. **Rotazione**: durante cura primer, **ruota di 90°** ogni 30 minuti i
   primi 2 giri per evitare drip in un solo punto. Marker permanente su
   skewer per tracking lato "1/2/3/4".

### Versione pegboard SKÅDIS (€12, riusabile per anni)

1. IKEA SKÅDIS 56 × 56 cm pegboard €10 + ganci €2/12 pz.
2. Monta a muro o su cavalletto da cucina.
3. Ogni gancio porta 1 pezzo. SKÅDIS standard ha 64 buchi → 64 pezzi.
4. Vantaggio: zero ingombro, sgancia in 1 secondo.

### Versione "tenda" (filo teso orizzontale)

1. 2 supporti laterali (cavalletti, tavolo, sedie ribaltate).
2. Filo Ø2 mm teso, lunghezza 2-3 m per linea.
3. 3-4 linee parallele a 15 cm di distanza verticale.
4. Mollette legno bucato — bucato perché lascia traspirare meglio la
   vernice fresca sotto la molletta.

---

## 2.4 Quanto spazio risparmi

Comparison con appoggio piano su tavolo:

| Setup | Pezzi simultanei in spazio 60 × 40 cm | Note |
|---|---|---|
| Piano tavolo | 12-15 (un ripiano) | print line, drip su tavolo |
| Piano tavolo + carta forno | 15-20 | meno drip, ma occupazione = 1 pezzo |
| **Rack skewer DIY** | **40-50** (3D, verticale) | aggancio dall'alto, drip libero |
| **Pegboard SKÅDIS verticale** | **50-64** (su muro 60×60 cm) | zero ingombro orizzontale |
| Drying cart pro Tamiya | 24 (rack 3 ripiani 40 cm) | costo €80 |

Throughput: **rack DIY = 3-4× più pezzi/m² rispetto al tavolo**.

---

## 2.5 Critical pairing con workflow R2

- Primer Maximum BricoIO: cura 4-6 ore tatto, 24 h riverniciatura. Su rack
  puoi caricare il batch sera 1, ricoprire colore mattina 2.
- Acrilico Maxi Color: tatto 30 min, riverniciatura 4 h. Su rack permette
  3-4 cicli di colore al giorno.
- Pledge clear coat: cura 2 h tatto. Caricamento rack ottimale.
- **Heat-set inserts dopo cura**: NO! L'inserzione termica vicino a
  vernice fresca la fa bollire. Esegui heat-set **prima** del primer.

---

## 2.6 STL printable per upgrade

Su Printables/Thingiverse:
- "drying rack 3d print" — basi forate per skewer custom OD:
  https://www.printables.com/search/models?q=drying+rack
- "miniature painting handle" — handles per pezzi piccoli:
  https://www.printables.com/search/models?q=miniature+painting+handle
- "alligator clip stand" — base con coccodrillini (per pezzi piatti):
  https://www.thingiverse.com/search?q=alligator+clip+stand+painting

Costo materiale base stampata 60×40 cm: 80-120 g PLA = €2-3.

---

## 2.7 Riferimenti

- r/minipainting "drying rack" thread:
  https://www.reddit.com/r/minipainting/search?q=drying+rack
- Tabletop Minions YouTube "DIY paint drying rack":
  https://www.youtube.com/c/TabletopMinions
- Adam Savage "rolling miniature painting station":
  https://www.tested.com (search drying station)
- Etsy keyword reference: "miniature painting drying rack" mostra prezzi
  retail €30-80 → riferimento break-even DIY.
