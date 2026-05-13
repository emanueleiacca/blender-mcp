# Esempio: Limone bassorilievo (wall art)

**Data**: 2026-05-01
**Soggetto**: Limone scolpito in bassorilievo, tela piatta posteriore
**Materiale originale**: Gesso
**Categoria asset (Regola 41)**: `relief` / `wall_art` / `2.5D`

---

## Foto sorgenti

- 1 foto frontale piatta, soggetto centrato
- Sfondo: tavolo grigio
- Illuminazione: diffusa, leggera ombra laterale (utile per stima depth)

## Prompt Gemini usato

- Base: `single_photo_cleanup.md`
- Block: `casting_defects.md` (gesso) + `detail_preservation.md`
- Photo fidelity lock applicato

## Output Gemini

- ✅ Sfondo bianco pulito
- ✅ Bolle gesso rimosse
- ✅ Texture buccia limone preservata
- ⚠️ Bordo leggermente ammorbidito (tela posteriore appare "fade" invece che taglio netto)

## Tool 3D scelto

**Tripo 3.1 HD** — wall art piatto è uso case banale, no occlusione, no decoro fitto. Tempo 2.5 min.

## Output mesh

- Polycount: ~150k
- Mesh watertight ✅
- Tela posteriore: leggermente curva (Tripo "arrotonda" la base piatta)

## Rework Blender

1. Apply Scale ✅
2. Non-manifold check: 0 ✅
3. **Spianamento base** (Regola 41 wall_art): bisect Z=tela_z → mantieni front portion → fill flat
4. Decimate a 80k tri (sufficiente per wall art 100mm)
5. Pre-export check: `bbox_z_min=0`, `contact_points_count=4` (tela quad) ✅
6. HIRES validation: silhouette ok, depth percepibile, tela piatta ✅

## Stampa A1

- Layer 0.12 mm (estetica)
- Orient: tela su piatto, frontale verso top
- Supporti: nessuno (tela è la base)
- Brim: 5mm
- **Tempo stampa**: ~1.5h per 100mm width
- Risultato: ottimo. Layer line invisibili al lato laterale (Z), dettagli buccia leggibili da 50cm

## Lezioni codificate

- ✅ Bassorilievi sono use case ideale image-to-3D (no occlusione)
- ✅ Tripo 3.1 sufficiente per wall art, no bisogno Hi3D
- ✅ `relief` naming + bisect Z per tela piatta → Regola 41 confermata

## Cross-reference

- Regola 41 TESTING_LOG
- `fdm_compatibility.md` § Tripo 3.1
