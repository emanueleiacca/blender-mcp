# Block: Transparency / Reflective (vetro, cristallo, cromo, specchio)

## Quando usarlo

Soggetto in **vetro trasparente**, **cristallo**, **metallo cromato/specchiato**, **ceramica iper-lucida** (smalto a specchio).

**Sintomo**: la foto sorgente mostra principalmente riflessi dell'ambiente — l'oggetto stesso è quasi invisibile come forma. Tutti gli engine image-to-3D falliscono perché non hanno informazione di geometria, solo di riflessione.

## ⚠️ Limite duro

Senza opacizzazione fisica (AESUB Blue spray) o cross-polarization rig, single-image AI **non funziona**. Questo block è un workaround che riduce il danno, non una soluzione completa.

## Block (da inserire dopo LIGHTING nel master_template)

```
=== TRANSPARENCY / REFLECTIVITY OPACIFICATION ===

The source subject is highly transparent or reflective.
Reflections in source are NOT geometry — they MUST be removed.

OPACIFICATION
- Re-render the subject's surface as if it were coated with matte gray
  primer (RGB ~150,150,150, fully diffuse, zero specular)
- All glass transparency MUST be replaced with opaque matte gray
- All chrome/mirror reflections MUST be replaced with diffuse matte
- Environment reflections (room, lights, photographer) MUST be empty

SHADOW PRESERVATION
- Self-shadows from the subject's OWN geometry MUST be preserved
  (under chin, behind ornaments, in recesses)
- These shadows are the only geometric signal available

COLOR
- Final surface MUST be matte gray (RGB ~150,150,150)
- Do not preserve original color (it's all reflection, unreliable)

STRUCTURE
- Glass thickness MUST be inferred as a solid wall
  (do not represent inner cavity unless visible from source)
```

## Strategia complementare

Se il workaround Gemini non basta:

1. **AESUB Blue spray** (rimovibile dopo 2-4 ore): spruzza l'oggetto, fotografa, ripeti workflow normale. ~50€/spray.
2. **Cross-polarization rig**: 2 filtri polarizzatori ortogonali (uno sulla luce, uno sull'obiettivo). Elimina riflessi specular fisicamente.
3. **Cerca asset esistente**: oggetti comuni (bicchieri, bottiglie, posate) sono spesso su Sketchfab/Smithsonian 3D Open Access.

## Quando NON usarlo

- Soggetto opaco normale (ceramica matte, gesso, terracotta) → usa `delight_aggressive.md` invece
- Soggetto solo parzialmente lucido (smalto leggero) → usa `delight_aggressive.md` con intensity 0.6

## Origine

Deepsearch 2026-05-13 § D7 (RESEARCH_2026-05-13.md).
