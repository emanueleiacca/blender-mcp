# 03 — Foto prodotto indie premium DIY (€0 setup)

**Obiettivo**: 6-shot listing Etsy/Shopify livello "indie premium" senza fotografo, senza camera reflex, senza software pagato. Solo smartphone + luce naturale + cartoncino.

Da R2-D `03_end_to_end_timeline.md` §2 Top-3 ROI: **foto + listing = leva ROI marginale più alta**. Investimento 4h una tantum + ~€20 ripaga in 10 pezzi.

---

## 1. Setup hardware costo €0–20

### 1.1 Base (€0)

| Componente | Sorgente DIY | Note tecniche |
|---|---|---|
| Camera | Smartphone (2020+) | iPhone 11+ / Pixel 5+ / Galaxy S20+ hanno sensore sufficiente. Modalità "Pro/RAW" se disponibile. |
| Luce principale | **Finestra grande, lato N** (luce diffusa stabile) | Lato N = no diretto, stabile tutto il giorno. Lato E/O = solo mattina/sera. |
| Diffusore | Tenda bianca leggera + finestra | Se sole diretto colpisce, tira la tenda. Carta forno A3 anche bene. |
| Bounce fill | Cartoncino A4 bianco (qualsiasi cartoleria) | Posizionato 30–45° opposto alla finestra. |
| Bounce nero (negative fill) | Cartoncino A4 nero | Aumenta contrasto, scava ombre. |
| Sfondo bianco | Foglio cartone presentation 70×100 cm bianco (€2 cartoleria) | Curva infinito: piega senza strappare il foglio. |
| Sfondo nero | Foglio cartone presentation 70×100 cm nero (€2) | Idem |
| Sfondo legno | Tagliere IKEA APTITLIG €8 o piano di vero legno | Texture reale, no carta finto-legno (si vede). |
| Sfondo travertino/marmo | Carrelage Brico campione gratuito | Chiedi campioni gratis Leroy Merlin. |
| Tripode | Pila libri + elastico, oppure tripod smartphone €8 Aliexpress | Anti-mosso essenziale per macro. |

**Totale**: **€2–20** se acquisti tutto. **€0** se ricicli.

### 1.2 Upgrade opzionale (€15–30)

| Componente | Costo | Sorgente | Quando serve |
|---|---:|---|---|
| LED ring 26 cm con tripod | 15–20 € | Aliexpress | Foto serali / inverno / poca luce naturale |
| Light tent 60 cm PULUZ | 25–35 € | Aliexpress (R2-F) | Whitebox ortho consistente, evita riflessi |
| Mini turntable IKEA SNUDDA / DIY | 5–15 € | IKEA (no più in catalogo, alternative: cuscinetti lazy susan Brico €8) | Video 360 + foto multi-angle |
| ColorChecker DIY (PDF stampato) | 0.50 € | Stampa colore A4 + carta fotografica | Color calibration |

**Cross-ref**: R3-C `02_lightbox_cardboard.md` (light box DIY cartone €3), R2-F `08_lighting_photo_setup.md`.

---

## 2. Color management DIY (ColorChecker free)

### 2.1 Il problema

PLA bianco fotografato senza riferimento appare **giallastro** (warm cast finestra mattina) o **bluastro** (luce ombra nord). Il cliente vede una foto, riceve il pezzo, lo trova "diverso" → resi.

### 2.2 Soluzione free

**ColorChecker PDF DIY** scaricabile:
- BabelColor "Free Color Patches": https://babelcolor.com/colorchecker.htm (link "Macbeth CC reference values")
- Stampato a colori su carta fotografica matte A4 (€0.50 fotocopia).
- Posizionato nel frame della prima foto di ogni sessione.

**Workflow color management**:
1. Scatto 1 = pezzo + ColorChecker DIY nel frame.
2. Apri in Lightroom Mobile FREE.
3. White balance picker → click sul patch grigio neutro (3° riga, 4° quadrato).
4. Salva come preset.
5. Applica preset batch a tutte le altre foto della sessione.

**Limite DIY**: stampa casalinga ha precisione cromatica limitata (~Δ-E 5–8 vs ColorChecker pro Δ-E 1–2). Sufficiente per **consistenza tra foto del proprio catalogo**, non per riproduzione cromatica assoluta. Per il nostro use case (Etsy/IG) è OK.

**Upgrade futuro**: X-Rite ColorChecker Passport Photo 2 (€100–130) o Datacolor SpyderCheckr 24 (€80) — solo se vendi >100 pezzi/mese.

### 2.3 Lightroom Mobile FREE

- Versione gratis sufficiente per: WB, exposure, contrast, crop, presets, batch.
- **Adobe Lightroom Mobile**: https://www.adobe.com/it/products/photoshop-lightroom/mobile.html
- Funzioni a pagamento (€10/mese): selective edits, healing, cloud sync — **non necessarie** per listing prodotto.

**Alternative free**:
- **Snapseed** (Google, totalmente free, https://snapseed.online/): selective edits gratis.
- **VSCO** free: presets film-look, limitato.
- **GIMP** desktop free: per editing avanzato batch.
- **Darktable** desktop free: open source equivalente di Lightroom.

---

## 3. Le 6 shot del listing (composizione)

Base R2-D già definita. Qui aggiungiamo **narrative function** di ogni shot.

### 3.1 Shot 1 — Hero shot drammatica

**Funzione**: cattura attenzione 0.3 sec scroll Etsy/IG. Decide il click.

| Parametro | Setting |
|---|---|
| Luce | Laterale 80–90° (finestra di lato), 1 m distanza |
| Bounce | Nero su lato finestra (negative fill) per accentuare ombre |
| Sfondo | Tinta unita scura (nero, blu navy, verde bottiglia) — il pezzo "esce" |
| Composizione | Regola dei terzi: pezzo su intersezione |
| DOF | Portrait mode smartphone → blur sfondo (anche se è già scuro/tinta unita aiuta) |
| Angolo | Leggermente sotto (5–15°) per "monumentalità", pezzo sopra l'occhio cliente |
| Storytelling | Texture marmorino/encausto **visibilissima** in luce radente, drammatica |

**Hero shot recipe operativa**:
1. Finestra lato sinistro pezzo.
2. Cartoncino nero a 30 cm dal pezzo lato destro (negative fill).
3. Sfondo: cartone presentation nero o vassoio in ardesia.
4. Smartphone in portrait mode, 50–80 cm dal pezzo, leggermente sotto.
5. Tocco su pezzo per AF + AE.
6. Riduci esposizione -0.3 / -0.7 EV (più drammatico, salva highlights).
7. Scatta 5–10 varianti.

### 3.2 Shot 2 — Ortho whitebox catalogo

**Funzione**: foto "neutra" che dice "ecco il prodotto come è". Etsy thumbnail standard.

| Parametro | Setting |
|---|---|
| Luce | Diffusa 360° (light tent + LED, o finestra + cartoncino bianco grosso 3 lati) |
| Sfondo | Bianco puro |
| Angolo | Frontale, dritto, orizzonte perfetto (livella smartphone) |
| Crop | Pezzo centrato, margine 15% bordo |
| Editing | Sfondo "pulito" a bianco puro: Snapseed → Selective → bianco 100. Oppure semplicemente exposure +0.3 EV su sfondo già chiaro |

### 3.3 Shot 3 — Detail macro

**Funzione**: dimostrare la **qualità della finitura**. Marmorino texture, shellac brillantezza, kaolin opacità, gesso bolognese trasparenza dello strato dorato.

| Parametro | Setting |
|---|---|
| Distanza | 10–15 cm (macro mode smartphone se disponibile) |
| Luce | Radente 70–80° (esalta texture 3D) |
| DOF | Tap-to-focus sul dettaglio, lascia sfocato il resto |
| Crop | Texture occupa 60–80% frame |
| Storytelling | "Vedi le pennellate". Garofalo trafilato bronzo style — il processo si vede |

**Trick smartphone macro**: aggiungi una lente clip-on macro €5 Aliexpress se il tuo smartphone non ha macro nativo (iPhone <13, Galaxy <S21).

### 3.4 Shot 4 — Scala (oggetto familiare)

**Funzione**: il cliente capisce **quanto è grande**. Etsy mostra dimensioni in cm/inch ma il cervello processa **oggetti familiari**.

| Oggetto comparativo | Quando usarlo | Effetto |
|---|---|---|
| Tazzina caffè espresso | Decor 10–20 cm | "Italian touch", giorno |
| Mano (la tua) | Decor 8–25 cm | Scala umana, intimità |
| Libro paperback | Decor 15–25 cm | Reading/study room context |
| Coltello tavola standard | Decor 15–25 cm | Scale industriale |
| Smartphone (modello generico) | Decor 8–15 cm | Universale |
| Pianta houseplant (pothos foglie) | Decor 10–30 cm | Lifestyle, soft |

**Evita**: monete (etsy bandisce monete come scala? — no, ma sembra "manuale eBay 2008"), gente intera (toglie focus), animali (cuteness ruba scena).

### 3.5 Shot 5 — Lifestyle (in situ)

**Funzione**: cliente proietta il pezzo **nel suo spazio**. Più persuasivo di qualsiasi descrizione.

| Setup | Audience target |
|---|---|
| Scaffale libreria sopra divano | Living minimal middle-class |
| Comodino con lampada + libro | Camera da letto, intimità |
| Mensole bagno con asciugamani arrotolati | Bagno spa (perfetto per marmorino) |
| Scrivania con MacBook + caffè | Work-from-home, professionista |
| Mensola cucina con vasi terracotta | Cucina toscana style |
| Mensola con piante (monstera, pothos) | Plant lover, urban jungle |

**Trick low-cost**: usa **casa tua** o **casa di un amico fotogenica**. Riarrangia 1–2 oggetti per "ambientazione coerente al target". Non serve set design, serve **1 angolo curato**.

**Composizione lifestyle**:
- Pezzo in posizione "secondaria" del frame (non centro), come "scoperto per caso".
- 2–3 oggetti contestuali (libro, candela, pianta).
- Luce naturale finestra, no flash.
- Crop verticale 4:5 (Instagram-friendly) o 1:1.

### 3.6 Shot 6 — Packaging / unboxing

**Funzione**: anticipa l'esperienza di ricezione, riduce ansia "arriverà rotto?", aumenta perceived value.

Da `04_sealing_presentation/05_packaging_brand_experience.md` (R1) + sezione 06 di questo round.

| Elemento da inquadrare | Effetto |
|---|---|
| Scatola brand chiusa con sticker sigillo | "C'è un brand, non Amazon generico" |
| Tissue paper aperto, pezzo dentro nido foam | "Lo curano, arriva bello" |
| Thank-you card visibile (scritta a mano se possibile) | "Persona reale, non factory" |
| Pezzo + tutto il contenuto del pacco "flat lay" | Riassunto unboxing completo |

**Composizione flat-lay**: tutto su sfondo neutro (legno, cemento, lino), vista dall'alto perpendicolare (90°), luce diffusa.

---

## 4. Workflow editing Lightroom Mobile FREE

### 4.1 Preset master (una tantum, 30 min setup)

Crea un preset "Brand Catalogue v1" che applica:
- **White balance**: shot calibrato + ColorChecker.
- **Exposure**: +0.2 EV (foto smartphone tendono sotto-esposte indoor).
- **Highlights**: -20 (salva texture).
- **Shadows**: +15 (apre dettagli ombra senza spegnere drammaticità).
- **Whites**: +10.
- **Blacks**: -5 (contrasto pulito).
- **Clarity**: +10 (mid-tone contrast = texture viene fuori).
- **Vibrance**: +8 (no Saturation che distorce).
- **Sharpening**: 40–50, masking 30 (evita aloni).

Salva come preset. Applica batch a tutte le foto di una sessione → **consistenza catalogo**.

### 4.2 Spot retouch (Snapseed FREE)

Per pulizia puntuale (polvere, capelli, riflessi):
- **Snapseed** → Healing tool → tap sulla macchia.
- 10 sec per foto, gratis, qualità Photoshop-like su singoli ritocchi.

### 4.3 Background cleanup

Per shot 2 whitebox dove sfondo non è bianco puro:
- Lightroom Mobile → Color Mix → White → Luminance +30.
- Oppure Snapseed → Selective → tap sfondo → Brightness +50.
- **NON** usare AI background remover (look artificiale, edge sharp innaturale).

### 4.4 Export

Etsy/Shopify accettano JPG fino a 8 MB.
- Risoluzione: **2000–3000 px lato lungo** (Etsy zooma fino a 3000 px).
- Quality: **85%** (sweet spot quality/size).
- Formato: JPG sRGB.
- Naming: `nomeSKU_01_hero.jpg`, `nomeSKU_02_ortho.jpg`, ...

---

## 5. Tabella riassuntiva 6-shot

| Shot | Funzione | Setup luce | Sfondo | Tempo scatto | Tempo edit |
|---|---|---|---|---:|---:|
| 1. Hero | Click trigger | Laterale + neg fill | Scuro tinta unita | 5 min | 3 min |
| 2. Ortho | Thumbnail catalogo | Diffusa 360° | Bianco | 3 min | 2 min |
| 3. Detail macro | Qualità finitura | Radente | Tinta unita | 5 min | 2 min |
| 4. Scala | Comprensione size | Diffusa | Neutro | 3 min | 1 min |
| 5. Lifestyle | Proiezione cliente | Finestra naturale | Casa target | 8 min | 3 min |
| 6. Packaging | Anticipo unboxing | Diffusa flat-lay | Legno/lino | 5 min | 2 min |
| | | | **Totale** | **29 min** | **13 min** |

**Con setup permanente + preset** (post-setup iniziale 4h): tempo scatto + edit per pezzo nuovo: **8–10 min totali** (vs 45 min senza setup). Da R2-D §2.

---

## 6. Errori comuni (skip these)

- **Foto sul tavolo cucina con tovaglia colorata** → distrae, colori sballati, look amateur.
- **Flash smartphone** → mai. Ombre dure, riflessi su gloss, colori sparati.
- **Filtri Instagram tipo "Clarendon"** → snatura colori, cliente vede pezzo "diverso".
- **Editing eccessivo HDR/saturation** → look "AliExpress photoshoppato", abbassa trust.
- **Foto verticali 9:16 su Etsy** → Etsy thumbnail orizzontale, viene tagliato.
- **Sfondo trasparente PNG cutout** → look e-commerce mass, anti-handmade.
- **Mostrare difetti reali "per onestà"** → no, mostra il pezzo nella **versione migliore della media**. Descrizione spiega variazioni naturali.
- **Watermark grosso al centro** → riduce conversion del 15–25% [stima consensus Etsy seller forum]. Se proprio servono, piccolo in angolo, opacità 30%.

---

## 7. Fonti

- **Karl Taylor**, free product photography tutorials: https://www.karltaylorphotography.com/ + YouTube.
- **Peter McKinnon**, smartphone product video: https://www.youtube.com/@PeterMcKinnon
- **Photofocus**, tutorial product DIY: https://photofocus.com/tag/product-photography/
- **BabelColor ColorChecker** values: https://babelcolor.com/colorchecker.htm
- **Adobe Lightroom Mobile** (free tier): https://www.adobe.com/it/products/photoshop-lightroom/mobile.html
- **Snapseed**: https://snapseed.online/
- **Etsy Seller Handbook** product photography: https://www.etsy.com/seller-handbook/article/the-ultimate-guide-to-photographing/22300023870
- Reddit r/Etsy thread "best free photo editing apps": https://www.reddit.com/r/Etsy/search/?q=photo+editing
- **Pat Flynn** product photography for makers (vari ep. Smart Passive Income).
