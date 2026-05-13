# Esempio: Albero corallo (FAILED — membrane intrinseche)

**Data**: 2026-05-05
**Soggetto**: Albero/corallo decorativo con rami ramificati intrecciati
**Materiale originale**: Gesso bianco
**Stato**: ❌ **FALLITO** — workflow non automatizzato. Documentato come case study negativo.

---

## Foto sorgenti

- 2 foto: frontale + lato

## Prompt Gemini

- `multi_photo_canonical.md` + `casting_defects.md` + `detail_preservation.md`

## Tool 3D scelto

**Hi3D 2.1** (1536³ Pro, ~2M poly) — oggetto con micro-dettaglio fitto, ramificazioni intrecciate.

## Output mesh

- Polycount: 2.1M (estremo)
- ⚠️ **Membrane intrinseche** dove i rami si "fondono" l'uno con l'altro nelle intersezioni
- Sintomo `analyze_mesh_for_print`: `quasi_flat_ceiling_pct = 18%` (sopra soglia 5%)

## Rework Blender — TUTTI I TENTATIVI FALLITI

### Tentativo 1: dissolve_verts cascade
- ❌ Peggiora — crea ulteriore non-manifold
- User feedback: "il dissolve_verts ha peggiorato"

### Tentativo 2: select_linked_flat (custom)
- ❌ Implementation iniziale era buggata (BFS edge non corretto)
- Rivisto come Regola 39 (1:1 C reimplementation)

### Tentativo 3: Bisect aggressive
- ❌ Taglia le ramificazioni intrecciate

### Tentativo 4: Cleanup → Decimate aggressivo (0.1)
- ❌ Distrugge la geometria

### Tentativo 5: Manual face deletion in Edit Mode
- ❌ Membrane sono troppe per cleanup manuale (centinaia)

### Tentativo 6: PyMeshLab AO (Regola 37)
- ⚠️ **Codificato come strategia** ma non testato empiricamente su questo asset
- AO threshold < 0.15 = candidato faccia interna

### Tentativo 7: BVHTree raycast (Regola 38)
- ⚠️ Codificato come strategia alternativa
- Hemisphere Fibonacci raycast da centroide faccia

### Tentativo 8: rebuild remesh quad
- ❌ Distrugge dettaglio fine

**User feedback finale**: "abbiamo ufficialmente fallito"

## Codifica nella KB (Regola 31)

**Regola 31 TESTING_LOG**: dopo 2 tentativi automatici falliti su membrane intrinseche → **propose Meshmixer alternative** invece di insistere. Membrane intrinseche di asset sculpt **NON sono automatizzabili** in modo affidabile.

**Strategia raccomandata 2026-05-13**:
1. Hi3D con Delight più aggressivo (riduce false membrane da ombre)
2. Cambia angolazione foto (rami visti da altro angolo riducono intersezioni)
3. **Cambia tool** (Hunyuan watertight forse meglio per ramificazioni — da testare)
4. **Meshmixer manual** (vedi `Bible/Blender for 3d print documentation/docs/membrane_removal.md`)
5. **Modella in Blender da zero** (rami come cilindri + ramify) — workflow non-AI

## Lezioni codificate

- ✅ **Regola 31** — stop after 2 attempts on membrane
- ✅ **Regola 37 (PyMeshLab AO)** — strategia teorica codificata
- ✅ **Regola 38 (BVHTree raycast)** — strategia teorica codificata
- ✅ **Regola 39 (Select Linked Flat 1:1)** — fix implementation bug
- ✅ **`membrane_removal.md` doc** in KB Blender — decision tree per quando usare cosa
- ⚠️ Asset sculpt con ramificazioni fitte = candidate al **fallimento automatico**: pianificare workflow manuale

## Cross-reference

- Regole 31, 37, 38, 39 TESTING_LOG
- `Bible/Blender for 3d print documentation/docs/membrane_removal.md`
- `tools/hitem3d-2.1.md` § 10.3 (membrane intrinseche post-generazione)
