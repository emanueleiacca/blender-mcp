# Tripo P1.0 / H3.1 (Tripo enterprise dual-track)

> **Status**: NEW Mar 2026 (P1.0) / UPDATE Apr 2026 (H3.1). Successor della Tripo 3.0 in MakerLab.

## 1. Cos'è

Tripo (azienda) ha lanciato due track paralleli nel 2026:

### Tripo P1.0 — "Print" track
- **Target**: FDM 3D printing diretta
- **Output**: mesh **watertight by design**
- **Tradeoff**: meno texture, più reliability per stampa

### Tripo H3.1 — "High-fidelity" track
- **Target**: alta fedeltà al source image
- **Output**: mesh dettagliata, texture PBR opzionale
- **Tradeoff**: post-processing più richiesto

⚠️ **Disambiguazione**: NON confondere con **Hi3D 2.1** (= Hitem3D, Math Magic). Tripo H3.1 e Hi3D 2.1 sono **due engine diversi** di due aziende diverse.

## 2. MakerLab integration

Stato a maggio 2026:
- **Tripo 3.0** in MakerLab → in fase di sostituzione con **Tripo P1.0**
- Verificare etichetta UI MakerLab: "Tripo 3.1" attuale potrebbe essere ribrand di P1.0
- H3.1 (high-fidelity track) probabilmente solo su web app Tripo diretta, non in MakerLab

## 3. Quando preferirlo

### P1.0 (print track):
| Scenario | Verdetto |
|---|---|
| Vuoi mesh watertight diretto, no rework Blender | ✅ usalo |
| Iterazione rapida (~2.5 min su MakerLab) | ✅ usalo |
| Top quality + micro-dettaglio | ❌ Hi3D 2.1 Pro |

### H3.1 (high-fidelity track):
| Scenario | Verdetto |
|---|---|
| Texture PBR per rendering | ✅ usalo (irrilevante per FDM) |
| Alta fedeltà al source image | ✅ compete con Hi3D |
| FDM diretto | ⚠️ richiede più rework di P1.0 |

## 4. vs Hi3D 2.1 (engine primario utente)

| Aspetto | Tripo P1.0 | Hi3D 2.1 |
|---|---|---|
| Tempo MakerLab | ~2.5 min | ~7 min |
| Watertight nativo | ✅ | Spesso |
| Polycount | ~150k | ~2M |
| Delight slider | ❌ | ✅ |
| Top per soggetti occluded | ❌ | ✅ |
| Top per soggetti banali | ✅ (velocità) | Overkill |

**Conclusione**: Tripo P1.0 è **complementare** a Hi3D, non sostitutivo. Usalo per smoke test rapidi o soggetti semplici.

## 5. Fonti

- https://www.tripo3d.ai/blog/tripo-p1
- https://www.tripo3d.ai/blog/tripo-h3-1
- (verificare quando si stabilizza etichettatura MakerLab)

## Changelog

- **2026-05-13**: file creato in seguito a deepsearch. Sostituisce gradualmente `tripo-3.1.md` quando MakerLab espone P1.0.
