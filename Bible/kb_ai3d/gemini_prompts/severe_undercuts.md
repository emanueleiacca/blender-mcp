# Block: Severe Undercuts (gabbie, intrecci chiusi, sottosquadri estremi)

## Quando usarlo

Soggetto con **cavità profonde con accesso stretto** o **strutture intrecciate chiuse**:
- Gabbie con celle < 10mm
- Pizzo 3D / intrecci tridimensionali
- Sculture con cavità interne accessibili solo da fori piccoli
- Anfore con manici-cavità

## ⚠️ Limite duro FDM

Gabbie con celle < 10mm e intrecci con loop chiusi sono **impossibili** in FDM senza supporti interni che poi non rimuovi. Questo block aiuta nella generazione, ma la **strategia primaria è split & glue** in Blender.

## Strategia (decisione di workflow, non solo prompt)

| Approach | Quando |
|---|---|
| **Split & glue** in Blender (taglia in pezzi, stampa, incolla) | Asset > 50mm, sottosquadri profondi |
| **Vase mode hollow** (Spiral Vase, parete singola) | Soggetto è contenitore, accetti parete sottile |
| **Resina SLA invece di FDM** | Sottosquadri così stretti che FDM non gestisce |
| **Stilizza in Gemini** (semplifica intrecci) | Accetti perdita di dettaglio per stampabilità |

## Block (per Gemini stylization, solo se accetti perdita dettaglio)

```
=== UNDERCUT SIMPLIFICATION ===

The source subject contains severe undercuts and closed inter-woven
features that are impossible to FDM-print without internal supports.

STYLIZATION
- Closed loops in the inter-weaving pattern MUST be visually preserved
  but slightly "opened" (gaps > 2mm at narrowest points)
- Deep undercuts MUST be reduced in depth to < 30° angle
  (printable without tree support)
- Maintain overall sculptural impression

DO NOT
- The output MUST be empty of: invisible internal cavities
  (anything not visible from outside should not exist in the mesh)
```

## Strategia post-Hi3D (Blender)

1. Generato il mesh, identifica i sottosquadri con MCP tool `analyze_overhang`
2. Se `overhang_45_pct > 30%`: considera vase mode, split&glue, o cambio strategia
3. Vedi Regola 25 TESTING_LOG (overhang analysis pre-print) per dettagli

## Origine

Deepsearch 2026-05-13 § D12. Cross-reference: `Workflow/TESTING_LOG.md` Regole 25/29.
