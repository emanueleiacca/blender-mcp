# Decision Tree — quale tool 3D per quale foto

Logica per scegliere tra i 5 engine MakerLab in base alle caratteristiche del soggetto fotografato. Ottimizzato per il dominio "prodotti decorativi artigianali" stampati FDM mono-colore su Bambu A1.

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

## Quando consultare di nuovo questo file

- **Prima di ogni soggetto**: fai sempre Domanda 0 (apertura?) e Domanda 4 (materiale: gesso o ceramica?) e Domanda 6 (quanti colori FDM?)
- Dopo un fallimento: salta al tool di rango successivo nella stessa "fascia di densità"
- Quando aggiungiamo esempi reali in `examples/`, aggiorniamo le risposte con dati empirici
