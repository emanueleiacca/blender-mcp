# Block: Articulated / Multi-part (statua con base separata, robot, oggetti con tappo)

## Quando usarlo

Soggetto **composto da più pezzi distinti**, anche se in foto appaiono assemblati. Esempi:
- Statua + piedistallo separato
- Vaso con coperchio
- Figurina con accessori smontabili (cappello, spada)
- Oggetti modulari assemblabili

## ⚠️ Limite tecnico

Nessun engine single-image-to-3D 2026 segmenta nativamente in parti separate. **PartCrafter** è sperimentale e instabile. Lo workaround più affidabile è single-shot + Boolean cut in Blender.

## Strategia A — Single-shot + Boolean cut (raccomandata)

Non aggiungere block speciale. Genera mesh come un singolo blob, poi in Blender:
1. Identifica i piani di separazione (statua/base, vaso/coperchio)
2. Bisect lungo i piani
3. Aggiungi pin/dovetail per ri-assemblaggio dopo stampa

## Strategia B — Foto-per-parte

Se i pezzi sono **fisicamente smontabili**:
1. Smonta l'oggetto fisicamente
2. Fotografa ogni pezzo separatamente
3. Genera mesh separata per ogni pezzo (workflow standard per ognuna)
4. Assembla in Blender con vincoli posizionali

## Block per Strategia A (informativo, di solito non necessario)

```
=== ARTICULATED OBJECT — SINGLE-SHOT NOTE ===

The source subject appears as multiple connected parts.
Generate a SINGLE merged mesh — do not attempt part segmentation.
Part separation will be performed in 3D software after generation.

PRESERVE PART BOUNDARIES VISUALLY
- Where parts meet (e.g., statue/base interface), preserve a sharp
  edge or visible seam in the geometry
- Do not smooth the seam — it serves as cutting guide in Blender

DO NOT
- The output MUST be empty of: artificial separations or floating pieces
- The output MUST be empty of: hollowed interiors at part interfaces
```

## Quando NON usarlo

- Oggetto monolitico (un solo pezzo) → workflow standard
- Hai accesso a PartCrafter e accetti instabilità → usa PartCrafter direttamente

## Origine

Deepsearch 2026-05-13 § D9.
