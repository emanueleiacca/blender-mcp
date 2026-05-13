# Block: Detail Preservation

**Da aggiungere** al master quando il soggetto ha **micro-rilievi fitti e ripetitivi** che i tool 3D tendono a "ammorbidire": squame, intrecci, capelli scolpiti, foglie d'acanto, motivi geometrici a basso rilievo, decori puntinati, micro-letterature scolpite.

## Perché serve

I tool image-to-3D applicano post-processing di smoothing per evitare rumore geometrico. In dosi sbagliate, questo smoothing **fonde dettagli vicini** (es. squame contigue di una pigna diventano una superficie liscia, capelli intrecciati di una testa di moro diventano un casco). Il pre-processing Gemini deve **enfatizzare i bordi** del micro-rilievo prima che arrivino al tool 3D, così che il post-processing lasci comunque qualcosa di leggibile.

## Block (aggiungi prima della sezione OUTPUT)

```
=== DETAIL PRESERVATION (micro-relief enhancement) ===
The subject features DENSE REPEATING SCULPTED DETAIL (e.g. carved
scales, intertwined hair or rope, leaves, scrollwork, geometric
patterns, puntinato/punching, raised filigree). These details are
the artistic core of the object and MUST survive into the 3D mesh.

Apply the following:

- Sharpen the EDGES of every micro-relief element. The transitions
  between high points and low points of the relief must be crisp
  and high-contrast, not soft gradients.
- Preserve the SEPARATION between adjacent details. Do not allow
  contiguous elements (e.g. neighboring scales, parallel braids)
  to fuse visually into a single surface.
- Maintain consistent depth cues for the relief: deeper areas should
  read as clearly darker (matte shadow), raised areas clearly lighter
  (matte highlight without specular). This contrast is what the
  image-to-3D tool will read as geometry.
- Do NOT add details that are not in the source. If a region of the
  source photo is blurry or unclear, leave it as a smoothly-modeled
  area — do not hallucinate decorative pattern.
- Do NOT regularize irregularities. Hand-crafted details have natural
  variation; preserve it. Do not snap to a perfect grid or symmetry.

VALIDATION: after this pass, micro-relief elements should be more
crisply defined than in the source photo, while remaining faithful
to the original artistic intent.
```

## Quando NON usarlo

- Soggetti con superfici grandi e lisce (vaso semplice, busto stilizzato senza decoro fitto) → rischio di overshooting, edge contrast spurio
- Soggetti dove il micro-rilievo è più una texture pittorica che scolpita (es. decoro dipinto su ceramica liscia) → questo block lo trasformerebbe in geometria fittizia. In quel caso, NON usare questo block e accetta che il decoro pittorico sparirà nel mesh

## Sinergia con `delight_aggressive.md`

Su ceramica smaltata fitta di dettagli (caso classico, es. testa di moro elaborata), usa **entrambi i block**: prima `delight_aggressive` rimuove i riflessi che mascherano i dettagli, poi `detail_preservation` enfatizza ciò che il delight ha rivelato.
