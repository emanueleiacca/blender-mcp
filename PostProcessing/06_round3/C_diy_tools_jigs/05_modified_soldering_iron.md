# 05 — Saldatore moddato per heat-set (€15-30)

> Obiettivo: ottenere uno strumento dedicato heat-set spendendo
> **€15-30** invece di €120 Weller / €150 Hakko / €80 Pinecil "pulito".
> Combinazione: saldatore base cinese + punte dedicate heat-set.

Cross-ref: `05_round2/D_pipeline_industrial/01_heat_set_inserts_protocol.md` §3.2.

---

## 5.1 BOM "saldatore base + punte dedicate"

### Opzione A — Yihua 936A clone (analogo Hakko)

| Item | Source | Cost € | Note |
|---|---|---|---|
| Yihua 936A clone Aliexpress (stazione completa + manipolo + base) | Aliexpress search "yihua 936" | 20-30 | regolazione 200-480 °C, T stabile ±5 °C |
| Set 5 punte heat-set brass M2/M2.5/M3/M4/M5 | Aliexpress search "heat set insert tip" | 4-6 | filettatura standard 900M (compatibile Hakko 936/Yihua) |
| Stand metallico + spugna | spesso incluso | 0-5 | — |
| **TOTALE Opzione A** | | **€24-36** | uso pesante, durata anni |

### Opzione B — Saldatore generico 60 W kit (R2-E)

| Item | Source | Cost € | Note |
|---|---|---|---|
| Saldatore 60 W con controllo temperatura | Amazon/Aliexpress | 12-18 | T regolata ma meno stabile |
| Set 5 punte heat-set (compatibile filetto M4 standard 30W/60W) | Aliexpress | 4-6 | verifica thread punta prima di acquisto |
| **TOTALE Opzione B** | | **€16-24** | uso hobby/leggero |

### Opzione C — Pinecil V2 (premium DIY)

| Item | Source | Cost € | Note |
|---|---|---|---|
| Pinecil V2 | pine64.com | 30-35 | USB-C PD, firmware OSS |
| Alimentatore USB-C PD 65W (se non hai) | Amazon | 12-18 | — |
| Punte heat-set Pinecil-compatible | Aliexpress search "TS100 heat set" | 6-10 | thread Pinecil = TS100 |
| **TOTALE Opzione C** | | **€48-63** | portatile, precisione, hobby + lavoro |

### Opzione D — "Sub-€10 disperato"

| Item | Source | Cost € | Note |
|---|---|---|---|
| Saldatore 30W non regolato (€5 Brico) | Brico | 5 | T ~400 °C non controllata |
| Punte universali generiche | recupero o Aliexpress | 3-5 | filo rame piegato? sì, ma… |
| **TOTALE D** | | **€8-10** | **SCONSIGLIATO**: T alta = PLA brucia, decompone (R2-D §3.1) |

**Verdetto**: budget €20-30 = sweet spot. Sotto €15 si perde
controllo termico critico per qualità heat-set.

---

## 5.2 Yihua 936A — note dettagliate

Clone analogo della stazione Hakko 936 (storica). Specifiche tipiche
clone Aliexpress 2024-2025:

- **Manipolo + cavo + stand + spugna** = configurazione completa
- **Range T**: 200-480 °C
- **Manopola analogica** o digitale (clone digitale costa €5 in più)
- **Stabilità T**: ±5-10 °C dichiarata, realistici ±15 °C entro 60 sec
- **Punte compatibili**: tip thread "900M" — standard universale, punte
  heat-set "900M heat set" comuni su Aliexpress (€1/punta)
- **Garanzia**: nessuna (Aliexpress), DOA rate ~3-5%
- **Sicurezza**: spina EU/UK/US selezionabile, isolamento 220V/110V

URL: https://it.aliexpress.com/wholesale?SearchText=yihua+936a

**Calibrazione consigliata per heat-set PLA**: impostare manopola a
**220 °C indicati**, verificare con termocoppia esterna (se hai
multimetro con sonda K, €15 Aliexpress) — spesso clone legge 220 ma
reale = 200-210 °C, che è perfetto per PLA (R2-D §3.1).

---

## 5.3 Punte heat-set — descrizione

```
        ┌──────┐
        │filett│  ← filetto 900M / M4 / TS100 (compatibile con manipolo)
        │ atura│
        └──┬───┘
           │
        ━━━│━━━  ← spalla cilindrica
           │
          ┌┴┐    ← cono terminale che ENTRA nel filetto dell'inserto
          │ │     M2 punta = Ø ~1.5 mm, M5 punta = Ø ~4.5 mm
          └─┘
```

La punta heat-set è un **cono interno** che si infila DENTRO l'inserto
M3 (non sopra). Centra l'inserto e trasferisce calore al corpo ottone,
non al filetto. Il PLA fuso non aderisce alla punta (brass più caldo
del PLA fuso scorre via).

Set tipico Aliexpress: 5 punte M2/M2.5/M3/M4/M5 = €4-6 + shipping.
Search: https://it.aliexpress.com/wholesale?SearchText=heat+set+insert+tip

**Trick economy**: se hai 1 sola misura inserto (es. M3), comprane 1
sola punta (€1). Non serve set completo se non userai mai M4/M5.

---

## 5.4 Build/setup step-by-step

1. **Unbox Yihua**: controlla stand, spugna, integrità manipolo cavo.
2. **Inserisci punta heat-set M3** al posto della punta saldatura
   classica. Avvita a mano + 1/4 giro con pinza (non stringere troppo:
   rovini il filetto).
3. **Accensione**: prima accensione fai 5 min a 250 °C per "burn-in"
   della punta (evaporazione protettivo di fabbrica).
4. **Calibrazione T**: imposta 210 °C indicati. Test su pezzo scarto
   PLA — affondamento in 3-5 s = ok. Se >7 s → alza a 220. Se <2 s
   con bava → abbassa a 200.
5. **Posizione lavoro**: stand sempre orientato in modo che il manipolo
   sia raggiungibile con la mano dominante senza torsioni del polso.
6. **Spegnimento**: 30 sec di raffreddamento prima di toccare la punta
   (rischio ustione 1-2° grado).

---

## 5.5 Punte alternative DIY (se hai punta saldatore vuota)

Trick noto:
- **Vite M3 lunga**: avvitala dentro un inserto Ruthex, poi avvitala con
  l'inserto in punta saldatore vecchia svuotata. La vite trasmette calore
  all'inserto, e tu posizioni inserto sul pezzo come al solito. Pro:
  funziona. Contro: la vite si scalda anche la testa, non hai presa.
- **Filo rame Ø2 mm piegato a cono**: arrotola filo rame attorno a punta
  esistente per simulare cono interno. Trasferimento calore peggiore,
  vita corta.

**Verdetto**: punte dedicate Aliexpress €1-1.50/pz battono qualsiasi
hack. Solo per emergenza notturna senza spedizione.

---

## 5.6 Confronto soluzioni

| Soluzione | Costo | T stabile | Affidabilità lungo termine | Note |
|---|---|---|---|---|
| Saldatore €5 + filo rame | €5 | ❌ | ❌ | Solo emergenza |
| Saldatore 60W €15 + punta €1 | €16 | ⚠️ media | ⚠️ 1-2 anni | OK hobby occasionale |
| **Yihua 936A €25 + 5 punte €5** | **€30** | ✅ buona | ✅ 3-5 anni | **Sweet spot** |
| Pinecil V2 + punta | €50 | ✅ ottima | ✅ 5+ anni | Portatile, hobby+lavoro |
| Hakko FX-888D | €120 | ✅✅ ottima | ✅ 10+ anni | Tier pro |
| Weller WE1010 | €150 | ✅✅ ottima | ✅ 10+ anni | Tier pro |
| Stazione Wepoxy/Insert (heat-set dedicato) | €180-300 | ✅✅ stabile | ✅✅ industriale | Solo se >500 pz/anno |

**Verdetto utente piccolo brand** (target R2-D = 10-100 pz/lotto):
**Yihua 936A clone + 1 punta M3 = €25-30**. Vita stimata 3-5 anni con
uso settimanale. Sopra 500 pezzi/anno valutare upgrade a Hakko o
Pinecil per maggior precisione/longevità.

---

## 5.7 Riferimenti

- CNC Kitchen review tools heat-set:
  https://www.youtube.com/c/CNCKitchen
- r/PrintedCircuitBoard "yihua 936a review":
  https://www.reddit.com/r/PrintedCircuitBoard/search?q=yihua
- Pine64 Pinecil wiki:
  https://wiki.pine64.org/wiki/Pinecil
- Ruthex official tips:
  https://www.ruthex.de/en/products/threaded-insert-tip-for-soldering-iron
- Project Farm test (saldatori economici):
  https://www.youtube.com/c/ProjectFarm
