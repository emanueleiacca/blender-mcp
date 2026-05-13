# Esempio: Vaso limoni (piccolo portavaso decorativo)

**Data**: 2026-05-08
**Soggetto**: Piccolo portavaso decorativo con limoni scolpiti in rilievo, cordone intrecciato al bordo, foglie, apertura superiore
**Materiale originale**: Gesso / plaster (prototipo artigianale, NON ceramica finita)
**Dominio**: Prodotti decorativi tradizionali — ceramica campano-siciliana

---

## Foto sorgenti

- 5 foto con cellulare (4 angolazioni distinte + 1 duplicato)
- Angolazioni: frontale bassa (×2), lato/retro basso, dall'alto, 3/4 frontale
- Sfondo: tavolo grigio chiaro
- Illuminazione: mista (finestra + lampada ambiente)
- Difetti foto: prospettiva forte (scattate molto vicino), mani visibili in 2 foto, sfondo non uniforme in 1

## Foto selezionate per Gemini (4)

| Foto | Angolazione | Motivo |
|------|-------------|--------|
| 5 (frontale bassa, no mano) | Frontale | vista principale |
| 4 (3/4 frontale sx) | 3/4 | foglie e bordo rim visibili |
| 2 (lato/retro basso) | Lato-retro | distribuzione limoni sul retro |
| 3 (dall'alto) | Top-down | cordone intrecciato + pianta quadrata |

## Prompt Gemini usato

- Base: `multi_photo_canonical.md`
- Block aggiuntivi: `casting_defects.md` (gesso) + `detail_preservation.md` + `perspective_correction.md`
- Nota specifica inserita nel prompt: forma pianta quasi quadrata smussata (non circolare), apertura superiore, cordone intrecciato al bordo rim, foglie, texture buccia limone

## Output Gemini

- **Qualità generale**: buona — sfondo bianco, vista 3/4, deglossed, proporzioni OK
- **Problemi rilevati**:
  - Bolle d'aria del gesso ancora visibili come micro-crateri sui limoni → **non rimosse** perché il prompt non includeva `casting_defects.md` (prima iterazione senza quel block)
  - Rope border sinistra leggermente meno definita del lato destro
  - Leggera fusione di 2-3 limoni in basso

## Decisioni Decision Tree

| Domanda | Risposta | Tool implicato |
|---------|----------|----------------|
| Volti? | No | tutti in gioco |
| Densità dettaglio | Alta-media (limoni grandi + cordone fino) | Tripo 3.1 HD |
| Simmetria | Semi-simmetrica (pianta quadrata smussata) | NON forzare symmetry |
| Materiale | Gesso (⚠️ scoperto a posteriori) | casting_defects block |
| Foto disponibili | 5 → multi-canonical | multi_photo_canonical.md |

**Tool scelto**: Tripo 3.1 HD (500k) — default robusto, tempo 2.5 min, adeguato per densità media-alta

## Output MakerLab — Tentativo 1 (FALLITO)

- Engine: **Tripo 3.1**
- Settings disponibili in MakerLab: **nessuno** (solo selezione engine — correzione importante alla KB)
- Tempo effettivo: ~2.5 min
- **Qualità mesh: PESSIMA** — il modello non è utilizzabile
  - Fondo bucato
  - Forma vaso assente: il tool ha generato una massa informe di blob organici
  - Cordone intrecciato sparito
  - Struttura cilindrica del contenitore non ricostruita
  - Limoni privi di forma definita, fusi tra loro

**Cause del fallimento identificate**:
1. ⚠️ **Apertura del vaso visibile nell'immagine Gemini** (vista 3/4 con angolo dall'alto inclusa nella sintesi). Il tool ha visto "oggetto aperto in cima con massa di elementi che lo coprono" → interpretato come pila di frutti, non come vaso.
2. ⚠️ **Limoni coprono ~100% della parete esterna** → nessuna zona di "muro neutro" che aiuti il tool a capire la struttura contenitore sottostante
3. ⚠️ **Immagine Gemini era multi-foto canonical con vista top-down inclusa** → non adatto per contenitori aperti

**Errori di processo scoperti**:
- La KB indicava settings MakerLab (geometry quality, topology, face limit, symmetry) che NON ESISTONO nell'UI → corretti su tutti i file
- La vista dall'alto NON va inclusa per soggetti con apertura: rivela l'interno e confonde il tool

## Tentativo 2 — Gemini (FALLITO) + 3D Rodin (FALLITO)

**Gemini output**: Gemini ha generato un render 3D idealizzato invece di elaborare le foto. Proporzioni completamente diverse dall'originale (vaso alto e cilindrico vs originale basso e panciuto), base cubica aggiunta che non esiste, limoni normalizzati e uniformi. Causa: prompt troppo descrittivo + sintesi multi-foto → Gemini ha "generato" invece di "editato".

**Rodin Gen-2 3D output**: blob informe di sferoidi gialli, fondo bucato, nessuna struttura vaso riconoscibile. FALLITO.

**Lezione codificata**: aggiunto `photo_fidelity_lock.md` a tutti i prompt. Documentato "Rischio allucinazione Gemini" in README.

---

## Tentativo 3 — Gemini (OK) + 3D comparativo su 3 tool

**Gemini output**: ✅ Proporzioni fedeli all'originale, sfondo bianco, aspetto matte, photo-fidelity lock funzionante. Problema Gemini risolto. L'apertura in cima rimane visibile — questo contribuisce al fondo bucato nei tool 3D.

**Comparativa 3 tool sulla stessa immagine Gemini**:

| Tool | Struttura | Fondo | Dettaglio | Verdetto |
|------|-----------|-------|-----------|---------|
| Rodin Gen-2 (~3 min) | ❌ blob | ❌ bucato | ⚠️ | Inutilizzabile |
| Meshy 6 (~4 min) | ❌ blob | ✅ chiuso | ⚠️ fronte ok / retro no | Parzialmente lavorabile |
| Hi3D 2.1 (~7 min) | ❌ blob | ✅ chiuso | ✅ migliore | Migliore, lavorabile in Blender |

**Problema fondamentale identificato**: il soggetto è un **"oggetto strutturalmente occluso"** — i limoni coprono 100% della parete, il tool non può inferire la forma del contenitore. Nessun tool ricostruisce la struttura cilindrica. Il blob Hi3D è il punto di partenza più valido per un rework Blender.

**Conclusione sessione**: Hi3D 2.1 è il tool da usare su soggetti complessi. I 7 min valgono. I tool veloci (Tripo, Rodin) non recuperano il gap di qualità su questa categoria.

---

## Prossimi passi — Rework Blender su output Hi3D

**Cambiamenti rispetto al tentativo 2**:

1. **Angolazione Gemini**: solo foto **laterali basse** (foto 5 + foto 4 + foto 2). NON includere foto 3 (dall'alto). Angolo ≤ 10° sopra il bordo del vaso.
2. **Istruzione Gemini aggiuntiva**: *"Render from near-ground lateral angle. The top rim must appear as a clean edge — DO NOT show the interior. The vessel must read as a solid sculptural object."*
3. **Tool**: cambiare a **Rodin Gen 2** (3 min) o **Hi3D 2.1** — meglio su forme scultoree complesse rispetto a Tripo
4. **Block Gemini**: aggiungere `casting_defects.md` (mancava nel tentativo 1 → bolle visibili)

## Lezioni codificate nella KB

1. **Domanda 0 nel decision tree**: chiedere PRIMA se il soggetto ha apertura/cavità visibile → cambia angolazione Gemini
2. **Settings MakerLab**: solo engine selezionabile, nessun altro parametro
3. **Materiale**: chiedere sempre gesso vs ceramica prima del prompt Gemini
4. **Vista dall'alto**: utile per capire la forma, MAI da includere se il soggetto è un contenitore aperto
