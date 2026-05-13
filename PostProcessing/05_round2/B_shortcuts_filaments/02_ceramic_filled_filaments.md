# 02 — Filamenti ceramic-/stone-filled: ProtoPasta Stoneworks, Fillamentum Vertigo Ceramic, FormFutura Atlas

> **Tesi**: questi filamenti contengono carica minerale **15-40 %** in matrice PLA. Output nudo ha texture e ottica **vicinissima alla pietra/ceramica grezza** — risparmiando 80-100 % del workflow di painting effetto stone. Costo: filamento 2-3× il prezzo del PLA basic, **ugello acciaio temprato obbligatorio**, fragility molto alta.

---

## 2.1 ProtoPasta Stoneworks line

ProtoPlant (Vancouver WA, USA) — pioneere dei filamenti "fancy". La linea Stoneworks:

| Prodotto | Filler reale | % stimata filler | Look nudo | €/kg EU (3DJake/iGo3D) |
|----------|--------------|------------------|-----------|------------------------|
| **Stoneworks Slate** | Polvere di ardesia | ~30 % | Grigio scuro opaco granulato | 49 |
| **Stoneworks Granite** | Granito macinato | ~30 % | Grigio chiaro con flecks scuri | 49 |
| **Stoneworks Marble** | Calcite | ~25 % | Bianco-avorio con vene | 49 |
| **Stoneworks Sandstone** | Quarzo + ossidi | ~30 % | Beige-arenaria | 49 |

Brillo: zero. Matte completo, leggermente "ruvido" al tatto (Ra ~25-50 µm vs PLA Basic ~5-15 µm).

### Compatibilità A1 / ugello
- **Ugello standard A1 (Hardened Steel 0.4)**: durata stimata 3-5 kg di stampa → progressivo elargimento foro, perdita precisione, eventuale clog.
- **Raccomandato**: nozzle hardened-steel Bambu €18, oppure **ruby/sapphire-tipped Olsson Ruby €90** (durata 100+ kg).
- **0.6 mm** consigliato per ridurre pressure: l'estrusione è "pastosa" e a 0.4 con velocità >80 mm/s si ottengono under-extrusion striature.

### Settings ProtoPasta Stoneworks (da datasheet ufficiale)
```
Nozzle: 0.5-0.6 hardened steel
Print temp: 195-215 °C (sotto Basic — il PLA host è low-melt)
Bed: 45-60 °C
Speed: 30-60 mm/s outer wall
Cooling: 100 %
Retraction: ridotta del 50 % (filler causa clog)
Layer height: 0.2-0.3 mm consigliato
```

### Look nudo
- Sandstone è il "winner" estetico — somiglia incredibilmente a **arenaria di Maastricht** o **pietra di Vicenza**, anche in close-up.
- Slate sembra ardesia da tetto, eccellente per basi/piedistalli.
- Granite ha flecks veri (le particelle di granito macinato si vedono nelle pareti).
- Marble: la vena è meno pronunciata che nel Bambu Marble; aspetto più "biscuit con macchie" che "Carrara".

### Necessità post-process
- **Zero**, per look stone autentico. Stampato e finito.
- Opzionale: 1 mano di Krylon Matte Clear o Vallejo Matte Varnish per fissare polvere superficiale e proteggere dall'unto.
- **NON usare gloss varnish**: trasforma il look pietra in "plasticone con sabbia dentro".

### Fragilità
- **Allungamento a rottura ~2 %** (vs 5-7 % PLA Basic) → snap test: si rompe netto a flessione moderata.
- Pareti sottili (< 2 mm) facilmente fragili al de-mold.
- **Pezzi piccoli (<5cm) con dettagli sottili**: rischio rottura al manipolo.

Fonti ProtoPasta:
- proto-pasta.com/pages/stoneworks-pla
- proto-pasta.com/products/sandstone-pla (datasheet PDF)
- Reddit r/3Dprinting "ProtoPasta Stoneworks review" (mar 2024, 1.8k upvote)

---

## 2.2 Fillamentum Vertigo / Crystal Clear Galaxy / Ceramic line

Fillamentum (Czech Republic, premium EU) — gamma "Vertigo" è la più conosciuta per effetti minerali.

| Prodotto | Filler | % stimata | Look nudo | €/kg EU |
|----------|--------|-----------|-----------|---------|
| **Vertigo Galaxy** | Glitter mica + filler | 10-15 % | Grigio con punti riflettenti | 39 |
| **Vertigo Grey** | Filler grigio | 10-15 % | Grigio antracite opaco | 35 |
| **PLA Extrafill "Vertigo Beige"** | Filler beige | 15 % | Beige sabbia | 35 |
| **PLA "Stone Age Light"** | Calcite | 20 % | Avorio "stone-y" | 39 |
| **CPE HG100 Gloss** (non ceramic) | — | — | — | — (lasciato per riferimento, NON ceramico) |

### Note Vertigo Galaxy
- È più "metallic galaxy" che "stone" — utile per cosplay, sfondi astrali; per ceramica vera non è il candidato.

### PLA Stone Age Light / Dark
- Più simile a ProtoPasta Stoneworks ma con **filler più fine** → texture meno granulosa, più "calcare liscio".
- Per "porcellana biscuit con sentore minerale" è il match ideale.
- Disponibilità EU: fillamentum.com/eu, 3DJake.it.

### Settings Fillamentum (datasheet)
```
Nozzle: 0.4-0.5 hardened
Temp: 190-210 °C
Bed: 50-60 °C
Speed: 40-60 mm/s
Cooling: 80-100 %
```

### Compatibilità Bambu A1
- AMS lite: ⚠️ sconsigliato per i filler abrasive
- Spool holder esterno (top mount) preferito.

Fonti Fillamentum:
- fillamentum.com/collections/pla-extrafill
- fillamentum.com/wp-content/uploads/2023/05/TDS_PLA-Vertigo.pdf (datasheet tecnico)
- YouTube "3D Printing Nerd — Fillamentum Vertigo unboxing" (2023)

---

## 2.3 FormFutura Atlas / EasyFil PLA Stone

FormFutura (Olanda) — più B2B/industrial.

| Prodotto | Filler | % | Look nudo | €/kg |
|----------|--------|---|-----------|------|
| **Atlas Support** | — | — | (è un support, non ceramic) | — |
| **StoneFil Pottery Clay** | Argilla + cellulosa | 30-40 % | "Terracotta" rossa autentica | 49 |
| **StoneFil Granite** | Granito | 30 % | Grigio screziato | 49 |
| **StoneFil Slate** | Ardesia | 30 % | Grigio antracite | 49 |
| **StoneFil Limestone** | Carbonato calcio | 30 % | Beige chiaro | 49 |
| **Ceramic PLA** (discontinued 2023) | Caolino + clay | 40 % | Bianco "porcellana grezza" | — |

> **Nota**: il "StoneFil Pottery Clay" è il match più convincente per **terracotta autentica**. Da 30 cm è indistinguibile da terracotta vera (testimoniato da prop maker su YouTube — vedi sotto).

### Settings StoneFil
```
Nozzle: 0.6 hardened obbligatorio (filler grosso)
Temp: 200-220 °C
Bed: 50-60 °C
Speed: 30-50 mm/s
Cooling: 100 %
Layer height: 0.25-0.30 mm (la grana nasconde, non serve fine)
```

### Resa look
- StoneFil Pottery Clay: **terracotta 9/10** nudo. Aggiungendo wash umber per recessi + sealer matte → 10/10.
- StoneFil Limestone: pietra calcarea **8/10** nudo.

### Reperibilità Italia (maggio 2026)
- 3DJake.it stocca StoneFil e Vertigo.
- formfutura.com (shipping EU).
- iGo3D (DE, shipping IT).
- ProtoPasta: solo via 3DJake/iGo3D o import diretto dagli USA (dazio + shipping = €70/kg arrivati a destino).

Fonti FormFutura:
- formfutura.com/shop/category/stonefil
- formfutura.com/wp-content/uploads/2021/02/TDS_StoneFil.pdf
- YouTube "Thomas Sanladerer — Filaments that look like stone" (2022) — review StoneFil

---

## 2.4 Tabella comparativa unica filamenti ceramic/stone

| Filamento | Tipo finitura | Filler % | Abrasività | €/kg EU | A1 hardened OK? | Resa "stone/ceramic" nudo |
|-----------|--------------|----------|------------|---------|------------------|----------------------------|
| Bambu PLA Matte White | Biscuit-bianco | ~10 | Bassa | 24.99 | ✅ | 7/10 biscuit |
| Bambu PLA Marble White | Marmo finto | ~15 | Media | 29.99 | ✅ (cambio ugello 5 kg) | 7/10 marmo decor |
| ProtoPasta Slate | Pietra scura | ~30 | Alta | 49 | ⚠️ | 9/10 ardesia |
| ProtoPasta Sandstone | Arenaria | ~30 | Alta | 49 | ⚠️ | 10/10 sandstone |
| ProtoPasta Granite | Granito | ~30 | Alta | 49 | ⚠️ | 9/10 granito |
| ProtoPasta Marble | Marmo | ~25 | Media-alta | 49 | ⚠️ | 8/10 carrara |
| Fillamentum Vertigo Grey | Pietra grigia | ~15 | Media | 35 | ✅ | 7/10 |
| Fillamentum Stone Age | Calcare | ~20 | Media | 39 | ✅ | 8/10 |
| FormFutura StoneFil Pottery | Terracotta | ~35 | Alta | 49 | ⚠️ | 10/10 terracotta |
| FormFutura StoneFil Limestone | Pietra chiara | ~30 | Alta | 49 | ⚠️ | 9/10 calcare |
| FormFutura StoneFil Granite | Granito | ~30 | Alta | 49 | ⚠️ | 9/10 granito |
| FormFutura StoneFil Slate | Ardesia | ~30 | Alta | 49 | ⚠️ | 9/10 |

> ⚠️ = serve ugello ruby/sapphire o sostituzione frequente hardened steel.

---

## 2.5 Costo per pezzo (oggetto 200 g)

| Filamento | Costo materiale | Post-process | Tempo totale | Resa stone |
|-----------|-----------------|--------------|--------------|------------|
| PLA Basic + Stone spray (Ricetta #2) | €0.40 + €4 = €4.40 | 20 min + 3 gg cal. | 3 gg | 9/10 |
| ProtoPasta Sandstone nudo | €9.80 | 0 min | 0 gg | 10/10 |
| StoneFil Pottery + matte varnish | €9.80 + €0.30 = €10.10 | 5 min + 24h dry | 1 gg | 10/10 terracotta |
| Fillamentum Stone Age | €7.80 | 0 min | 0 gg | 8/10 |

**Tradeoff**: il filamento stone-filled raddoppia il costo materiale ma azzera tempo di post-process e spray paints. **ROI positivo se** l'utente fa volume (più di ~10 pezzi/mese) o vuole eliminare bombolette (garage ventilato ma limited).

---

## 2.6 Limiti e gotchas

1. **Nozzle hardened o ruby OBBLIGATORIO** per i ProtoPasta/FormFutura (filler ≥30 %). L'A1 viene con hardened steel di serie, ma se è già usurato il primo segno è "ghost lines" parallele.
2. **Filtro AMS lite**: l'AMS ha sensori capacitivi sui filamenti; alcuni utenti riportano che i filler ad alta opacità confondono il sensore "no spool". Workaround: top-mount holder.
3. **Stringing severo**: i stone-filled producono stringing 2-3× più di Basic. Aumentare retraction (paradosso: di solito si riduce per evitare clog, ma con stone-fill servono micro-tweak). Usare temp tower per fine-tuning.
4. **Bed adhesion**: i filler riducono la "tackiness" del PLA fuso. Brim 5 mm consigliato sempre per pezzi >5 cm.
5. **Storage**: i stone-filled assorbono umidità più velocemente del PLA Basic (il filler è igroscopico). Drybox indispensabile.
6. **Multi-color con AMS**: il purge dei stone-filled è doloroso, lascia "macchie pietra" su altri filamenti per 200+ mm. Multi-color con stone-fill: SCONSIGLIATO.
7. **Vase mode con stone-fill**: ⚠️ il filler grosso può causare under-extrusion sul perimetro singolo. Usare nozzle 0.5-0.6 + speed ≤40 mm/s. **Layer height 0.25-0.30 mm va benissimo**, anzi è meglio (nasconde imperfezioni).

---

## 2.7 Workflow shortcut suggerito per ogni effetto

| Effetto target | Filamento + shortcut | Tempo totale | Costo €/pezzo |
|----------------|----------------------|--------------|---------------|
| Porcellana biscuit unglazed | Bambu PLA Matte White nudo | 0 min | €3.75 |
| Marmo finto decor | Bambu PLA Marble nudo | 0 min | €4.50 |
| Stone/granito | ProtoPasta Sandstone o Slate nudo | 0 min | €9.80 |
| Terracotta autentica | FormFutura StoneFil Pottery Clay nudo + matte varnish | 5 min | €10 |
| Porcellana lucida | (nessun filamento sostituisce — serve Ricetta #3) | 4 gg | €10 |
| Crackle/raku | (nessun filamento sostituisce — serve Ricetta #6) | 6 gg | €10 |
| Glazed colorata | Bambu Silk + Pledge come base, color spray sopra | 1 gg | €5 |

> **Insight**: i filamenti shortcut coprono **3 dei 5 effetti ceramici** (biscuit, marmo, stone). Per porcellana lucida e crackle non c'è sostituto al workflow di painting.

---

## 2.8 Fonti

- proto-pasta.com/pages/stoneworks-pla — pagina ufficiale linea Stoneworks
- proto-pasta.com/products/sandstone-pla — datasheet Sandstone
- fillamentum.com/collections/pla-extrafill — PLA Vertigo e Stone Age
- fillamentum.com/wp-content/uploads/2023/05/TDS_PLA-Vertigo.pdf — datasheet tecnico
- formfutura.com/shop/category/stonefil — gamma StoneFil
- formfutura.com/wp-content/uploads/2021/02/TDS_StoneFil.pdf — datasheet StoneFil
- 3DJake.it — reperibilità EU dei tre brand
- iGo3D.de — alternative DE shipping IT
- CNC Kitchen YouTube "Why your nozzle is wearing out — abrasive filaments tested" (2024)
- Thomas Sanladerer YouTube "Filaments that look like stone" (2022)
- 3D Printing Nerd YouTube "Fillamentum Vertigo first look" (2023)
- Reddit r/3Dprinting "ProtoPasta Stoneworks: is it worth the price?" (mar 2024)
- Reddit r/functionalprint "Best filament for natural stone look" (gen 2025)
