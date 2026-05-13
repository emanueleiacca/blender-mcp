# 06 — Filamento PLA cinese bulk (eSun, Sunlu, Anycubic, Creality, Eryone)

Categoria a **risparmio reale 40-60%** vs Bambu Lab originale, qualità generalmente buona, ma con caveats su finitura post-processing e compatibilità A1.

> Prezzi 2025-2026, **verificare al momento**.

---

## A. Brand cinesi rilevanti

| Brand | Origine | Posizionamento | Recensioni 2024-2026 |
|-------|---------|----------------|----------------------|
| **eSun** | CN — Shenzhen | Storico, mass-market consistente | ★★★★ Stabile, batch variability bassa |
| **Sunlu** | CN — Zhuhai | Mass-market, vasta gamma | ★★★★ Buono, ottimo Q/P, Silk PLA noto |
| **Anycubic** | CN — Shenzhen | Brand stampante + filamento | ★★★ Buono ma non eccezionale, comodo se hai Anycubic |
| **Creality** | CN | Brand stampante + filamento | ★★★ Variabile, lotto-dipendente |
| **Eryone** | CN | Specialty (matte, silk, marble, wood) | ★★★★ Eccellente per estetica matte |
| **Jayo** | CN — Shenzhen | Budget extreme | ★★★ Lotteria, ok per prototipi |
| **Geeetech** | CN | Mass-market | ★★★ Standard |
| **Polymaker** | CN-USA | Premium tier (PolyTerra, PolyLite, PolyMax) | ★★★★★ Top — costa di più ma top-tier |
| **Bambu Lab** | CN (Shenzhen) | Premium, ottimizzato per A1/X1C | ★★★★★ Profili AMS + spool nativi |
| **3DFillies / Inland (Microcenter)** | US-CN OEM | Rebrand eSun/Sunlu | ★★★★ Affidabile |

---

## B. Prezzi orientativi

### B.1 PLA standard 1 kg

| Brand | Piattaforma | MOQ | Prezzo unitario | Equivalente Amazon/3DJake IT | Risparmio | Note |
|-------|-------------|-----|------------------|-------------------------------|-----------|------|
| eSun PLA+ 1 kg | Aliexpress | 1 | €11-16 | €18-22 IT | 25-40% | Aliexpress IOSS, no dogana |
| eSun PLA+ 10 kg bundle | Aliexpress | 10 kg | €100-150 (€10-15/kg) | €180-220 | 30-45% | Bulk |
| Sunlu PLA+ 1 kg | Aliexpress | 1 | €10-14 | €16-22 IT | 30-45% | Idem |
| Sunlu PLA+ 10 kg | Aliexpress | 10 kg | €90-130 | €170-220 | 40-50% | Tier "best Q/P" |
| Anycubic PLA 1 kg | Aliexpress | 1 | €12-17 | €18-25 IT | 25-40% | — |
| Creality CR-PLA 1 kg | Aliexpress | 1 | €10-15 | €16-22 IT | 30-40% | Variabile |
| Eryone Matte PLA 1 kg | Aliexpress | 1 | €15-22 | €25-35 IT | 30-40% | **Specialty matte** — eccellente per post-finish poco/nullo |
| Eryone Silk PLA 1 kg | Aliexpress | 1 | €17-25 | €30-40 IT | 35-45% | Silk shiny / multicolor |
| Eryone Marble PLA 1 kg | Aliexpress | 1 | €20-28 | €30-45 IT | 30-40% | Effetto pietra "out of nozzle" |
| Bambu PLA Basic 1 kg refill (no spool) | Bambu store CN | 1 | €13-17 | €18-25 IT (con spool) | 25-35% | Compatibile AMS, profili nativi |
| Polymaker PolyTerra Matte 1 kg | 3DJake EU oppure Aliexpress | 1 | €18-23 | €22-30 IT | 15-25% | Già scontato globalmente |

### B.2 Bulk 5-10 kg con sconto + 1688

Sopra 10 kg singolo ordine **rischio €150 superato** → dazio + IVA + handling. Quindi:

| Strategia | Prezzo target | Note |
|-----------|---------------|------|
| Aliexpress 5 kg singolo ordine (sub-€150) | €60-90 per 5 kg eSun = €12-18/kg | Sicuro, IOSS |
| Aliexpress 2 ordini da 5 kg (intervallati 1-2 gg) | come sopra | Splitting per restare sotto €150 cad |
| 1688 bulk 20-50 kg via agent | $5-8/kg + 8% agent + freight | Solo se >100 kg/anno consumo regolare |
| Container 500 kg LCL via freight forwarder | $4-6/kg landed | Per produzione vera |

---

## C. Compatibilità Bambu A1

L'A1 (e A1 Mini) ha **slot AMS Lite** che funziona con qualunque spool standard 200 mm + filamento 1.75 mm. **Tutti i brand cinesi sopra sono compatibili meccanicamente**.

### C.1 Profili stampa

Profili AMS nativi solo per **Bambu Lab proprietary filaments** (riconoscimento RFID). Per altri brand:

1. **Bambu Studio**: caricare manualmente il tipo materiale (PLA generic, PLA Matte generic, PLA Silk).
2. Calibrazione **Flow rate** + **Pressure advance** per il nuovo brand (15-30 min, fatto 1 volta per brand).
3. **Temp tower**: stampare 190-220 °C per identificare ottimo (eSun PLA+ tipico 210 °C, Sunlu 205 °C, Eryone Matte 200 °C, Bambu Basic 210 °C).
4. Salvare il profilo come custom in Bambu Studio.

### C.2 Performance reale brand cinesi su A1

| Brand | Temp nozzle | Velocità stabile | Diametro tolleranza | Stringing | Finitura visiva |
|-------|-------------|------------------|----------------------|-----------|------------------|
| eSun PLA+ | 210-220 | 200-300 mm/s | ±0.02 mm | basso | uniforme, opaco semi-lucido |
| Sunlu PLA+ | 200-215 | 200-300 mm/s | ±0.03 mm | basso-medio | uniforme |
| Eryone Matte | 195-210 | 150-200 mm/s | ±0.03 mm | basso | **matte vero**, micro-texture pietra |
| Eryone Silk | 210-225 | 100-150 mm/s | ±0.05 mm | medio (silk è "wet") | shiny dorato/argento |
| Anycubic PLA | 200-215 | 180-280 mm/s | ±0.05 mm | medio | uniforme |
| Bambu PLA Basic | 210-220 | 300-500 mm/s | ±0.02 mm | molto basso | uniforme, slight gloss |

### C.3 Impatto su post-processing

**Filamento matte (Eryone, Polymaker PolyTerra)** = **layer lines nascoste/attenuate**:
- Riduce sanding richiesto del 60-70%.
- Spesso si può saltare il primer filler.
- Topcoat va diretto.

**Per piccolo brand commerciale**, **PolyTerra Matte / Eryone Matte è il vero shortcut** — costa €18-25/kg vs €11-15 PLA standard, ma elimina 1-2 ore di sanding e 1 mano di filler primer. ROI positivo in 2 utilizzi.

---

## D. Recensioni reali (sintesi community 2024-2026)

Da YouTube (CNC Kitchen, Maker's Muse, 3D Printing Nerd, MyTech Fun) + Reddit r/3Dprinting r/BambuLab:

- **eSun PLA+** → batch consistent, ottimo per produzione.
- **Sunlu PLA+** → spesso "best Q/P" raccomandato; alcuni batch leggermente sottodimensionati 1.73 mm.
- **Sunlu Silk** → primo posto silk economici.
- **Eryone Matte** → unanime "buy more, you'll love it".
- **Anycubic PLA** → ok ma non eccelle in nessuna metrica.
- **Creality CR-PLA** → grandissima varianza tra lotti; alcuni eccellenti altri pessimi.
- **Jayo / TRONXY / random AliExpress** → solo per prototipi non commerciali.
- **Bambu Basic** → benchmark, profili AMS nativi, velocità top.

---

## E. Rischio dogana filamenti

- HS code **3916.91** (PLA monofilament) → dazio UE **6.5%**.
- Sotto €150 ordine via Aliexpress: **IVA inclusa via IOSS**, no dazio applicato.
- Sopra €150: dazio 6.5% + IVA 22% + handling corriere.

**Trick**: bobine eSun/Sunlu da Aliexpress arrivano in lotti €50-100 → 5-7 kg per ordine, ripetibile. Per consumo medio piccolo brand (10-30 kg/anno), questo è il modo più economico senza complessità.

**Per consumi >50 kg/anno**: cominciare con LCL mare via freight forwarder (commercio B2B).

---

## F. Verdetto

### F.1 Best buy 2025-2026 da Aliexpress

1. **Sunlu PLA+ 10 kg bundle bulk** ~€100-130. Workhorse colore base (nero, bianco, grigio).
2. **Eryone Matte PLA 1 kg** ~€18-22. Pezzi che vanno verniciati con poco lavoro.
3. **eSun PLA+ 1 kg singoli colori** ~€12-15. Colori specifici occasionali.
4. **Bambu PLA Basic refill (no spool)** ~€13-17 via Bambu store IT. Per pezzi premium dove serve profilo AMS nativo + max velocità.

### F.2 NON da Aliexpress

- **PLA "no brand" ultra-cheap** < €8/kg: lotteria, scarsa consistenza dimensione, contaminazioni in lotto.
- **Filamenti tecnici (PETG, ABS, PA6 CF)**: per uso commerciale conviene Polymaker / FormFutura / Fillamentum EU (qualità garantita, no rischio scrap).

---

## G. Riferimenti

- 3DJake (alternativa EU): <https://www.3djake.it>
- Sunlu Official Aliexpress store.
- eSun Official Aliexpress store.
- Eryone Official Aliexpress store.
- Bambu Lab IT store: <https://eu.store.bambulab.com>
- Reddit r/BambuLab thread tag "filament": confronti aggiornati.
- YouTube "best PLA 2025" (My Tech Fun, CNC Kitchen).
