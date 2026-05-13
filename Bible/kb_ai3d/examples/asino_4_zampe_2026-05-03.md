# Esempio: Asino siciliano (4 zampe, statua decorativa)

**Data**: 2026-05-03
**Soggetto**: Asinello siciliano scolpito, 4 zampe, bardatura/decoro
**Materiale originale**: Gesso
**Categoria asset (Regola 41)**: `statue` / `figurine`

---

## Foto sorgenti

- 3 foto: frontale 3/4, lato sx, retro
- Sfondo: tessuto bianco
- Illuminazione: diffusa

## Prompt Gemini

- Base: `multi_photo_canonical.md` (3 foto)
- Block: `casting_defects.md` + `detail_preservation.md` (bardatura)
- Photo fidelity lock

## Output Gemini

- ✅ Vista canonica 3/4
- ✅ Bardatura preservata
- ⚠️ Cap di Nano Banana drift su multi-foto (vedi nota README)

## Tool 3D scelto

**Hi3D 2.1** (1536³) — figurine con decoro = uso case Hi3D primario. Tempo 7 min.

## Output mesh

- Polycount: 1.2M (alto)
- 4 zampe presenti ma a quote Z diverse (asino inclinato)
- Base spuria sotto le zampe

## Rework Blender — Highlight Regola 29

1. **Decimate pre-flight**: 1.2M → 400k (ratio 0.33)
2. Apply Scale
3. **Identificazione contact points** (Regola 29):
   ```python
   # MCP analyze_mesh_for_print → contact_points_count=4 ✅
   # Identifica i 4 punti più bassi (le zampe)
   ```
4. **Plane-fit SVD** sui 4 contact points → calcola normale piano
5. **Allineamento Z=0**: ruota il mesh per allineare il piano contact al piano XY mondo
6. **Verifica `bbox_z_min == 0`** (Regola 36 pre-export check)
7. HIRES validation: 4 zampe a contatto, asino dritto ✅

**Errore evitato**: senza Regola 29, il primo export aveva asino inclinato — l'utente dovette chiedere "l'stl risulta inclinato e spostato sul lato, le 4 zampe devono stare tutte a contatto". Regola 29 codifica il fix.

## Stampa A1

- Layer 0.16 mm (figurine standard)
- Orient: SVD-corrected, 4 zampe a Z=0
- Supporti: tree organic 30° (orecchie, coda)
- Brim: 5 mm
- **Tempo stampa**: ~5h per 120mm height
- Risultato: 4 zampe ben in contatto, no warping

## Lezioni codificate

- ✅ **Regola 29 plane-fit SVD** per soggetti multi-foot
- ✅ **Regola 36 pre-export check** `bbox_z_min=0` + `contact_points_count > 0` obbligatorio
- ✅ **Hi3D ottimo per figurine** con decoro fitto
- ⚠️ Multi-foto > 3 → drift Gemini, considerare Nano Banana Pro

## Cross-reference

- Regole 29, 36 TESTING_LOG
- `tools/hitem3d-2.1.md` § 10.4 (multi-foot)
