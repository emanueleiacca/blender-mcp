# 01 — Spray booth in cartone (€10-15)

> Obiettivo: ridurre overspray + catturare aerosol di primer/acrilico/sealer
> durante la spruzzatura **airbrush o bombolette piccole** nel garage o in
> uno spazio semi-chiuso. **NON sostituisce la maschera ABEK1**: i vapori
> solventi (VOC) passano attraverso filtro carbone solo in piccola parte e
> con saturazione rapida. Serve a: contenere la nebbia, proteggere pareti
> e attrezzature, abbattere particolato che si depositerebbe sui pezzi vicini.

---

## 1.1 BOM — versione "scatola Amazon"

| Item | Source | Cost € | Time to build | Alternative |
|---|---|---|---|---|
| Scatola cartone 50×40×40 cm (Amazon, IKEA reso, supermercato) | recupero | 0 | 0 | bacinella plastica IKEA TROFAST €5 |
| Ventola PC 120 mm 12V (case fan generico) | Aliexpress / recupero PC vecchio | 4-7 | 0 | ventola estrazione bagno €15 (più potente) |
| Alimentatore 12V 1-2A (caricatore vecchio router/laptop) | recupero | 0 | 0 | USB powerbank + cavo USB→DC €3 |
| Filtro carbone cappa cucina (universale tagliabile) | Brico/Leroy €3-5 | 3 | 0 | filtro G3/G4 ventilazione €3/m² Leroy |
| Tubo flessibile Ø100 mm (asciugacapelli vecchio o aspirapolvere) | recupero | 0 | 0 | tubo asciugatrice Brico €6 |
| Nastro americano / nastro carta | casa | 0 | 0 | colla a caldo €2 |
| Cutter + righello | casa | 0 | 0 | — |
| **TOTALE** | | **€7-10** | **30-45 min** | versione +tubo esterno €15 |

Versione "premium DIY" con ventola estrazione bagno + filtro doppio: **€20-25**.

---

## 1.2 Schema costruttivo (ASCII)

```
        ┌────────────────────────────────┐
        │   scatola cartone (top open)   │
        │  ┌──────────────────────────┐  │
        │  │                          │  │
        │  │   ←  zona spruzzatura    │  │
        │  │   (pezzo qui)            │  │
        │  │                          │  │
        │  │  filtro carbone────►██████│←─┤  ventola PC 120mm
        │  │  (incollato dietro)       │  │  aspira aria fuori
        │  └──────────────────────────┘  │
        │                                │
        └────────────────────────────────┘
              ↓ tubo flessibile opzionale
              ↓ verso finestra
```

Vista laterale:
```
       fronte aperto (mano + airbrush entra qui)
       ┌──┐
       │  │ ← cartone lato dx (tagliato a 30° per visibilità top)
   ┌───┘  └────────────────┐
   │  pezzo su lazy susan   │  ventola
   │  / supporto rotante    │   │  filtro carbone
   │       O                │   ▼  /
   │      ─┴─               │ ┌──┐██████
   │   tornio carteggio     │ │  │      │ → aria fuori
   └────────────────────────┘ └──┘      │
                                         ▼
                                       tubo
```

---

## 1.3 Build step-by-step (skill richiesto: principiante)

1. **Scatola**: scegli scatola Amazon grande (50×40×40 cm minimo). Apri
   completamente il top — sarà il lato osservatore. Rinforza con nastro tutti
   i bordi interni.
2. **Foro ventola**: sul retro, traccia cerchio Ø115 mm (per ventola 120 mm
   con flangia). Taglia con cutter.
3. **Fissaggio ventola**: ventola PC montata con 4 viti M3 + dadi attraverso
   il cartone (forare con punta da trapano o chiodo riscaldato). Direzione:
   **aspirante** (aria esce dalla scatola, controlla freccia stampata sulla
   ventola).
4. **Filtro carbone**: taglia un quadrato di filtro cappa cucina (tipicamente
   foglio 47×57 cm da Brico) a misura **leggermente più grande** del foro
   ventola (es. 15×15 cm). Fissalo all'**interno** della scatola con nastro
   carta, prima della ventola. L'aria sporca passa filtro → ventola → fuori.
5. **Alimentazione**: ventola PC 12V → caricatore router 12V (verifica polarità
   con multimetro, rosso = +). Connettore Molex o splice diretto. In
   alternativa, USB→DC step-up 5V→12V (€2 Aliexpress).
6. **Tubo opzionale**: se vuoi scaricare fuori dalla finestra, accoppia
   tubo asciugacapelli (Ø ~50 mm) o tubo asciugatrice (Ø100 mm) al lato
   esterno della ventola con nastro americano.
7. **Piattino rotante interno**: lazy susan IKEA SNUDDA €4-5 (anche se
   discontinued, equivalenti su Amazon €6) — permette di ruotare il pezzo
   senza interrompere lo spray.
8. **Illuminazione**: LED strip USB €3 attaccato al "tetto" della scatola
   (cartone laterale ripiegato).

---

## 1.4 Performance reale vs versione acquistata

| Parametro | DIY €10 | Booth Master Airbrush €70 | Spray booth pro €250 |
|---|---|---|---|
| Portata aria | ~40-80 m³/h (ventola 120 mm @ 1500 RPM) | 110 m³/h | 350 m³/h |
| Filtro carbone attivo | sì (filtro cappa generico) | sì (incluso) | sì + HEPA |
| Cattura overspray | ~70-80% | ~85-90% | >95% |
| Rumore | 30-40 dB | 55-60 dB | 60-65 dB |
| Volume scatola | ~80 L (utile per pezzi 3-25 cm) | ~30 L | ~100 L |
| Durata | 6-12 mesi (cartone si impregna) | anni | anni |
| **Spese** | **€10** | **€70** | **€250** |

**Verdetto**: per **airbrush acrilici diluiti** la versione DIY è
sufficiente. Per **bombolette spray classiche** (Maximum, MaxMeyer) o
**SprayMax 2K**, la cabina di cartone è insufficiente: serve estrazione
con cappa cucina recuperata (vedi `06_extraction_hood_diy.md`) o
spruzzare all'aperto con maschera.

---

## 1.5 Riferimenti video

- **Punished Props "DIY spray booth"** — costruzione cartone + ventola PC,
  uso prop maker:
  https://www.youtube.com/c/PunishedProps (search "spray booth")
- **Bigfoot Films IT** — esempi cabina spray hobby:
  https://www.youtube.com/@bigfootfilms
- **Adam Savage's Tested "spray booth tour"**:
  https://www.youtube.com/c/tested
- Reddit thread r/minipainting "DIY spray booth on a budget":
  https://www.reddit.com/r/minipainting/search?q=diy+spray+booth
- Thingiverse "spray booth":
  https://www.thingiverse.com/search?q=spray+booth

---

## 1.6 Limiti & sicurezza

- **NO solventi forti** (acetone puro, isocianati 2K): il cartone si
  impregna e diventa rischio incendio + i vapori 2K passano dal filtro
  carbone senza essere fermati. Per 2K usa garage aperto + maschera +
  cappa estrazione esterna.
- **Statica**: il movimento d'aria attraverso il filtro carbone può
  generare microcariche. Non spruzzare materiali pirofori (raro
  nell'hobby).
- **Igiene filtro**: sostituire ogni 5-10 sessioni o quando l'odore
  trapassa (carbone saturo).
- **NON usare al chiuso senza maschera**: la ventola sposta l'aria ma
  l'aria che esce è ancora contaminata. La maschera ABEK1 (R2-E PPE)
  rimane obbligatoria.
