# Prompt Gemini — guida d'uso

Cartella di template di prompt da copiare-incollare nell'app Gemini (o AI Studio) per pre-processare foto del soggetto **prima** di darle al tool 3D.

## File

| File | Quando usarlo |
|------|---------------|
| **`photo_fidelity_lock.md`** | **⚠️ Sempre — inserire come prima sezione in qualsiasi prompt. Previene allucinazione Gemini.** |
| `master_template.md` | Il template di base, parametrizzato. Tutti gli altri sono sue specializzazioni |
| `single_photo_cleanup.md` | Hai 1 sola foto, va pulita: scontorno + delight + raddrizzamento prospettiva |
| `multi_photo_canonical.md` | Hai 2-4 foto da angolazioni diverse, vuoi fonderle in 1 vista canonica 3/4 |
| `casting_defects.md` | Block aggiuntivo: soggetto in gesso — rimuove bolle, linee stampo, macchie |
| `delight_aggressive.md` | Block aggiuntivo: per ceramica smaltata, metallo lucido — riflessi forti da rimuovere |
| `detail_preservation.md` | Block aggiuntivo: per soggetti con micro-rilievi (intrecci, squame, foglie) — evita lo smoothing |
| `perspective_correction.md` | Block aggiuntivo: per foto scattate troppo vicine o con grandangolo — raddrizza la deformazione |
| **`color_simplification.md`** | **Block aggiuntivo: soggetto multicolore + stampa FDM con AMS (max 4 colori). Unifica le zone cromatiche a colori piatti con bordi netti.** |

## Come si compongono

I prompt sono **modulari**. Il template master è la spina dorsale; i block specializzati (`delight_aggressive`, `detail_preservation`, `perspective_correction`) si **aggiungono** al master in base alle sfide del soggetto specifico.

Quando ti chiedo di pre-processare una foto, ti darò già il prompt completo composto. Questo file ti serve solo se vuoi capire la logica o costruirti varianti.

## Gemini app vs AI Studio

| Piattaforma | Vantaggi | Svantaggi |
|-------------|----------|-----------|
| **App Gemini** | Veloce, mobile, "just works" | Rate limit, prompt non riproducibili, no parametri avanzati |
| **AI Studio** ([aistudio.google.com](https://aistudio.google.com)) | Stesso modello (Gemini 2.5 Flash Image), gratis, prompt riproducibili, no rate limit utili, controllo temperatura | Solo desktop, UI un filo più tecnica |

**Raccomandazione**: parti con app Gemini per i primi test. Quando avrai trovato i prompt che funzionano e vorrai ripeterli identici per nuovi soggetti, passa ad AI Studio.

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
3. **Proporzioni sbagliate**: aggiungi "PROPORTION LOCK" esplicito (vedi `photo_fidelity_lock.md`)
4. **Sfondo non pulito**: separa in due passaggi — prima solo scontorno, poi tutto il resto
5. **Torna da me con l'output**: ridiscutiamo prompt o cambiamo strategia
