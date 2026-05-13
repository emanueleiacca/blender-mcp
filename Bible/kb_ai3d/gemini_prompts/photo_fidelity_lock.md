# Block: Photo Fidelity Lock

**Da aggiungere SEMPRE come prima sezione** di qualsiasi prompt Gemini, prima di qualsiasi altra istruzione. Previene il rischio di allucinazione — Gemini che genera una versione "ideale" dell'oggetto invece di elaborare la foto reale.

## Perché esiste questo block

Gemini è addestrato sia su editing fotografico che su generazione di immagini. Quando il prompt descrive l'oggetto in modo dettagliato o accumula molte trasformazioni, Gemini può scegliere il percorso più "facile": generare ex-novo un'immagine che corrisponde alla descrizione invece di elaborare la foto sorgente. Il risultato può sembrare corretto ma tradisce le proporzioni, i dettagli, e la forma reale dell'oggetto originale.

**Confermato empiricamente**: vaso limoni, tentativo 2 (2026-05-08) — Gemini ha prodotto un render 3D idealizzato invece di elaborare le foto del gesso.

## Block (inserire COME PRIMA SEZIONE del prompt, prima di tutto)

```
=== CRITICAL: PHOTO EDITING TASK — NOT IMAGE GENERATION ===
This is a PHOTO EDITING and CLEANUP task, NOT an image generation task.

Your ONLY source of truth is the attached source photo(s).
You MUST NOT:
- Reconstruct, reimagine, or reinterpret the subject
- Generate a new image that "matches the description"
- Normalize, regularize, or idealize the subject's form
- Add elements not visible in the source photo(s)
- Change the proportions, silhouette, or arrangement of elements
- Make the object "better looking" or more symmetrical than it is

You MUST:
- Work directly from the pixel content of the source photo(s)
- Preserve the EXACT proportions and aspect ratio of the subject
- Preserve the EXACT arrangement and relative sizes of all elements
- Preserve irregularities, asymmetries, and imperfections that are
  part of the original design (not manufacturing defects)
- Treat the source photo(s) as the ground truth for what exists

PROPORTION LOCK: the width-to-height ratio of the subject must match
the source photo within ±5%. If the source shows a squat wide vessel,
the output must also be squat and wide. Do not elongate or compress.

ARRANGEMENT LOCK: if elements appear in certain positions, sizes, or
quantities in the source, preserve them exactly. Do not regularize
irregular arrangements into uniform grids.

ONLY the following may differ from the source:
- Background (replace with pure white)
- Surface finish (remove specular highlights if instructed)
- Manufacturing defects (remove if instructed)
- Camera perspective distortion (correct if instructed)
```

## Quando è particolarmente critico

- Soggetti che Gemini "conosce" da training data (vasi con limoni, pigne, maioliche tipiche) → alto rischio di generate-instead-of-edit
- Prompt con molte istruzioni di trasformazione accumulate → più trasformazioni = più libertà creativa
- Sintesi multi-foto → dare a Gemini più foto è dare più libertà

## Posizione nel prompt assembla

```
[PHOTO FIDELITY LOCK]      ← sempre primo
[TASK description]
[FRAMING]
[BACKGROUND]
[casting_defects oppure delight_aggressive]
[detail_preservation]
[perspective_correction]
[OUTPUT]
```

## Segnale d'allarme nell'output

Se l'output Gemini sembra un "bel render 3D" invece di una "foto elaborata", è quasi certamente un'allucinazione. Segnali:
- Superficie troppo uniforme e pulita
- Elementi troppo simmetrici e regolari
- Proporzioni diverse dall'originale
- Elementi aggiunti (basi, piedistalli, dettagli non presenti)
- Stile "CGI" invece di fotografico
