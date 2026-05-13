# Prompt Gemini — guida d'uso

Cartella di template di prompt da copiare-incollare nell'app Gemini (o AI Studio) per pre-processare foto del soggetto **prima** di darle al tool 3D.

## File

| File | Quando usarlo |
|------|---------------|
| **`photo_fidelity_lock.md`** | **⚠️ Sempre — inserire come prima sezione in qualsiasi prompt. Previene allucinazione Gemini.** |
| `master_template.md` | Il template di base, parametrizzato (riformulato 2026-05-13 con affirmative framing) |
| `single_photo_cleanup.md` | Hai 1 sola foto, va pulita: scontorno + delight + raddrizzamento prospettiva |
| `multi_photo_canonical.md` | Hai 2-4 foto da angolazioni diverse, vuoi fonderle in 1 vista canonica 3/4 |
| **`proportion_anchor_block.md`** | **Safety net per drift proporzioni Gemini (raccomandato sempre)** |
| `casting_defects.md` | Block aggiuntivo: soggetto in gesso — rimuove bolle, linee stampo, macchie |
| `delight_aggressive.md` | Block aggiuntivo: per ceramica smaltata, metallo lucido — riflessi forti da rimuovere |
| `detail_preservation.md` | Block aggiuntivo: per soggetti con micro-rilievi (intrecci, squame, foglie) — evita lo smoothing |
| `perspective_correction.md` | Block aggiuntivo: per foto scattate troppo vicine o con grandangolo — raddrizza la deformazione |
| **`color_simplification.md`** | **Block aggiuntivo: soggetto multicolore + stampa FDM con AMS (max 4 colori). Unifica le zone cromatiche a colori piatti con bordi netti.** |
| `transparency_reflective.md` | Edge case D7: vetro/cromo/specchio |
| `fibrous_subject.md` | Edge case D8: pelo/tessuto/paglia |
| `articulated_multipart.md` | Edge case D9: multi-pezzo articolato |
| `severe_undercuts.md` | Edge case D12: sottosquadri estremi |
| `engraved_text_lt_2mm.md` | Edge case D11: testo scolpito < 2mm |
| `archaeological_restoration.md` | Edge case D14: frammenti danneggiati |
| `video_only_input.md` | Edge case D15: solo video disponibile |

## Come si compongono

I prompt sono **modulari**. Il template master è la spina dorsale; i block specializzati (`delight_aggressive`, `detail_preservation`, `perspective_correction`) si **aggiungono** al master in base alle sfide del soggetto specifico.

Quando ti chiedo di pre-processare una foto, ti darò già il prompt completo composto. Questo file ti serve solo se vuoi capire la logica o costruirti varianti.

## Gemini app vs AI Studio

| Piattaforma | Vantaggi | Svantaggi |
|-------------|----------|-----------|
| **App Gemini** | Veloce, mobile, "just works" | Rate limit, prompt non riproducibili, no parametri avanzati |
| **AI Studio** ([aistudio.google.com](https://aistudio.google.com)) | Stesso modello (Gemini 2.5 Flash Image), gratis, prompt riproducibili, no rate limit utili, controllo temperatura | Solo desktop, UI un filo più tecnica |

**Raccomandazione**: parti con app Gemini per i primi test. Quando avrai trovato i prompt che funzionano e vorrai ripeterli identici per nuovi soggetti, passa ad AI Studio.

## ⚠️ Choosing Gemini version (2026)

Aggiornamento 2026: Google ha pubblicato due modelli specifici per image editing. La scelta del modello impatta significativamente la fedeltà.

| Model | Quando usarlo | Costo orientativo |
|---|---|---|
| **Gemini 2.5 Flash Image** ("Nano Banana") | Default per cleanup/delight/BG removal. Veloce ed economico | ~$0.04/img |
| **Gemini 3 Pro Image** ("Nano Banana Pro") | Multi-image fusion (fino a 14 foto, 5 reference ID), engraved text, 4K, canonical view critica per input image-to-3D | ~$0.40/img |
| **Gemini 1.5** | **DEPRECATO** per image editing — non usare | n/a |

**Workflow raccomandato**:
1. **Default**: Gemini 2.5 Flash per la maggior parte dei cleanup
2. **Escalate** a Gemini 3 Pro se:
   - Stai fondendo > 2 foto in canonical view
   - Il soggetto ha testo scolpito da preservare
   - L'output sarà input a Hi3D 1536³ Pro (max fedeltà richiesta)
   - Hai già tentato 2 volte con 2.5 Flash senza successo

**Cap multi-foto**: oltre 3 foto Gemini 2.5 Flash drifta sulla fusione (perde fedeltà). Per multi-photo canonical → preferisci Gemini 3 Pro o limita a 3 foto.

## ⚠️ Iteration protocol — single-variable change

Best practice Google 2025-2026 (confermata empiricamente):

### Regola: 1 cambio per re-prompt

**❌ Pattern obsoleto** (stacking di correzioni):
```
"Apply delight pass AND fix proportions AND remove background AND
 correct perspective AND increase detail AND..."
```
Risultato: Gemini ne applica solo alcune o le applica male.

**✅ Pattern corretto** (single-variable iteration):
1. Prompt 1: solo background removal → output A
2. Prompt 2: re-upload output A + "apply delight pass" → output B
3. Prompt 3: re-upload output B + "correct perspective" → output C
4. Etc.

### Regola: re-upload last good image

Per fix incrementali: ri-upload l'ultima immagine "buona" come **nuova source**, NON ricominciare da zero. Questo:
- Preserva identity / silhouette / proporzioni
- Permette a Gemini di applicare 1 modifica chirurgica
- Evita la regressione di trasformazioni precedenti

### Regola: aspect ratio anchor verbatim

Sempre includere `"Do not change the input aspect ratio."` come frase a sé stante (è la formulazione **verbatim** dei Google AI docs).

### Regola: affirmative framing (no MUST NOT stacking)

Gemini 2.5/3 e Imagen 3+ **non interpretano** correttamente lo stacking di "MUST NOT". Convertire sempre:

| ❌ Pattern obsoleto | ✅ Pattern corretto |
|---|---|
| "Do not include hands" | "The frame MUST be empty of: hands" |
| "Do not stylize" | "Style MUST remain photographic" |
| "No cast shadows" | "The background MUST be empty of cast shadows" |
| "Don't change proportions" | "Proportions MUST match source within ±5%" |

Vedi `master_template.md` per il template aggiornato.

### Quando uscire dal loop

Se dopo **3 iterazioni single-variable** l'output non converge:
1. Torna alla foto sorgente (è il problema di partenza)
2. Cambia strategia (es. multi-foto canonical → single-photo)
3. Considera tool alternativo (BiRefNet per BG removal, ChatGPT 4o per cleanup)
4. Torna da me — ridiscutiamo prompt/tool

## Lingua dei prompt

I prompt sono in **inglese** anche se la tua interfaccia è in italiano. Gemini 2.5 Flash Image segue meglio le istruzioni tecniche in inglese, e il rischio di traduzioni "creative" su termini come "delight pass" o "orthographic projection" è zero.

## ⚠️ Regola #1 — Meno processing = migliori risultati 3D

**Confermato empiricamente (vaso limoni, 2026-05-08)**:

I tool image-to-3D inferiscono la profondità e la forma tridimensionale principalmente dalle **ombre e dai gradienti di luce** nella foto sorgente. Un delight aggressivo, una illuminazione completamente piatta, o una sintesi multi-foto "troppo pulita" **rimuovono esattamente le informazioni geometriche** di cui il tool ha bisogno.

**Risultato**: la foto "più semplice" (sfondo bianco, matte moderato, proporzioni fedeli, minima manipolazione) ha prodotto il miglior risultato 3D di tutta la sessione — meglio delle versioni con delight aggressivo, multi-foto canonical, e correzioni elaborate.

**Gerarchia di processing consigliata** (dal meno al più aggressivo):
1. **Minimo** (default per soggetti non smaltati/opachi): solo sfondo bianco + eventuale crop. Niente delight, niente forte correzione prospettiva.
2. **Moderato** (default per ceramica smaltata): sfondo bianco + delight leggero (riduce highlights estremi ma non appiattisce tutto). Non azzerare le ombre dell'oggetto.
3. **Aggressivo** (solo se strettamente necessario per riflessi che distorcono la geometria): delight completo. Rischio: il tool 3D perde le informazioni di profondità.

**Regola pratica**: il delight serve per ceramiche smaltate dove i riflessi *falsificano* la geometria. Ma deve essere il minimo necessario, non il massimo possibile.

## ⚠️ Rischio allucinazione — regola fondamentale

**Confermato empiricamente (vaso limoni, tentativo 2, 2026-05-08)**:

Quando il prompt:
1. Descrive in dettaglio **cosa deve esserci** nell'immagine (forma, elementi, layout)
2. Somma troppe trasformazioni pesanti in un colpo solo (prospettiva + material cleanup + sintesi multi-foto + angolazione)
3. Il soggetto corrisponde a qualcosa che Gemini conosce bene dai training data

...Gemini abbandona le foto sorgenti e **genera una versione idealizzata** dell'oggetto descritto. Il risultato sembra corretto ma non corrisponde all'originale (proporzioni diverse, elementi inventati, base aggiunta, elementi "normalizzati").

**Regola**: il prompt deve descrivere solo **cosa rimuovere/correggere**, non cosa deve esserci. Le foto sono la fonte di verità, non la descrizione testuale.

**Anti-pattern da evitare**:
```
❌ "The vessel has TWO ROWS of lemons, a TWISTED ROPE BORDER, 
    LEAVES near the top, a SQUARE cross-section..."
```
**Pattern corretto**:
```
✅ "Process the source photo(s) faithfully. Do not reconstruct 
    or reimagine. Only remove: background, casting defects, 
    specular highlights."
```

**Regola sul numero di foto**: la sintesi multi-foto dà a Gemini più libertà creativa. Quando la fedeltà all'originale è critica, **preferire single-photo** come ancora. Se si usano più foto, mettere la foto principale per prima e dichiarare esplicitamente che è la fonte di verità.

## Quando un prompt non funziona

Se l'output Gemini è insoddisfacente dopo 2 tentativi:

1. **Allucinazione** (output bello ma non corrisponde all'originale): semplifica il prompt drasticamente, passa a single-photo, togli tutte le descrizioni di cosa deve esserci
2. **Difetti non rimossi** (bolle, riflessi ancora visibili): rinforza le istruzioni di rimozione, aggiungi esempi specifici
3. **Proporzioni sbagliate**: aggiungi `proportion_anchor_block.md` esplicito (vedi anche `photo_fidelity_lock.md`)
4. **Sfondo non pulito**: separa in due passaggi — prima solo scontorno (preferisci **BiRefNet RMBG-2.0** se hai accesso, IoU 0.87/Dice 0.92), poi tutto il resto con Gemini
5. **Torna da me con l'output**: ridiscutiamo prompt o cambiamo strategia

## ⚠️ Alternative AI cleanup tools (oltre Gemini)

Quando Gemini non basta, considerare:

| Tool | Use case | Note |
|---|---|---|
| **BiRefNet (RMBG-2.0)** | TOP per silhouette/background removal — IoU 0.87/Dice 0.92 | Pre-pass BEFORE Gemini |
| **rembg (ISNet/U2Net)** | Local Python alternative | Backup BiRefNet, meno preciso |
| **ChatGPT 4o / GPT-4.1 Image** | Image editing alternativo | Più debole su fidelity lock vs Gemini |
| **Stable Diffusion + ControlNet (Canny/Depth)** | Silhouette preservation guarantee | "Hero" job Patreon/MyMiniFactory |
| **Adobe Firefly / Photoshop AI** | Fine-pass cleanup post-Gemini | Commercially safe |

**Workflow professionale (Patreon-level)**:
1. BiRefNet → clean alpha PNG
2. Gemini 2.5 Flash → delight + perspective
3. Gemini 3 Pro → canonical view multi-photo (se serve)
4. Photoshop manual fine-pass (opzionale)
5. → image-to-3D (Hi3D 2.1 raccomandato)
6. Blender/ZBrush mesh cleanup
