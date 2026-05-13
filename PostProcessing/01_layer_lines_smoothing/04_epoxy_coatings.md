# 04 — Epoxy & UV Resin Coatings

> Idea base: coprire il PLA con uno strato **fluido auto-livellante** che cura duro. Il liquido si rifugia nelle "valli" delle layer lines e crea una superficie quasi liscia senza dover carteggiare per ore.

## Prodotti principali

| Prodotto | Tipo | Tempo lavoro | Cure full | Pro | Contro | Prezzo indicativo |
|---|---|---|---|---|---|---|
| **Smooth-On XTC-3D** | epoxy 2-part 2:1 (resin:hardener) | ~10 min open time | 4 h tack-free, 24 h full | self-level, no melting, sandabile dopo cure, applicabile a pennello | può colare in dettagli, pooling in concavità, va lavorato in fretta | 30-45 € / 644 g kit |
| **Smooth-On EpoxAcoat** | epoxy 2-part (gel coat) | ~30 min | ~16 h | strato spesso, ideale come "skin" per mold | troppo spesso per dettagli fini | 60-80 € / 1 kg kit |
| **UV resin (varie marche: Anycubic, Elegoo, Bondic)** | mono-componente fotocurabile | infinito finché non illumini | 5-60 s sotto UV 405 nm | cura on-demand, sub-strati sottili, lavoro senza fretta | più costoso per area grande, sensibile a inibizione ossigeno (sticky surface) | 20-40 € / 500 ml |
| **Sophisticated Finishes / fai-da-te epoxy clear** | clear epoxy "table top" | 20-30 min | 24-72 h | cheap su grandi superfici | molto fluido, drip control, lungo cure | 25-40 € / kit 500 ml |

Fonti: [Smooth-On XTC-3D product page](https://www.smooth-on.com/products/xtc-3d/), [MatterHackers tutorial](https://www.matterhackers.com/articles/how-to-smooth-and-finish-3d-prints-with-xtc-3d), [Makezine review](https://makezine.com/article/digital-fabrication/3d-printing-workshop/review-smooth-xtc-3d-brush-coating-3d-printed-parts/), [Xometry overview](https://www.xometry.com/resources/3d-printing/xtc-3d/), [Hackaday UV resin smoothing](https://hackaday.com/2018/03/08/3d-printering-print-smoothing-tests-with-uv-resin/), [Hackaday UV resin 2022](https://hackaday.com/2022/01/04/uv-resin-perfects-3d-print-but-not-how-you-think/).

---

## XTC-3D — dettagli

- Mix 2 (A) : 1 (B) per peso, **mescolare bene 1-2 min**.
- 28 g coprono ~600 cm² (1 oz / 100 in²) → economico.
- Stendere a pennello morbido, in mani sottili. Lavorare in fretta (open time 10 min).
- Posizionare il pezzo con dettagli verso il basso o ruotarlo per evitare drip nelle concavità.
- Dopo 4 h è "tack-free", a 24 h è sandable (200→400→600).
- Risultato tipico: layer lines a 0.1 mm quasi invisibili in una sola passata; a 0.2 mm spesso serve doppia passata + carteggio intermedio.

### Pro / Contro vs sanding puro

| | Sanding puro + filler primer | XTC-3D |
|---|---|---|
| Tempo manuale | 3-6 h per pezzo medio | 30 min applicazione + 24 h attesa |
| Costo per pezzo | basso | medio (~3-5 € di prodotto) |
| Dettaglio mantenuto | alto (se carteggi piano) | rischio annegamento dettagli sottili (<0.5 mm) |
| Adatto a curve organiche | medio | **eccellente** (helmet, maschere, sculpt) |
| Adatto a superfici piane grandi | sì | rischio "pooling" e disuniformità |
| Hand strength richiesto | tanto | basso |
| Sicurezza | medio-alta (mascherina, no chimica forte) | medio (epossidico = sensibilizzante cutaneo, ventilare) |

Citato da [RPF thread Bondo vs XTC-3D](https://www.therpf.com/forums/threads/bondo-or-xtc-3d-on-3d-printed-blaster-parts-which-one-works-better.253981/): split fra "Bondo per piani, XTC-3D per curve". Consenso.

---

## UV resin — approfondimento

Tecnica "[print-smoothing] con UV resin" raccomandata da Hackaday:

1. Mix base: UV resin (qualsiasi marca per LCD MSLA va bene) + opzionalmente **baby powder/talco** (rapporto 2:1) per stenderla più ferma e meno colante.
2. Pennello morbido, sezione per sezione (10-20 cm² alla volta).
3. Cura con torcia UV 405 nm (5-60 s a seconda spessore e potenza).
4. Carteggiare leggero fra mani per **scuffing** (la resina cura "vetrosa" e non aggrappa bene una seconda mano se non scuffi).
5. Surface "sticky" finale → inibizione ossigeno: lavare con IPA o esporre più a lungo alla UV.

### Pro / Contro UV resin

| Pro | Contro |
|---|---|
| Cura controllata (no fretta) | costosa su grandi superfici |
| Mani sottilissime possibili | sticky surface da gestire |
| Eccellente nei dettagli | non strutturale come epoxy |
| Set 5-60 s | irritante cutaneo, **PPE obbligatorio** |

Fonti tecnica: [Hackaday print-smoothing tests UV resin](https://hackaday.com/2018/03/08/3d-printering-print-smoothing-tests-with-uv-resin/), [3D Printr.com — resin + baby powder](https://www.3printr.com/maker-shows-how-to-smooth-3d-printed-surfaces-with-resin-and-baby-powder-2665243/).

> ⚠️ UV resin liquida è **sensibilizzante** (può causare allergia permanente con esposizione ripetuta a pelle). Guanti nitrile sempre, niente contatto cute.

---

## Quando scegliere coating epoxy/UV vs sanding/primer

| Caso | Migliore tecnica |
|---|---|
| Helmet, maschera, prop con curve organiche grandi | **XTC-3D** + light sand + primer + paint |
| Mini ad alto dettaglio (28-32 mm) | **NO XTC-3D** (annega dettagli) → sanding leggero + Mr. Surfacer 1200 |
| Prop con dettagli da preservare (es. weapon greebles) | UV resin **localizzata** sui piani lisci, sand sui dettagli |
| Superfici piane grandi (pannelli) | filler primer + sanding (più predictable) |
| Pezzo che dovrà essere stagno / impermeabile | XTC-3D (sigilla) |
| Pezzo che deve restare flessibile | nessuno dei due (resta in PLA carteggiato) |

---

## Workflow ibrido consigliato (curve organiche, prop cosplay)

1. Sand 220 wet su tutto (per rimuovere i picchi).
2. **XTC-3D mano 1**, sottile, asciutta 24 h.
3. Sand 400 wet sulle aree con drip o pooling.
4. (Opzionale) XTC-3D mano 2 se layer lines ancora visibili.
5. Sand 600 wet.
6. Filler primer (Rust-Oleum/Tamiya) come base pittura.
7. Sand 800-1000 wet.
8. Verniciatura.

---

## Disaccordi / da verificare

- "XTC-3D è meglio di Bondo per blaster": opinioni split (RPF thread linkato sopra). **[da verificare con test misurato]**.
- "UV resin + baby powder dà la stessa finitura di XTC-3D a costo inferiore": affermazione hobbystica ([Hackaday 2018](https://hackaday.com/2018/03/08/3d-printering-print-smoothing-tests-with-uv-resin/)), nessun dato Ra trovato.
- Tempi cure XTC-3D in ambienti freddi (<18 °C): possono superare le 24 h dichiarate. **[da verificare]**.
