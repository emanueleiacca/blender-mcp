# TRELLIS.2 / TRELLIS.2-4B — local OSS

> **Status**: NEW 2026, Microsoft Research, MIT license. **Opzione primaria open-source local** per chi ha GPU adeguata. Da considerare come fallback locale al workflow MakerLab.

## 1. Cos'è

**TRELLIS.2** è il modello image-to-3D di Microsoft Research (evoluzione del TRELLIS originale 2024), rilasciato in versione **4B parametri** sotto licenza **MIT** (permissiva: uso commerciale OK).

**Differenze chiave vs cloud (Hi3D/Tripo/Hunyuan)**:
- Eseguibile in locale su GPU consumer (RTX 4070+ con 12GB VRAM raccomandati; RTX 4090 ideale)
- Niente costi per generazione
- Niente rate limit
- **Ships hole-filling scripts** specifici per print-readiness (vantaggio significativo vs altri OSS)
- Setup non banale (ambienti Python, CUDA, modelli da scaricare)

## 2. Capacità tecniche

- **Architettura**: Latent diffusion 3D + Sparse Voxel Representation (SVR)
- **Polycount**: configurabile, default ~200k tri
- **Resolution**: voxel grid fino a 1024³ (paragonabile a Hunyuan, sotto Hi3D 1536³)
- **Print-ready scripts**: include `hole_fill.py` e `watertight_check.py` nello repo ufficiale
- **Format export**: GLB, OBJ, PLY → conversione STL via Blender o trimesh
- **Multi-view**: supportato (2-8 viste)

## 3. Quando preferirlo

| Scenario | Verdetto |
|---|---|
| Hai RTX 4070+ disponibile, vuoi batch processing | ✅ usalo |
| Costi cloud Hi3D/Tripo diventano significativi (uso intensivo) | ✅ usalo |
| Lavori offline / no internet | ✅ usalo |
| Hai bisogno di privacy (soggetti riservati, prototipi non rilasciati) | ✅ usalo |
| Workflow ad alta iterazione / sperimentazione | ✅ usalo |
| Vuoi qualità top assoluta su singolo soggetto | ❌ Hi3D 1536³ Pro è marginalmente migliore |
| Non hai GPU / hai GPU < 12GB VRAM | ❌ usa cloud |
| Setup complicato è un blocco | ❌ usa MakerLab |

## 4. Install/setup (sintesi)

```bash
git clone https://github.com/microsoft/TRELLIS-2
cd TRELLIS-2
conda create -n trellis2 python=3.10
conda activate trellis2
pip install -r requirements.txt
# scarica modelli (~15GB)
python download_models.py
```

Per workflow integration con ComfyUI: esiste un node `ComfyUI-TRELLIS2` (community).

## 5. Quality vs Hi3D/Tripo

Benchmark indipendenti (3DAIStudio 2026):
- **Silhouette accuracy**: ~equivalente a Tripo 3.1, sotto Hi3D 1536³
- **Print-ready out-of-the-box**: TOP fra OSS (script integrati)
- **Tempo generazione**: 30-90 sec su RTX 4090, 2-4 min su RTX 4070

## 6. Adatto al nostro caso d'uso?

**Sì, come fallback locale**. Specificamente:

- Per **iterazione veloce** se hai RTX 4090 disponibile → batch testing rapido
- Per **soggetti che NON richiedono micro-dettaglio fitto** (per i quali Hi3D 2.1 Pro è meglio)
- Per **privacy** se lavori su prototipi non rilasciati

**Limiti per il workflow utente**:
- Setup non triviale (servono Python, CUDA, modelli)
- Qualità marginalmente inferiore a Hi3D su decoro fitto
- No integration MakerLab → workflow due-step (TRELLIS local → import Bambu Studio)

## 7. Workflow ricetta (futuro)

⚠️ Sezione da popolare empiricamente quando l'utente avrà testato TRELLIS.2 in locale.

```
[Photo cleanup via Gemini]
  ↓
[TRELLIS.2 local: python infer.py --image <path> --output <stl>]
  ↓
[hole_fill.py + watertight_check.py applicati automaticamente]
  ↓
[Blender: analyze_mesh_for_print via MCP]
  ↓
[Export STL finale → Bambu Studio]
```

## 8. Fonti

- https://github.com/microsoft/TRELLIS-2
- https://huggingface.co/microsoft/TRELLIS-2-4B
- https://www.3daistudio.com/best-ai-tools-3d-printing-2026
- https://arxiv.org/abs/2025.xxxxx (paper TRELLIS-2, da verificare ID arXiv specifico)

## Changelog

- **2026-05-13**: file creato in seguito a deepsearch RESEARCH_2026-05-13.md. Da popolare con dati empirici dopo primo test locale.
