# 05 — Heat-set inserts + Packaging commerciale

Due cluster operativi importanti per **uso commerciale piccolo-batch**:
1. Inserti filettati a caldo (per montaggio robusto pezzi PLA)
2. Packaging per spedizioni e brand identity

> Prezzi 2025-2026 — **verifica al momento dell'acquisto**.

---

## A. Heat-set inserts (inserti filettati a caldo)

### A.1 Brand di riferimento

| Brand | Origine | Punto forte | Dove (IT) |
|-------|---------|-------------|-----------|
| **Ruthex** | DE | Standard EU, dimensioni metriche complete, kit + saldatore | Ruthex direct, Amazon.it |
| **CNC Kitchen** | DE / USA partner | Promosso da Stefan canale YT, formato Voron-style | tindie, Amazon, Aliexpress (cloni) |
| **TriCorpScrew** | UK | Pro, prezzi volume | tricorpscrew.co.uk |
| **Generici Aliexpress** | CN | Economici, qualità variabile | Aliexpress |
| **Bossard / EJOT** | DE | Pro industriale | RS Components, ferramenta pro |

### A.2 Prezzi orientativi

| Prodotto | Quantità | €IT |
|----------|----------|-----|
| **Ruthex M3** set 100 pz | 100 | €15-22 |
| **Ruthex M3 + M4 + M5** kit assortito | 200-300 pz | €30-45 |
| **Ruthex saldatore + punte M3/M4/M5** kit | 1 | €40-60 |
| **CNC Kitchen M3 inserts** | 100 | $20-30 + ship |
| **Aliexpress generic M3 brass** | 100 | €5-10 — qualità lotteria |
| **Bossard inserts M3 pro** | 100 | €25-40 |

### A.3 Saldatori adatti

Servono saldatori a **temperatura controllata** (per PLA: 200-220 °C tipico, mai oltre 240 °C).

| Modello | Range | €IT | Note |
|---------|-------|-----|------|
| **Pinecil V2** (Pine64) | 100-400 °C | €45-55 + tip | Open-source, USB-PD, ottimo Q/P |
| **TS80P / TS101** (Miniware) | 100-400 °C | €70-90 | Compatto, USB-C |
| **Hakko FX-888D** | 200-480 °C | €110-140 | Stazione classica |
| **JBC CD-2BE** | pro | €400+ | Solo se uso intensivo |
| **Stannol generic** | display | €30-60 | Variabile |
| **Aliexpress T12 station** | 200-450 °C | €40-80 | Buono Q/P, hackable |

**Punte dedicate heat-set**:
- Ruthex fornisce kit punte dedicate (M3/M4/M5) per il suo saldatore.
- Pinecil/TS80P: stampare adattatore o usare punta conica fine e tenerla flat sull'inserto.

### A.4 Protocollo PLA (gap KB round 1)

- Foro stampato: **0.05-0.1 mm sotto OD inserto** (es. Ruthex M3 OD 4.6 mm → foro 4.5 mm).
- Depth: **almeno 1.5× altezza inserto** (consente PLA spostato di alloggiarsi).
- Temperatura saldatore: **210-220 °C** (PLA fonde ~165 °C ma serve margine per inserto freddo).
- Pressione: **leggera e verticale**, lasciare che la fusione faccia il lavoro.
- Tempo: **3-6 secondi**, inserto deve essere flush o leggermente sotto la superficie.
- Raffreddamento: **non avvitare M3 per 1-2 minuti** dopo inserzione.

> Approfondimento dedicato in cartella separata round 3 candidata.

---

## B. Packaging commerciale piccolo-batch

### B.1 Scenari tipici

1. **Spedizione singolo pezzo €10-50** → scatola cartone semplice + pluriball + label.
2. **Pezzo premium €50-200** → scatola brandizzata + tissue paper + insert riciclato + nameplate.
3. **Kit / multi-pezzo** → scatola maggiorata + divisori in cartone fustellato.

### B.2 Fornitori — confronto

| Fornitore | Origine | Punto forte | MOQ | Lead time |
|-----------|---------|-------------|-----|-----------|
| **Packhelp** | PL | EU, custom small batch, eco-claims FSC | 30-100 pz | 8-15 gg |
| **Noissue** | UK/US | Custom tissue + tape + sticker, ottimo brand identity | 100 pz | 10-20 gg + dogana UK |
| **Sticker Mule** | NL (EU warehouse) | Sticker, packaging tape, mailers | 10-50 pz | 4-7 gg |
| **Pixartprinting** | IT (Vicenza) | Stampa custom **completo IT**, fattura, fast | 1+ pz | 3-7 gg |
| **Stampaprint** | IT | Print + packaging completo IT | 1+ | 3-7 gg |
| **Vistaprint** | NL/IT | Print + packaging consumer | 1+ | 4-8 gg |
| **Print24** | DE | Stampa pro EU | 50+ | 5-10 gg |
| **Imballaggi Roma / Cartotecnica Italiana** | IT | Cartone stock + custom su volumi | 50+ | varia |
| **RajaPack** | FR/IT | Pluriball, scatole stock, sacchetti, **catalogo enorme** | 1+ | 1-3 gg IT |
| **PackagingItalia** | IT | E-commerce packaging | 1+ | 2-4 gg |

### B.3 Listino orientativo

**Scatole cartone stock (per resistenza)**:
| Tipo | €IT |
|------|-----|
| Scatola cartone 200×150×100 mm (singola) RajaPack | €0.50-1.20 |
| Scatola cartone 150×100×80 mm bulk 100 pz | €30-50 |
| Bauletto / piccola scatola cubica 80×80×80 | €0.40-0.80 / pz |

**Imballaggio interno**:
| Materiale | €IT |
|-----------|-----|
| Pluriball rotolo 50 cm × 50 m | €15-25 |
| Carta riciclata kraft a nido d'ape (per ammortizzo eco) | €18-30 / rotolo |
| Trucioli legno bianchi (kraft fillers) 5 kg | €15-25 |
| Tissue paper bianco/colorato 100 fogli | €8-15 |
| Tissue paper custom brandizzato (Noissue/Packhelp) min 100 | €60-150 |
| Sacchetti polybag biodegradabili 100 pz | €8-18 |

**Custom branding**:
| Item | €IT |
|------|-----|
| Sticker tondi 50 mm 100 pz (Sticker Mule, Pixartprinting) | €30-60 |
| Stampe etichetta indirizzo termiche (rotolo) | €15-30 |
| Nastro custom brandizzato (Noissue 50 m) | €25-45 |
| Biglietto thank-you 100 pz stampato (Pixartprinting) | €15-35 |

### B.4 Eco-claims e certificazioni

Per shop italiani che spediscono UE/IT con claim "sostenibile":

- **FSC (Forest Stewardship Council)**: certificazione carta/cartone da foreste gestite. Packhelp/Noissue/Pixartprinting offrono carta FSC su richiesta. Per usare il logo FSC **nel proprio packaging serve catena di custodia certificata** o citare il fornitore.
- **PEFC**: alternativa europea FSC, simile.
- **PSV / Compostabile EN 13432**: certificazione bioplastiche e carta compostabile.
- **CONAI**: ente italiano gestione imballaggi — non è "certificazione green" ma serve per la dichiarazione di immesso al consumo (rilevante se sopra soglie volume; per piccoli batch hobbisti, irrilevante).

**Pratico per shop italiano piccolo**:
- Usare cartone FSC standard (RajaPack lo specifica).
- Filler kraft riciclato.
- Tape carta gommato (no plastica).
- Comunicare "spedito con materiali FSC e biodegradabili" — claim onesto senza green-washing.

### B.5 Spedizione Italia — corrieri piccoli batch

| Corriere | Tipo | Costo singolo (S, ~1kg) | Note |
|----------|------|--------------------------|------|
| **Poste Italiane Crono** | rete capillare | €8-12 | Standard |
| **BRT (Bartolini)** | corriere | €6-10 | Affidabile, ritiro |
| **GLS** | corriere | €7-11 | Affidabile |
| **Poste Postacelere1** | espresso | €15-22 | Veloce, traccia |
| **InPost / Locker** | locker | €4-7 | Eco, no fascia oraria |
| **Packlink PRO** | aggregatore | varia | Marketplace tariffe |
| **Sendcloud** | aggregatore | varia | Per e-commerce volumi |

Per piccoli batch: **Packlink PRO o Sendcloud** offrono tariffe -30/-50% vs sportello.