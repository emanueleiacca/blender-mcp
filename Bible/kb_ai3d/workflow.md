# Workflow — da foto a STL stampabile

Pipeline manuale completa. Ogni step descrive cosa fare, dove, e cosa controllare prima di passare al successivo. Non saltare gli step di verifica: un errore allo step N si paga moltiplicato negli step successivi.

---

## Panoramica

```
[1] Scatto foto del riferimento (cellulare, 1 o più angolazioni)
        ↓
[2] Claude analizza le foto → sceglie tool 3D + prompt Gemini adatto
        ↓
[3] App Gemini: incolla prompt + carica foto → ottieni 1 immagine pulita
        ↓
[4] Verifica visiva dell'output Gemini (checklist sotto)
        ↓
[5] Carica immagine su MakerLab (o web app del tool) → genera mesh
        ↓
[6] Download STL/3MF
        ↓
[7] Blender: ispezione + fix non-manifold + scala + base
        ↓
[8] Bambu Studio → slice → A1
```

---

## Step 1 — Scatto foto

**Obiettivo**: massimizzare l'informazione utile per Gemini, non per il tool 3D direttamente. Gemini farà il filtro.

**Quante foto scattare**:
- **1 foto sola** se il soggetto è asialmente simmetrico semplice (vaso liscio, pigna senza decoro asimmetrico) e Gemini deve solo pulire
- **3-4 foto** (front, 3/4 sinistra, 3/4 destra, retro) se il soggetto ha:
  - asimmetrie significative (volto, scena narrativa, decoro non ripetuto)
  - dettagli che spariscono in una vista (sottosquadri, parte posteriore decorata)
  - vuoi sfruttare la fusione canonica via Gemini

**Come scattare**:
- soggetto su superficie neutra (foglio bianco, panno grigio chiaro)
- luce diffusa (giorno coperto, vicino a una finestra senza sole diretto, softbox improvvisato con un drappo bianco)
- evita flash diretto e luci puntiformi
- distanza ~50 cm con teleobiettivo cellulare se disponibile (riduce distorsione prospettica)
- soggetto riempie ~70% dell'inquadratura
- foto da angolo leggermente sopra l'altezza del soggetto (vista 3/4 frontale)

**Cosa evitare**:
- mani che reggono il soggetto (occlusione)
- riflessi del flash sulla smaltatura
- ombre dure proiettate sul piano
- foto storte / soggetto centrato male

> Una foto "buona ma non perfetta" + Gemini dà risultati migliori di una foto "perfetta" senza Gemini. Non perdere tempo a fotografare in studio — perdici tempo a scegliere il prompt giusto.

---

## Step 2 — Claude sceglie tool + prompt

Mostrami le foto. **Prima di qualsiasi altra cosa**, devo sapere:

> ⚠️ **Domanda 1 obbligatoria**: il pezzo fotografato è in **gesso** (prototipo/maquette artigianale) o in **ceramica/terracotta/legno finiti**?

Questa risposta cambia completamente il prompt Gemini:
- **Gesso** → serve il block `casting_defects.md` per rimuovere bolle e linee di stampo. NON serve delight (già opaco).
- **Ceramica smaltata** → serve `delight_aggressive.md` per i riflessi. NON serve casting defects.

> ⚠️ **Domanda 2 obbligatoria**: la stampa sarà **multicolore** con AMS? Se sì, quanti filamenti/colori hai disponibili?

- **Mono-colore** → colore nell'immagine irrilevante, nessun block aggiuntivo
- **Multicolore (max N colori)** → aggiungere block `color_simplification.md`. Identifica le N zone cromatiche distinte e compattale a colori piatti con bordi netti nell'immagine Gemini. **Bambu A1 AMS standard = max 4 colori.**

**Regola**: sfumature pittoriche (blend, wash, patine variegate) → sempre compattare a colore singolo per zona. Non lasciare gradients che non puoi riprodurre con filamenti separati.

Poi ti dico:
1. **Tool 3D** scelto tra Tripo 3.1 / Hi3D 2.1 / Hunyuan 3.1 / Meshy 6 / Rodin Gen 2 (vedi `decision_tree.md`)
2. **Prompt Gemini** specifico, già assemblato (vedi `gemini_prompts/`)
3. **Modalità**: single-image cleanup o multi-photo→canonical
4. **Settings MakerLab** consigliati per il tool scelto

Ti darò il prompt come blocco di testo da copia-incollare nell'app Gemini insieme alla/e foto.

---

## Step 3 — Gemini cleanup

**Tool**: app Gemini (o AI Studio per controllo migliore — vedi `gemini_prompts/README.md`)

**Operazione**:
1. Apri nuova chat
2. Allega le foto (1 o più)
3. Incolla il prompt che ti ho dato
4. Genera

**Se l'output non convince**:
- chiedi a Gemini "do another version, more faithful to the original silhouette" (o "stronger delight pass" / "less stylization")
- non accettare un output "quasi giusto" → un'imperfezione qui diventa un difetto fisso nel mesh 3D
- se dopo 3 tentativi non funziona, torna da me con l'output e ridiscutiamo prompt/tool

---

## Step 4 — Verifica output Gemini (CHECKLIST)

Prima di mandare l'immagine al tool 3D, verifica:

- [ ] Sfondo è **bianco puro uniforme** (no gradiente, no ombre residue)
- [ ] Il soggetto **occupa 70-80%** del frame, centrato
- [ ] **Nessun riflesso speculare** sulla superficie (lo smalto deve apparire opaco)
- [ ] **Nessuna ombra proiettata** sul piano d'appoggio
- [ ] La **silhouette** è identica a quella reale (Gemini a volte allunga/accorcia)
- [ ] I **dettagli ornamentali** sono nitidi, non sfocati né "ammorbiditi"
- [ ] **Nessun elemento estraneo** (mani, supporti, sfondo residuo)
- [ ] **Nessuna stilizzazione cartoon** — deve sembrare ancora il tuo oggetto reale, solo pulito

Se anche solo un punto fallisce, rigenera con prompt corretto. Non andare avanti.

---

## Step 5 — Generazione mesh

### 5a. Su MakerLab (Tripo, Hunyuan, Meshy, Hi3D, Rodin)

1. Vai su `makerworld.com/makerlab/imageTo3d`
2. Seleziona engine consigliato da `decision_tree.md`
3. Carica la singola immagine pulita uscita da Gemini
4. Imposta i parametri secondo il file del tool (es. `tools/tripo-3.1.md` §6)
5. Genera (1-6 minuti)
6. Anteprima: ruota il modello per vedere se i dettagli ornamentali sono presenti
7. Se OK → export STL o 3MF (2 crediti)

### 5b. Decision: rifare o procedere?

**Rigenerare se**:
- silhouette deformata
- volti deformati (Hunyuan → cambia engine)
- dettagli ornamentali "spariti" (smoothing eccessivo) → aumenta polycount o cambia tool
- base appiattita non corrispondente al reale
- mesh con grossi buchi visibili

**Procedere se**: i difetti sono piccoli e fissabili in Blender (qualche non-manifold, normali invertite, base da spianare).

---

## Step 6 — Download

Salva STL nominato in modo descrittivo: `<soggetto>_<tool>_<data>.stl`
Esempio: `pigna_siciliana_tripo31_2026-05-08.stl`

Tieni anche l'immagine Gemini di partenza nello stesso folder per tracciabilità.

---

## Step 7 — Blender (rework FDM)

Vedi `fdm_compatibility.md` per la check-list specifica per tool. In sintesi:

1. **Import STL**, applica scala (`Object → Apply → Scale`)
2. **Verifica scala assoluta**: dimensioni reali in cm/mm devono corrispondere a quanto vuoi stampare. Usa il KB Blender (`Blender for 3d print documentation/docs/scale_detection.md`) se serve
3. **Check non-manifold**: `Edit Mode → Select → All by Trait → Non Manifold`. Se trovi vertici/edge problematici, fix con Mesh → Clean Up
4. **Spiana la base** (i tool spesso lasciano basi inclinate o spurie)
5. **Verifica spessori minimi** per A1 (0.4 mm nozzle: pareti minime 0.8-1.2 mm) — `Blender for 3d print documentation/docs/fdm_printing_constraints.md`
6. **Decimate** se polycount > 500k (rallenta lo slicer senza vantaggi visivi)
7. **Export STL** finale

---

## Step 8 — Bambu Studio + A1

Workflow standard:
- Import STL
- Auto-orient o orient manuale (per minimizzare supporti su dettagli ornamentali)
- Materiale: PLA standard è il default per decorativi mono-colore
- Quality: 0.16 mm per dettaglio fine; 0.20 mm per pezzi più grandi
- Supporti: tree support se ci sono sottosquadri (frequenti su volti scolpiti)
- Slice → check anteprima → invia ad A1

Per parametri specifici A1 e materiali → `Bambu Wiki documentation/INDEX.md` (KB Bambu).

---

## Note di tracciabilità

Per ogni progetto, tieni in `output_stl/<nome_progetto>/`:
- foto originali (`source/`)
- output Gemini (`gemini/`)
- STL grezzo dal tool 3D (`raw_<tool>.stl`)
- STL post-Blender (`final.stl`)
- nota markdown con: prompt Gemini usato, tool 3D scelto, settings, problemi incontrati

Questo è il materiale per popolare `kb_ai3d/examples/` e affinare il decision tree.
