# 02 — Ironing in Bambu Studio: pre-finishing scalabile

Domanda: posso usare l'ironing del slicer per **ridurre il sanding sul top** dei
pezzi e quindi accorciare la pipeline industriale?

Risposta breve: **sì, ma solo per i top piatti**. Riduce il sanding del top da
~10 min a ~2 min, ma non sostituisce il sanding dei walls (che restano i veri
colpevoli delle layer lines visibili).

---

## 1. Cos'è l'ironing

Definizione (Bambu Lab wiki https://wiki.bambulab.com/en/software/bambu-studio/ironing):

> Ironing is a slicer feature that makes a second pass over the top surface of
> a print at high temperature with little or no extrusion, melting the surface
> traces together.

Meccanica:
1. Top layer è stampato normalmente.
2. Subito dopo, nozzle ripassa con pattern denso (line spacing ~0.1 mm).
3. Estrusione **molto bassa** (5-15%) o nulla, solo calore.
4. Tracce esistenti rifondono superficialmente → superficie continua.

Si applica **solo a superfici "top"** (rivolte verso l'alto, identificate dallo
slicer). Mai walls, mai overhangs, mai bottom (a contatto col plate).

---

## 2. Parametri Bambu Studio (preset PLA)

In Bambu Studio: **Quality > Ironing**. Default per "0.16 mm Standard PLA Bambu A1":

| Parametro | Default | Range utile | Note |
|---|---|---|---|
| **Ironing type** | "Top surfaces" | Top / All solid / Topmost only | "Top surfaces" sufficiente nella maggior parte dei casi |
| **Ironing pattern** | Concentric | Concentric / Rectilinear / Zigzag | **Concentric** miglior risultato su forme curve/organiche; **Rectilinear** su rettangolari |
| **Ironing flow** | 9-10% | 5-15% | Sotto 5% non rifonde abbastanza; sopra 15% over-extrude visibile |
| **Ironing speed** | 20 mm/s | 15-30 mm/s | Più lento = più calore = più liscio, ma rischio blob |
| **Ironing line spacing** | 0.10 mm | 0.08-0.15 mm | < 0.10 troppo lento; > 0.12 visible wave |
| **Ironing inset** | 0.21 mm (default) | 0.1-0.5 mm | Distanza dal bordo: troppo poco = blob sul perimetro |

Per Bambu A1 con PLA Bambu Basic, il preset "Standard" è già ben tarato; il
profilo "Strength" disabilita l'ironing per default.

**Solo top? Anche walls?** No. I walls non sono iron-abili (la fisica:
l'ironing pass è orizzontale, non può "stirare" superfici verticali). Per i
walls le opzioni sono: layer più sottile (0.08-0.12 mm), arc-fitting (Klipper),
oppure sanding/filler post-stampa.

---

## 3. Effetto reale misurato

### 3.1 Ra "macro" (occhio nudo, foto a contrasto laterale)

[CONS, da Reddit / YouTube — non strumentato]:
- Top senza ironing: layer lines visibili a luce radente, Ra stimato 6-12 μm.
- Top con ironing default: superficie quasi continua, layer lines visibili solo
  a 30° con luce dura. Ra stimato 3-5 μm.
- Top con ironing + sanding 400: Ra < 2 μm (paragonabile a filler primer + 400).

### 3.2 Dato strumentato (paper PMC citato in round 1)

Studio 2023 "Effect of surface treatments on the roughness of FDM parts" — PMC
https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10301527/ riporta su PLA:

- **No treatment**: Ra ~12.5 μm
- **Ironing (parametri default)**: Ra ~4.6 μm (**-63%**)
- **Sanding manuale 600 grit**: Ra ~3.4 μm (**-72%**)
- **Ironing + sanding 600**: Ra ~1.8 μm (**-86%**)

**Caveat**: paper non testa Bambu A1 specifico né Bambu Basic. Numeri
indicativi di magnitudo, non valori assoluti per la pipeline utente.

### 3.3 Costo tempo

Su pezzo decorativo tipico 12 cm con top piatto ~30 cm²:
- Senza ironing: **4h30** (esempio statuetta 100 g 0.16 mm).
- Con ironing default su top: **4h45-5h00** (**~+8-12%** tempo totale).

Per pezzi con grande superficie top (es. coperchio scatola 15×15 cm): ironing
può aggiungere **+20-30%** tempo. In quel caso valutare se conviene davvero o
se basta sanding 400 + filler primer.

### 3.4 Compatibilità con filamenti

| Filamento | Ironing? | Note |
|---|---|---|
| PLA Bambu Basic | Sì | Risultato eccellente, è il caso testato |
| PLA Bambu Matte | Sì, ma effetto **lucidante** indesiderato | L'ironing aumenta gloss locale, contrasto con matte circostante. Sconsigliato se si vuole mantenere texture matte uniforme |
| PLA Bambu Silk | Sì, intensifica lucentezza | Effetto interessante per finiture "porcellana" senza vernice |
| PLA Marble / Stoneworks (ProtoPasta, Bambu) | **Evitare** | L'ironing fonde le inclusioni e crea aloni / smear |
| PLA+/Tough | Sì | Comportamento simile a Basic |
| PETG | Sì ma flow 6-8% | Più appiccicoso, rischio stringing visibile |

---

## 4. Limitazioni e failure modes

| Issue | Causa | Mitigazione |
|---|---|---|
| **Wave/ondulazione** visibile sul top | Line spacing > 0.12 mm | Ridurre a 0.10 |
| **Blob sui bordi** | Inset troppo piccolo, flow alto | Aumentare inset a 0.3-0.5, ridurre flow a 7% |
| **"Pelle d'arancia"** | Top layer non solido (top layers count basso) | Top shell layers ≥ 5 (0.16 mm × 5 = 0.8 mm pelle solida) |
| **Gloss patch** che rompe matte uniforme | Filamento matte + ironing | Disabilitare ironing OR vernicare tutto con matte clear |
| **Top concavo / convesso** non viene ironato | Slicer non rileva come "top" | Forzare con override locale OR accettare e sanding |
| **Ironing su pezzi piccoli** (< 2 cm² top) | Nozzle non ha tempo di scaricare il calore | Disabilitare; sanding manuale è più veloce comunque |

---

## 5. Quando usare l'ironing nella pipeline industriale

**SÌ** se:
- Top piatto grande (> 5 cm²), visibile, parte estetica chiave.
- Filamento Basic o Silk (non Matte/Marble).
- Pezzo destinato a finitura **gloss** (l'ironing prepara perfettamente per primer fine).
- Lotto > 5 pezzi (il +10% tempo si ammortizza vs il sanding manuale risparmiato).

**NO** se:
- Top complesso/curvo: lo slicer non lo identifica come "top".
- Filamento matte/marble: rovina la texture.
- Pezzo che andrà comunque con filler primer pesante: il filler livella anche
  le layer lines del top, l'ironing diventa ridondante.
- Pezzi piccoli (< 30 g): il setup ironing non si ripaga.

### Ricetta consigliata per finitura "porcellana lucida" su top piatto

1. Bambu Basic White, 0.16 mm, **ironing ON** (Concentric, 9%, 20 mm/s, 0.10 mm).
2. No sanding sul top, solo IPA wipe.
3. Filler primer **sui walls soltanto** (mascheratura del top con washi tape).
4. Sanding 400 → 600 sui walls.
5. Primer fine globale.
6. Topcoat + gloss.

Riduce il sanding manuale del **30-40%** complessivo del pezzo [stima basata su
ripartizione superficie tipica top/walls = 30/70].

---

## 6. Fonti

- Bambu Lab wiki — Ironing: https://wiki.bambulab.com/en/software/bambu-studio/ironing
- Bambu Lab forum — thread "Ironing best settings PLA":
  https://forum.bambulab.com/t/ironing-best-settings/
- Reddit r/BambuLab — search "ironing": https://www.reddit.com/r/BambuLab/search/?q=ironing
- PMC 2023 paper su Ra FDM: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10301527/
- Maker's Muse YouTube — "Ironing in slicer is magic":
  https://www.youtube.com/c/MakersMuse (search "ironing")
- CNC Kitchen — "Ironing - the secret to perfect tops":
  https://www.youtube.com/c/CNCKitchen (search "ironing")
- Teaching Tech — "PrusaSlicer ironing test" (parametri trasferibili a Bambu Studio):
  https://www.youtube.com/c/TeachingTech
