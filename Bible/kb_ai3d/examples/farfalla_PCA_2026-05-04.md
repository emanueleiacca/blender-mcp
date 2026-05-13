# Esempio: Farfalla (PCA orientation case)

**Data**: 2026-05-04
**Soggetto**: Farfalla decorativa, ali aperte
**Materiale originale**: Ceramica/gesso (semi-finita)
**Categoria asset**: `figurine` / `wall_art` (ali piatte)

---

## Foto sorgenti

- 1 foto frontale, ali aperte simmetriche
- Sfondo: tavolo grigio

## Prompt Gemini

- `single_photo_cleanup.md` + `detail_preservation.md` (texture ali)

## Tool 3D scelto

**Tripo 3.1 HD** — soggetto piatto a bassa profondità, no occlusione.

## Output mesh

- Polycount: ~180k
- Asse "naturale" della farfalla NON corrispondeva a Z=up nel mesh esportato (Tripo ha orientato secondo bbox)
- Ali sembravano "verticali" invece di "orizzontali"

## Rework Blender — PCA orientation

1. **MCP `analyze_mesh_for_print`** → `pca_thickness_ratio` indicava soggetto piatto (ali su 2 assi, depth minimale terzo asse)
2. **PCA orientation** (Jacobi 3x3):
   - Asse 1 (massima varianza): orizzontale ali → asse X
   - Asse 2: verticale corpo → asse Y
   - Asse 3 (minima varianza, depth): up → asse Z
3. **Errore di direzione iniziale** (Regola 28):
   - La prima volta orientai le ali a Z+, ma "TOP screen" mostrava la pancia
   - **User feedback**: "l'hai fatto di nuovo al contrario. devi ruotare l'oggetto di 180 gradi"
   - **Regola 28 codificata**: dopo PCA, **OBBLIGATORIO** screenshot TOP + BOTTOM + chiedere conferma utente prima di salvare
4. Rotazione 180° → ali up correttamente
5. Bisect Z=epsilon per tela posteriore piatta (è wall art di fatto)

## Stampa A1

- Layer 0.12 mm
- Orient: ali su piatto (back face = tela)
- Supporti: nessuno (ali sono già flat)
- Brim: 8mm (superficie contatto ridotta)
- Tempo: ~2h per 150mm wingspan

## Lezioni codificate

- ✅ **Regola 28 — PCA + TOP/BOTTOM check obbligatorio** prima di esportare
- ✅ **`pca_thickness_ratio` metric** per identificare soggetti "piatti" candidati a wall art treatment
- ⚠️ Image-to-3D non sa "su" semantico — PCA solo dà gli assi, l'utente conferma direzione

## Cross-reference

- Regola 28 TESTING_LOG
- `WORKFLOW_END_TO_END.md` § stop rules (PCA validation)
