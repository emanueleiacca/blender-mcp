# Block: Perspective Correction

**Da aggiungere** al master quando la foto sorgente è scattata **troppo vicina** (deformazione grandangolare), **storta**, o **non frontale** (soggetto inclinato rispetto al piano dell'immagine).

## Perché serve

I tool image-to-3D si aspettano una proiezione **quasi-ortografica** o moderatamente prospettica. Una foto scattata a 20 cm con cellulare grandangolare ingrandisce la parte vicina e rimpicciolisce quella lontana — il mesh ricostruito eredita la deformazione (es. base esageratamente larga, testa rimpicciolita). Anche un'inclinazione di 15° dell'asse del soggetto può portare a un mesh "che pende".

## Block (aggiungi prima della sezione OUTPUT)

```
=== PERSPECTIVE CORRECTION ===
The source photo has perspective distortion or non-frontal framing.
Render the output as if the photo had been taken with a long focal
lens (telephoto, ~85-135mm equivalent) from a few meters away,
producing minimal perspective foreshortening.

Apply the following:

- Render the subject in QUASI-ORTHOGRAPHIC projection. Parallel
  vertical edges of the subject should appear as parallel in the
  output (no convergence to a vanishing point).
- Correct any tilt: the subject's main vertical axis must be
  perfectly perpendicular to the bottom edge of the frame, regardless
  of how the subject was oriented in the source.
- The horizon line (implied by the subject's natural "up" direction)
  must be horizontal.
- The 3/4 view angle should be exactly 45° azimuth, ~15° elevation,
  measured from the subject's own canonical reference frame.
- Maintain TRUE PROPORTIONS: undo any wide-angle stretching of
  near features. The output should reflect the actual physical
  proportions of the object, not the camera-induced distortion.

VALIDATION: in the output, the silhouette of the subject should
match what a careful observer would draw if observing the object
from a few meters away with normal vision — neither stretched
near the camera nor compressed in the distance.
```

## Come capire se serve

Indicatori che la foto sorgente ha problemi di prospettiva:
- Scattata con cellulare a < 30 cm dal soggetto (grandangolo nativo)
- Linee verticali del soggetto (asse di un vaso) appaiono **convergenti** invece che parallele
- Soggetto sembra "inclinarsi indietro" o "sporgersi avanti"
- Una parte del soggetto è sproporzionatamente grande/piccola rispetto al ricordo dal vivo

Se nessuno di questi sintomi è evidente, **non aggiungere** questo block — Gemini è bravo a non introdurre prospettiva forte se il prompt master già chiede "quasi-orthographic projection".

## Quando NON usarlo

- Foto scattata correttamente da distanza con teleobiettivo cellulare → già OK
- Soggetto **intenzionalmente** inclinato (es. busto su piedistallo inclinato) → questo block lo raddrizzerebbe falsando l'opera
