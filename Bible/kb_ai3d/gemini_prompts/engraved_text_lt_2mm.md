# Block: Engraved Text < 2mm (lettering scolpito fine)

## Quando usarlo

Soggetto con **testo inciso, numeri, lettering scolpito** con tratto < 2mm di larghezza. Esempi:
- Targhe commemorative
- Date scolpite su ceramica
- Firme dell'artista
- Iscrizioni religiose / dediche

## ⚠️ Limite duro FDM A1

Tratto < 0.8mm di larghezza = 1 perimeter line con nozzle 0.4mm → potenzialmente invisibile a stampa. Per text < 2mm, ricostruzione manuale in Blender è più affidabile della generazione AI.

## Strategia raccomandata

**Ricostruzione testo separata** (NON affidare al image-to-3D):
1. Genera il mesh dell'oggetto **senza testo** (Gemini rimuove il testo dalla foto)
2. In Blender: aggiungi un **Text object** con il lettering corretto, font scelto, dimensione adeguata
3. **Boolean union** del Text object sul mesh principale
4. Verifica spessore tratto > 0.8mm (Bambu Studio thickness check)

## Block A — "Rimuovi testo" (per Gemini, prima della generazione mesh)

```
=== TEXT REMOVAL FOR LATER RECONSTRUCTION ===

The source subject contains engraved or sculpted text/numbers/letters.

REMOVAL RULE
- All sculpted text MUST be removed from the output
- The surface where text was MUST be flattened to match surrounding area
- Text will be reconstructed precisely in 3D software later

PRESERVE
- Note the LOCATION where text was (mention in description)
- Note the APPROXIMATE FONT STYLE if recognizable

DO NOT
- The output MUST be empty of: any sculpted text, numbers, letters
- The output MUST be empty of: depressions/grooves where text was
```

## Block B — "Preserva testo" (solo se text > 3mm e vuoi single-shot)

```
=== ENGRAVED TEXT PRESERVATION (text > 3mm only) ===

The source subject contains engraved text with strokes > 3mm width.

PRESERVATION RULE
- All sculpted text MUST remain visible with strokes intact
- Local contrast around text MUST be increased ~+15% to enhance
  groove depth signal for the 3D generation model
- Preserve original font style and spacing exactly

DO NOT
- The output MUST be empty of: text reconstruction or "improvement"
- Style and content of text MUST match source exactly
```

## Workflow Blender per ricostruzione testo

```python
# In Blender (via blender-mcp execute_blender_code)
import bpy

# 1. Aggiungi text object
bpy.ops.object.text_add(location=(0, 0, 0))
text_obj = bpy.context.object
text_obj.data.body = "ANNO 1923"
text_obj.data.size = 0.005  # 5mm
text_obj.data.extrude = 0.001  # 1mm depth

# 2. Convert to mesh
bpy.ops.object.convert(target='MESH')

# 3. Boolean union sul mesh principale
# ... (vedi playbook boolean_union nel KB Blender)
```

## Quando NON usarlo

- Soggetto senza testo → ovvio
- Testo > 3mm stroke width + vuoi single-shot → usa Block B
- Testo critico per fedeltà (firma artista) → usa Strategia "Ricostruzione separata"

## Origine

Deepsearch 2026-05-13 § D11. Cross-reference: KB Blender boolean playbook.
