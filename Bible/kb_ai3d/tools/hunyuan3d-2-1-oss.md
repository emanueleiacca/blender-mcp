# Hunyuan3D 2.1 OSS (Tencent open-source)

> **Status**: Open-source local, Tencent. **Secondary OSS option** dopo TRELLIS.2. Da NON confondere con Hunyuan 3D 3.1 (cloud, in MakerLab).

## 1. Cos'è

**Hunyuan3D 2.1** è la versione open-source rilasciata da Tencent del loro modello image-to-3D. Disponibile su GitHub e HuggingFace. Print-ready out-of-the-box (mesh watertight).

**Differenze chiave vs Hunyuan 3D 3.1 cloud (MakerLab)**:
- Open-source vs proprietario
- Eseguibile in locale
- Versione precedente (3.1 cloud ha più feature, ma 2.1 OSS è "stable")
- Niente costi, niente rate limit

**Differenze vs TRELLIS.2**:
- Setup leggermente più semplice di TRELLIS.2
- Watertight scripts meno robusti
- Stessa fascia di qualità (~Tripo 3.1)

## 2. Capacità tecniche

- **Architettura**: Diffusion + neural implicit representation
- **Polycount**: configurabile, default ~150k tri
- **Resolution**: voxel grid 512³ (sotto TRELLIS.2 1024³, molto sotto Hi3D 1536³)
- **Print-ready**: mesh watertight nativamente, no script di repair necessari
- **Format export**: GLB, OBJ
- **VRAM richiesta**: 8GB+ (più accessibile di TRELLIS.2)

## 3. Quando preferirlo

| Scenario | Verdetto |
|---|---|
| Hai GPU 8-12GB VRAM (RTX 3060/3070/4060) | ✅ TRELLIS.2 richiede più VRAM |
| Setup TRELLIS.2 fallisce / troppo complicato | ✅ Hunyuan3D 2.1 OSS è più friendly |
| Mesh watertight è priorità su quality | ✅ usalo |
| Vuoi top quality assoluta | ❌ Hi3D 2.1 Pro cloud |
| Soggetti con micro-dettaglio fitto | ❌ Hi3D 2.1 |

## 4. Install/setup (sintesi)

```bash
git clone https://github.com/Tencent/Hunyuan3D-2.1
cd Hunyuan3D-2.1
pip install -r requirements.txt
# scarica modelli (~8GB)
huggingface-cli download tencent/Hunyuan3D-2.1
```

## 5. Quality vs cloud Hunyuan 3.1

- **Silhouette**: ~equivalente
- **Dettaglio fine**: cloud 3.1 marginalmente migliore
- **Watertight**: identico (entrambi nativi watertight)
- **Speed locale**: 60-120 sec su RTX 4070; cloud 3.1 ~3 min su MakerLab

## 6. Adatto al nostro caso d'uso?

**Sì, come secondary OSS option** dopo TRELLIS.2.

Vantaggi specifici:
- Più accessibile sul piano hardware (8GB VRAM è common)
- Mesh watertight = meno rework Blender per soggetti semplici
- Backup robusto se TRELLIS.2 fallisce su setup

Limiti:
- Qualità sotto Hi3D 2.1 Pro (cloud) su micro-dettaglio
- No integration MakerLab → workflow due-step

## 7. Fonti

- https://github.com/Tencent/Hunyuan3D-2.1
- https://huggingface.co/tencent/Hunyuan3D-2.1
- https://3d.hunyuan.tencent.com (cloud version)
- Paper: arXiv:2401.xxxxx (originale Hunyuan3D)

## Changelog

- **2026-05-13**: file creato in seguito a deepsearch RESEARCH_2026-05-13.md. Da non confondere con `hunyuan-3d-3.1.md` (cloud MakerLab).
