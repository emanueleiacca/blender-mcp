# 07 — Hydrostone, Aqua-Resin, plaster-of-Paris come coating sottile su PLA

> **Tesi**: i coating gesso/cement-like rendono il PLA "vera pietra/ceramica" al tatto. **Hydrostone** (USG industrial gypsum) è il gold standard prop-maker. Limiti severi: spessore minimo 1-2 mm, fragility extreme su substrato flessibile, sandabilità mediocre, peso aumentato del 200-400 %. Non un vero shortcut, ma un **upgrade tier sopra il kaolin slurry** quando serve **massa autentica**.

---

## 7.1 I tre prodotti principali

### Hydrostone (USG)
- **Gypsum cement** industriale (solfato di calcio idratato).
- Forza compressione 70 MPa (vs plaster-of-Paris 8 MPa).
- Asciuga in 30-45 min al touch, full cure 24 h.
- Bianco brillante, lavorabile a sand 220-400.
- €25/sacco 11 kg, reperibilità EU difficile (USA via Smooth-On reseller).
- Alternativa EU: **Cremnitz Hydrocal** o **Mapei Mapecem** simili formulazioni.

### Aqua-Resin
- **Acrylic emulsion + gypsum filler**, prodotto Aqua-Resin Inc. (USA).
- Coating brush-on, asciuga 2-4 h, full cure 24 h.
- Più flessibile di hydrostone (acrylic binder).
- €70/kit 1 kg, reperibilità EU solo via import.
- Eccellente su prop teatrali grandi.

### Plaster-of-Paris (gesso comune)
- **Solfato calcio emihydrato**, comune da ferramenta.
- Cure 15-30 min flash.
- Bianco opaco, sandabile.
- €5/sacco 5 kg, ovunque.
- **Fragility estrema**, non adatto a parti manipolate.
- Per coating sottile su PLA: marginalmente OK.

---

## 7.2 Workflow tipico prop maker (Bill Doran, Punished Props)

### Preparazione PLA
1. Sand 220, pulizia IPA.
2. Primer base spray (Rust-Oleum Filler Primer) 1-2 mani — **CRITICO** per adesione gesso al PLA.
3. (Opz.) Scratch coat con mesh fiberglass leggero su superfici grandi.

### Applicazione Hydrostone
1. Mix Hydrostone 100 g + acqua 30 ml (rapporto 100:28-32 da datasheet USG).
2. Stendere a pennello rigido o spatola, **layer 1-2 mm**.
3. Working time: 5-7 min (poi inizia a rapprendere).
4. Cure 30 min al touch, 24 h full.
5. Sand 220 → 400.
6. Primer ulteriore + paint a piacere.

**Spessore minimo realistico su PLA**: **1.5 mm**. Sotto, fragility cause sciamatura.

### Applicazione Aqua-Resin
1. Mix parte A + parte B (acrylic emulsion + gypsum) secondo datasheet.
2. Pennello 2-3 mani, ciascuna 0.5-1 mm.
3. Working time più lungo (15-20 min).
4. Cure 2-4 h tra mani, 24 h full.
5. Sand 320 → 600.
6. Paint.

**Vantaggio Aqua-Resin**: più flessibile, meno cracking su PLA.

---

## 7.3 Compatibilità con PLA — limiti

### Problema 1: Tg PLA ~60 °C
Il calore esotermico del gesso indurente (Hydrostone esotermico ~10-15 °C sopra ambiente) **NON è un problema** per PLA in spessore sottile. La massa termica è insufficiente per raggiungere 60 °C.

### Problema 2: rigidità differenziale
PLA ha modulo elastico ~3.5 GPa; gesso ~10-15 GPa. Sotto stress termico (giorno/notte, sole/ombra), espansione differenziale crea **crack al perimetro**.

Soluzione: **mesh fiberglass intermedia** o **layer flessibile** di acrylic medium tra PLA e gesso.

### Problema 3: peso
Un vaso PLA 200 g, ricoperto Hydrostone 1.5 mm, può diventare 600-800 g. **3-4× peso**. Trade-off: il pezzo "sente vera ceramica" in mano (perché lo è quasi diventata), ma diventa **fragile-pesante** — combinazione peggiore (cade più facilmente perché pesante, rompe peggio perché gesso).

### Problema 4: sandabilità su PLA flessibile
Sanding Hydrostone su PLA sottile (vase mode 0.4 mm wall) → la pressione del sanding flette il PLA → micro-crack nel gesso. Workaround: **riempire l'interno con espandente PU o sabbia** per dar massa, oppure usare solo su pareti spesse (>2 mm).

---

## 7.4 Casi d'uso prop-maker

### Bill Doran (Punished Props Academy)
- Workflow tipico per cosplay teatrali/film: 3D print PLA → primer → Aqua-Resin brush-on → sand → paint.
- Punished Props YouTube "Aqua-Resin tutorial" (2019).
- Usato per **scudi, mazze, props grandi** dove peso e fragility non sono problemi (props mostrati non manipolati intensamente).

### Adam Savage / Tested
- Workflow occasionale Hydrostone su pezzi singoli.
- Tested YouTube "One day builds — Hydrostone helmet" (2017).

### Frank Ippolito
- Coat di gesso su foam/PLA per finitura "stone/ancient artifact".
- YouTube channel Tested e proprio.

---

## 7.5 Confronto con kaolin slurry (file 06)

| Caratteristica | Kaolin slurry | Hydrostone | Aqua-Resin |
|----------------|----------------|------------|-------------|
| Spessore minimo | 0.2 mm | 1.5 mm | 0.5 mm |
| Cure time | 24-48 h | 30 min + 24 h full | 2-4 h + 24 h full |
| Costo/pezzo | €0.30 | €1-2 | €3-5 |
| Look "ceramica" | 10/10 biscuit | 9/10 stone-cement | 8/10 stone-cement |
| Sandability | OK fine grit | Eccellente | Eccellente |
| Fragility su PLA | Media | Alta | Bassa |
| Peso aumentato | +5-10 % | +200-400 % | +100-200 % |
| Reperibilità IT | ✅ | ⚠️ import | ⚠️ import |
| Skill richiesto | ★★★ | ★★★ | ★★★ |

**Insight**: per **biscuit ceramico autentico** = kaolin slurry vince in tutto.
Per **"pietra/cemento autentico"** con sandability premium = Hydrostone/Aqua-Resin vincono, ma serve pezzo robusto.

---

## 7.6 Quando vale la pena

✅ **SÌ Hydrostone/Aqua-Resin se**:
- Pezzo è **grande e robusto** (>15 cm, wall >2 mm).
- Serve un look **artefatto antico, statue museum, fossile**.
- Si fa **prop teatrale/cosplay** (display non manipolato).
- Si accetta peso aumentato.

❌ **NO Hydrostone se**:
- Pezzo piccolo o sottile.
- Manipolazione frequente.
- Serve resistenza a urti.
- Si vuole "ceramica fine porcelain" → kaolin slurry o Ricetta #3.

---

## 7.7 Alternative italiane per "pietra autentica"

| Prodotto IT | Tipo | Prezzo | Note |
|-------------|------|--------|------|
| **Mapei Mapecem** | Cement-based topping | €25/25 kg | Industriale, troppo grosso per dettagli |
| **Saratoga Stucco Cemento** | Stucco edilizio fine | €8/kg | Per coating spesso, sandable |
| **Polyfilla Big Hole** | Filler edilizio | €10/kg | Coating sottile su PLA primerizzato OK |
| **Stucco veneziano marmorino** | Marmorino bianco | €40/5kg | Look marmo veneziano premium, cure 48h |
| **Bauwerk Limewash** | Calce naturale | €15/kg | Look "intonaco antico", molto fragile |
| **Sennelier Texture Gel Coarse** | Acrilico texturizzato | €25/250ml | Look "stone artistica" |

Marmorino veneziano è il **dark horse** di questa lista — applicato a mestolo su PLA primerizzato dà look **villa veneta autentico** con burnishing finale.

---

## 7.8 Workflow combinato sperimentale: "marmorino veneziano su PLA" (Ricetta #12)

Per ottenere effetto **marmo lucido stuccato lombardo-veneto**:

| Step | Operazione | Prodotto | Tempo |
|------|-----------|----------|-------|
| 1 | Sand 220 | Carta | 5 min |
| 2 | Primer filler 2 mani + sand 400 | Rust-Oleum Filler Primer | 10 min + 4 h |
| 3 | Mesh fiberglass adesivo su superfici grandi (opz.) | — | 5 min |
| 4 | Marmorino mano 1 spatola fine | Saint-Astier Marmorino bianco | 15 min + 4 h |
| 5 | Marmorino mano 2 (color base) | Marmorino tinto | 15 min + 24 h |
| 6 | Spatola lucida burnishing | Spatola inox lucidata | 10 min |
| 7 | Cera d'api liquida | Cera trasparente Linea Pavè | 5 min + 24 h cure |

- **Attivo**: ~70 min
- **Calendar**: 2 giorni
- **Costo per pezzo**: €5
- **Skill**: ★★★★☆
- **Resa "marmo lucido veneziano"**: 9/10 (verificare con test diretto — claim teorica)

---

## 7.9 Sicurezza

- **Hydrostone**: polvere di gesso, **maschera P2 essenziale** durante mixing e sanding (silicosi se inalato regolarmente).
- **Aqua-Resin**: acrylic + gypsum, low odore, ma stesse precauzioni anti-polvere.
- **Marmorino**: contiene calce + grasselli + polveri marmo, **maschera P2** + occhiali.

---

## 7.10 Fonti

- usg.com/content/dam/USG_Marketing_Communications/united_states/product_promotional_materials/finished_assets/usg-hydrostone-gypsum-cement-data-submittal-sheet-en.pdf — Hydrostone datasheet ufficiale
- aqua-resin.com — sito ufficiale Aqua-Resin Inc.
- smooth-on.com/products/hydrostone — reseller US
- Bill Doran / Punished Props YouTube "Aqua-Resin tutorial" (2019)
- Adam Savage Tested YouTube "Hydrostone helmet build" (2017)
- Frank Ippolito YouTube "Plaster on foam props" (2018)
- mapei.com/it — Mapecem datasheet
- saint-astier.com — Marmorino tradizionale Vicenza
- saratoga.it — Stucco edilizio italiano
- Reddit r/cosplayprops thread "Hydrostone vs Aqua-Resin" (2022)
- YouTube "Frank Ippolito / Tested" "Coating foam with rigid materials" (2020)
