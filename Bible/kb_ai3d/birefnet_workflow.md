# BiRefNet workflow — pre-pass background removal

> **Status**: workflow opzionale per **massima precisione di scontorno** prima di Gemini. Benchmark indipendente: IoU 0.87, Dice 0.92 (top fra modelli BG removal 2026).

## Quando usarlo

Il workflow Gemini fa già un buon scontorno per soggetti con sfondo chiaro/uniforme. **BiRefNet pre-pass è utile** quando:

- Sfondo **complesso** (libreria piena, vetrina con riflessi, scena outdoor)
- Bordi del soggetto **sottili** (pelo, foglie, frange) che Gemini perde
- Riflessi/glow attorno al soggetto che Gemini interpreta come geometria
- Vuoi **massima fedeltà silhouette** per Hi3D 1536³ Pro

## Pipeline ibrida (raccomandata per "hero jobs")

```
[Foto sorgente]
    ↓
[BiRefNet RMBG-2.0] → alpha PNG con bordo pixel-perfect
    ↓
[Gemini 2.5 Flash] → delight + perspective (lavora su alpha già pulito)
    ↓
[Gemini 3 Pro] → canonical view (se multi-foto)
    ↓
[Hi3D 2.1] → mesh
```

## Tool BiRefNet — opzioni

### Opzione 1 — HuggingFace Spaces (no install)

```
https://huggingface.co/spaces/ZhengPeng7/BiRefNet
```

Upload foto → download alpha PNG. Gratis, no install. Limite: rate limit / queue.

### Opzione 2 — Local Python

```bash
pip install transformers torch torchvision pillow
```

```python
from transformers import AutoModelForImageSegmentation
from PIL import Image
import torch

model = AutoModelForImageSegmentation.from_pretrained(
    "ZhengPeng7/BiRefNet",
    trust_remote_code=True
)
model.eval()

img = Image.open("input.jpg")
# preprocess: resize 1024x1024
# inference: model(img_tensor)
# output: alpha mask PNG
img.save("output_alpha.png")
```

VRAM: 4GB+ sufficient.

### Opzione 3 — Photoshop AI / Affinity (alternativa commerciale)

Funzioni "Select Subject" o "Remove Background" — meno preciso di BiRefNet ma workflow integrato.

## Quality comparison (2026 benchmarks)

| Tool | IoU | Dice | Note |
|---|---|---|---|
| **BiRefNet RMBG-2.0** | **0.87** | **0.92** | Top accuracy |
| ISNet | 0.84 | 0.90 | Solid baseline |
| U2Net | 0.81 | 0.88 | Storica, ancora ok |
| rembg (combined) | 0.83 | 0.89 | Library Python wrap |
| Photoshop AI | ~0.80 | ~0.87 | Workflow-friendly |
| Gemini standalone | ~0.75 | ~0.83 | Adatto per sfondi facili |

Source: 3DAIStudio 2026 benchmark, Hugging Face leaderboard BG removal.

## Quando NON usare BiRefNet

- Foto con sfondo bianco/grigio uniforme già pulito → Gemini basta
- Iterazione veloce (testing rapido) → costa tempo extra
- Setup local non disponibile e queue HuggingFace lenta → skippa

## Cross-reference

- `gemini_prompts/README.md` § Alternative AI cleanup tools
- `tools/hitem3d-2.1.md` § 3.3 (workflow Gemini pre-cleanup raccomandato)

## Origine

Deepsearch 2026-05-13 § B5 (RESEARCH_2026-05-13.md).
