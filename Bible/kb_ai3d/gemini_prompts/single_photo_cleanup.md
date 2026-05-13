# Single Photo Cleanup — prompt completo

Versione "tutto incluso" del master, per il caso più comune: **1 foto** di un manufatto decorativo, da pulire al volo con scelte ragionevoli per la maggior parte dei soggetti.

## Quando usarlo

- 1 sola foto disponibile
- Soggetto generico decorativo artigianale (ceramica, terracotta, legno, metallo)
- Non sai ancora se servono block specializzati (delight aggressivo, detail preservation, ecc.) → questo prompt include una versione **moderata** di tutti

## Prompt (copia-incolla)

```
You are preparing a single reference image for an image-to-3D AI tool
(Tripo / Hi3D / Hunyuan / Meshy / Rodin). The subject is a HANDCRAFTED
DECORATIVE ARTIFACT. The downstream goal is FDM 3D printing in single
color: only sculpted GEOMETRY matters. Colors, paint, and surface texture
will be discarded — but ALL sculpted relief must be preserved.

PRODUCE ONE OUTPUT IMAGE with the following properties:

=== FRAMING ===
- Single 3/4 frontal view, camera slightly above (~15° tilt down)
- Subject centered, occupying 70-80% of frame height
- Quasi-orthographic projection — minimize perspective foreshortening
- Square aspect ratio, 2048x2048 minimum

=== SILHOUETTE FIDELITY ===
- Preserve the original silhouette and proportions EXACTLY
- Do not stretch, shrink, slim, or alter the outline
- Do not "complete" or "fix" the original design

=== BACKGROUND ===
- Pure white seamless (#FFFFFF)
- Subject cleanly cut out, sharp edges, no halos
- No cast shadows on background
- Remove all supporting hands, props, stands, surrounding objects

=== LIGHTING (delight pass, moderate) ===
- Neutral diffuse studio lighting, soft and even
- Remove specular highlights and glossy reflections from the subject
  (treat the surface as if it were matte, even if originally glazed)
- Soften cast shadows on the subject itself (under chin, inside recesses,
  beneath ornaments) so they do not read as geometric depth to the AI
- Do NOT add new lighting effects, rim lights, or stylized shadows

=== DETAIL PRESERVATION ===
- Preserve all sculpted ornamental detail with high fidelity:
  carved patterns, raised motifs, facial features, hair/textile texture,
  scales, leaves, intertwining elements
- Slightly enhance edge contrast on these details so they read clearly,
  but do NOT add detail that is not present in the source photo
- Do NOT smooth, simplify, or "clean up" small sculpted features

=== STYLE LOCK ===
- Photographic look (do not stylize, no cartoon, no painterly, no illustration)
- Material identity preserved (ceramic looks like ceramic, wood like wood)
- No 3D-rendered look, no synthetic-CGI feel
- No watermarks, no text, no annotations

=== EDGE CASES ===
- If a part of the subject is occluded in the source photo, do NOT invent it.
  Either crop it out or render the visible part faithfully and stop there.
- If the source has motion blur or focus issues, sharpen subtly but do not
  hallucinate detail.
- If the source has multiple subjects, pick the most prominent one and
  isolate it.

OUTPUT: one PNG, 2048x2048+, no watermark.
```

## Verifica output

Dopo aver ricevuto l'immagine da Gemini, controlla la checklist in `../workflow.md` Step 4 prima di passarla al tool 3D.
