# Block: Video-only Input (solo video disponibile, no foto statiche)

## Quando usarlo

Hai **solo un video** del soggetto:
- Video smartphone (orbit around object)
- Video drone (oggetti grandi)
- Video LiDAR scan (iPhone 12 Pro+)
- Video drift / handheld

## ⚠️ Limite duro

Tutti i workflow image-to-3D richiedono **foto statiche di alta qualità**. Video shaky, low-light, o con motion blur **non funzionano**. Questo block è una guida per estrarre/usare il video al meglio.

## Strategie alternative

### Strategia A — Nerfstudio + splatfacto → 3DGS → Poisson mesh (TOP)

Per video di buona qualità (smartphone stabile, ~30 sec orbita completa):
1. Install Nerfstudio (richiede CUDA)
2. `ns-process-data video --data <video.mp4> --output <out>` (estrae frames)
3. `ns-train splatfacto` (training 3DGS, ~30 min su RTX 4070)
4. Export → mesh Poisson reconstruction
5. → workflow standard Blender (rework, decimate, export STL)

**Quality**: ottima per oggetti texturati. Setup CUDA non triviale.

### Strategia B — Keyframe estrazione manuale

Fallback per video shaky o senza CUDA:
1. Apri il video in un player (VLC, Premiere)
2. Identifica 4-8 frame stabili da angolazioni diverse (front, 3/4 dx, 3/4 sx, retro)
3. Esporta come PNG (con `ffmpeg -ss <time> -frames:v 1 frame.png`)
4. Workflow multi-photo standard (Gemini canonical + image-to-3D)

### Strategia C — KIRI Engine (mobile)

Per video iPhone LiDAR:
- Carica video in KIRI Engine app
- Esegue photogrammetry automatica
- Export mesh OBJ
- Limite: 150 foto/scan free tier; qualità variabile

### Strategia D — Luma AI

Per 3DGS da video smartphone:
- Upload video alla web app Luma AI
- Genera 3DGS
- Limite: **no mesh export FDM-ready** (Luma è ottimizzato per rendering, non stampa)

## Block per Strategia B (estrazione keyframe + Gemini canonical)

```
=== VIDEO-EXTRACTED KEYFRAMES — CANONICAL FUSION ===

The source images are keyframes extracted from a video.
Source quality may vary: some frames may be slightly blurry or
have different lighting due to handheld capture.

FUSION RULES
- Treat the SHARPEST frame as the ground truth for geometry
- Use other frames only to fill in angles not visible in primary
- DO NOT average lighting across frames (use primary's lighting)
- DO NOT introduce motion blur or temporal artifacts

OUTPUT
- Single canonical 3/4 frontal view (cf. master_template)
- Lighting and clarity must match the BEST source frame
```

## Quando NON usarlo

- Hai foto statiche di qualità → usa workflow standard
- Video < 10 sec o senza orbita completa → riprenderlo con orbita

## Origine

Deepsearch 2026-05-13 § D15. Cross-reference: Nerfstudio docs, KIRI Engine, Luma AI.
