# Master Template — Gemini cleanup per AI image-to-3D

Template di base per pre-processare 1 foto di un manufatto decorativo artigianale, da dare poi a un tool image-to-3D (Tripo / Hi3D / Hunyuan / Meshy / Rodin) via MakerLab o web app dedicata.

## Quando usarlo

- Hai 1 foto del soggetto, scattata con cellulare
- Vuoi un'immagine pulita e canonica come input al tool 3D

## Prompt (copia-incolla in Gemini)

```
You are preparing a single reference image for an image-to-3D AI tool.
The subject in the photo is a HANDCRAFTED DECORATIVE ARTIFACT
(ceramic, terracotta, carved wood, hammered metal, or similar).
The downstream goal is FDM 3D printing in single color, so only the
SCULPTED GEOMETRY matters — colors, paint, and surface texture will be discarded.

Produce ONE output image with these properties:

GEOMETRY & FRAMING
- Single 3/4 frontal view, camera slightly above eye level (~15° tilt down)
- Subject perfectly centered, occupying 70-80% of the frame height
- Quasi-orthographic projection (minimize perspective foreshortening)
- Original silhouette and proportions preserved EXACTLY — do not stretch,
  shrink, or alter the outline in any way
- All sculpted ornamental detail visible and CRISP (decorations, raised
  patterns, carved lines, facial features if any)

BACKGROUND & ISOLATION
- Pure white seamless background (#FFFFFF)
- Subject cleanly cut out, edges sharp, no halos or fringe artifacts
- No cast shadows on the background
- No supporting hands, props, stands, or objects of any kind in frame

LIGHTING (DELIGHT PASS)
- Neutral diffuse studio lighting
- Remove all specular highlights and glossy reflections
- Soften any cast shadows on the subject itself (especially under chin,
  ornaments, recesses) so they do not read as geometry
- Do NOT add new shadows or rim light

CONSTRAINTS — MUST NOT
- Do not stylize (no cartoon, no painterly, no illustration look)
- Do not add or remove ornamental detail
- Do not "improve" or "complete" the design — keep faithful to the original
- Do not alter material identity (ceramic stays ceramic, wood stays wood)
- Do not generate a fictional 3D rendering — keep the look photographic
- Do not invent missing parts even if part of the subject is occluded;
  if you must complete, mark the inferred part as a clearly distinct color

OUTPUT
- One PNG, square 2048x2048 minimum
- No watermark, no annotations, no text overlay
```

## Come adattarlo

Il template sopra è "neutro". Se la foto presenta sfide specifiche, **aggiungi** uno o più block dai file:

- `delight_aggressive.md` ← se il soggetto è smaltato/lucido
- `detail_preservation.md` ← se ci sono micro-rilievi a rischio smoothing
- `perspective_correction.md` ← se la foto è scattata troppo vicina o storta

Aggiungi i block **prima** della sezione `OUTPUT`, come sezioni aggiuntive.

## Esempio di adattamento

Se il soggetto è una ceramica smaltata fitta di dettagli e la foto è leggermente storta, il prompt finale è:

```
[master_template]
+ [delight_aggressive content]
+ [detail_preservation content]
+ [perspective_correction content]
+ OUTPUT section (sempre alla fine)
```

Quando ti chiederò di pre-processare una foto specifica, ti darò già il prompt **assemblato e pronto** — non dovrai comporlo a mano. Questo file serve a documentare la logica.
