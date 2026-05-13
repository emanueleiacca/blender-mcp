# 01 — Sanding / Carteggiatura PLA

> Stampa: Bambu A1, PLA, pezzi estetici. Obiettivo: rimuovere layer lines prima del primer/pittura.

## TL;DR
- PLA si ammorbidisce intorno ai **60-65 °C** (Tg ~60 °C). L'attrito della carta a secco genera abbastanza calore da **smearare** la superficie invece di rimuovere materiale. Conclusione condivisa: **wet sanding obbligatorio dalla grana 400 in su**, fortemente consigliato anche prima.
- Progressione consigliata trasversalmente: **120/180 → 220 → 320/400 → 600 → 800 → 1200 → 1500 → 2000** (skippare uno step lascia graffi profondi visibili dopo il primer).
- Su superfici piane usa blocco rigido, su curve usa spugna abrasiva o foam-backed pad.
- Stop al carteggio "puro" quando i graffi sono uniformi a 600/800: poi passare a **filler primer + carteggio fine** (vedi file 02). Solo se vuoi un mirror finish "verniciato" trasparente o lucidatura a polish hai senso arrivare a 2000+.

---

## 1. Perché PLA è particolarmente delicato

| Parametro | Valore | Implicazione |
|---|---|---|
| Tg (glass transition) | ~60-65 °C | Si gomma con poca frizione |
| Melting point | ~170-180 °C | Non rilevante per sanding (lontano), ma rilevante per heat gun |
| Hardness | Shore D ~83 | Più tenero di ABS, intaglia ma si scolpisce facilmente |

Fonte: [Prusa Knowledge Base — PLA](https://help.prusa3d.com/article/pla_2062), [Clever Creations — PLA Smoothing](https://clevercreations.org/smooth-pla-smoothing-3d-print-layer-lines/).

Il calore generato dall'attrito è il vero nemico: una grana grossa (120) a secco, premuta forte su un punto, **fonde le punte delle layer lines invece di abraderle**, creando una superficie viscosa che intasa la carta ("clogging") e rovina la geometria. Wet sanding raffredda la zona e fa galleggiare via lo slurry. Fonte: [Sinterit Sanding Guide](https://sinterit.com/3d-printing-guide/post-processing-in-3d-printing/sanding-3d-prints/), [eQualle Grit Guide](https://equalle.com/blogs/grit-guides/how-to-sand-3d-printed-pla-parts-smooth-320-400-600-1000-grit-guide).

---

## 2. Tabella progressione grane

| Step | Grana | Modalità | Scopo | Tempo indicativo / pezzo medio (palmo di mano) |
|---|---|---|---|---|
| 1 | 120-180 | secco o umido, **leggera pressione** | abbattere layer lines più marcate, scalini di support, seams | 5-10 min |
| 2 | 220-320 | umido consigliato | rimuovere graffi step 1 | 5-8 min |
| 3 | 400 | **wet sanding obbligatorio** | superficie uniforme pre-primer | 5 min |
| 4 | 600 | wet | rifinitura pre-primer | 3-5 min |
| 5 | 800-1000 | wet | **dopo** filler primer (vedi file 02) | 3-5 min |
| 6 | 1200-1500 | wet | finitura semi-glossy | 3 min |
| 7 | 2000+ | wet + polish compound | mirror finish (raro per modelli che si dipingono) | 5+ min |

**Regola d'oro** (citata da [eQualle](https://equalle.com/blogs/grit-guides/how-to-sand-3d-printed-pla-parts-smooth-320-400-600-1000-grit-guide), [Sovol](https://sovol.eu/blogs/new/how-to-remove-layer-lines-from-3d-prints-smooth-finishes), [QIDI](https://us.qidi3d.com/blogs/news/how-to-sand-and-polish-pla-prints-for-a-smooth-finish)): **non saltare grane** — ogni grana deve rimuovere completamente i graffi della precedente. Cambia direzione di carteggio di ~45° fra una grana e l'altra: se vedi ancora graffi nella vecchia direzione, non sei pronto a salire.

> Per la pittura "normale" da prop/mini il vero target è **graffi uniformi a grana 400-600**, poi filler primer chiude tutto. Carteggiare a 2000 il PLA "nudo" è quasi sempre uno spreco di tempo se poi ci verniciamo sopra.

---

## 3. Wet vs dry sanding

| | Dry | Wet |
|---|---|---|
| Velocità di rimozione | maggiore | minore |
| Rischio di melting | **alto** sopra 220 grit | basso |
| Polvere | tanta (PPE!) | nessuna (slurry) |
| Vita carta | breve (si intasa) | lunga |
| Visibilità progresso | buona | richiede asciugatura |
| Quando | grane molto grosse (≤180) e lavoro veloce | tutto dal 220-400 in su |

Fonti: [3DSourced — Sanding PLA](https://www.3dsourced.com/guides/sanding-pla/), [3D Insider — Sanding PLA](https://3dinsider.com/sanding-pla-prints/), [Siraya Tech](https://siraya.tech/blogs/news/sanding-3d-prints).

Acqua a temperatura ambiente, eventualmente con una goccia di sapone per piatti per ridurre la tensione superficiale. Asciugare bene fra una grana e l'altra per ispezionare con luce radente.

---

## 4. Strumenti: blocco rigido vs spugna

| Strumento | Quando | Note |
|---|---|---|
| **Blocco rigido** (sughero, plastica, MDF) | superfici **piane** o lievemente convesse | mantiene la planarità, evita "onde" |
| **Sanding sponge / foam pad** | curve, raccordi, dettagli | abrasivo flessibile, si adatta alla geometria |
| **Lime ad ago / detail files** | seam piccoli, fori, supporti residui | controllo locale, no calore |
| **Cabinet scraper** (raschietto) | grandi superfici di PLA | rimuove materiale **senza calore**, suggerito su Reddit/Prusa forum per evitare melting ([Prusa forum](https://forum.prusa3d.com/forum/original-prusa-i3-mk3s-mk3-general-discussion-announcements-and-releases/how-to-best-sand-prints-e-g-when-removing-supports/)) |
| **Sanding stick** (lima a carta multi-grana) | mini, dettagli, gunpla | grana 400/600/800 in un solo strumento |

Errore tipico: usare un blocco rigido su superficie curva — crea sfaccettature piatte. Inversamente, usare solo spugna su superficie piana → "rounding" degli spigoli e ondulazioni.

---

## 5. Errori comuni (citati ricorrentemente)

1. **Saltare grane** → graffi profondi che riappaiono dopo il primer. Fonte: [eQualle](https://equalle.com/blogs/grit-guides/sanding-pla-3d-printed-enclosure-reduce-layer-lines-before-primer).
2. **Troppa pressione** → calore, deformazione, smearing. Pressione leggera + più passate.
3. **Sandpaper a secco oltre la grana 220** → carta che si impasta, layer line "rifuse" sul pezzo.
4. **Non ispezionare con luce radente** → si scopre solo dopo il primer che il pezzo è ancora a "zebra".
5. **Carteggiare dettagli sottili con grana grossa** → si perdono incisioni, panel lines, bordi crisp. Usa lime fini o salta direttamente alla 400 in quelle aree.
6. **Non cambiare direzione fra grane** → impossibile capire quando una grana ha "finito il lavoro".
7. **Carteggiare a 2000 il PLA nudo prima di verniciare** → opinione hobbysta diffusa: spreco. Misurato: nessuno studio Ra trovato che mostri beneficio oltre 600-800 se segue primer/paint.

---

## 6. Quando NON carteggiare (o carteggiare poco)

- Mini con dettagli sub-mm: meglio **filler primer (Mr. Surfacer 1200) → carteggio leggero localizzato** che rischiare di limare via incisioni.
- Pezzi che andranno comunque coperti da resina (XTC-3D, UV resin): un 220 grossolano basta come "grip" prima del coating.
- Texture intenzionali (zigrinature, knurling stampato).

---

## 7. PPE

Anche in wet sanding usa **mascherina** (idealmente FFP2/N95) e occhiali se passi a grane grosse: micro-particelle PLA + acqua = aerosol comunque inalabile. PLA non è particolarmente tossico ma è plastica nei polmoni. Fonte: consenso generale, es. [Sinterit](https://sinterit.com/3d-printing-guide/post-processing-in-3d-printing/sanding-3d-prints/).

---

## 8. Riferimenti scientifici (Ra prima/dopo)

- **Lavoro PMC** sui parametri FDM che influenzano Ra: layer height basso + nozzle diam basso + temp bassa → Ra < 8 µm. [PMC8309545](https://pmc.ncbi.nlm.nih.gov/articles/PMC8309545/).
- **Ironing** (post-process digitale, non sanding) → riduzione Ra ~63% in X, ~72% in Y. [ResearchGate study](https://www.researchgate.net/publication/384103836_An_Experimental_Study_On_The_Effect_Of_Ironing_Process_On_Surface_Roughness_Of_PLA_Parts_Produced_By_FDM_Type_3D_Printer).
- **Trattamenti chimici** → fino a **97% riduzione Ra, 95.85% riduzione Rz** (max riportato; condizioni di lab). [Springer 2025](https://link.springer.com/article/10.1007/s40964-025-01341-9).
- **Slurry impact**: -42% Ra trasversale, -24% longitudinale. [Springer ANFIS model](https://link.springer.com/article/10.1007/s40964-022-00314-6).

> ⚠️ Nota: questi paper misurano **Ra** in laboratorio. Nessuno fra quelli trovati misura specificamente "sanding manuale a grana progressiva 120→2000" su PLA con dati Ra a ogni step → **[da verificare]** se esiste lavoro dedicato.

---

## 9. Workflow consigliato sintesi (per Bambu A1 / PLA / pezzo estetico)

1. Stampare con layer 0.12 o 0.08 mm se possibile (riduce sanding del 50%+).
2. Rimuovere supporti con tronchesi, rifinire con lima/cutter.
3. Grana 220 a umido su tutte le superfici visibili — pressione leggera, blocco/spugna a seconda geometria.
4. Grana 400 a umido — cambio direzione.
5. Ispezione con luce radente. Se ok → primer filler (file 02).
6. Dopo primer asciutto: grana 800 wet → secondo strato primer se serve → 1000-1200 wet → vernice.

Tempo stimato per pezzo grosso (es. cosplay helmet 30 cm): **3-6 ore** di sanding totali distribuite in più sessioni.
