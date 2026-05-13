# PostProcessing — Knowledge Base

KB sul post-processing di stampe estetiche in **PLA** su **Bambu A1**. Focus:
pittura a bomboletta/pittura fredda, effetti ceramici/pietra, smoothing layer
lines, sigillatura e presentazione del prodotto finito.

**Constraint trasversale**: PLA Tg ~60 °C → tutto cold-cure. Niente forno, kiln,
heat gun. Per ogni tecnica citata si è verificata la compatibilità con questo
limite.

## Struttura

```
PostProcessing/
  INDEX.md                       # questo file
  01_layer_lines_smoothing/      # eliminazione layer lines, sanding, filler, smoothing chimico, epoxy
  02_painting_and_primers/       # primer, topcoat, tecniche spray, effetti, errori
  03_ceramic_stone_finish/       # 5 interpretazioni di "ceramica" + ricette multi-layer
  04_sealing_presentation/       # clear coat, UV, basi/display, foto, packaging
```

Ogni sottocartella contiene file numerati `01_*.md` … e:
- `_sources.md` — URL consultati, categorizzati
- `_next_questions.md` — spunti emersi per round successivi di ricerca

## Round 1 — sintesi finding (maggio 2026)

### 01 — Layer lines smoothing
- **Default trasversale**: Rust-Oleum Filler Primer + wet sanding 220→400→600→800
- **Smoothing chimico PLA**: PLA NON reagisce all'acetone. Solo etile acetato è
  hobby-feasible (con PPE), DCM/THF troppo tossici. Per la maggior parte dei
  casi conviene meccanico+filler.
- **Epoxy**: Smooth-On XTC-3D è il riferimento per curve organiche grandi
  (cosplay, helmet, busti). Possibile perdita di adesione vernice acrilica
  → scuffing 400 obbligatorio dopo cure.
- **Trick**: CA glue + baking soda per gap profondi, sandable subito.

### 02 — Painting & primers
- **Top 3 primer**: Tamiya Surface Primer (gold standard hobby), Rust-Oleum
  Filler Primer (best Q/P per high-build), Citadel Wraithbone/Grey Seer
  (primer + zenithal in un colpo).
- **Workflow base**: sgrassare con IPA → filler primer (se necessario) →
  carteggio 600 → primer fine → 2-3 mani sottili a 25cm, 18-25 °C, 40-60% RH
  → topcoat → clear coat.
- **Da evitare su PLA**: acetone, MEK, lacche celluloiche, automotive 2K
  isocianati senza precauzioni (solvent crazing).

### 03 — Ceramic / stone finish (focus principale)
5 interpretazioni con ricetta dedicata in `06_multilayer_recipes.md`:
1. **Porcellana liscia bianca lucida** — Rust-Oleum Filler Primer x3 + wet
   sand 400/600/800 + Vallejo Surface Primer White + Tamiya TS-26 + Mr. Hobby
   Premium Gloss + polish Tamiya Fine. ~€7/pezzo, 4 giorni, ★★★.
2. **Matte / biscuit** — Gesso + Liquitex Light Modeling Paste tamponata +
   wash terra ombra + Vallejo Matte Varnish.
3. **Stone / granito** — Primer nero + Montana GRANIT (water-based, PLA-safe)
   o MaxMeyer effetto pietra + matte sealer.
4. **Smaltato lucido** — XTC-3D base + Mr. Hobby Premium Gloss x3 wet coats,
   **oppure** trick Pledge Floor Care su porcellana satinata (€0.20).
5. **Crackle/raku** — Vallejo Black satin + Vallejo Crackle Medium 70.598 +
   Vallejo White matte UNA mano densa + wash Indian ink + solo acrylic gloss
   varnish (lacquer scioglie le crepe).

### 04 — Sealing & presentation
- **Sigillatura 2-strati**: Mr. Hobby Mr. Super Clear UV Cut (gloss prima,
  poi satin/matte). Aggiunge barriera UV che PLA non ha nativamente.
- **PLA outdoor**: degrada in mesi con UV. Per duty-cycle prolungato valutare
  SprayMax 2K aerosol (isocianato, PPE serio).
- **Base/plinth dedicata** (legno noce oliato o acrilico nero) + pin ottone o
  magnete annegato + nameplate inciso laser → moltiplicatore di percepito.
- **Foto prodotto minima**: light tent 60cm o finestra+bounce, sfondo PVC,
  smartphone Pro RAW + Lightroom Mobile + ColorChecker.
- **Standard 6-shot listing**: hero, ortho, detail, scale, lifestyle, packaging.

## Pattern cross-area emersi (candidati round 2)

1. **SprayMax 2K aerosol** — citato in 3 agenti come "tier above" per durabilità.
   Sicurezza casalinga, applicazione su PLA, longevità → deep dive dedicato.
2. **Filamenti ceramic-filled** (ProtoPasta Stoneworks, Fillamentum Vertigo
   Ceramic) e **Silk PLA + Pledge** → potenziale shortcut radicale del workflow.
3. **Heat-set inserts su PLA** — protocollo solido non pubblicato. Temperatura,
   geometria foro, depth ratio. Critico per montaggio prodotti commerciali.
4. **Reperibilità Italia** — mappare equivalenti IT dei prodotti USA/UK
   (Crelando Lidl, MaxMeyer, Saratoga, Ivea per stone; shop fisici Tamiya/Mr.Hobby).
5. **Ironing Bambu Studio** come pre-finishing per ridurre sanding sul top.
6. **End-to-end time/cost study** — meta-questione: tracciare un singolo prodotto
   CAD→packaging per identificare la fase ROI marginale più alto.
7. **Test misurati** (Ra, delta-E, pull-off ASTM D3359) — gap scientifico per
   la maggior parte dei prodotti hobby. Possibili test casalinghi.

## Domande dirette all'utente per indirizzare round 2

1. Dimensioni tipiche dei pezzi (statuetta 5cm vs vaso 30cm cambia tutto)?
2. Quale dei 5 effetti ceramici è priorità #1 ora?
3. Spazio di lavoro: bombolette spray fattibili (terrazzo/garage) o solo airbrush indoor?
4. Budget tool (filler primer + airbrush ~€90 OK?).
5. Tempo per pezzo (24h calendario o 1 settimana OK)?
6. I pezzi vanno manipolati o solo display?
7. Outdoor/finestra (criticità UV) o interno protetto?
8. Stai vendendo (commerciale) o produzione personale?
