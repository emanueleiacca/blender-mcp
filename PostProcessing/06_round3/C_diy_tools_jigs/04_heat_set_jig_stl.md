# 04 — Jig per heat-set inserts: STL + parametri (€0.15/stampa)

> Obiettivo: ridurre il **failure rate "inserto storto"** dal ~20% del
> protocollo manuale al **3-5%** target R2-D. Il jig vincola la punta del
> saldatore perpendicolare al pezzo. Stampa in **PETG** (PLA si rammollisce
> vicino alla punta calda).

Cross-ref: `05_round2/D_pipeline_industrial/01_heat_set_inserts_protocol.md` §3.4.

---

## 4.1 BOM

| Item | Source | Cost € | Time to build | Alternative |
|---|---|---|---|---|
| 5-10 g filamento PETG | bobina esistente | 0.15-0.30 | 30-60 min stampa | PLA+ se hai fretta (dura meno) |
| Tempo CAD/slicer | 15 min (parametri sotto) | 0 | — | scaricare STL Printables free |
| Calibro 0.1 mm (per misure post-stampa) | Aliexpress/Brico | 5-8 (una tantum) | 0 | regolo + occhio (peggio) |
| **TOTALE per jig** | | **€0.15** | **45-75 min** | — |

**Alternativa zero-stampa**: trapano a colonna manuale recuperato
(mercatino dell'usato €20-40) usato come guida verticale per saldatore —
vedi §4.5.

---

## 4.2 Geometria del jig (descrizione)

**Concept**: cilindro forato che si appoggia attorno al boss del pezzo
e ha un foro guida concentrico in cui scorre la punta del saldatore.
Mantiene la punta perpendicolare durante i 3-5 secondi di pressione.

### Parametri base — versione M3 Ruthex (R2-D §1.2)

```
       ┌───┐  ← foro superiore Ø 6.5 mm (passaggio punta saldatore + maniglia)
       │   │
       │   │  ← altezza guida 15 mm (= 2.5× L_inserto, sufficiente per centramento)
       │   │
       └─┬─┘
         │
       ┌─┴─┐  ← foro inferiore Ø 4.0 mm (= OD min Ruthex M3, scende sul boss del pezzo)
       │ I │  ← I = inserto M3 (OD zigrinatura 4.6, OD corpo 4.0)
       │ I │
       └───┘
         ▼
       pezzo PLA con foro Ø 4.0 (R2-D § datasheet)

OD esterno cilindro: 14 mm (mano-presa comoda + parete 5 mm)
H totale: 15 mm
```

### Tabella parametri per misura inserto

| Inserto | OD min datasheet (foro pezzo) | Foro inferiore jig | Foro superiore jig | H jig | OD esterno jig |
|---|---|---|---|---|---|
| **M2** | 3.2 mm | 3.2 mm | 5.5 mm | 12 mm | 12 mm |
| **M2.5** | 3.6 mm | 3.6 mm | 6.0 mm | 14 mm | 13 mm |
| **M3** | 4.0 mm | 4.0 mm | 6.5 mm | 15 mm | 14 mm |
| **M4** | 5.6 mm | 5.6 mm | 8.5 mm | 18 mm | 17 mm |
| **M5** | 6.4 mm | 6.4 mm | 9.5 mm | 20 mm | 19 mm |

**Tolleranze**: lascia +0.05 mm sul foro inferiore (per fit pezzo senza
sforzo) e -0.1 mm sul foro superiore (la punta saldatore reale può
essere conica, deve scorrere ma con minimo gioco).

---

## 4.3 OpenSCAD parametrico (copy-paste)

```scad
// Heat-set insert jig — parametrico
// Cross-ref: PostProcessing/06_round3/C_diy_tools_jigs/04_heat_set_jig_stl.md

// === PARAMETRI ===
hole_bottom = 4.0;      // = OD min datasheet (Ruthex M3 = 4.0)
hole_top    = 6.5;      // = diametro punta saldatore + clearance 0.5 mm
height      = 15;       // = ~2.5 × L_inserto, M3 → 15 mm
od_outer    = 14;       // = hole_top + parete 4 mm × 2 (presa con dita)
wall_floor  = 0;        // 0 = passante (preferibile per QC visivo)
chamfer_top = 1.0;      // facilita ingresso punta
// =================

$fn = 64;

difference() {
    // corpo esterno
    cylinder(d=od_outer, h=height);
    
    // foro guida (svasato)
    union() {
        cylinder(d=hole_bottom, h=height/2);
        translate([0, 0, height/2])
            cylinder(d=hole_top, h=height/2 + 0.1);
        // chamfer top
        translate([0, 0, height - chamfer_top])
            cylinder(d1=hole_top, d2=hole_top + 2*chamfer_top, h=chamfer_top + 0.1);
    }
}
```

Stampa: PETG, 0.2 mm layer, 4 wall, 30% infill, no support.

---

## 4.4 Bambu Studio settings consigliati

- **Filamento**: PETG generic (Esun, Sunlu, Overture). PLA si deforma a
  ~60 °C — la punta calda a 210 °C trasferisce calore al jig per
  contatto + radiazione. PETG Tg ~80 °C resiste 20-30 sessioni prima di
  ammorbidimento visibile.
- **Layer**: 0.20 mm.
- **Wall**: 4 perimetri (mura interne fori critiche per tolleranza).
- **Top/bottom**: 5 layer.
- **Infill**: 30% gyroid.
- **Orientamento**: asse del foro **verticale** (perpendicolare al
  build plate). Fori cilindrici stampati verticalmente sono più tondi.
- **No support**: i fori sono passanti, ponti < 6 mm OK.

**Time-to-print**: 30-45 min per jig M3 su Bambu A1.

---

## 4.5 Alternativa zero-stampa: trapano a colonna recuperato

Se non hai stampante calibrata o sei in attesa di filamento:

1. **Trapano a colonna manuale** (drill press) — mercatino dell'usato
   €15-35, oppure Brico (modelli da banco €60-90).
2. Sostituisci la punta nel mandrino con la **punta saldatore** (NO,
   meglio: fissa il **saldatore intero** al mandrino con fascette o
   collare di plastica stampata).
3. **Disattiva il motore** del trapano. Usa solo il **carrello
   verticale** come guida. La leva del trapano spinge la punta giù in
   modo perfettamente perpendicolare.
4. Pezzo posato sul **piano del trapano** (orientato in modo che il foro
   sia verticale).
5. Pre-heat saldatore 30 s, scendi con la leva, 3-5 s pressione, sali.

**Trick noto** dalla community r/functionalprint:
https://www.reddit.com/r/functionalprint/search?q=heat+set+drill+press

Pro: zero stampa, riusabile per inserti di tutte le misure.
Contro: serve trapano a colonna disponibile.

---

## 4.6 Confronto failure rate (R2-D §3.4)

| Setup | Failure rate "inserto storto >5°" |
|---|---|
| Mano libera, no jig | **~15-20%** |
| Jig stampato PETG dedicato | **~3-5%** |
| Trapano a colonna disattivato | **~2-4%** |
| Macchina pneumatica industriale | **<1%** |

**Throughput su lotto 100 pezzi**:
- Senza jig: 15-20 pezzi da rilavorare → +30 min lavoro + scarti.
- Con jig DIY: 3-5 pezzi → +5 min lavoro.

ROI jig: stampi 1 volta (0.15 €), risparmi 25 min/100 pezzi.

---

## 4.7 Pre-fatti scaricabili (Printables / Thingiverse / MakerWorld)

Search term consigliati (al 2025):
- **Printables**: https://www.printables.com/search/models?q=heat+set+insert+jig
- **Thingiverse**: https://www.thingiverse.com/search?q=heat+set+jig
- **MakerWorld**: https://makerworld.com/en/search?keyword=heat%20set%20jig

Modelli noti / popolari (verifica esistenza + licenza prima di
scaricare; URL stabili tipiche del 2024 ma possono cambiare):
- "Heat Set Insert Soldering Tool" — multi-size jig parametrico:
  https://www.printables.com/search/models?q=heat+set+insert+soldering
- "CNC Kitchen heat set jig":
  https://www.printables.com/search/models?q=cnc+kitchen+heat+set
- "Ruthex insert holder/jig":
  https://www.ruthex.de/en (download dal sito Ruthex)

Licenza: tipicamente CC-BY-NC (uso personale e maker, NO rivendita STL).

---

## 4.8 Variant: jig per multi-thread

Per chi ha pezzi con 4 inserti M3 in pattern fisso (es. piastra montaggio
con 4 vite agli angoli):
- **Jig multi-foro**: cilindri guida concentrici × 4, distanziati come da
  CAD del pezzo. Pesa 10-15 g PETG (€0.30-0.45). Riduce ulteriormente il
  tempo (4 inserti in 1 setup invece di 4 setup).
- Da progettare al volo in OpenSCAD modificando il punto di traslazione
  dei cilindri.

---

## 4.9 Limiti e usi sbagliati

- **Pezzi con foro inclinato**: il jig assume foro verticale. Per pezzi
  con inserto angolato, ruota il pezzo nello slicer in modo che il foro
  sia verticale durante l'heat-set (non durante la stampa).
- **PLA come materiale jig**: dopo 3-5 inserzioni il PLA inizia a
  rammollirsi a contatto con il calore residuo del saldatore (la punta
  a 210 °C scalda il jig). Sostituire ogni sessione con PETG/ABS.
- **Inserti micro M1.6**: tolleranze foro 0.05 mm difficili in FDM.
  Considerare risiera SLA per jig di precisione.
