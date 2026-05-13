# 08 — Polishing wheel DIY con Dremel/trapano (€15-25)

> Obiettivo: lucidare clear coat (Pledge / Mr. Super Clear) o **resin-
> -less smoothing** del PLA carteggiato fino a 2000-3000 grit, ottenendo
> riflessione speculare senza pagare Tamiya Polishing Compound + tampone
> dedicato.

---

## 8.1 BOM

### Versione A — Dremel clone €15-25

| Item | Source | Cost € | Note |
|---|---|---|---|
| Dremel clone Aliexpress / Lidl Parkside rotary tool | Aliexpress, Lidl | 15-25 | 12V o 220V, regolazione velocità |
| Set ruote feltro Ø20-30 mm con gambo M2.3 (universal Dremel) | Aliexpress / Brico | 2-5 / set 10 pz | — |
| Compound abrasivi (dentifricio o Tamiya) | casa / hobby shop | 0-5 | dentifricio bianco classico (no gel) |
| Panno cotone vecchio + acqua | recupero | 0 | per pulire residui |
| **TOTALE A** | | **€17-30** | |

### Versione B — Trapano economico €20

| Item | Source | Cost € | Note |
|---|---|---|---|
| Trapano economico Brico/Lidl 220V | Brico | 20-35 | con regolatore velocità preferibile |
| Adattatore mandrino → gambo Dremel M2.3 | Aliexpress / Brico | 3-5 | "drill chuck adapter dremel" |
| Set ruote feltro | come sopra | 2-5 | — |
| **TOTALE B** | | **€25-45** | bassa velocità più difficile (trapani non sempre regolano sotto 1000 RPM) |

### Versione C — Mototool USB / Mini cordless €10

| Item | Source | Cost € | Note |
|---|---|---|---|
| Mini grinder USB 5V (Aliexpress) | Aliexpress | 8-15 | bassa potenza, ok per PLA |
| Powerbank o caricatore USB 2A | casa | 0-5 | — |
| Punte/ruote feltro | come sopra | 2-5 | — |
| **TOTALE C** | | **€10-25** | sweet spot economy |

---

## 8.2 Tecnica polishing PLA + clear coat

### Setup

- **Velocità target**: **1000-2000 RPM** per PLA. Sopra 3000 RPM = PLA
  fonde localmente (Tg 60 °C facilmente superato per attrito).
- Dremel clone tipicamente regola 5000-35000 RPM → usa **velocità
  minima** o monta dimmer.
- Trapano regolato + tampone feltro → spesso ~1500-2000 RPM con
  pressione leggera.

### Compound

| Compound | Source | €/100g | Note |
|---|---|---|---|
| **Dentifricio bianco classico** (no whitening gel) | supermercato | €1 / tubo 75 ml | abrasivi micronizzati (silica), ottimo per PLA |
| **Bicarbonato + acqua** (pasta) | supermercato | €0.50 / kg | abrasivo medio, attenzione a graffi |
| **Tamiya Polishing Compound fine** | hobby shop | €8 / 22 ml | dedicato ma costoso |
| **3M Compound restauro auto** | Brico | €15 / 250 ml | per finish auto-grade |
| **Bicarbonato + dentifricio mix** | casa | €0.50 | DIY hack tested r/minipainting |

### Procedura

1. **Pre-lucidatura**: carta vetrata wet 1500 → 2000 → 3000 grit
   (R2-E step). Mai saltare al polish direttamente: graffia.
2. **Applica compound** sul pezzo o sulla ruota feltro (NON la
   testa Dremel: spruzza via).
3. **Polish a bassa velocità** con passate brevi (2-3 s zona piccola),
   movimento continuo (no fermo statico = brucia PLA).
4. **Controlla ogni 5 passate**: pulisci compound con panno umido, vedi
   se hai raggiunto lucidatura target.
5. **Rifinitura ultima**: panno cotone asciutto (microfibra) a mano,
   no Dremel.

### Failure mode da evitare

- **Bruciatura PLA**: traccia bianca/opaca dove la ruota si è fermata.
  Recuperabile solo con re-sand 800→2000. Prevenzione: muovi sempre.
- **Riscaldamento clear coat**: Pledge soft anche dopo cura completa.
  Polishing a Tg PLA 60 °C = clear si rammollisce. Prevenzione: sessioni
  brevi, pezzo a temperatura ambiente.
- **Compound annidato in crepe/dettagli**: dentifricio bianco residuo
  visibile. Pulizia con IPA + cotton swab.

---

## 8.3 Confronto risultato

| Setup | Costo | Riflessione speculare (1-10) | Note |
|---|---|---|---|
| Solo carta vetrata 3000 + manuale | €5 | 5/10 | finitura satinata |
| **Dremel clone + ruota feltro + dentifricio** | **€20** | **7-8/10** | sweet spot DIY |
| Dremel clone + Tamiya Polishing | €30 | 8-9/10 | quasi-mirror |
| Tornio lucidatura industriale | €200+ | 9-10/10 | mirror auto-grade |
| Servizio lucidatura pro auto | €30-50/pezzo | 10/10 | per show piece |

---

## 8.4 Caso d'uso: lucidatura post-Pledge

Workflow integrato con R2-E (Pledge clear coat €0.03/pezzo):

1. Spray/pennella Pledge come al solito (1-2 mani).
2. Cura **24 h minimo** (Pledge è soft fino a cura completa).
3. Carta vetrata wet 2000 grit → 3000 grit (rimuove dust/peel).
4. Polish Dremel + ruota feltro + dentifricio (1-2 min / pezzo piccolo).
5. Panno microfibra pulisci.

Risultato: aspetto **vernice automotive 2K** a costo €0.05/pezzo
incrementale (compound + ammortamento Dremel).

---

## 8.5 Riferimenti

- **Project Farm** comparison polish compound:
  https://www.youtube.com/c/ProjectFarm
- r/minipainting "polish PLA":
  https://www.reddit.com/r/minipainting/search?q=polish+pla
- r/3Dprinting "polishing wheel dremel":
  https://www.reddit.com/r/3Dprinting/search?q=polishing+dremel
- AvE YouTube engineering hack rotary tools:
  https://www.youtube.com/@arduinoversusevil2025
- DIY Cosplay polish prop YouTube Punished Props:
  https://www.youtube.com/c/PunishedProps

---

## 8.6 Limiti

- **NO PLA su pezzi piccoli flessibili**: si deformano sotto pressione
  ruota. Usa polish a mano.
- **NO compound diamond/heavy duty**: per PLA basterebbe 0.5-3 μm,
  diamond paste 6+ μm graffia visibilmente.
- **Velocità non regolabile** = il trapano economico Brico senza
  regolatore non è adatto. Compra dimmer €5 in linea (220V) o spendi
  €5 in più per modello regolato.
- **Dremel originale Bosch** (€80-120): durata vita 10× clone Aliexpress,
  ma per uso hobby max 50 pezzi/mese il clone è sufficiente.
