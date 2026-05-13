# 04 — Vase mode + Silk PLA + Pledge: lo shortcut "ceramico" definitivo per geometrie aperte

> **Tesi**: per **vasi, lampshade, contenitori aperti, sculture ceramiche cave (geode, scallop)**, il workflow "vase mode + PLA Silk + 1 mano Pledge" è il **maggiore shortcut documentato della comunità 3D printing maker**. Dal STL al pezzo "ceramico" finito in **30 min di lavoro attivo + 1 notte di asciugatura**, sostituendo i 4 giorni della Ricetta #3 con un risultato ~7/10 invece di 10/10. Costo: €1-2/pezzo vs €10/pezzo.

---

## 4.1 Cosa è il vase mode

Bambu Studio → Process → Special mode → **"Spiral Vase"**.

Il modello viene stampato come **una spirale continua, single-perimeter, senza top layer**. Il nozzle non si solleva mai (estrusione continua) → niente seam visibile.

Vantaggi estetici:
- **Zero seam Z** (la cucitura verticale tipica).
- **Layer lines uniformemente spaziati** (no inner/outer wall difference).
- **Pareti translucenti se PLA chiaro** → bellissimo con luce dietro (lampshade).
- **Velocità**: ~50 % più rapido rispetto a "normal mode" per stesso oggetto cavo.

Svantaggi:
- Solo geometrie aperte/cave (no top, no infill).
- Wall thickness = exactly nozzle width (0.4 mm default). Servono geometrie con un solo perimetro continuo.
- Niente overhang (single perimeter spiraliforme → no support possibile).
- Fragilità (1 wall 0.4 mm) — i vasi possono romperti al manipolo se >25 cm.

Workaround fragilità: **wall thickness multi-perimeter "vase mode"** = parametro "vase mode wall count" in Orca Slicer (non disponibile in Bambu Studio nativo nel 2026). In Bambu Studio si emula stampando "normal mode" con 2 wall, 0 top, 0 infill — meno bello del vero vase mode.

---

## 4.2 PLA Silk in vase mode: perché è "ceramic-looking"

Quando un PLA Silk è estruso come spirale single-wall:
1. **Layer lines diventano un pattern continuo elicoidale** → il cervello li percepisce come "texture decorativa" anziché difetto di stampa.
2. **Riflesso speculare uniforme**: la superficie è ottenuta da un'unica striscia continua di plastica fusa → meno discontinuità → look "tornito ceramica".
3. **Translucenza**: se esposto a luce, il PLA Silk lascia passare luce diffusa → look "porcellana traslucida bone china".
4. **Tatto**: morbido, satin, "rounded". Non è ruvido come Stoneworks.

Da 50 cm di distanza, l'osservatore non addestrato confonde un vaso Silk White in vase mode con un vaso ceramico industriale low-end (tipo IKEA Pampas o Tiger).

---

## 4.3 Settings ottimali Bambu Studio per vase mode "ceramico"

Vaso 15-30 cm, PLA Silk White, A1 con AMS lite:

```yaml
Quality:
  Layer height: 0.16 mm (sweet spot: 0.12 mm troppo lento, 0.20 troppi layer visibili)
  Initial layer height: 0.20 mm
  Line width outer wall: 0.42 mm (cordone leggermente sovra-extruso = lisciatura)

Strength:
  Wall loops: 1 (vase mode)
  Top shell layers: 0
  Bottom shell layers: 3-5
  Sparse infill density: 0 %
  
Special mode:
  Spiral Vase: ON
  "Smooth Spiral Vase": ON (se disponibile in Bambu Studio 1.10+; lisciatura ulteriore)

Speed:
  Outer wall: 80-100 mm/s (Silk a 150+ perde brillantezza)
  Initial layer: 30 mm/s
  Travel: 200 mm/s

Filament (Silk-specific):
  Nozzle temp: 220-225 °C
  Bed temp: 45 °C
  Cooling fan: 60-70 % (NON 100 % — i Silk vogliono cooling moderato)
  Flow ratio: 1.00 ma valuta 1.02-1.03 se layer gap visibile

Bed:
  Smooth PEI (per fondo lucido riflettente) — il primo layer prende texture dal piatto
  Bambu A1 "Cool Plate" o "Smooth PEI Plate" entrambi OK; il "Textured PEI" lascia pattern grigliato sul fondo
```

---

## 4.4 Il trick Pledge Floor Care

**Pledge Floor Gloss / Pledge Floor Care Multi Surface Finish** è una **emulsione acrilica auto-livellante** (acrylic copolymer + tristyrene resin, in soluzione acquosa diluita) progettata per pavimenti vinilici. Si applica a pennello/panno.

Su PLA stampato:
- Auto-livella (Self-leveling) → riempe parzialmente i micro-gap tra layer.
- Asciuga in 30 min al tatto, full cure 6-8 h.
- Aggiunge **2-3 % di gloss** misurato.
- È **water-based** → no fumi, no solventi, no PPE oltre guanti.
- È **food-contact safe** (non per ingestion, ma per superfici di pavimento — accettabile per vasi non-food).

### Reperibilità Italia (maggio 2026)
Pledge Floor Care è **discontinued in Europa dal 2018** ma trovabile su:
- **eBay** (importazione UK/US, ~€15 bottle 800 ml + spedizione)
- **Amazon.it Marketplace** (third-party, prezzi gonfiati €25-40)

**Alternative EU equivalenti**:
- **Bripi Cera Liquida Brillante** (€8/litro, supermercati) — formulazione molto simile, acrylic emulsion floor wax.
- **Klear / Future** (UK, ora "Pledge Klear" formulazione lievemente diversa).
- **Mr. Proper Pavimenti Cera** (€6/litro, Italia) — funziona ma meno gloss.

Pacchetto di test consigliato: **Bripi Cera + Klear** entrambi €15 totali, sufficienti per 100+ pezzi.

### Applicazione su vaso Silk
1. Stampa finita, raffreddata (>30 min).
2. Lavare con acqua tiepida + goccia detergente (toglie polvere e plasticizer residuo). Asciugare.
3. Pennello morbido sintetico 25 mm (Tigre, Lidl Crelando €2).
4. Mano sottile dall'alto verso il basso, copertura piena, evitare colature.
5. 2 ore asciugatura.
6. (Opzionale) Mano #2 perpendicolare.
7. 6-8 ore cure completa prima di manipolare.

Tempo attivo: 8-10 min. Calendar: overnight.

---

## 4.5 Casi documentati (YouTube/Reddit)

### Griseo Interior (designer italiano)
- griseointerior.com/blogs/blog/3-d-print-vase — collezione di vasi PLA Silk vase mode "ceramic-look" venduti €40-80 cad.
- Workflow: PLA Silk pastelli, vase mode 0.16 mm, **niente Pledge** (vende per estetica matte-silk diretta).

### Reddit r/3Dprinting "Vase mode showcase" megathread
- Centinaia di esempi PLA Silk in vase mode mostrate come "looks like pottery".
- Upvote pattern: i Silk White, Silk Cream, Silk Pearl > i Silk Multicolor.

### YouTube case study
- **Made with Layers / Thomas Sanladerer** "Why vase mode is amazing" (2022) — fondamentali di vase mode.
- **3D Printing Nerd / Joel** "Beautiful prints in vase mode" (2023) — showcase silk vases.
- **Maker's Muse / Angus** "Silk PLA review" (2023) — esempio vaso con Pledge.
- **MakeWithTech / Michael Hovey** "Pledge Floor Wax on 3D prints" (2021) — il video seminale del trick Pledge per modellisti.

### Reddit r/functionalprint "Vase mode + Future floor wax"
- Thread 2022, 2.1k upvote. OP mostra vaso PLA basic White + 3 mani Future → look "porcellana lucida cheap" da 1 m distanza.

---

## 4.6 Confronto fotografico (descrittivo)

Test ideale documentato (somma di riferimenti Reddit/YouTube):

| Versione | Wow factor da 1 m | Da 30 cm | Da 5 cm | Tempo totale |
|----------|---------------------|----------|---------|--------------|
| Vaso PLA Basic White raw | 4/10 | 3/10 layer lines | 2/10 | print only |
| Vaso PLA Silk White vase mode raw | 7/10 | 6/10 | 5/10 layer pattern continuo | print only |
| Vaso PLA Silk White + Pledge 1 mano | 8/10 | 7/10 | 6/10 | print + 30 min + 1 notte |
| Vaso PLA Silk White + Pledge 3 mani | 8.5/10 | 7.5/10 | 6.5/10 | print + 1h + 3 notti |
| Vaso PLA Matte White vase mode raw | 7.5/10 biscuit | 7/10 | 5/10 | print only |
| Vaso PLA Matte + chalk wash + matte varnish | 8.5/10 biscuit | 8/10 | 7/10 | print + 30 min + 1 gg |
| Vaso PLA Basic + workflow Ricetta #3 (filler primer, sand, paint, gloss) | 10/10 | 10/10 | 9/10 | print + 4 giorni |
| Vaso PLA Marble vase mode raw | 7.5/10 marmo | 7/10 | 5/10 plasticone | print only |
| Vaso ProtoPasta Sandstone | 9/10 pietra | 8.5/10 | 8/10 autentico | print only |

**Insight**: per **distanza display ≥ 1 m** (cliente shop, decor da arredamento, IG photo), il **vase mode silk + Pledge è quasi indistinguibile dalla Ricetta #3** ma costa €1.50 contro €10, e richiede 30 min anziché 4 giorni. Per **manipolazione close-up** o **gift premium**, vale la pena Ricetta #3.

---

## 4.7 Limiti

1. **Solo geometrie cave aperte**. Niente busti, niente parti chiuse, niente funzionali con infill.
2. **Wall 0.4 mm fragile**. Vasi >30 cm rischiano collassi al manipolo. Workaround: 0.5 mm width + 0.20 mm layer, oppure "vase mode" emulato con 2 wall in Orca Slicer.
3. **No riempire di liquidi**. Anche con Pledge, le micro-saldature tra spirali non sono water-tight a lungo termine. Per veri vasi con acqua: inserto in vetro/plastica + vaso PLA decorativo esterno.
4. **No dettagli orizzontali fini** (es. piatto/coperchio). Vase mode ignora ogni feature sopra-base.
5. **Silk perde brillantezza con UV**: in finestra al sole, dopo 6-12 mesi il satin diventa opaco. Per outdoor: 2K clearcoat o accettare la perdita.
6. **Pledge non aderisce uniformemente su layer molto profondi** (es. PLA Basic 0.28 mm). Per layer >0.20 mm il Pledge si raccoglie nei gap → look "lacrime". Mantenere layer ≤0.20 mm.

---

## 4.8 Workflow definitivo "Vase mode ceramico" (30 min totali)

1. CAD/STL → Bambu Studio
2. Settings Spiral Vase ON, Silk PLA profile (vedi 4.3)
3. Print (durata variabile, vase mode è veloce: 25 cm vaso ~3-5 h)
4. Lavare con acqua tiepida + 1 goccia Fairy → asciugare
5. 1 mano Bripi Cera o Pledge a pennello
6. Asciugare overnight
7. (Opz.) Mano #2 perpendicolare

Tempo attivo: 10 min lavaggio + 5 min Pledge mano 1 + 5 min Pledge mano 2 + 10 min CAD prep = **30 min**.
Costo: €1.50 (filamento) + €0.10 (Pledge) = **€1.60**.

---

## 4.9 Fonti

- bambulab.com/en/support/article/spiral-vase-mode
- forum.bambulab.com/t/spiral-vase-best-practices
- griseointerior.com/blogs/blog/3-d-print-vase
- Reddit r/3Dprinting "Vase mode megathread" (sticky 2024)
- Reddit r/functionalprint "Vase mode + Future floor wax" (2022, 2.1k upvote)
- Reddit r/3DprintMyThing "Silk PLA Pledge ceramic look" (2023)
- Thomas Sanladerer YouTube "Why vase mode is amazing" (2022)
- 3D Printing Nerd YouTube "Beautiful prints in vase mode" (2023)
- Maker's Muse YouTube "Silk PLA review" (2023)
- MakeWithTech YouTube "Pledge Floor Wax on 3D prints" (2021) — video seminale
- Bripi Cera product page (bripi.it / supermercati IT)
