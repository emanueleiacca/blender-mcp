# 01 — Bambu Lab PLA Silk / Silk+ / Marble / Matte

> **Tesi**: i filamenti "estetici" di casa Bambu (Silk, Silk+, Marble, Matte) sono lo shortcut numero uno per ottenere un look "ceramico/decorativo" senza dipingere. Non sostituiscono la porcellana lucida di Ricetta #3, ma per **vasi, lampshade, oggetti decor a media distanza** abbattono il workflow da 4 giorni a 0 giorni post-print.

---

## 1.1 Cosa cambia chimicamente

I PLA "Silk" non sono PLA puro: hanno tipicamente **5-15 % di copolimeri / modificatori glossy** (PHA, TPU rubber-toughening, o additivi acrilici proprietari) che alterano l'indice di rifrazione superficiale. Risultato:

- **Riflesso speculare** (Fresnel) molto più alto del PLA opaco → effetto "satin".
- Layer lines **otticamente attenuati** perché la luce rimbalza sull'intera estrusione invece di sui micro-pori del PLA basic.
- Colori più "saturi"/profondi, spesso descritti come "metallic sheen" o "pearlescent".

I **PLA Matte** invece contengono **filler microsferici opacizzanti** (talco, gesso micronizzato, microspheres ceramiche al 5-20 %) che:

- Diffondono la luce in modo Lambertiano (riflesso diffuso) → look "biscuit"/"bone-china unglazed".
- Nascondono i layer lines per assenza di riflessi speculari (le linee si vedono dove la luce striscia; senza riflesso, sparizione visiva).
- Aumentano la rigidità (filler) ma riducono leggermente allungamento a rottura.

Il **PLA Marble** è una sottospecie del Matte: stessa base + **granuli di pietra macinata (in genere calcite o gesso colorato) di 50-200 µm** distribuiti in matrice PLA opaca. La granulosità è macroscopica → vena marmorea visibile a occhio nudo.

---

## 1.2 Tabella prodotti Bambu (prezzi maggio 2026, store EU)

| Prodotto | Tipo additivo | Colori | €/kg (EU) | Print T °C | Bed T °C | Note |
|----------|--------------|--------|-----------|------------|----------|------|
| **PLA Basic** | Nessuno | 35+ | 19.99 | 190-230 | 35-45 | Baseline, opaco semi-satin |
| **PLA Matte** | Filler opacizzante | 18 | 24.99 | 210-230 | 35-45 | "Chalk" / unglazed |
| **PLA Silk** | Copolimero glossy | 14 | 28.99 | 215-235 | 35-45 | Brillo satin metallic |
| **PLA Silk+** | Silk migliorato, layer-adh | 12 | 32.99 | 215-235 | 35-45 | "Dual-color" disponibili |
| **PLA Marble** | Filler minerale grosso | 3 (white/grey/red) | 29.99 | 210-230 | 35-45 | Vena visibile, ugello acciaio temprato consigliato |
| **PLA Galaxy** | Glitter mica | 4 | 29.99 | 215-235 | 35-45 | Particelle riflettenti |
| **PLA Sparkle** | Glitter fine | 6 | 26.99 | 200-230 | 35-45 | Effetto "sand" da lontano |

Fonti prezzo: store.bambulab.com/it (verificato 13 maggio 2026), 3DJake.it, Polyfilamento.it.

---

## 1.3 Look "nudo" subito post-print

### PLA Silk (es. Silk White, Silk Champagne Gold)
- Da 50 cm di distanza: **resa "porcellana satinata" 7/10** se layer height ≤ 0.16 mm.
- Da 20 cm: layer lines residui visibili in luce radente. Resa ~5/10.
- Soggetti consigliati: vasi, supporti tablet, lampshade, statuine geometric-art.
- Soggetti **sconsigliati**: pezzi con dettagli figurativi fini (le piattezze silk sembrano "plasticone" da vicino).

### PLA Matte White
- Da 30 cm: **resa "biscuit/eggshell" 8/10**. Eccellente per finto-gesso, ceramica unglazed, busti scultorei.
- Da 10 cm: layer lines ancora distinguibili ma molto meno marcati che su Basic.
- È il filamento "default ceramico" se non si vuole dipingere. Si lascia nudo o si fa solo wash + matte varnish.

### PLA Marble
- Vena visibile: il colore base (bianco o grigio) ha **inclusioni nere/grigio scuro 100-200 µm** distribuite in modo pseudo-random.
- A 30 cm somiglia **realmente a marmo grezzo** (Carrara venato).
- A 5 cm si vede che è plastica, ma per decor è convincente.
- **Limit**: la grana ha pattern visibile lungo la direzione di stampa (le inclusioni si "allungano" nei perimetri perché la trafila estrude come "salsiccia").

### PLA Silk+ Dual-Color
- Due bobine intrecciate (es. bianco + oro) → strisce iridescenti orizzontali sui layer.
- Effetto "geode" o "wave silk" — interessante per arte astratta.
- **Per ceramica autentica non è la scelta**, troppo metallico.

---

## 1.4 Bambu Studio settings ottimali per look ceramico

### Per PLA Silk / Silk+ (vasi, decor)
```
Layer height: 0.12 mm (per detail) o 0.16 mm (per velocità)
Initial layer height: 0.20 mm
Wall loops: 3
Top shell layers: 0 (vase mode) OPPURE 5 (closed parts)
Sparse infill density: 10-15 % (Gyroid)
Nozzle temp: 220-225 °C (5 °C sopra Basic — i silk amano caldo)
Bed temp: 45 °C
Print speed outer wall: 100-150 mm/s
Print speed inner wall: 200-300 mm/s
Cooling fan: 70-80 % (NON 100 % — i silk diventano "stringosi" con troppo cool)
Ironing: ON solo se NON vase mode (vedi file 03)
```

### Per PLA Matte
```
Layer height: 0.12-0.16 mm
Nozzle temp: 220 °C
Cooling fan: 100 %
Ironing: ON (top finish ottima)
Bed adhesion: smooth PEI o textured PEI
```

### Per PLA Marble
```
Nozzle: ACCIAIO TEMPRATO 0.4 (sostituzione obbligatoria, il marble abrade
        l'ugello hardened-steel standard A1 in ~3-5 kg di stampa).
        Bambu Hardened Steel Nozzle 0.4 €18 oppure E3D Nozzle X €25.
Layer height: 0.20 mm (grana più visibile, e nascondi micro-imperfezioni)
Nozzle temp: 225 °C
Cooling fan: 80 %
Outer wall speed: max 80 mm/s (riduce pressure spikes con filler)
Retraction: ridurre del 30 % (i filler causano stringing extra)
```

---

## 1.5 Compatibilità AMS lite (A1)

| Filamento | AMS lite OK? | Note |
|-----------|--------------|------|
| PLA Basic | ✅ | Nessun problema |
| PLA Matte | ✅ | Nessun problema |
| PLA Silk | ✅ ma | I silk **purgano colore lentamente** (~80-120 mm vs 60 mm di Basic). Aumentare flush volume del 30-50 % per evitare "ghosting" colore. |
| PLA Silk+ | ✅ ma | Stesso. Inoltre il dual-color Silk+ è **single-spool dual-extrusion intrinseca** → non mescolare con AMS, già fa l'effetto da solo. |
| PLA Marble | ⚠️ | Tecnicamente sì, ma sconsigliato: l'AMS lite ha tubi PTFE stretti e i filler abrasivi accelerano l'usura. Stampare da spool diretto su top-mount holder. |
| PLA Galaxy / Sparkle | ⚠️ | Stesso problema marble: glitter abrasivo. |

Fonte: forum.bambulab.com thread "AMS lite filament compatibility" (febbraio 2026), wiki ufficiale bambulab.com/en/filament-guide.

---

## 1.6 Costo per pezzo (vaso 25 cm, ~150 g)

| Setup | Filamento | Costo €/pezzo | Tempo post-process | Resa "ceramica" |
|-------|-----------|---------------|--------------------|------------------|
| PLA Basic + workflow porcellana #3 | €3 + €7 vernici = €10 | €10 | 4 giorni cal. | 10/10 |
| PLA Matte nudo | €3.75 | €3.75 | 0 min | 7/10 biscuit |
| PLA Silk nudo | €4.35 | €4.35 | 0 min | 6/10 satin |
| PLA Silk + Pledge | €4.35 + €0.20 | €4.55 | 30 min + 6h dry | 7/10 |
| PLA Marble nudo | €4.50 | €4.50 | 0 min | 8/10 marmo decor |

**Conclusione**: il marmo "decor" e il biscuit "matte" sono **shortcut da 0 min post-process** se l'utente accetta una resa 7-8/10 anziché 10/10. ROI immenso per produzione di volume.

---

## 1.7 Limiti tecnici

1. **Temperature di estrusione più alte** dei Basic → l'A1 (hotend standard) gestisce fino a 300 °C, OK per qualsiasi PLA.
2. **Brittleness PLA Matte**: il filler riduce allungamento a rottura. Per parti funzionali sotto stress (clip, snap-fit) preferire Basic. Per decor irrilevante.
3. **Layer adhesion Silk**: ~10-15 % peggiore del Basic. Su pezzi sottili (perimetri singoli, vase mode wall 1.2 mm) può causare splitting al de-mold se PEI textured. Soluzione: aumentare wall a 1.6 mm o usare 4 perimeter loops.
4. **Marble nozzle wear**: documentato su CNC Kitchen "Abrasion test" (2024) — ottoni si distruggono in 1 kg, hardened-steel in 5-10 kg, ruby in 100+ kg.
5. **Print temp window stretta**: i silk fuori range (sotto 215 °C) → adesione povera e finish "ruvido"; sopra 240 °C → degradazione, perdita di brillantezza.
6. **Non waterproof**: nessun PLA estetico nudo è water-tight per uso vaso reale con acqua. Servono Pledge ≥3 mani o XTC-3D interno (vedi file 04).

---

## 1.8 Test diretti suggeriti

1. **6-vaso shoot-out**: stampare lo stesso vaso 15 cm in PLA Basic White, Matte White, Silk White, Silk+ White, Marble White, Galaxy White. Vase mode 0.16 mm. Foto identica luce → ranking "ceramica" da occhio non addestrato (chiedere a 5 persone diverse).
2. **Pledge boost**: ripetere shoot-out con 2 mani Pledge Floor Care su tutti — quanto migliora il Matte vs il Silk?
3. **Ugello duro**: stampare 1 kg di PLA Marble con ugello standard A1 0.4 → misurare diametro foro pre/post con microscopio. Calcolare quanti kg sopporta.

---

## 1.9 Fonti

- bambulab.com/en/filament-guide
- store.bambulab.com/eu (verificato 13 maggio 2026)
- forum.bambulab.com/t/silk-pla-best-settings (thread sticky)
- CNC Kitchen YouTube "Why your nozzle is wearing out" (2024) — abrasion test
- Maker's Muse YouTube "Silk PLA: is it worth it?" (2023)
- Reddit r/BambuLab thread "Best filament for vase mode aesthetic" (gen 2025, 2.4k upvote)
- 3DJake.it product pages PLA Bambu (prezzi EU)
