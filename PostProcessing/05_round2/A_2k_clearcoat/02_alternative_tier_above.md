# 02 — Alternative "tier above" al clear coat 1K hobby

Panoramica delle opzioni alternative o complementari a SprayMax 2K, per situazioni in cui la bomboletta 2K non è praticabile (pot life, costo, MOQ piccolo, mancanza setup) o per casi specifici (effetto vetroso, glaze profondo, costo zero).

---

## 1. Tabella riassuntiva alternative

| Soluzione | Tipo | Applicazione | Hardness/Durata | UV protection | Prezzo EU | Pro | Contro |
|---|---|---|---|---|---|---|---|
| **Spies Hecker Permasolid 8800 + hardener** | 2K PU automotive pro | Pistola HVLP | 3H+, anni outdoor | Eccellente (HALS+UVA) | 80-120 €/kit | Standard body shop, qualità top | Serve pistola HVLP + compressore + cabina |
| **Standox Standocryl VOC Clear 2K** | 2K PU automotive pro | Pistola HVLP | 3H+, anni outdoor | Eccellente | 90-130 €/kit | Stesso livello di Spies Hecker | Idem |
| **UV resin clear sottile** (Anycubic UV Clear, Smooth-On XTC) | Mono-componente UV / 2K epossi | Pennello | Variabile, gloss vetroso | **Scarsa (ingiallisce!)** | 20-40 € | Effetto resin gloss profondo | Yellowing visibile in mesi, pennellate |
| **Smooth-On XTC-3D** | Epossi 2K manuale | Pennello | Dura, autolivellante | Scarsa | ~35 €/350 g | Riempie layer lines, gloss | Spessore alto, pot life 10 min |
| **Varathane Crystal Clear** (Rust-Oleum) | PU water-based 1K | Pennello / spray | Media, "deep glaze" | Decente (con HALS additivati) | 15-20 € / 946 ml | Costo basso, applicazione facile | Tempo cura lungo, build spesso |
| **Minwax Polycrylic** | PU water-based 1K | Pennello | Media | Limitata | 15-20 € / 946 ml | Alternativa US-style a Varathane | Reperibilità IT scarsa |
| **Pledge Floor Care (ex Future)** | Polish acrilico water | Pennello / airbrush / dip | Bassa-media | **Nessuna** | 8-12 € / 750 ml | Economicissimo, autolivellante | Solo finish gloss, no UV, fragile |
| **PROtect QuickSilver Iron** | Ceramic coating auto | Pennello + applicatore | Altissima | Eccellente | 50-80 € / 30 ml | Hardness ceramica, anni di durata | Non testato su PLA, richiede flash off precisi |
| **Cerakote Cosmetic** | Ceramic-poly | Spray + **forno** | Estrema | Eccellente | 50-100 €/kit | Industry standard armi/utensili | **Richiede cura 90-150 °C → no PLA** |
| **Liquitex Soluvar Varnish** | Vernice artistica (mineral spirit) | Pennello | Bassa-media | Buona | 18-25 € | Removibile per restauro (reversibile) | Per quadri, troppo morbida per touchpoint |
| **Krylon Triple-Thick Crystal Clear Glaze** | Acrilico spesso | Spray | Media | Limitata | 10-12 € | Effetto "resin look" con bomboletta | Cola facile, no UV serio |

---

## 2. 2K automotive pro applicato via pistola HVLP

### Quando ha senso
- Volume **>20 pezzi/lotto** (la pistola HVLP richiede tempo setup/cleanup che si ammortizza solo su batch).
- Pezzi grandi (>20 cm) dove l'aerosol non basta o spreca troppo.
- Si dispone già di compressore + pistola HVLP + zona di spruzzo.

### Setup minimo
- Compressore 50 L, 8 bar, almeno 200 L/min FAD.
- Filtro deumidificatore + filtro coalescente (acqua nell'aria = clear coat rovinato).
- Pistola HVLP gravity feed, ugello 1.3-1.4 mm (es. SATA Jet 3000 economic, Devilbiss FLG-5, oppure clone Iwata-like ~80 €).
- Cabina di spruzzo (o box pieghevole + estrattore) — minimo legale per attività hobby in casa, ma **importante per qualità: zero polvere**.

### Prodotti consigliati
- **Spies Hecker Permasolid HS Clear Coat 8800** + hardener appropriato per temperatura ambiente.
- **Standox Standocryl VOC Clear K9580** + hardener.
- **U-POL S2080 2K HS** — più economico, prestazioni leggermente sotto, ma ottimo per maker.

Costo a pezzo: una volta investiti i ~600-1000 € di attrezzatura iniziale, il **costo materiale per pezzo scende a 0.50-1.50 €** (rispetto ai 2.50-4 € della bomboletta SprayMax). ROI break-even ~300-500 pezzi.

Fonti: forum AutoBody101 (https://www.autobody101.com), tutorial Refinish Network (https://refinishnetwork.com), YouTube "Refinish School" e "Paint Society".

---

## 3. UV resin clear sottile come clear coat — pro/contro

### Concetto
Stendere un velo sottile di **resina UV trasparente** (stessa famiglia delle MSLA stampanti) sul pezzo verniciato, poi curare con lampada UV 405 nm.

### Prodotti
- **Anycubic UV Resin Clear** (https://www.anycubic.com): ~25 €/L. Diluibile con isopropanolo per layer sottili (1:5 in volume) [da verificare con test compatibilità acrilico sottostante].
- **Elegoo Standard Clear**: ~25 €/L, simile.
- **Siraya Tech Blu / Tenacious Clear**: ~40 €/L, low yellowing claim più credibile (formulazione modificata).
- **Smooth-On XTC-3D** (epossi 2K, NON UV): ~35 €/350 g. Mix 1:1, pot life 10 min, gloss profondo. Non è "UV resin" ma è in stessa categoria "resin clear coat".

### Pro
- Effetto "vetroso" / glaze profondo, impossibile da ottenere con vernice.
- Build spesso possibile (riempimento layer lines residue).
- Cura istantanea in lampada UV (10-30 min) — niente attesa di settimane.

### Contro **importanti**
- **Yellowing reale**: anche le resine "non-yellowing" commercial-grade ingialliscono visibilmente in 6-24 mesi sotto luce ambientale. Per un prodotto commerciale **bianco** è inaccettabile.
- Applicazione a pennello / autolivellante: difficile uniformità su geometria complessa.
- Spessore difficile da controllare: facilmente "gocciola" su bordi/sottosquadri.
- Compatibilità con acrilico sottostante **non sempre testata**: alcune resine sono leggermente acide a pH e possono attaccare vernici cure-incomplete.
- Cura UV richiede esposizione uniforme — pezzo grande va ruotato/multiplo passaggio in lampada.

### Verdetto
**UV resin coat = non valida alternativa al 2K per uso commerciale generico**. Utile per:
- Effetti speciali deliberati (look vetroso, gemme finte, "wet rock").
- Cosplay / prop dove pochi mesi di vita sono sufficienti.

Non per: prodotti bianchi/chiari da vendere, oggetti display-shelf, qualsiasi cosa con orizzonte >12 mesi.

Fonti: post Smooth-On forum su XTC-3D yellowing, Reddit r/3Dprinting threads "UV resin as clear coat", YouTube "3D Printing Pro" review.

---

## 4. Varathane Crystal Clear (water-based PU 1K)

### Cosa è
Poliuretano water-based monocomponente, formulato per **finitura legno interni**. In USA è citato come trick maker per "deep glaze look" su stampe 3D.

### Caratteristiche
- 1K, no isocianato, sicurezza casalinga buona.
- Water-based: bassi VOC, lavabile fino a cura.
- Build pennello buono: 3-4 mani danno effetto "glass coat" superficiale.
- Tempo cura: 2 h tape-free, 24 h light handling, 7-30 giorni full hardness.
- UV protection: dichiarata "HALS additivata" sui claim Rust-Oleum, ma **inferiore al 2K** (1K water + HALS è il livello di vernice mobili interni, non automotive).
- Hardness finale: ~F-2H (intermedio).

### Reperibilità EU
**Difficile**: Varathane è linea Rust-Oleum USA, in Italia poco presente. Equivalenti EU:
- **Bondex Acquaragia Trasparente** (Bondex, https://www.bondex.it).
- **V33 Vernice Parquet Idro** — gamma DIY Leroy Merlin / Bricoman.
- **Bona Mega Clear HD** (mercato pavimenti professionali).
- **Sikkens Cetol HLS Plus** (Akzo Nobel, https://www.sikkens.it).

### Caso d'uso utente
Buon compromesso per **display interno + costo basso + scelta sicura senza isocianati**, dove però la durabilità non è critica come per il 2K. Applicazione a pennello fine o aerografo (diluire 10-20 % con acqua deionizzata).

Fonti: Rust-Oleum technical data sheet Varathane Crystal Clear, https://www.rustoleum.com; FineHomebuilding.com "Water-based vs oil-based polyurethane" article; Sikkens technical info Italia.

---

## 5. Pledge Floor Care (ex "Future") — il trick storico delle miniature

### Cosa è
**Pulitore-lucidante per pavimenti** a base acrilica autolivellante. Il prodotto vero non è venduto come vernice — è un detergente con polimero acrilico in soluzione. Tuttavia, per decenni è stato usato dai modellisti per layer di gloss perfettamente liscio sotto i decal.

### Caratteristiche
- Acrilico water-based, autolivellante.
- Applicazione: pennello, immersione (dip), airbrush diluito 1:1 con acqua.
- Asciuga "polvere-free" in 30 min, ricoatabile in 2 h.
- Cura completa 24 h.
- **Hardness bassissima** (~HB): si graffia con unghia.
- **Nessuna UV protection**.
- Costo: 8-12 € / bottiglia da 750 ml. Una bottiglia tratta letteralmente centinaia di pezzi.

### Quando usarlo
- Base intermedia gloss prima dei decal/transfer.
- "Gloss istantaneo" su selective gloss (occhi gemme) tramite pennello fine.
- **Mai come finish finale** per prodotti commerciali touchpoint o outdoor.
- Backup economico durante prototipazione.

### Reperibilità IT
Pledge è ridotta come gamma in Italia. Alternative funzionalmente equivalenti:
- **Vif Pavimenti Brillanti** (Henkel).
- **Mr. Proper Pavimenti Lucidante**.
- **Pronto Bagno Brilla** (alcune varianti).

Attenzione: la formulazione **cambia tra paesi** (Pledge USA ≠ Pledge UK ≠ Pledge IT). Il trick "Future" originale era specifico al prodotto USA Future Floor Wax pre-rebranding. **Verificare etichetta**: deve contenere "acrylic resin" o "polimero acrilico", non solo "tensioattivi".

Fonti: storica thread Britmodeller "Future floor polish use", Squidmar YouTube "Cheap gloss trick", r/minipainting wiki.

---

## 6. Cerakote Cosmetic / PROtect / ceramic coating auto

### Cerakote Cosmetic
- Standard industria armi/utensili. Hardness estrema (~9H), UV+chimica resistance top.
- **Cura: 90-150 °C in forno per 1-2 h** → **incompatibile con PLA** (Tg 60 °C).
- Esiste linea "Cerakote H-Series Air Cure" (cura ambiente), ma le prestazioni sono inferiori e la disponibilità EU è scarsa.

### PROtect QuickSilver Iron e coating "9H ceramic"
- Coating ceramici nano-SiO₂ originariamente automotive.
- **Possibilità reale** di applicarli su clear coat 2K curato come **topcoat finale** per anti-graffio + idrofobicità.
- Hardness percepita 9H, ma su substrato plastico la performance reale dipende dal supporto (vedi caveat al §1 di `01_spraymax_2k_deep_dive.md`).
- Costo: 50-80 €/30 ml, ne bastano poche gocce per pezzo.
- Applicazione: panno microfibra, applicatore in spugna, 2-3 mani.
- Cura: 12-24 h.

### Caso d'uso utente
**Topcoat di protezione su pezzi premium commerciali**: 2K SprayMax come clear strutturale + ceramic coating come "hydrophobic barrier" finale. Costo aggiuntivo ~0.50 €/pezzo, effetto cliente "wow" (acqua scivola, impronte si puliscono).

Fonti: GTECHNIQ technical info (https://gtechniq.com), Cerakote H-Series datasheet (https://www.cerakote.com), Reddit r/Detailing thread su ceramic coating su plastica.

---

## 7. Matrice decisionale finale

| Caso d'uso | Soluzione primaria | Soluzione alternativa | Da escludere |
|---|---|---|---|
| **Commerciale outdoor / vetrina sole** | SprayMax 2K + ceramic topcoat | 2K HVLP pro (se volume alto) | UV resin, Pledge, Varathane economico |
| **Commerciale display interno premium** | SprayMax 2K | Mr. Super Clear UV Cut + Sikkens HLS | Pledge come finish |
| **Commerciale entry-level (€<20)** | Mr. Super Clear UV Cut | Krylon UV-Resistant | 2K (overkill) |
| **Personale display** | Mr. Super Clear UV Cut | Vallejo Polyurethane | UV resin |
| **Effetto vetroso deliberato** | UV resin sottile (Siraya Blu) | XTC-3D (epossi) | — |
| **Prototipo / costo zero** | Pledge / Future | Varathane water-based 1K | — |

---

## 8. Fonti

- Spies Hecker product range: https://www.spieshecker.com
- Standox by Axalta: https://www.standox.com
- U-POL Group: https://www.u-pol.com
- Smooth-On XTC-3D: https://www.smooth-on.com/products/xtc-3d/
- Anycubic UV resin: https://www.anycubic.com/collections/3d-printer-resin
- Siraya Tech Blu: https://sirayatech.com
- Rust-Oleum Varathane: https://www.rustoleum.com
- Sikkens Italia: https://www.sikkens.it
- Bondex Italia: https://www.bondex.it
- Gtechniq ceramic coating: https://gtechniq.com
- Cerakote H-Series Air Cure: https://www.cerakote.com/coatings/h-series
- Reddit r/Detailing thread "Ceramic on plastic": https://www.reddit.com/r/Detailing/
- Reddit r/3Dprinting thread "Clear coat alternatives for PLA": https://www.reddit.com/r/3Dprinting/
- FineHomebuilding "Comparing polyurethane finishes": https://www.finehomebuilding.com
- BoatDesign.net forum "1-part vs 2-part urethane": https://www.boatdesign.net
