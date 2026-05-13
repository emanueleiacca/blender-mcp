# Block: Delight Aggressivo

**Da aggiungere** al master template (o al `single_photo_cleanup` / `multi_photo_canonical`) quando il soggetto ha una superficie **molto riflettente**: ceramica smaltata lucida, metallo lucidato/sbalzato, vernici a smalto, finiture cromate.

## Perché serve

I tool image-to-3D **interpretano i riflessi specular come variazioni di geometria**. Una smaltatura ceramica con un highlight forte sotto il mento di una testa di moro può diventare un'incavatura nel mesh. Un riflesso a banda su un vaso può diventare una "cintura" rilevata. Il delight pass moderato del prompt master può non bastare per superfici molto riflettenti.

## Block (aggiungi prima della sezione OUTPUT)

```
=== AGGRESSIVE DELIGHT PASS ===
The subject has a HIGHLY REFLECTIVE finish (glazed ceramic, polished
metal, lacquered wood, or similar). Treat ALL specular and glossy
information as photographic noise to be ELIMINATED:

- Remove every specular highlight, hot spot, and glossy reflection,
  no matter how prominent in the source photo
- Render the surface as if it were COMPLETELY MATTE — like unfired
  bisque ceramic, untreated terracotta, or chalk-finished surface
- Where reflections obscured detail, infer the underlying matte form
  consistently with adjacent matte areas — but do NOT invent new detail
- Reflections of the environment, light sources, or photographer must
  be ENTIRELY removed and replaced with neutral matte diffuse rendering
- Color saturation and hue may be slightly desaturated to compensate
  for the loss of specular contrast — this is acceptable, since
  downstream we discard color anyway
- Do NOT replace specular highlights with painted-on light/shadow
  (this would re-introduce the same fake-geometry problem)

VALIDATION: after the delight pass, the subject should look as if
it were photographed in completely flat overcast light, with NO
indication of light direction visible on the surface.
```

## Quando NON usarlo

- Terracotta non smaltata, gesso, legno opaco → il delight moderato del master basta
- Tessuti / pelli / superfici già intrinsecamente diffuse → questo block può rimuovere micro-contrasti utili
- Soggetti con **legittime** variazioni di colore/finitura matte (es. ceramica grezza con macchie di cottura) → meglio detail preservation, non delight

## ⚠️ Avvertenza profondità

**Confermato empiricamente (2026-05-08)**: il delight aggressivo rimuove le ombre dell'oggetto che il tool image-to-3D usa per inferire la profondità e la forma 3D. Un delight troppo aggressivo può **peggiorare** il risultato 3D rispetto a un'immagine con le ombre originali preservate.

Usare sempre il delight **minimo necessario** per gestire i riflessi speculari più distorsivi, non il massimo possibile. Se i riflessi non falsificano la geometria (es. piccoli highlight su limoni rotondi), meglio lasciarli piuttosto che appiattire tutto.
