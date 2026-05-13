# Meta SAM 3D Objects

> **Status**: NEW Apr 2026, Meta. **Niche** per scene-level segmentation + 3D, not standalone image-to-3D.

## 1. Cos'è

**SAM 3D Objects** è l'evoluzione del modello SAM (Segment Anything) di Meta, esteso al 3D. Differisce dagli image-to-3D classici:

- **Input**: scena con multipli oggetti
- **Output**: mesh separate per ogni oggetto segmentato + scene context
- **Use case**: foto di interni / scene complesse dove serve isolare un oggetto da contesto

## 2. Quando preferirlo

| Scenario | Verdetto |
|---|---|
| Foto contiene più oggetti, vuoi isolarli singolarmente | ✅ usalo |
| Foto in contesto (oggetto su tavolo con altri elementi) | ✅ alternativa a manual masking |
| Foto isolata di un singolo oggetto su sfondo neutro | ❌ overkill, usa Hi3D 2.1 |
| Vuoi top quality del singolo oggetto isolato | ❌ Hi3D 2.1 Pro è meglio |

## 3. Workflow tipo (futuro)

```
Foto scena → SAM 3D Objects → seleziona oggetto di interesse →
mesh isolata → Blender cleanup → workflow standard
```

⚠️ **Status**: integrazione MakerLab NON ancora disponibile (maggio 2026). Web app diretta Meta. Da monitorare.

## 4. Limiti

- Print-readiness: **partial** — output è scene-level, non FDM-optimized
- Mesh qualità inferiore a Hi3D/Tripo dedicati image-to-3D
- Setup non semplice (account Meta, eventuali API key)

## 5. Adatto al nostro caso d'uso?

**Marginale**. Il workflow utente parte da foto isolate del soggetto, niente scene complesse. Resta utile come **fallback** se:
- Hai solo foto del soggetto in contesto (es. ceramica in vetrina del negozio)
- Non puoi spostare l'oggetto / rifotografare in setup pulito

## 6. Fonti

- https://ai.meta.com/research/publications/sam-3d-objects/
- https://github.com/facebookresearch/sam-3d (placeholder, verificare release)

## Changelog

- **2026-05-13**: file creato in seguito a deepsearch. Da popolare con dati empirici quando integrato.
