# Master Template — Gemini cleanup per AI image-to-3D

Template di base per pre-processare 1 foto di un manufatto decorativo artigianale, da dare poi a un tool image-to-3D (Tripo / Hi3D / Hunyuan / Meshy / Rodin) via MakerLab o web app dedicata.

## Quando usarlo

- Hai 1 foto del soggetto, scattata con cellulare
- Vuoi un'immagine pulita e canonica come input al tool 3D

## ⚠️ Cambiamento 2026-05-13 — Affirmative framing

Gemini 2.5/3 e Imagen 3+ **non interpretano correttamente** prompt con stacking di "MUST NOT". Best practice 2026 (Google AI docs):
- **Affirmative framing**: trasformare ogni "MUST NOT X" in "MUST be empty of: X" o "MUST show only: Y"
- **Single-variable iteration**: cambia 1 cosa per re-prompt, mai stacking di correzioni
- **Re-upload last good image**: per fix incrementali, ri-carica l'immagine "buona" come nuova source — non ricominciare da zero
- **Aspect ratio anchor verbatim**: includere `"Do not change the input aspect ratio."` (frase ufficiale Google)

Vedi `README.md` § Iteration protocol per il dettaglio.

## Prompt (copia-incolla in Gemini)

```
You are preparing a single reference image for an image-to-3D AI tool.
The subject in the photo is a HANDCRAFTED DECORATIVE ARTIFACT
(ceramic, terracotta, carved wood, hammered metal, or similar).
The downstream goal is FDM 3D printing in single color, so only the
SCULPTED GEOMETRY matters — colors, paint, and surface texture will be discarded.

=== INPUT ASPECT RATIO LOCK ===
Do not change the input aspect ratio.
Preserve the original silhouette and proportions of the subject EXACTLY
(width/height ratio within ±5% of source).

Produce ONE output image with these properties:

GEOMETRY & FRAMING
- Single 3/4 frontal view, camera slightly above eye level (~15° tilt down)
- Subject perfectly centered, occupying 70-80% of the frame height
- Quasi-orthographic projection (minimize perspective foreshortening)
- The output silhouette MUST match the source silhouette exactly
- All sculpted ornamental detail MUST remain visible and CRISP
  (decorations, raised patterns, carved lines, facial features if any)

BACKGROUND & ISOLATION
- Pure white seamless background (#FFFFFF)
- The frame MUST be empty of: background objects, supporting hands,
  props, stands, secondary subjects, text, watermarks
- Subject cleanly cut out, edges sharp, no halos or fringe artifacts
- The background MUST be empty of cast shadows

LIGHTING (DELIGHT PASS)
- Neutral diffuse studio lighting
- The surface MUST be empty of specular highlights and glossy reflections
- Cast shadows ON the subject itself (under chin, ornaments, recesses)
  MUST be softened so they do not read as geometry
- The output MUST be empty of: new shadows, rim light, dramatic lighting

CONTENT FIDELITY
- The output MUST show only the ORIGINAL subject, faithfully
- Style MUST remain photographic (no cartoon, no painterly, no illustration)
- Ornamental detail count and placement MUST match the source exactly
- Material identity MUST be preserved (ceramic stays ceramic, wood stays wood)
- The output MUST be empty of: invented parts, completed sections, "improvements"
- If part of the subject is occluded in source, leave it occluded
  (do not infer or reconstruct the hidden portion)

OUTPUT
- One PNG, square 2048x2048 minimum
- Empty of: watermark, annotations, text overlays, borders
```

## Come adattarlo

Il template sopra è "neutro". Se la foto presenta sfide specifiche, **aggiungi** uno o più block dai file:

- `proportion_anchor_block.md` ← se Gemini drifta sulle proporzioni (sempre raccomandato come safety)
- `delight_aggressive.md` ← se il soggetto è smaltato/lucido
- `detail_preservation.md` ← se ci sono micro-rilievi a rischio smoothing
- `perspective_correction.md` ← se la foto è scattata troppo vicina o storta
- `casting_defects.md` ← se gesso/prototipo artigianale
- `color_simplification.md` ← se stampa multicolore AMS

**Block edge case** (vedi `decision_tree.md` D7-D15):
- `transparency_reflective.md` — vetro/cromo/specchio
- `fibrous_subject.md` — pelo/tessuto/paglia
- `articulated_multipart.md` — multi-pezzo
- `severe_undercuts.md` — sottosquadri estremi
- `engraved_text_lt_2mm.md` — testo scolpito fine
- `archaeological_restoration.md` — frammenti danneggiati
- `video_only_input.md` — solo video disponibile

Aggiungi i block **prima** della sezione `OUTPUT`, come sezioni aggiuntive.

## Esempio di adattamento

Se il soggetto è una ceramica smaltata fitta di dettagli e la foto è leggermente storta, il prompt finale è:

```
[master_template GEOMETRY/BACKGROUND/LIGHTING/CONTENT FIDELITY]
+ [proportion_anchor_block content]
+ [delight_aggressive content]
+ [detail_preservation content]
+ [perspective_correction content]
+ OUTPUT section (sempre alla fine)
```

Quando ti chiederò di pre-processare una foto specifica, ti darò già il prompt **assemblato e pronto** — non dovrai comporlo a mano. Questo file serve a documentare la logica.

## Changelog

- **2026-05-13**: convertito tutto il template a **affirmative framing** (best practice Gemini 2.5/3 docs). Rimossa sezione "MUST NOT". Aggiunto INPUT ASPECT RATIO LOCK verbatim Google. Aggiunti edge case block come opzioni.
- **2026-05-08**: versione originale con "MUST NOT" stacking (deprecato).
