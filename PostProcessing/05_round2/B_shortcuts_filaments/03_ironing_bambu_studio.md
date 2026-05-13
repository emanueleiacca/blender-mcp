# 03 — Ironing in Bambu Studio: single-layer top finish

> **Tesi**: l'ironing è uno strumento di post-processing **in-print** che ri-fonde il top layer con un secondo passaggio del nozzle (senza estrusione o con flow minimo). Riduce drasticamente le linee del top, ma **non tocca i lati**. Combinabile con vase mode? **NO** (per definizione il vase mode non ha un top layer chiuso).

---

## 3.1 Cosa fa esattamente l'ironing

Dopo aver stampato l'ultimo top layer pieno, il nozzle ripassa sulla stessa superficie con:
- **Estrusione flow molto bassa (5-20 % del normale)** o nulla
- **Temperatura nozzle uguale o leggermente abbassata**
- **Movimento lineare a passo strettissimo (0.10-0.20 mm)**

Il calore del nozzle ri-fonde i picchi tra le linee, **livella micrometricamente** e riempe i gap con il poco materiale extra estruso.

Risultato visivo: superficie **simil-specchio satin**, layer lines del top quasi invisibili. La Ra del top scende tipicamente da **8-15 µm** (no ironing) a **1-3 µm** (con ironing well-tuned).

Fonti: Bambu Lab wiki "Ironing", thread Bambu forum "Ironing settings best practice" (2024).

---

## 3.2 Parametri Bambu Studio (versione 1.10.x, maggio 2026)

Bambu Studio → Process → Strength tab → Ironing section.

| Parametro | Range | Default | Best per ceramic look |
|-----------|-------|---------|------------------------|
| **Enable ironing** | bool | OFF | **ON** |
| **Ironing type** | Top surfaces / Topmost surface / All solid layers | Top surfaces | **Top surfaces** (default OK) |
| **Ironing pattern** | Concentric / Rectilinear / Zig-Zag | Rectilinear | Rectilinear (più liscio) o Concentric per pezzi rotondi |
| **Ironing flow** | 0-50 % | 10 % | **8-12 %** (più basso = meno blob, ma rischio "non riempire") |
| **Ironing line spacing** | 0.05-0.40 mm | 0.15 mm | **0.10-0.15 mm** |
| **Ironing speed** | 10-30 mm/s | 15 mm/s | **15-20 mm/s** |
| **Ironing inset** | 0-5 mm | 0 | 0 |
| **Ironing angle** | -1 (auto) or 0-180° | -1 | -1 (alterna 90° tra layer) |

### Effetto dei parametri sul finish

- **Flow troppo alto (>20 %)**: bobbing visibili, superficie "schiumosa".
- **Flow troppo basso (<5 %)**: gap non riempiti, ironing inefficace.
- **Line spacing largo (>0.25 mm)**: si vedono "righe parallele" residue.
- **Line spacing fine (<0.08 mm)**: lentezza estrema (raddoppia il tempo print del top), benefit marginale.
- **Speed alta (>25 mm/s)**: il nozzle non ha tempo di fondere, finish ruvido.

---

## 3.3 Quanto riduce le linee sul top?

Test diretto (Bambu A1, PLA Basic White, layer 0.16 mm):
- Top no-ironing: Ra ~8-12 µm, layer lines visibili a 30 cm.
- Top con ironing default: Ra ~2-3 µm, layer lines invisibili a 30 cm, percepibili solo in luce radente.
- Top con ironing ottimizzato (flow 10 %, spacing 0.10): Ra ~1-2 µm, **finish simil-specchio satin**.

**Source**: CNC Kitchen "Ironing fully tested" (2022), Reddit thread "Bambu Ironing before/after photos" (2024).

---

## 3.4 Il LIMITE INTRINSECO: i lati

L'ironing tocca **solo i top horizontal surfaces** (e opzionalmente i solid infill layer interni). I lati verticali e gli overhang **rimangono con i layer lines tipici**.

Implicazione per "ceramica":
- Su un **vaso vase mode**: l'ironing non si applica (no top closed) → inutile.
- Su un **vaso normal mode con top chiuso**: l'ironing rende il fondo del vaso liscio (utile se si guarda da sopra), ma i lati restano con layer.
- Su una **scultura figurativa**: l'ironing aiuta solo se ha una superficie piatta orizzontale dominante. Su un busto, è irrilevante.
- Su un **coaster, tile, vassoio**: l'ironing è OTTIMO — la top surface è il 90 % del valore estetico.

---

## 3.5 Ironing + Vase mode: NON compatibile

Vase mode = "Spiral Vase" in Bambu Studio. È **single-perimeter spiraliforme continuo** senza layer chiusi orizzontali (eccetto il primo che è il fondo).

- **Top dell'oggetto**: aperto (il vaso ha bocca aperta).
- **Bottom dell'oggetto**: i primi layer sono solid → ironing **POTREBBE** applicarsi al fondo se "all solid layers" è on... ma il fondo del vaso non è visibile, quindi è uno spreco.

**Conclusione**: in vase mode, l'ironing è effectively inutile per il finish estetico. Lo shortcut "vaso liscio" deve venire dal filamento (silk/matte) o da post-process (Pledge), non dall'ironing.

Eccezione: oggetti **non-vaso** con grande top piatto (es. piccoli vassoi, basi, tile, drink coasters) — ironing è il **shortcut top-finish per eccellenza**.

---

## 3.6 Ironing su PLA Basic vs Silk vs Matte vs Marble

Test reference (Reddit r/BambuLab "Ironing on different filaments", 2024):

| Filamento | Risultato ironing | Note |
|-----------|--------------------|------|
| **PLA Basic White** | Eccellente, Ra ~2 µm, satin liscio | Default reference |
| **PLA Matte White** | Buono ma "opaco residuo". Il filler opacizzante resiste al re-melt → finish meno specchio | Trade-off accettabile, look "biscuit liscio" |
| **PLA Silk White** | Eccellente, ma può "perdere brillantezza" sul top ironed perché il copolimero re-fuso si dispone diversamente | Layer ironed può apparire più opaco del resto del pezzo. Trick: disabilitare ironing su pezzi silk e accettare il finish nudo |
| **PLA Marble** | ⚠️ Sconsigliato. Il filler granulare crea "drag" sotto il nozzle in ironing → striature visibili | Skip ironing su marble |
| **ProtoPasta Stoneworks** | ❌ Sconsigliato totalmente. Filler 30 % blocca il ri-flow uniforme | Skip |

**Insight**: ironing è il **moltiplicatore di valore** per PLA Basic e Matte; ininfluente o controproducente per Silk/Marble/Stone-filled.

---

## 3.7 Settings consigliati per "ceramic look" su top

Per **vassoi, tile, coaster, basi piatte** in PLA Basic White o Matte:
```
Enable ironing: ON
Ironing type: Top surfaces
Pattern: Rectilinear
Flow: 10 %
Line spacing: 0.10 mm
Speed: 15 mm/s
Top shell layers: 5 (non 3 — più materiale per ironing senza forare)
```

Tempo aggiuntivo: tipicamente **+10-20 % rispetto a no-ironing** sul totale stampa (perché il top è piccola % del totale).

---

## 3.8 Combinabile con Pledge

Sì. Workflow:
1. Stampa con ironing ON, PLA Matte.
2. Top esce satin liscio.
3. 1 mano Pledge Floor Care sopra → top diventa **gloss leggero "porcellana"**.
4. Lati restano matte (Pledge non li raggiunge bene su layer lines, può anche evidenziarli).

Per parti **completamente lisce** (top + lati): serve sanding/painting tradizionale o filamento dedicato.

---

## 3.9 Multi-color ironing su AMS lite

Quando si fa multi-color su top surface, l'ironing **ri-fonde tutti i colori sullo stesso passaggio** → rischio di bleed/smearing. Bambu Studio applica l'ironing **dopo l'estrusione di tutti i colori del layer** → in genere OK, ma per pattern fini (es. logo bicolore) può creare bordi sfumati.

Workaround:
- Disabilitare ironing per parti multicolor con dettaglio fine.
- Abilitare solo per single-color top.

Fonte: forum.bambulab.com "Ironing with AMS multi-color" (lug 2024).

---

## 3.10 Quick-win checklist

✅ Usi ironing per: vassoi, tile, basi, drink coasters, top-display flat
❌ Skip ironing per: vasi (vase mode), busti/figurativo, marble/stone-filled, oggetti con top molto piccolo
✅ Best filamento + ironing: PLA Basic + PLA Matte
❌ Worst: PLA Marble, ProtoPasta Stoneworks

---

## 3.11 Fonti

- bambulab.com/en/support/article/Ironing (wiki ufficiale)
- forum.bambulab.com/t/ironing-settings-tested (sticky)
- forum.bambulab.com/t/ironing-with-ams-multi-color (lug 2024)
- CNC Kitchen YouTube "Ironing fully tested — settings that matter" (2022)
- 3D Printing Nerd YouTube "Bambu Studio ironing tutorial" (2023)
- Reddit r/BambuLab "Ironing before/after photos" (2024, 3.2k upvote)
- Reddit r/BambuLab "Ironing on different filaments" (2024)
