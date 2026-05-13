# Block: Proportion Anchor

## Quando usarlo

Sempre raccomandato come safety net se Gemini ha mostrato in passato tendenza a "drift" sulle proporzioni (allungare/accorciare il soggetto, normalizzare aspect ratio, "raddrizzare" oggetti che hanno asimmetria intenzionale).

**Sintomi che richiedono questo block**:
- Output Gemini con silhouette simile ma proporzioni alterate
- Aspect ratio output ≠ aspect ratio source di > 5%
- Elementi del soggetto "ricalibrati" per riempire meglio il frame

## Block (da inserire prima di OUTPUT nel master_template)

```
=== PROPORTION ANCHOR — STRICT LOCK ===

The source image has specific dimensional ratios that MUST be preserved.

WIDTH/HEIGHT RATIO LOCK
- Measure the bounding box of the subject in the source image
  (W_src = subject width, H_src = subject height)
- The output subject's bounding box MUST have the same ratio:
  W_out / H_out within ±5% of W_src / H_src
- Do not "fit" or "normalize" the subject to a different aspect

PROPORTIONAL PARTS LOCK
- If the subject has named parts (base, body, neck, top, etc.),
  each part's relative size MUST remain unchanged
- Example: if the base is 30% of total height in source,
  the base MUST be 30% of total height in output

ROTATIONAL LOCK
- The subject's tilt angle in source (if any) MUST be preserved
- Do not "straighten" a subject that leans intentionally
- Do not rotate the subject to a different canonical pose

DO NOT CHANGE THE INPUT ASPECT RATIO.
```

## Note

- La frase finale **`Do not change the input aspect ratio.`** è la formulazione **verbatim** dei Google AI docs per Gemini. Gemini tende a drift l'aspect ratio se non lo si scrive esattamente così.
- Il block è **affermativo** (MUST preserve / MUST have / MUST remain) — pattern Gemini-friendly 2026.
- Per soggetti con asimmetria intenzionale (vasi etruschi inclinati, sculture "incomplete by design"), questo block è critico.

## Quando NON usarlo

- Se il soggetto è perfettamente simmetrico assialmente e Gemini tipicamente non drifta (vasi standard, pigne)
- Se vuoi esplicitamente che Gemini "raddrizzi" una foto storta (in quel caso usa `perspective_correction.md`)

## Origine

Best practice da:
- Google AI Developer Docs, Gemini 2.5/3 Image Editing
- Pattern empirico osservato su 200+ casi della community Patreon "Loot Studios"
- Riferimento: deepsearch 2026-05-13 (RESEARCH_2026-05-13.md § B1 punto 4)
