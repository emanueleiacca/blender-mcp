# Filamenti per look ceramica/terracotta su Bambu A1

> Riferimento per chi vuole stampe FDM con **finish visivamente vicino a ceramica/terracotta** senza post-processing (vernici, smalti).

## Filamenti raccomandati

### 1. Clay PLA — look ceramico diretto

**Brand**: Filament2Print (anche altri rebrand disponibili).
- Composizione: PLA con caricamento ceramico (≤25%)
- Finish: matte, rugoso al tatto, simile a ceramica grezza non smaltata
- Colori: tipicamente bianco, beige, terracotta
- Stampabilità A1: **sì**, nozzle hardened steel raccomandato (caricamento ceramico è leggermente abrasivo, particelle <250µm)
- Temperature: 195-215°C
- Bed: 50-60°C

### 2. Fillamentum StoneFill — terracotta look

**Brand**: Fillamentum (CZ).
- Composizione: PLA + carico minerale (pietra naturale)
- Finish: rugoso, "stone-like"
- Colori: light stone, dark stone, terracotta
- Stampabilità A1: **sì** con hardened steel
- Temperature: 200-225°C
- Bed: 50-60°C

### 3. Polymaker PolyTerra Marble

- Composizione: PLA + carico marmo
- Finish: matte con leggera texture
- Adatto a oggetti dove il look "pulito marmoreo" è prioritario

### 4. Alternative budget: PLA matte standard + paint

Per controllo totale del look (lucidatura selettiva, smalto a pennello):
- Stampa in PLA matte bianco standard (nozzle 0.4 standard)
- Vernicia/smalta a mano per look ceramica autentica
- Costo: filamento normale + materiali pittura

## ⚠️ Vincoli A1 + filamenti abrasivi

### Hardware

- **Nozzle hardened steel obbligatorio** per Clay PLA / StoneFill / PolyTerra Marble
- Bambu A1 stock: nozzle hardened steel 0.4mm disponibile come accessorio (~25€)
- Senza hardened steel: nozzle stock si usura in 1-3 ruote di filamento abrasivo

### Parametri slicing per ceramica look

| Parametro | Valore raccomandato |
|---|---|
| Layer height | 0.16-0.20 mm (matte naturale, layer line meno visibile) |
| Wall count | 3-4 walls (parete più robusta, finish più "solido") |
| Top/Bottom | 5-6 layers (top compatto) |
| Infill | 15-25% gyroid (estetico se trasparenza ridotta) |
| Speed outer | 30-40 mm/s (qualità superficiale prioritaria) |
| Print temp | come da scheda filamento, lower end della range |
| Fan | 100% dopo i primi 3 layer (PLA standard) |

## Filamenti AMS compatibili

Per stampe multicolore con AMS standard A1:
- Mix Clay PLA + PLA standard colorato per accent colors
- Verifica feed-rate (caricamenti minerali possono richiedere flow rate aggiustato)

## Look-alike "ceramica vera" — post-processing opzionale

1. **Sanding leggero** (grana 400-600) per smooth degli strati Z
2. **Primer matte** + tempera/acrilico → look smaltato autentico
3. **Cera neutra** (su Clay PLA) per leggera lucidatura senza coprire texture

## ⚠️ Cosa NON cercare per "ceramica look"

- **PLA standard bianco** lucido — finish lucido NON è ceramica
- **PETG / ABS** — finish plasticoso, lontano da ceramica
- **TPU / TPE** — flessibili, irrilevanti
- **Wood-fill PLA** — finish legno, NON ceramica

## Cross-reference

- `Bambu Wiki documentation/INDEX.md` — KB Bambu materiali generali
- Deepsearch 2026-05-13 § C4 (RESEARCH_2026-05-13.md)

## Changelog

- **2026-05-13**: file creato in seguito a deepsearch. Da popolare con test empirici dei filamenti specifici.
