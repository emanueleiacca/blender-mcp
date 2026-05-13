# Multi-Photo → Canonical View — prompt completo

Caso d'uso: hai **2-4 foto** del soggetto da angolazioni diverse e MakerLab accetta solo 1 foto. Gemini fonde le viste in **1 immagine canonica 3/4 ottimizzata** per il tool 3D.

Questo è il workflow più potente che hai a disposizione: dài a Gemini più informazione su cosa c'è dietro/sotto/sopra, e Gemini sintetizza una vista canonica che il tool 3D non potrebbe ricostruire da una sola foto.

## Quando usarlo

- 2-4 foto da angolazioni diverse (front, 3/4 dx, 3/4 sx, retro)
- Soggetto con dettagli che spariscono in una vista singola (sottosquadri, retro decorato, asimmetrie)
- Vuoi massima fedeltà al soggetto reale

## Come scattare le foto sorgenti

Per dare a Gemini il materiale migliore:
- **Front**: vista frontale, camera al livello del soggetto
- **3/4 destra**: ~45° a destra
- **3/4 sinistra**: ~45° a sinistra
- **Retro** (opzionale ma utile): vista posteriore frontale
- Tutte le foto con la **stessa luce diffusa** (non spostarsi tra angoli con luci diverse)
- Stesso sfondo (anche imperfetto va bene, Gemini lo elimina)
- Stessa distanza approssimativa

Se hai solo 2 foto, scegli **front + 3/4** (la più informativa).

## Prompt (copia-incolla, allega 2-4 foto)

```
You are receiving N reference photos of the SAME handcrafted decorative
artifact, taken from different angles. Your task: SYNTHESIZE A SINGLE
CANONICAL VIEW that combines information from all source photos into
one clean image, suitable as input to an image-to-3D AI tool.

The downstream goal is FDM 3D printing in single color: only the
sculpted GEOMETRY matters. Colors and texture will be discarded — but
all sculpted relief must be preserved with high fidelity.

=== TASK ===
1. Identify the subject across all input photos (it is the same physical
   object photographed from different angles).
2. Mentally reconstruct the 3D form using the multiple views.
3. Render a SINGLE OUTPUT IMAGE in canonical 3/4 frontal view that
   accurately reflects the synthesized 3D form.

=== OUTPUT FRAMING ===
- 3/4 frontal view, camera slightly above (~15° tilt down)
- Subject centered, occupying 70-80% of frame height
- Quasi-orthographic projection — minimize perspective foreshortening
- Square aspect ratio, 2048x2048 minimum

=== SYNTHESIS RULES ===
- Use information from ALL source photos to inform the canonical view
- Where photos disagree (e.g. lighting differences), produce a NEUTRAL
  consistent rendering, not a copy of any single photo
- Preserve the EXACT silhouette and proportions of the real object —
  do not stretch, shrink, slim, or stylize
- If the back of the subject is visible only in some photos, infer
  correctly the back-facing details (they will be partially visible
  in the 3/4 canonical view through silhouette and edge details)
- DO NOT hallucinate details not present in any source photo
- DO NOT "improve" the design

=== BACKGROUND ===
- Pure white seamless (#FFFFFF)
- Subject cleanly isolated, sharp edges, no halos
- No cast shadows on background
- Remove all hands, props, stands, surrounding objects from all sources

=== LIGHTING (unified delight pass) ===
- Neutral diffuse studio lighting, soft and even, consistent across the form
- Remove all specular highlights and glossy reflections from the subject
- Treat surface as matte regardless of the original finish (glazed ceramic,
  polished metal, varnished wood — all rendered as if matte)
- Soften any shadows in recesses so they do not read as geometric depth
- DO NOT add stylized lighting

=== DETAIL PRESERVATION ===
- All sculpted ornamental detail clearly visible: patterns, raised motifs,
  facial features, hair, textile texture, scales, leaves, intertwining elements
- Cross-reference details across photos for maximum accuracy
- DO NOT smooth, simplify, or fuse small sculpted features
- Slightly enhance edge contrast on details so they read clearly, but do
  NOT invent new details

=== STYLE LOCK ===
- Photographic look (no cartoon, no painterly, no illustration)
- Original material identity preserved (ceramic looks ceramic, etc.)
- No 3D-rendered or synthetic-CGI look
- No watermark, no text, no annotations

=== EDGE CASES ===
- If photos contradict each other (e.g. asymmetric details visible from
  one side but not another), choose the side that shows MORE detail and
  reproduce it faithfully on that side. Do not make the object
  symmetric if it is not.
- If a part is occluded in ALL photos, do NOT invent it. Render only
  what is collectively visible.

OUTPUT: one PNG, 2048x2048+, no watermark, ready for image-to-3D.
```

## Verifica output

Particolare attenzione a:
- La vista canonica **rispetta** ciò che si vede nelle sorgenti? (non ha "appiattito" un decoro asimmetrico in simmetrico)
- I dettagli del retro/lato visibili in una sola foto sono **correttamente proiettati** nella 3/4?
- Nessuna invenzione di parti non viste?

Se Gemini ha "regolarizzato" troppo (fatto simmetrico ciò che non lo era, riempito sottosquadri), rigenera con istruzione più forte: *"the original is asymmetric — preserve the asymmetry visible in photo 2"*.
