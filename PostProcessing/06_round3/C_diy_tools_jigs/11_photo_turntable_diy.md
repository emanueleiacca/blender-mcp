# 11 — Photo turntable DIY per video 360° (€0-5)

> Obiettivo: ottenere foto/video 360° del prodotto per **Etsy listing
> dinamico** e **Instagram reel** senza pagare €25 turntable Aliexpress.

---

## 11.1 Tre approcci

| Approccio | Costo | Velocità rotazione | Note |
|---|---|---|---|
| **A — Lazy susan IKEA SNUDDA / generic manuale** | €5 | manuale (qualsiasi velocità) | semplice, affidabile |
| **B — Motore microonde rotante recuperato** | €0 | 3-6 RPM (lentissimo, perfetto per 360° smooth) | richiede demolizione microonde + cablaggio |
| **C — Disco vinile vecchio + grammofono** | €0 (se hai grammofono) | 33⅓ o 45 RPM | troppo veloce per video, ok per "stop motion" 24 fps |
| **D — Motore stepper + Arduino/ESP32** | €15 | programmabile | per chi sa Arduino, qualità top |

---

## 11.2 A — Lazy susan manuale (raccomandato base)

### BOM

| Item | Source | Cost € | Note |
|---|---|---|---|
| Lazy susan IKEA SNUDDA Ø39 cm (discontinued, equivalenti) | IKEA Snudda / SNUDDA / VARIERA o Amazon | 5-8 | piatto rotante con cuscinetti |
| Disco MDF/legno Ø30 cm (se Lazy susan piccola) | Brico, recupero | 0-3 | fondo solido per stabilità |
| Carta nera/bianca rotonda (sfondo) | cartoleria | 1 | per uniformità foto |
| **TOTALE A** | | **€5-10** | |

### Procedura

1. Posiziona Lazy susan al centro del light box (vedi
   `03_light_box_cardboard.md`).
2. Pezzo sopra il piatto.
3. Smartphone su tripod o pila libri puntato dritto.
4. **Foto stop-motion 360°**: scatta foto, ruota di 30° (12 foto totali),
   ripeti. Combina in GIF con app gratis (Photoshop Express, EZGIF.com).
5. **Video continuo**: avvia registrazione, ruota a mano a velocità
   costante per ~10-15 secondi (un giro). Buona se hai mano stabile.

### Vantaggi

- Zero elettronica.
- Affidabilità eterna.
- Riusabile per molti scopi (foto, spruzzo, painting).

### Limiti

- Velocità non costante → video "scatta" se mano trema.
- Per video Instagram/TikTok di qualità servono ~20-30 sec smooth.

---

## 11.3 B — Motore microonde rotante (zero spesa hardcore)

> **AVVISO**: la demolizione microonde è **pericolosa** se NON sai cosa
> stai facendo. Il **capacitore alta tensione** (~2000 V) può rimanere
> carico settimane dopo lo scollegamento e provocare folgorazione
> mortale. **Far scaricare il capacitore con cortocircuito tramite
> cacciavite isolato** prima di toccare anything. Se non sai, non farlo.
> Consulta tutorial AvE o cerca corso elettronica base.

### BOM

| Item | Source | Cost € | Note |
|---|---|---|---|
| Microonde rotto/dismesso | recupero RAEE, Subito.it gratis | 0 | per il **motore piatto rotante** (5/6/8 RPM tipico) |
| Disco MDF Ø25-30 cm | Brico, recupero | 0-3 | piano di rotazione |
| Cavo + spina + interruttore | recupero / Brico | 2-5 | wiring motore |
| Scatola legno/cartone base | recupero | 0 | enclosure |
| **TOTALE B** | | **€2-8** | |

### Identificazione motore

Il motore microonde "synchronous turntable motor" è:
- Marcatura tipica: "Synchron motor 220-240V, 4-6 RPM, 3-4 W"
- Posizionato sotto il piatto del microonde, accessibile aprendo
  pannello inferiore.
- Wiring: 2 fili 220V (no controllo velocità, gira sempre alla stessa
  RPM nominale).

### Procedura

1. **Scollega microonde dalla rete almeno 1 settimana prima** (per
   scarica capacitore).
2. **Apri** pannello inferiore (no quello dell'alta tensione!). Trova
   motore piatto rotante.
3. **Identifica i 2 fili 220V** del motore (escludi il cablaggio del
   magnetron e dell'alta tensione).
4. Cortocircuita capacitore con cacciavite isolato (tocco fra i 2
   terminali del capacitor con resistenza 10k Ω in serie se preferisci
   metodo sicuro).
5. **Smonta** solo il motore piatto + driver shaft.
6. Cabla il motore a spina 220V + interruttore.
7. Monta disco MDF sull'asse driver.
8. Test su banco prima di usare per foto.

### Vantaggi

- Rotazione **3-6 RPM perfetta** per video 360° smooth.
- Costo zero se microonde disponibile.
- Estetica "maker hack" interessante per documentare brand.

### Sicurezza

- **Mai** lavorare microonde da accesa.
- **Scaricare** capacitore alta tensione.
- **Differenziale** salvavita 30 mA obbligatorio sulla presa.
- Se incerto: chiama elettricista o usa opzione A.

---

## 11.4 C — Disco vinile + grammofono

Solo se hai grammofono vecchio in cantina:
- 33⅓ RPM: troppo veloce per video smooth (1 giro / 1.8 sec).
- 45 RPM: idem.
- 78 RPM: troppo veloce.
- **Utile solo per**: stop-motion (foto 1 ogni N rotazioni) o effetti
  speciali video con motion blur.

---

## 11.5 D — Motore stepper + Arduino (premium DIY)

Per chi conosce Arduino:

| Item | Source | Cost € | Note |
|---|---|---|---|
| Stepper NEMA17 + driver A4988 | Aliexpress | 8-12 | 200 step/giro, controllo preciso |
| Arduino Nano clone | Aliexpress | 3-5 | — |
| Alimentatore 12V 1A | recupero / Aliexpress | 2-5 | — |
| Pulsantiera + display OLED 0.96" (opz) | Aliexpress | 3-5 | per controllo RPM |
| Disco MDF + cuscinetti | recupero | 0-5 | — |
| **TOTALE D** | | **€16-32** | |

Codice Arduino: ~20 righe per rotazione velocità variabile.

---

## 11.6 Workflow foto 360° Etsy/Instagram

### Setup

```
   ┌────────────────────────────────────┐
   │  Light box DIY                     │
   │  (file 03_light_box_cardboard.md)  │
   │                                    │
   │     ◢◣ LED diffuser sopra          │
   │     ░░░                            │
   │  pezzo                             │
   │   ▓▓▓                              │
   │  ─────                             │
   │   ────  ← lazy susan / turntable   │
   │                                    │
   │ smartphone tripod                  │
   │       ───►📷                       │
   └────────────────────────────────────┘
```

### Procedura video 360°

1. **Pezzo centrato** sul turntable (segna centro con croce removibile).
2. **Smartphone fisso** su tripod, distanza 30-50 cm dal pezzo,
   inquadratura include intero pezzo + 5 cm di margine.
3. **Registrazione 1080p 60 fps** (smartphone moderno).
4. **Avvia motore** (opzione B) o **inizia rotazione manuale costante**
   (opzione A).
5. **Tempo target**: 10-15 secondi per 1 giro completo = perfetto per
   reel Instagram, story TikTok.

### Post-prod gratis

- **CapCut** (gratis): trim + speed + transizione.
- **Davinci Resolve** (gratis, desktop): color grade + audio.
- **InShot Pro** trial (gratis 7gg): mobile editing veloce.

---

## 11.7 Conversion rate impact (R2-D)

Stime industria e-commerce:
- Listing solo foto statiche: baseline.
- Listing con 1 video 360° smooth: **+20-40% conversion** (Etsy
  internal data per "video shop section").
- Listing con 6 foto + 1 video 360°: **+35-60% conversion** (multi-sensory).

ROI turntable DIY €5: paga in **1-2 ordini** addizionali ai prezzi
medi €30-50.

---

## 11.8 Riferimenti

- AvE YouTube "microwave teardown":
  https://www.youtube.com/@arduinoversusevil2025
- ElectroBOOM YouTube (capacitore safety):
  https://www.youtube.com/@ElectroBOOM
- Adam Savage "DIY turntable":
  https://www.tested.com (search turntable)
- r/3Dprinting "turntable photo":
  https://www.reddit.com/r/3Dprinting/search?q=turntable+photo
- Printables "photo turntable" search:
  https://www.printables.com/search/models?q=photo+turntable
- Etsy listing video guidance:
  https://help.etsy.com (search "listing videos")
