# Membrane Removal — Rimozione di tele/membrane decorative interne in asset sculpt

---

> ## 🚨 REGOLA PRIMARIA — LEGGERE PRIMA DI TENTARE QUALSIASI RIMOZIONE
>
> **Una "tela del fondo" topologicamente integrata allo sculpt NON è automatizzabile via geometric analysis Blender pura.**
>
> Stop rule documentata (`TESTING_LOG.md` regola 31, SESSION 004): dopo 2 tentativi falliti con tecniche Blender native (flood-fill, decimate dissolve, voxel remesh, snap+fill, fan triangolare, curvature analysis, ecc.) **FERMARSI** e proporre alternative manuali. Caso reale documentato: `albero_corallo`, 8+ tecniche fallite consecutive.
>
> **Path operativo definitivo (priorità decrescente):**
> 1. **PRIMA verifica nomenclatura** (regola 41): se filename contiene `relief|wall_art|2.5D|plaque|medallion|lithophane` → la tela è **intenzionale**, NON tentare di rimuoverla.
> 2. **PyMeshLab Ambient Occlusion per-vertex** (regola 37) — automazione pulita, 10 min setup. Documentato come pattern prototipico in MeshLab Stuff blog + CFD Engine #119.
> 3. **Blender BVHTree raycast hemisphere** (regola 38) — alternativa nativa Blender, no PyMeshLab. Per-face raycast su semisfera.
> 4. **Meshmixer Select + Expand to Connected + Discard** (regola 40) — fallback manuale robusto.

---

## Quando usarlo
Asset sculpt 3D dove l'artista ha scolpito una **superficie piatta interna decorativa** (= "tela del fondo") tra i dettagli sporgenti. Esempi:
- Alberi corallo/decorativi con rami sporgenti su un fondale
- Bassorilievi simulati come 3D ma con "campo" continuo dietro al rilievo
- Asset wall-art venduti come "2.5D" che hanno scolpito anche lo sfondo

**NON usarlo per**:
- Bassorilievi con backplane piatta vera (= asset progettato come 2.5D) — è elemento strutturale
- Lithophane / plaque / medallion (= tela è il design principale)
- Asset con "fondo" che è effettivamente la backplane di stampa

---

## Tecnica 1 — PyMeshLab Ambient Occlusion per-vertex (RACCOMANDATA #1)

Bake AO sui vertici → la membrana interna è "in ombra" (vertici scuri), i dettagli esterni sono "visibili" (vertici chiari). Filtra le facce con tutti i 3 vertici sotto soglia.

```python
import pymeshlab
ms = pymeshlab.MeshSet()
ms.load_new_mesh('coral_tree.stl')

# Compute AO per-vertex (128+ raggi su sfera completa)
# Per GPU: usa compute_scalar_ambient_occlusion_gpu(...)
ms.compute_scalar_ambient_occlusion(
    occmode='per-Vertex',
    dirbias=0,
    reqviews=128,
    usegpu=True
)

# Seleziona facce con TUTTI e 3 i vertici sotto soglia (= membrana interna)
ms.compute_selection_by_condition_per_face(
    condselect='(q0 < 0.15) && (q1 < 0.15) && (q2 < 0.15)'
)

# Rimuovi
ms.meshing_remove_selected_faces()
ms.meshing_remove_unreferenced_vertices()
ms.save_current_mesh('coral_clean.stl')
```

**Quando funziona meglio**: forme dove l'esterno è davvero "visibile da fuori" e l'interno no — alberi, gabbie, decori ramificati. Rimuove fino al 63% di facce interne preservando i dettagli.

**Limiti**: zone concave esterne ai rami (forcelle profonde) possono essere falsamente classificate interne. **Mitigazioni**:
- Soglia più bassa (0.05–0.10) preserva zone di transizione
- Filtro "TUTTI e 3 i vertici" evita falsi positivi su edge della tela
- Aumentare `reqviews=256` per AO più stabile

**Alternative metriche** (stesso framework PyMeshLab, scelta migliore in casi specifici):
- `compute_scalar_by_shape_diameter_function_per_vertex` → **SDF analysis**: assegna a ogni vertice il diametro locale. Membrana sottile = SDF piccolo (~1mm), rami spessi = SDF grande (~3-5mm). Più discriminante di AO quando la membrana NON è in ombra.
- `compute_scalar_by_volumetric_obscurance` → variante volumetrica di AO, più robusta su concavità esterne.

---

## Tecnica 2 — Blender BVHTree raycast hemisphere (alternativa nativa)

Implementabile direttamente in Blender via `mathutils.bvhtree`, NON richiede PyMeshLab. Per ogni faccia, casta 32 raggi su semisfera (Fibonacci) lungo la normale; se <10% raggi escono dal mesh → faccia interna → cancella.

```python
import bpy, bmesh, math
from mathutils.bvhtree import BVHTree
from mathutils import Vector

obj = bpy.context.object
bm = bmesh.new(); bm.from_mesh(obj.data); bm.faces.ensure_lookup_table()
bvh = BVHTree.FromBMesh(bm)

EPS = 1e-4; N_RAYS = 32; VIS_THRESHOLD = 0.10

def fibonacci_hemisphere(n):
    pts = []
    for i in range(n):
        phi = math.acos(1 - (i + 0.5) / n)
        theta = math.pi * (1 + 5**0.5) * i
        pts.append(Vector((math.sin(phi)*math.cos(theta),
                          math.sin(phi)*math.sin(theta),
                          math.cos(phi))))
    return pts

base_pts = fibonacci_hemisphere(N_RAYS)
to_delete = []
for f in bm.faces:
    origin = f.calc_center_median() + f.normal * EPS
    # Ruota base_pts per allineare Z locale alla normale
    rot = Vector((0,0,1)).rotation_difference(f.normal).to_matrix()
    free = 0
    for d_local in base_pts:
        d = rot @ d_local
        hit, *_ = bvh.ray_cast(origin, d, 10.0)
        if hit is None: free += 1
    if free / N_RAYS < VIS_THRESHOLD:
        to_delete.append(f)

bmesh.ops.delete(bm, geom=to_delete, context='FACES')
bm.to_mesh(obj.data); bm.free()
```

**Performance**: ~30–90s su 250k tri (BVH è O(log n) per ray).

**Quando funziona meglio**: stesso caso d'uso della Tecnica 1 ma in workflow Blender puro (senza export STL→PyMeshLab→re-import).

**Limiti**: bordi della membrana (= dove tela incontra rami) hanno visibility intermedia → soglia critica. **Pattern multi-pass**:
1. Pass aggressivo con threshold 0.10 → rimuove la membrana centrale
2. Pass conservativo con threshold 0.30 SOLO su componenti connesse alla selezione precedente → pulisce i bordi

---

## Tecnica 3 — Meshmixer (fallback manuale, ROBUSTO)

Quando le tecniche automatiche falliscono o producono falsi positivi, workflow manuale community-tested:

1. **Import STL** in Meshmixer (gratis, 110MB, [meshmixer.com](http://www.meshmixer.com/))
2. **Select** (tasto `S`) → click su una face della tela
3. **Modify → Expand to Connected** con **angle threshold ~20°** → autoseleziona TUTTA la superficie planare connessa
4. **Edit → Discard** (tasto `X`) → cancella le facce selezionate
5. **Edit → Erase & Fill** per buchi residui (rimuove e ricostruisce smooth)
6. **Analysis → Inspector** → chiude eventuali non-manifold residui
7. **Export STL** pulito → import in Bambu Studio

**Pattern di trigger**: usare Meshmixer quando in Blender 2 tecniche automatiche consecutive (Tecnica 1 + Tecnica 2) hanno fallito.

---

## Tecnica 4 — Bambu Studio Mesh Boolean / Negative Part (slicer-level)

Solo come ultimissimo fallback, per asset già in slicer:

- **Mesh Boolean Subtract** ([Bambu Wiki](https://wiki.bambulab.com/en/software/bambu-studio/mesh-boolean)): import asset + cubo grande quanto la tela ma più sottile dei rami → boolean difference. **Limite**: rigido (taglia in piano), fallisce su transizioni smooth.
- **Negative Part** ([Bambu Wiki](https://wiki.bambulab.com/en/software/bambu-studio/subtract-a-part)): più rapido del boolean ma **slice-only** (non esporta STL modificato). Right-click sul cubo → Change Type → Negative Part.

---

## Decision tree per il workflow

```
asset con "tela del fondo" sospetta
├── filename contiene relief|wall_art|2.5D|plaque|medallion|lithophane?
│   ├── SÌ → tela INTENZIONALE, NON rimuovere
│   └── NO → procedi
│
├── PyMeshLab disponibile?
│   ├── SÌ → Tecnica 1 (AO per-vertex)
│   └── NO → Tecnica 2 (BVHTree raycast)
│
├── risultato OK? (verifica HIRES 1920×1440 multi-vista)
│   ├── SÌ → FINE
│   └── NO (residui o danno collateral)
│       ├── tentativo #2 con soglie diverse
│       └── tentativo #2 fallito → STOP, proponi Tecnica 3 (Meshmixer)
```

**STOP RULE assoluta** (regola 31 TESTING_LOG): dopo **2 tentativi falliti automatici**, NON iterare ulteriormente. Proporre Meshmixer all'utente. Caso `albero_corallo` documenta come 8+ tecniche consecutive abbiano peggiorato l'asset invece che migliorare.

---

## Validazione post-rimozione

Sempre **render HIRES 1920×1440 multi-vista** (regola 30 TESTING_LOG):
- Vista TOP ortografica (silhouette piano XY)
- Vista BOTTOM ortografica (base del modello, evidenzia "buchi" interni)
- Vista perspective dalla **stessa angolazione** che l'utente vede in viewport
- Se l'utente ha mandato uno screenshot, REPLICARE quell'angolazione

**Confidence calibration**: mai dichiarare "membrana rimossa" senza aver visto risultato HIRES + multi-vista. Render basse risoluzioni nascondono la membrana.

---

## Riferimenti

- `Workflow/TESTING_LOG.md` — regole 31, 37, 38, 40, 41 + Appendice A (Research Report)
- [PyMeshLab filter_list](https://pymeshlab.readthedocs.io/en/latest/filter_list.html)
- [MeshLab Stuff — Remove internal faces with AO](http://meshlabstuff.blogspot.com/2009/04/how-to-remove-internal-faces-with.html)
- [CFD Engine #119 — Removing internal details from STLs](https://cfdengine.com/newsletter/119/)
- [varkenvarken/visiblevertices.py](https://github.com/varkenvarken/blenderaddons/blob/master/visiblevertices.py)
- [Blender BVHTree API](https://docs.blender.org/api/current/mathutils.bvhtree.html)
- [Meshmixer (Autodesk, free)](http://www.meshmixer.com/)
- [Maker Hacks — Meshmixer STL editing](https://medium.com/@makerhacks/meshmixer-tutorial-using-meshmixer-to-delete-and-edit-parts-of-an-existing-stl-32a3ed4faad8)

---

## Casi storici documentati

| Asset | Tecniche tentate | Esito |
|---|---|---|
| `albero_corallo` (SESSION 003e + 004) | Flood-fill, Decimate Dissolve, Voxel Remesh, snap+fill, fan triangolare, curvature analysis, BVH raycast (8+) | Tutti falliti → asset accettato con membrana, alternative: PyMeshLab AO o Meshmixer |
| `vaso_limoni` (SESSION 004) | Snap vertici a Z=0 → distorto. Delete+fill → caotico. Fan triangolare → pulito. Bisect Z=4.98 → SOLUZIONE FINALE | Bisect singolo era la soluzione corretta dall'inizio (KISS principle, regola 34) |
