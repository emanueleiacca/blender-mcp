# 03 — Chemical Smoothing su PLA

> **Verità di partenza**: PLA **non** è acetone-soluble come l'ABS. L'acetone su PLA produce al massimo una superficie appiccicosa/gommosa, talvolta opaca, **non un vapor smoothing pulito**. Fonte: [Wevolver — PLA and Acetone](https://www.wevolver.com/article/acetone-pla), [3DISM — Vapor smoothing PLA alternatives](https://3dism.org/vapor-smoothing-pla-safe-alternatives-to-acetone/), [3D Insider — Solvents for PLA](https://3dinsider.com/smooth-pla-solvents/).

## Sintesi: cosa funziona davvero su PLA

| Sostanza | Effetto su PLA | Sicurezza domestica | Verdetto |
|---|---|---|---|
| **Acetone** | poco / gommifica | media (infiammabile) | ❌ inutile |
| **IPA (isopropil alcool)** | nessuno su PLA standard | sicura | ❌ inutile sul PLA "puro" (✅ vedi Polysher per PolySmooth) |
| **Etile acetato** | scioglie superficie, vapor smoothing efficace | media (infiammabile, vapori irritanti) | ⚠️ SI, con ventilazione e PPE |
| **MEK (metiletilchetone)** | aggressivo, scioglie | scarsa (tossico, infiammabile) | ⚠️ sconsigliato a casa |
| **THF (tetraidrofurano)** | dissolve completamente PLA (industriale) | **molto scarsa** (mutageno, perossidi esplosivi) | ❌ NO domestico |
| **DCM / Diclorometano (cloruro di metilene)** | scioglie PLA molto bene | **pessima** (cancerogeno, neurotossico) | ❌❌ NO |
| **Cloroformio** | dissolve PLA (industriale) | pessima (cancerogeno) | ❌ NO |
| **Caustic soda (NaOH) diluito** | smussa lentamente | media (corrosivo) | ⚠️ marginale |
| **IPA + PolySmooth (Polymaker)** | smoothing eccellente *solo se filamento è PolySmooth/PVB* | ottima | ✅ ma serve filamento dedicato |
| **Limonene (d-limonene)** | nessuno apprezzabile su PLA | ottima | ❌ (utile per HIPS, non PLA) |

---

## 1. Acetone — perché non funziona

PLA = polilattide, polimero cristallino/semi-cristallino. Acetone è un solvente polare aprotico che attacca polimeri amorfi (ABS, HIPS) ma non rompe efficacemente le catene di PLA. Risultato: superficie appiccicaticcia, opacizzazione localizzata, nessuna fusione di layer lines.

Eccezione marginale: PLA **mescolato con additivi** (alcuni "PLA+" o blend) può reagire un po'. Aneddotico.

Fonte: [Wevolver](https://www.wevolver.com/article/acetone-pla), [Hackaday — Smoothing PLA Parts](https://hackaday.com/2013/06/07/smoothing-pla-printed-parts/), [3D Printer Bee](https://the3dprinterbee.com/dissolving-pla/).

## 2. Etile acetato — la "miglior" via chimica per PLA

- Solvente "amico" della comunità maker: meno tossico/aggressivo di DCM/THF/MEK, comunemente reperibile (anche come componente del solvente per smalto unghie, ma in alta purezza).
- Vapor smoothing: vaschetta sigillata, panno carta imbevuto sulle pareti, pezzo sospeso, **10-30 min**. Monitorare ogni 5 min — sovraesposizione = perdita dettagli, "lava" la superficie.
- Brush-on: stendere a pennello fino una mano sottile, lasciar evaporare. Risultato meno lucido, più controllabile su dettagli.

### Sicurezza (etile acetato)

- **Infiammabile** (flash point ~-4 °C). No fiamme libere, no scintille, no vicino a heat gun.
- **VLE 8h**: 400 ppm (ACGIH TLV-TWA). Vapori irritanti per occhi e vie respiratorie.
- PPE: respiratore con filtro organici (A1/A2), occhiali, guanti nitrile o butile. Outdoor o cappa.
- Smaltimento: come rifiuto chimico, non in lavandino.

Fonte tecniche: [Xometry — Vapor smoothing PLA](https://www.xometry.com/resources/3d-printing/vapor-smoothing-pla/), [3DISM safe alternatives](https://3dism.org/vapor-smoothing-pla-safe-alternatives-to-acetone/).

> ⚠️ **Disaccordo / da verificare**: alcune fonti hobbyste affermano "vapor di EtOAc → finitura lucida pari ad ABS+acetone". Test misurati (Ra) non trovati nelle fonti consultate. Aneddotico finora.

## 3. DCM (diclorometano / metilene cloruro) — **NON USARE A CASA**

- Funziona benissimo chimicamente (PLA si scioglie / smoothing rapido).
- **Cancerogeno classificato** (IARC 2A; EPA: rischio cancro polmonare e fegato).
- TLV: 50 ppm (ACGIH), OSHA PEL: 25 ppm, EPA worker action level 2 ppm.
- Bolle a **39.6 °C** (104 °F) → satura l'aria di vapori a temperatura ambiente.
- Negli USA, EPA ha **vietato la maggior parte degli usi consumer** di DCM (2024). In EU regolato pesantemente.
- Effetti acuti: deprime SNC, può convertirsi a monossido di carbonio nel sangue → ipossia.

Fonti: [Thingiverse DCM smoothing](https://www.thingiverse.com/thing:74093), [Ultimaker community PLA/PET DCM](https://community.ultimaker.com/topic/34919-pla-and-pet-smoothing-with-dichloromethane-ch2cl2/), [Science Insights — What melts PLA](https://scienceinsights.org/what-melts-pla-heat-solvents-and-everyday-risks/).

> **Verdetto netto**: il risultato estetico non vale il rischio. Per pezzi estetici ci sono alternative meccaniche/chimiche più sicure (sanding + filler primer + XTC-3D).

## 4. THF (tetraidrofurano)

- Dissolve PLA completamente, usato come **solvente di laboratorio**.
- Forma **perossidi esplosivi** se stoccato a lungo (come l'etere etilico).
- Mutageno mammifero, teratogeno probabile.
- TLV: 50 ppm, ma irritazione e neurotossicità da molto meno.
- Inutile per "smoothing" — più per dissolvere.

Fonti: [3D Printer Bee](https://the3dprinterbee.com/dissolving-pla/), [ACS community](https://communities.acs.org/t5/Ask-An-ACS-Chemist/Help-potentially-exposing-a-scam-Solubility-of-PLA-in-Chloroform/td-p/86162).

**NO domestico.**

## 5. MEK (metil etil chetone, butanone)

- Solvente per styrene e altri polimeri.
- Su PLA: effetto **debole**, ammorbidimento parziale.
- Tossico (epatico, neurotossico), infiammabile.
- Usato più per ABS/ASA che PLA. Vedi [Alliance Chemical — MEK for ABS/ASA](https://alliancechemical.com/blogs/articles/mek-for-3d-print-finishing-the-pros-alternative).

## 6. Caustic soda (NaOH) — bagno alcalino

- Idrolisi alcalina del PLA → degradazione superficiale lenta.
- Tipicamente NaOH 5-10% in acqua tiepida, immersione 30-60 min.
- Liscia poco e può corrodere dettagli.
- Pericoloso per pelle/occhi (corrosivo grave).

Conclusione: marginale, sconsigliato.

## 7. Polymaker Polysher + PolySmooth (caso speciale)

Filamento **PolySmooth** (PVB, NON PLA classico) progettato per essere smussato con **vapori di IPA** (70-99%) in un device dedicato (Polysher) o anche manualmente.

- **Device Polysher**: nebulizzatore IPA, camera chiusa, ciclo ~10-30 min.
- Risultati: superficie quasi liscia speculare; sopra i 20-30 min si arrotondano dettagli.
- IPA è molto sicuro rispetto agli altri solventi (infiammabile ma poco tossico; serve solo ventilazione).
- **Limite**: funziona solo con PolySmooth (PVB). Su PLA "classico" l'IPA **non fa nulla**.

Fonti: [Polymaker — PolySmooth](https://us.polymaker.com/products/polysmooth), [Polymaker Wiki](https://wiki.polymaker.com/printing-tips/post-processing/smoothing), [Hackster review](https://www.hackster.io/news/review-polymaker-s-polysher-makes-your-3d-prints-shiny-and-smooth-b28f8cd4eaac).

> Per pezzi estetici futuri, **valutare PolySmooth invece di PLA** se la finitura liscia è critica e non vuoi sandare ore.

## 8. Tabella safe-vs-effective

```
            EFFICACIA SU PLA →
            bassa       media       alta
   ALTA   │  IPA        EtOAc*      PolySmooth
SAFETY    │  (nullo)    (con PPE)   + IPA
   ↑      │
   media  │  acetone    MEK         
          │  (gommifica)            
   ↓      │
   BASSA  │             THF         DCM
          │             (laboratorio)
```
*EtOAc = etile acetato

---

## 9. Cosa raccomando per Bambu A1 + PLA + pezzi estetici

**Consenso, e mia conclusione dalla ricerca**: dimentica il chemical smoothing per PLA "classico". Tre opzioni utili:

1. **Sanding + filler primer (file 01/02)**: lavoro maggiore, controllo totale, sicuro.
2. **XTC-3D / UV resin (file 04)**: chimicamente non scioglie PLA ma colma le layer lines con un coating duro.
3. **(Se cambi filamento)** PolySmooth + Polysher con IPA: chimicamente sicuro ed efficacissimo.

Se proprio vuoi sperimentare il vapor chimico su PLA standard: **solo etile acetato**, all'esterno, con respiratore organico, su pezzi sacrificali, mai oggetti sottili o con dettagli fini.
