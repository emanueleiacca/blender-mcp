# Block: Archaeological Restoration (frammento, oggetto danneggiato)

## Quando usarlo

Soggetto **rotto, parzialmente mancante, riconosciuto come reperto storico**:
- Ceramica antica con manici rotti
- Statue archeologiche con arti mancanti
- Frammenti di affresco
- Vasi etruschi / greci con porzioni ricostruite

## ⚠️ Considerazioni etiche e legali

- **Limite etico**: > 50% mancante = ricostruzione speculativa, dichiararlo esplicitamente
- **Diritti italiani**: ceramiche storiche e reperti archeologici sono soggetti a tutela soprintendenza (Codice dei Beni Culturali D.Lgs 42/2004). Prima di vendere stampe → verificare licenze
- **Onestà filologica**: alcune comunità preferiscono mantenere il "frammento" come testimonianza piuttosto che ricostruzione

## Strategie alternative

### Strategia A — Mirror simmetrico (se applicabile)

Se l'oggetto è **simmetrico** e la parte mancante ha un gemello sull'altro lato:
1. Genera il mesh as-is (con la metà danneggiata)
2. In Blender: bisect lungo asse di simmetria → elimina lato danneggiato → mirror
3. Risultato: oggetto completo, ricostruzione basata sulla parte intatta

### Strategia B — Mantieni frammento (raccomandata per onestà)

Genera il mesh as-is. Stampa il frammento come testimonianza. Niente speculazione.

### Strategia C — AI inpaint (speculativa, dichiararlo)

Usa il block sotto per chiedere a Gemini di "ricostruire" digitalmente le parti mancanti **prima** del image-to-3D.

⚠️ **Avvertenza**: la ricostruzione AI è **speculativa**. Marca SEMPRE l'output come "speculative reconstruction" se vendi/condividi.

## Block (Strategy C — AI inpaint)

```
=== ARCHAEOLOGICAL RECONSTRUCTION (SPECULATIVE) ===

The source subject is a damaged/fragmentary historical object.
This reconstruction is SPECULATIVE and should be marked as such.

RECONSTRUCTION RULES
- Missing portions MUST be inferred from:
  1. Symmetry (if intact half is visible)
  2. Typological knowledge of similar artifacts
  3. Visible stylistic patterns from intact portions
- Inferred portions MUST be visually consistent with intact portions
  (same material, same style, same scale)

VISUAL MARKER FOR SPECULATIVE PARTS
- Inferred portions MUST be rendered in a slightly DIFFERENT tone
  (e.g., 5-10% lighter) so they remain distinguishable
- This visual marker will be removed before final 3D generation

CONFIDENCE LEVELS
- High confidence: clearly symmetric missing piece → reconstruct
- Medium confidence: typological inference → reconstruct with marker
- Low confidence: no basis → leave fragmentary
```

## Strategia D — Tool specializzati

- **ORGAN GAN**: per ricostruzione organi/parti anatomiche di sculture antropomorfe
- **Stable Diffusion + ControlNet (depth-conditioned)**: per ricostruzione "in stile" pittorico
- **Sketchfab Cultural Heritage**: cercare se esiste già un modello del manufatto restaurato (Smithsonian 3D Open Access ha molti reperti)

## Quando NON usarlo

- Oggetto intatto → workflow standard
- Frammento dove > 50% manca → preferire "Mantieni frammento" o cercare asset esistente
- Soggetto soggetto a tutela museale → consultare professionalmente prima di proseguire

## Origine

Deepsearch 2026-05-13 § D14. Cross-reference: Smithsonian 3D Open Access, Codice Beni Culturali IT.
