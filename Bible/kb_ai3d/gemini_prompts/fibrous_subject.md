# Block: Fibrous Subject (pelo, tessuto, paglia, capelli sciolti)

## Quando usarlo

Soggetto con **filamenti < 0.4mm** di larghezza: pelo animale, capelli sciolti, paglia, tessuto frangiato, fili tessuti, fibre vegetali, frange.

## ⚠️ Limite duro FDM

Nessun nozzle FDM (compreso 0.2mm) stampa filamenti singoli < 0.4mm di larghezza. Questo block trasforma i filamenti in una **superficie continua texturizzata** che è stampabile.

## Block (da inserire dopo GEOMETRY nel master_template)

```
=== FIBROUS / STRAND STYLIZATION ===

The source subject contains thin strand-like features (hair, fur,
fabric fringe, straw, fibers) that are too fine to FDM-print as
individual filaments.

STYLIZATION RULE
- Individual strands MUST be merged into a continuous bumpy surface
- The bumpy surface MUST preserve the GENERAL DIRECTION of the strands
  (e.g., hair flow, fur grain direction)
- Surface MUST appear sculpted, not photorealistic strand-by-strand
- Resulting bumps MUST be at least 1mm scale (printable feature size)

PRESERVATION
- Overall silhouette / mass of the fibrous region MUST be preserved
- Volumetric distribution MUST be respected (e.g., a wig has volume,
  preserve that volume as a solid)

DO NOT
- The output MUST be empty of: individual thin strands < 1mm scale
- The output MUST be empty of: photorealistic strand textures
```

## Soluzioni alternative per soggetti hair-critical

- **DiffLocks** (workflow specializzato hair-to-3D): per ritratti con capelli importanti
- **Sculpting manuale in Blender** dopo image-to-3D del corpo base
- **Cambia angolo foto** (3/4 dietro per nascondere fibre frontali)

## Quando NON usarlo

- Capelli scolpiti già stilizzati nella ceramica (sono già "merged" → usa `detail_preservation.md`)
- Tessuti con drappeggio largo (non strand-like → trattalo come superficie normale)

## Origine

Deepsearch 2026-05-13 § D8.
