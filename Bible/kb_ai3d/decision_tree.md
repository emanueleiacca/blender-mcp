# Decision Tree — quale tool 3D per quale foto

Logica per scegliere tra i 5 engine MakerLab in base alle caratteristiche del soggetto fotografato. Ottimizzato per il dominio "prodotti decorativi artigianali" stampati FDM mono-colore su Bambu A1.

> **🎯 Default operativo (decisione utente 2026-05-13)**: **Hi3D 2.1 è l'engine primario** per soggetti complessi/decorati. Tripo 3.1 solo per smoke test rapidi su soggetti banali. Vedi anche `tools/hitem3d-2.1.md`.

---

## Domanda 1 — Densità di dettaglio scolpito

> Quanto del valore decorativo dell'oggetto sta nel **micro-rilievo** (squame, intrecci, foglie, lineamenti scolpiti, motivi a sbalzo)?

| Risposta | Tool consigliato | Note |
|----------|------------------|------|
| **Altissima** (l'oggetto è "un tappeto di dettagli", es. testa di moro decorata, pigna fitta, vaso a sbalzo) | **Hi3D 2.1 (1536³ Pro)** o **Rodin Gen 2 (high)** | I 1536³ di Hi3D + Delight slider sono il massimo per densità. Rodin secondo se Hi3D non disponibile/lento |
| **Alta** (volto stilizzato + decoro moderato, ornamenti ripetitivi medi) | **Tripo 3.1 HD (500k)** | Buon compromesso qualità/velocità/integrazione MakerLab |
| **Media** (forma scultorea ma superfici prevalentemente lisce, vaso con poco decoro) | **Tripo 3.1 standard** o **Hunyuan 3.1 Pro** | Hunyuan se la silhouette è semplice e simmetrica |
| **Bassa** (oggetto liscio, geometria primaria, minimo ornamento) | **Hunyuan 3.1 Rapid** o **Meshy 6** | Più veloci, mesh pulita; Meshy ottimo se vuoi quad pulito (ma per FDM è equivalente) |

---

## Domanda 2 — Simmetria assiale

> Il soggetto è **assialmente simmetrico** (vaso, pigna, candelabro)?

- **Sì, fortemente**: imposta sempre `symmetry = on` quando esposto. Su Tripo usa la modalità **Multi View** se hai più foto. Su Meshy `symmetry=on` (parametro). Su Hunyuan toggle in MakerLab.
- **No** (asimmetrie intenzionali): usa single-view o multi-view senza forzare simmetria.

---

## Domanda 3 — Foto disponibili

| Numero foto | Strategia |
|-------------|-----------|
| **1 foto** | Tripo 3.1 single, Hi3D, Hunyuan, Meshy, Rodin → tutti supportano single. Gemini fa il pre-clean |
| **2-4 foto da angolazioni diverse** | Due opzioni: <br>**A.** Fondi via Gemini in 1 vista canonica → input single al tool (`gemini_prompts/multi_photo_canonical.md`) <br>**B.** Usa Tripo 3.1 Multi View, Hunyuan multi-view (8 viste), Rodin multi-image (su web app) — **richiedono** che il tool accetti multi-view direttamente; verifica su MakerLab |
| **>4 foto** | Sceglierne le 4 migliori (front, 3/4 dx, 3/4 sx, retro) e procedere come 2-4 |

> **Default raccomandato**: opzione **A** (fonderle in Gemini → single al tool). Più semplice, copre tutti i tool, e Gemini fa un lavoro eccellente di vista canonica anche da foto subottimali.

---

## Domanda 4 — Materiale / finish del soggetto reale

> Che tipo di superficie ha l'oggetto fotografato?

| Finish | Sfida principale | Prompt Gemini | Tool con vantaggio |
|--------|------------------|---------------|-------------------|
| **Gesso / plaster** (prototipo artigianale) | bolle d'aria → micro-crateri; linee di stampo; NO riflessi | `single_photo_cleanup.md` + **`casting_defects.md`** + `detail_preservation.md` | Tripo 3.1 HD > Hi3D 2.1 (ma gesso è già ottimo per i tool — opaco, bianco) |
| **Ceramica smaltata lucida** | riflessi specular interpretati come geometria | `single_photo_cleanup.md` + **`delight_aggressive.md`** | Hi3D (Delight slider hardware) > Rodin > Tripo |
| **Terracotta / opaco** | nessuna sfida specular; possibili dettagli a basso rilievo che scompaiono | `single_photo_cleanup.md` + **`detail_preservation.md`** | Hi3D / Rodin / Tripo HD |
| **Legno intagliato** | grain del legno può essere letto come rumore | `single_photo_cleanup.md` con nota texture | Tripo (preserva linee) > Rodin |
| **Metallo battuto / sbalzato** | riflessi forti + dettagli a bassissimo rilievo | `single_photo_cleanup.md` + **`delight_aggressive.md`** + `detail_preservation.md` | Hi3D 1536 Pro > Rodin |
| **Nero lucido / monocromatico scuro** | caso limite: riflessi enormi + ombre = unica informazione geometrica. Delight standard appiattisce tutto → blob. | **Strategia: DELIGHT TO MATTE [stesso colore]** — chiedere a Gemini di rimuovere il finish glossy/metallico mantenendo il colore base originale (es. nero lacca → nero matte; blu metallico → blu matte opaco). ⚠️ NON convertire a bisque/grigio — i colori vanno sempre preservati (segnale geometrico per i tool 3D + riferimento per FDM multicolore). Preservare le ombre di forma (depth-cue shadows). | Hi3D 2.1 > Rodin (volti) |
| **Misto / multimedia** | dipende dalla parte dominante | trattare come elemento dominante | tool del finish dominante |

> ⚠️ **Domanda da fare sempre prima di scegliere il prompt**: *"è una ceramica finita o un prototipo in gesso?"* Cambiano completamente le sfide (riflessi vs bolle/seam).

---

## Domanda 5 — Volti scolpiti?

> Il soggetto include **un volto** stilizzato (testa di moro, busti, putti)?

- **Sì** → **NON usare Hunyuan 3.1**. Ha tendenza documentata a deformare volti.
- **Sì** → preferire nell'ordine: **Rodin Gen 2** (top per volti scolpiti) > **Hi3D Portrait mode** (modello dedicato a 1536) > **Tripo 3.1 HD**
- **No** → tutti e 5 gli engine sono in gioco, decidi su altre dimensioni

---

## Albero decisionale combinato

```
START
  │
  ├─ Volti scolpiti presenti?
  │     ├─ SÌ → escludi Hunyuan
  │     │       ├─ Densità dettagli ALTISSIMA?
  │     │       │     ├─ SÌ → Hi3D 1536 Pro Portrait (o Rodin high)
  │     │       │     └─ NO → Rodin Gen 2 medium (o Tripo 3.1 HD)
  │     │       └─ ...
  │     └─ NO →
  │           ├─ Densità dettagli ALTISSIMA?
  │           │     ├─ SÌ → Hi3D 1536 Pro o Rodin high
  │           │     └─ NO →
  │           │           ├─ Forma assialmente simmetrica + dettagli medi?
  │           │           │     ├─ SÌ → Hunyuan 3.1 Pro (multi-view)
  │           │           │     └─ NO → Tripo 3.1 HD
  │           │           └─ Forma semplice + bassa densità?
  │           │                 ├─ SÌ → Hunyuan 3.1 Rapid o Meshy 6
  │           │                 └─ ...
  │
  └─ Sempre, in parallelo, scegli il prompt Gemini in base al finish del soggetto
```

---

## Tabella di sintesi (priorità per dominio "prodotti decorativi artigianali")

Tempi confermati da MakerWorld UI (maggio 2026):

| Tool | Tempo MakerWorld | Quando è la scelta migliore | Quando evitarlo |
|------|------------------|-----------------------------|-----------------|
| **Tripo 3.1** | **~2.5 min** | Default robusto, buon equilibrio, scelta sicura per iterare | Mai escludere a priori |
| **Hunyuan 3.1** | **~3 min** | Forme assialmente simmetriche pulite, no volti, watertight | Volti, micro-rilievi fitti |
| **Rodin Gen 2** | **~3 min** | Volti scolpiti + ornamenti densi + qualità top | Quando serve iterare velocemente |
| **Meshy 6** | **~4 min** | Sculpting-level modeling (rivisto dalla descrizione MakerWorld) | Smoothing ancora una variabile — verificare |
| **Hi3D 2.1** | **~7 min** | Densità dettagli altissima + ceramica smaltata (Delight slider) | Quando servono iterazioni rapide (7 min = lento per test) |

> **Strategia iterazione confermata empiricamente (2026-05-08)**: su soggetti complessi, i tool veloci (Tripo 2.5 min, Rodin 3 min) non recuperano il gap con Hi3D 7 min neanche sul risultato finale. **Su soggetti non banali, usare direttamente Hi3D 2.1.** Il risparmio di 4-5 minuti non vale il rischio di risultati inutilizzabili.

> **Usa Tripo 3.1 per test rapidi SOLO su soggetti semplici** (forme con parete visibile, geometria non occlusa, decorazione parziale). Su soggetti complessi parti direttamente da Hi3D.

---

---

## ⚠️ Domanda 0 — Il soggetto ha un'apertura/cavità visibile?

> Il soggetto è un **contenitore aperto in cima** (vaso, ciotola, portafrutta, alzatina)?

Questa domanda va posta **prima di tutte le altre** perché cambia radicalmente la strategia dell'immagine Gemini.

**Se SÌ** (apertura visibile nella foto):

I tool image-to-3D — quando vedono un'apertura in una vista 3/4 dall'alto — interpretano il soggetto come *"una massa di elementi decorativi"* invece di *"un contenitore con decoro esterno"*. Risultato tipico: mesh informe, fondo bucato, struttura del contenitore assente. **Confermato empiricamente su vaso limoni (2026-05-08).**

**Soluzione obbligatoria — Angolazione Gemini laterale bassa**:
- Usare solo le foto scattate **quasi a livello del piano** (angolazione < 10° sopra il bordo)
- L'apertura non deve essere visibile: il bordo superiore deve apparire come un profilo, non come un'imboccatura
- NON includere la vista dall'alto nel set multi-foto se il soggetto ha un'apertura
- Istruzione da aggiungere al prompt Gemini: *"Render the subject from a near-ground lateral angle. The top rim must appear as a clean edge/silhouette — DO NOT show the interior cavity. The vessel must read as a solid sculptural object."*

**Quale tool scegliere per soggetti cavi**:
- **Hi3D 2.1** (7 min) — confermato empiricamente il migliore su questo tipo di soggetto
- **Meshy 6** — fondo chiuso, fronte accettabile, retro problematico
- **Evitare Tripo e Rodin** su contenitori con decoro fitto che copre tutta la parete
- L'apertura e il fondo andranno **sempre sistemati in Blender** dopo la generazione

**⚠️ Caso "oggetto strutturalmente occluso"**: se il decoro copre il 100% della parete e la forma del contenitore è completamente nascosta, **nessun tool produce un risultato accettabile in autonomia**. Il blob generato va usato come punto di partenza per un rework Blender manuale. Valutare se il soggetto è adatto a questa pipeline o se è meglio cercare un modello di riferimento online.

---

---

## ⚠️ Domanda 6 — Quanti colori FDM sono disponibili?

> La stampa è **multicolore** con AMS? Quanti filamenti hai disponibili?

**Bambu A1 con AMS standard = max 4 colori.**

Questa domanda è rilevante SOLO per stampe multicolore. Se la stampa è mono-colore, il colore nell'immagine Gemini è irrilevante per la stampa finale (ma rimane utile per il tool 3D come segnale di separazione geometrica).

**Se il soggetto ha più di N colori (sfumature, patine variegate, blend pittorici)**:
→ Aggiungere il block `color_simplification.md` al prompt Gemini.

**Obiettivo**: compattare ogni zona cromatica a un colore piatto uniforme (N colori max), con confini netti tra zone.

**Regola pratica**:
1. Conta i "colori sostanziali" dell'oggetto — quante zone cromaticamente distinte vedi se guardi da lontano?
2. Se > N → unifica i colori simili (es. "verde chiaro + verde scuro" → "dark green"; "arancio + rosso + giallo" → "orange-red")
3. Includi il block nel prompt Gemini con la lista delle N zone colorate

**Perché farlo in Gemini e non in post**:
- Il tool image-to-3D usa il colore come segnale di separazione geometrica — bordi netti = mesh più definita
- Bambu Studio: la selezione manuale delle zone di colore per assegnarle ai filamenti richiede bordi netti nell'immagine di riferimento
- Se le sfumature rimangono nell'immagine Gemini, rimangono (peggiorate) nel mesh e diventano impossibili da selezionare

---

## ⚠️ Domande edge case (D7-D15) — strategie per soggetti difficili

Queste domande si applicano **solo** se il soggetto rientra in una di queste categorie. Per soggetti standard (ceramica/gesso/terracotta opaca), proseguire con Domande 0-6.

### D7 — Soggetto trasparente o specchiante?

> Il soggetto è in **vetro, cristallo, ceramica iper-lucida, metallo cromato/specchio**?

| Strategia | Quando |
|---|---|
| **Spray opacizzante AESUB Blue** + photogrammetry | Hai l'oggetto fisicamente, accetti di spruzzarlo (rimovibile) |
| **Cross-polarization rig** (2 filtri polarizzatori) | Hai banco fotografico setup-able |
| **Gemini → opacizza in foto** (`gemini_prompts/transparency_reflective.md`) | Non hai accesso fisico, accetti perdita info geometrica |
| **Cerca asset esistente** (Sketchfab, Smithsonian 3D) | Soggetto comune (bicchiere, bottiglia standard) |

**Limite duro**: senza opacizzazione fisica o cross-pol, single-image AI **non funziona** su vetro/specchio. Tutti gli engine vedono solo riflessi.

### D8 — Soggetto peloso, fibroso, tessuto?

> Il soggetto ha **pelo, capelli sciolti, tessuto frangiato, fiori secchi, paglia, fili**?

| Strategia | Quando |
|---|---|
| **Stilizza in foto** → continuous bumpy surface | FDM non stampa strand individuali < 0.4mm |
| **DiffLocks** (workflow specializzato) | Capelli/pelo critici per ritratti |
| **Modella separato in Blender** + glue | Capelli/fili sono elemento accessorio |

**Limite duro**: FDM (qualunque nozzle) non stampa singoli filamenti < 0.4mm di larghezza. Devi stilizzare a superficie continua.

### D9 — Soggetto articolato, multi-parte, assemblato?

> Il soggetto è **composto da più pezzi distinti** (robot articolato, statua + base separata, oggetto con tappo)?

| Strategia | Quando |
|---|---|
| **PartCrafter** (sperimentale, image-to-3D con part segmentation) | Hai accesso al tool, accetti instabilità |
| **Foto-per-parte** → genera mesh separate → assembla in Blender | Soluzione robusta, più tempo |
| **Boolean cut Blender** post-mesh blob | Single-shot accettabile come baseline |

**Limite duro**: nessun engine single-image-to-3D 2026 gestisce nativamente part separation. Mesh blob è ineludibile single-shot.

### D10 — Liquido contenuto?

> C'è **liquido visibile dentro una bottiglia/calice/vaso**?

| Strategia | Quando |
|---|---|
| **Svuota fisicamente** prima della foto | Hai accesso all'oggetto |
| **Gemini mask** → cancella liquido in foto | No accesso fisico, contenitore opaco |
| **Modella liquido separato** in Blender se serve | Multi-color FDM, vuoi separazione AMS |

**Trappola tipica**: AI confonde "liquido + contenitore" → genera mesh unica con discontinuità nel punto di interfaccia.

### D11 — Testo o lettering scolpito < 2mm?

> Il soggetto ha **testo inciso, numeri, lettering scolpito** con tratto < 2mm di larghezza?

| Strategia | Quando |
|---|---|
| **Genera mesh** + **ricostruisci testo in Blender** (Text object + Boolean union) | Sempre raccomandato — testo AI è inaffidabile |
| **Hi3D 2.1 Pro 1536³** con Delight 0.3 (testo conserva ombre = depth) | Testo > 3mm, vuoi single-shot |

**Limite duro FDM A1**: tratto < 0.8mm di larghezza diventa invisibile (1 perimeter line). Pianificare testo come boolean ricostruito.

### D12 — Sottosquadri estremi (gabbia, intreccio chiuso)?

> Il soggetto ha **cavità con accesso stretto** o **strutture intrecciate chiuse** (gabbia, pizzo 3D, intrecci tridimensionali)?

| Strategia | Quando |
|---|---|
| **Split & glue** (taglia in Blender, stampa pezzi, incolla) | Asset > 50mm con sottosquadri profondi |
| **Vase mode hollow** | Soggetto è contenitore, vuoi parete singola |
| **Resina invece di FDM** | Sottosquadri così stretti che FDM non gestisce |

**Limite duro FDM**: gabbie con celle < 10mm e intrecci con loop chiusi sono **impossibili** in FDM senza supporti interni che poi non rimuovi.

### D13 — Dimensioni estreme (> 256mm o < 10mm)?

> Il soggetto reale è **più grande del piatto A1 (256×256×256mm)** o **microscale (< 10mm)**?

| Strategia | Quando |
|---|---|
| **Split orizzontale Blender** + dovetail/pin alignment | > 256mm, mantenere proporzione 1:1 |
| **Upscale 2-3x** | < 10mm, dettagli illeggibili |
| **Stampa modulare** (N pezzi assemblabili) | > 400mm, design-friendly |
| **Resina SLA** | < 10mm con dettaglio fine |

### D14 — Antico, danneggiato, frammento archeologico?

> Il soggetto è **rotto, parzialmente mancante, riconosciuto come reperto storico**?

| Strategia | Quando |
|---|---|
| **Mirror simmetrico** (se la parte mancante ha gemello simmetrico) | Soggetto simmetrico, < 50% mancante |
| **AI inpaint** (`gemini_prompts/archaeological_restoration.md`) | Vuoi "ricostruzione speculativa" |
| **Mantieni frammento** as-is | Vuoi onestà filologica, niente speculazione |
| **ORGAN GAN / SD 3D condizionato** | Hai modello AI specializzato disponibile |

**Limite ethico**: > 50% mancante = ricostruzione speculativa, dichiararlo. ⚠️ **Diritti museali italiani** (soprintendenza) per ceramiche storiche.

### D15 — Solo video disponibile, no foto statiche?

> Hai **solo un video** del soggetto (smartphone, drone), niente foto?

| Strategia | Quando |
|---|---|
| **Nerfstudio + splatfacto** → 3DGS → Poisson mesh | Video stabile, setup CUDA disponibile |
| **Keyframe manuale** (estrai 4-8 frame migliori) | Video shaky, fallback |
| **KIRI Engine** (mobile) | Video iPhone LiDAR, mobile-only |
| **Luma AI** (3DGS da video) | Video smartphone, no export FDM diretto |

**Limite duro**: video shaky/con motion blur → tutti i workflow falliscono. Stabilizzare prima.

---

## Quando consultare di nuovo questo file

- **Prima di ogni soggetto**: fai sempre Domanda 0 (apertura?) e Domanda 4 (materiale: gesso o ceramica?) e Domanda 6 (quanti colori FDM?)
- **Soggetti non standard**: verifica D7-D15 prima di scegliere il tool
- Dopo un fallimento: salta al tool di rango successivo nella stessa "fascia di densità"
- Quando aggiungiamo esempi reali in `examples/`, aggiorniamo le risposte con dati empirici
