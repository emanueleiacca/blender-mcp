# Block: Casting Defects Repair (Gesso / Plaster)

**Da aggiungere** al master quando il soggetto è un **prototipo in gesso** (maquette, modello di studio artigianale) invece di un pezzo in ceramica cotta. Frequente nel dominio artigianale italiano: i bottegai usano calchi in gesso come modelli di riferimento per le produzioni in ceramica.

## Perché serve un block dedicato

Il gesso ha difetti di produzione caratteristici che **non esistono** nel pezzo finale in ceramica e che **NON devono** diventare geometria nel mesh 3D:

| Difetto | Come appare | Origine |
|---------|-------------|---------|
| **Bolle d'aria** (buchi) | Micro-crateri circolari, Ø 1-5 mm, distribuiti casualmente sulle superfici piane | Aria intrappolata nel gesso liquido durante il colaggio |
| **Linee di stampo** | Linee sottili e rettilinee che percorrono il pezzo lungo i piani di separazione dello stampo | Giunzione tra le due metà dello stampo |
| **Macchie di umidità** | Zone più scure o grigio-giallastre su base bianca/crema | Assorbimento d'acqua nel tempo |
| **Stuccature** | Piccole zone con texture diversa (più liscia o più granulosa) | Riparazioni con stucco/gesso fresco post-colaggio |

**Il problema specifico**: il tool image-to-3D interpreta le bolle come micro-concavità scultoree e le linee di stampo come solchi decorativi → il mesh output ha difetti "scolpiti" che nel pezzo reale non esistono.

## Block (aggiungi prima della sezione OUTPUT)

```
=== CASTING DEFECT REPAIR (plaster/gesso source material) ===
The subject is a PLASTER CAST PROTOTYPE (gesso), NOT the finished
ceramic piece. Plaster casting produces manufacturing defects that
must be ELIMINATED — they are NOT part of the original design.

Identify and remove the following defects:

1. AIR BUBBLE PITS (most common): small circular holes or craters,
   typically 1-5 mm in diameter, distributed randomly on flat or
   gently curved surfaces (walls of the vessel, background surfaces
   of the fruit, etc.). Fill these completely — smooth the surface
   to match the surrounding geometry as if the hole never existed.

2. MOLD SEAM LINES: thin raised or recessed lines running in straight
   or gently curved paths along the sides of the object, typically
   following the natural split plane of a two-part mold. These are
   NOT decorative grooves. Remove by smoothing them flush with the
   surrounding surface. Do NOT remove intentional sculpted grooves
   (e.g. the twist of the rope border, furrows between fruit, leaf
   veins).

3. MOISTURE STAINING: darker patches or discoloration on an otherwise
   uniform-colored plaster surface. Normalize to a uniform neutral
   matte surface color.

4. REPAIR PATCHES: zones where texture changes abruptly on otherwise
   uniform areas (smoother or rougher than surroundings). Blend to
   match the dominant surrounding texture.

=== HOW TO DISTINGUISH DEFECTS FROM DESIGN ===
Use these rules to avoid removing intentional detail:
- Defects (remove): round holes on flat surfaces, straight lines
  that cross decorative zones without following the artistic form,
  random patches, staining
- Design (keep): sculpted fruit volumes, rope twist, leaf veins,
  stems, concave boundaries between fruit elements, facial features
  if any, all repeating ornamental patterns
- When in doubt: look at whether the feature is SYMMETRICALLY or
  RHYTHMICALLY repeated (design) vs RANDOM (defect)

=== RESULT SURFACE QUALITY ===
After defect removal, plaster surfaces should appear as smooth,
clean, uniformly textured forms — similar in quality to a perfectly
cast and sanded gesso surface, or equivalently to the final glazed
ceramic piece if it were rendered matte.
The citrus-peel texture of lemons (if present) IS a design feature:
do NOT smooth it away; only remove the bubble pits that sit ON TOP
of or within that texture.
```

## Sinergia con altri block

- **NON serve** `delight_aggressive.md` — il gesso è già opaco/matte, non ha riflessi specular
- **USARE** `detail_preservation.md` — per assicurarsi che la rimozione dei difetti non intacchi i dettagli scolpiti intenzionali
- **Usare** `perspective_correction.md` se la foto è storta o grandangolare

## Combinazione tipo per un prototipo in gesso con dettagli fini

```
[master_template]
+ [casting_defects.md content]     ← rimuove bolle e seam
+ [detail_preservation.md content]  ← assicura che i dettagli sopravvivano
+ OUTPUT section
```

## Note sul colore

Il gesso è quasi sempre **bianco/crema**. Il soggetto su sfondo bianco può essere difficile da isolare per Gemini. Se hai problemi di isolamento, fotografa il pezzo su un panno **grigio medio** (non nero — troppo forte; non bianco — sparisce). Aggiungi questa nota al prompt: *"The subject is white/cream plaster on a grey background — isolate based on edge geometry, not color contrast."*

## Nota KB (2026-05-08)

Scoperta durante la prima sessione reale (vaso limoni). L'utente aveva fotografato un prototipo in gesso assumendolo fosse ceramica. I buchi da bolle erano visibili nell'output Gemini. Da allora questa distinzione è documentata nel workflow: **chiedi sempre all'utente quale è il materiale del pezzo fotografato** (gesso prototipo vs ceramica finita vs terracotta vs legno).
