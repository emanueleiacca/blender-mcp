# Block: Color Simplification — Max N Colori FDM

**Da aggiungere** quando il soggetto ha più colori e la stampa è su **stampante FDM con AMS** (max 4 colori per Bambu A1 con AMS standard).

## Perché serve

Le sfumature pittoriche (blending, gradients, wash multicolore, patine variegatissime) non sono riproducibili in FDM filament-by-filament. Ogni colore corrisponde a un filamento separato. Un'immagine con sfumature graduali crea due problemi:

1. **Tool image-to-3D**: usa il colore come segnale di separazione geometrica degli elementi. Sfumature ambigue → confini geometrici incerti nella mesh.
2. **Bambu Studio**: la separazione manuale delle zone di colore (per assegnarle ai filamenti) diventa impossibile se le zone non hanno confini netti.

**L'obiettivo**: ogni zona cromatica dell'oggetto deve essere un colore piatto uniforme, con confini netti tra zone. Come se l'oggetto fosse dipinto con N barattoli di tempera piatta, senza sfumature.

## Block (aggiungi prima della sezione OUTPUT)

```
=== FDM COLOR SIMPLIFICATION — MAX [N] COLORS ===
This object will be printed on an FDM printer with a maximum of [N] color
filaments. Simplify ALL color information accordingly:

PRIMARY COLORS for this subject:
  - Zone 1: [DESCRIZIONE ZONA] → render as uniform flat [COLORE]
  - Zone 2: [DESCRIZIONE ZONA] → render as uniform flat [COLORE]
  - Zone 3: [DESCRIZIONE ZONA] → render as uniform flat [COLORE]
  (add/remove zones up to N total)

RULES:
- ELIMINATE all color gradients, blending, and tonal variation within
  each zone — each zone must be a SOLID, FLAT color
- WHERE two zones meet, create a SHARP, CLEAN edge/boundary
  (no feathering, no blending, no transition gradients between zones)
- Any color not in the PRIMARY COLORS list must be ABSORBED into the
  nearest matching zone color
- Gold speckles, silver highlights, patina variations, paint brush
  strokes → absorb into the dominant color of the zone they appear on
- The goal: if you posterize the output image to [N] colors, you should
  see the same clean zoning as listed above
- IMPORTANT: do NOT change the geometric structure or 3D form of any
  element to achieve color uniformity — only the painted surface
  color treatment changes
- IMPORTANT: do NOT remove the depth-cue shading gradients (light/shadow
  that defines 3D curvature). Color simplification applies to PIGMENT
  variations only, not to light/shadow — those must be preserved for
  3D reconstruction.
```

## Come compilare i campi

1. **[N]**: numero massimo di colori AMS. Bambu A1 standard = **4**.
2. **PRIMARY COLORS**: elencare le zone cromatiche DOPO aver mentalmente eliminato le sfumature.
   - Guarda l'oggetto e chiediti: *"se potessi usare solo N colori di tempera piatta, come lo dipingerei?"*
   - Se hai più di N colori → unifica le zone simili: "verde chiaro + verde scuro" → "dark green"; "arancio + rosso" → "orange-red"
   - Dai priorità ai colori che corrispondono a **zone geometricamente separate** (un elemento diverso = un colore diverso)
3. **[COLORE]**: nome colore in inglese semplice (dark green, orange-red, gold, ivory, terracotta, navy blue, etc.)

## Esempio compilato — Fico d'India

```
PRIMARY COLORS for this subject:
  - Zone 1: cactus pad (pala/foglia) → uniform flat DARK GREEN
  - Zone 2: prickly pear fruits → uniform flat ORANGE-RED
  - Zone 3: craquelé vein pattern on pad → uniform flat GOLD/YELLOW
             (keep as flat pattern on top of the green pad,
              do not remove — it is a design feature)
```

## Nota importante: sfumature vs informazione di profondità

⚠️ **Non confondere** color simplification con delight pass:

| Operazione | Rimuove | Preserva |
|------------|---------|----------|
| **Delight pass** | Riflessi speculari (highlight di luce) | Ombre che definiscono la forma 3D |
| **Color simplification** | Variazioni di pigmento (blend pittorici, wash, sfumature di colore) | Tutto il resto, incluse le ombre di forma |

Sono operazioni distinte e non in conflitto. Specificale **separatamente** nel prompt — non combinarle in un'unica istruzione vaga.

## Quando NON usarlo

- Stampa **mono-colore** (single filament) → colore irrilevante, block inutile
- Oggetti dove i colori coincidono già con zone nette senza sfumature → va già bene, block opzionale
- Oggetti dove **le sfumature di colore sono la forma geometrica** (es. un gradient di colore indica rilievo o profondità su un oggetto monocromatico) → il block può rimuovere informazioni geometriche utili. Non usare quando il colore è l'unica indicazione della geometria sottostante.
