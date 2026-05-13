# 01 — SprayMax 2K Aerosol: Deep Dive

Approfondimento tecnico sui clear coat **2K poliuretano in formato aerosol**, applicati a stampe PLA verniciate destinate a uso commerciale, esposizione UV o duty-cycle prolungato (manipolazione cliente, scrivania, vetrina).

> Round 1 li aveva citati come "tier above". Qui entriamo nei dettagli reali: chimica, applicazione, sicurezza, ROI.

---

## 1. Chimica del 2K aerosol — come funziona la bomboletta "knock to activate"

Un clear coat **2K (two-component)** poliuretano è composto da:
- **Componente A** — resina poliolica (hydroxyl-functional acrylic o polyester).
- **Componente B** — hardener isocianato alifatico (tipicamente HDI — hexamethylene diisocyanate — o IPDI — isophorone diisocyanate — entrambi non-aromatici, low yellowing). Vedi sezione 2 per dettagli SDS.

In una bomboletta SprayMax 2K il componente B è alloggiato in una **piccola capsula interna sotto pressione**, separato dal componente A che riempie la lattina. L'utente:

1. Capovolge la bomboletta e appoggia il **pulsante rosso/base** su una superficie dura.
2. Preme con forza (il "knock") → la capsula interna si rompe e l'hardener si miscela con la resina.
3. Agita energicamente **2 minuti**, lascia riposare **5 minuti**, poi riagita **1 minuto** prima dell'uso.

Da quel momento parte il **pot life** ad ambiente: la reazione di crosslinking poliuretanica procede dentro la bomboletta, **stessa logica della pistola HVLP body shop**.

- **Pot life dichiarato**: 24-48 ore a 20 °C (SprayMax USC datasheet). Dopo questo tempo la viscosità interna sale e la bomboletta si "blocca". Da quel momento è rifiuto chimico, non recuperabile.
- **Conseguenza pratica**: pianificare il lavoro in modo da svuotare la bomboletta entro la finestra. Stimare 2-4 pezzi medi (10-20 cm) o 1 pezzo grande (40 cm) per bomboletta da 400 ml.

### Confronto chimica vs 1K

| Parametro | 1K acrilico lacca (Mr. Super Clear, Tamiya TS-13) | 2K poliuretano aerosol (SprayMax 2K) |
|---|---|---|
| Meccanismo cura | Evaporazione solvente + ossidazione lenta | Reazione chimica crosslinking isocianato-poliolo |
| Tempo dust-free | 10-20 min | 15-30 min |
| Tempo tape-free | 1-3 h | 2-4 h |
| Cura completa | 2-6 settimane (continua a indurire) | 24-48 h (8-16 h forzata a 60 °C, **non applicabile a PLA**) |
| Reversibilità | Risolubile in solvente origine | **Irreversibile** dopo cura |
| Tg film finale | ~40-60 °C | ~70-85 °C [da verificare su datasheet specifico] |
| Resistenza chimica | Bassa-media (alcol, benzina aggrediscono) | Alta (resiste benzina, alcol, detergenti) |
| Resistenza UV | Da scarsa (Tamiya TS-13) a buona (Mr. Super Clear UV Cut) | **Eccellente** (HALS + UV absorber standard) |

Fonte: SprayMax USC technical datasheet (https://spraymax.com), confronto chimico generico in Wicks et al., *Organic Coatings: Science and Technology* (Wiley, 3rd ed.).

---

## 2. Prodotti reali sul mercato EU (aerosol 2K)

| Prodotto | Hardener | Volume | Prezzo EU indicativo | Reperibilità IT | Note |
|---|---|---|---|---|---|
| **SprayMax 2K Clear Glamour** (3680061) | HDI alifatico | 400 ml | 22-28 € | Carrozzeria, online (Carrozzeria Express, Ricambi-Auto-24, eBay) | Il riferimento di mercato. Gloss alto, UV resistance dichiarata. |
| **SprayMax 2K Clear Coat Matt** | HDI alifatico | 400 ml | 22-28 € | Stesso canale | Versione matte/satin. |
| **USC Spray Max 2K Glamour High Gloss** | HDI alifatico | 400 ml | 25-30 € (più costoso in IT) | Limitata, spesso import US | Stesso produttore (Peter Kwasny GmbH), branding USA. |
| **MIPA 2K Clear Coat Spray** | IPDI/HDI [da verificare] | 400 ml | 18-25 € | Carrozzerie professionali IT | Marca tedesca, alternativa solida. |
| **Standox 2K Clear Spray** | HDI | 400 ml | 30-40 € | Solo canali Axalta / officine | Top tier, premium, raro in retail. |
| **U-POL Clear #1 2K Aerosol** | HDI | 450 ml | 20-25 € | Diffuso UK, meno IT | Buon compromesso. |
| **Wurth 2K Klarlack Spray** | HDI | 400 ml | 25-30 € | Würth shop fisici IT | Affidabile, garanzia distribuzione capillare. |

**Da verificare**: la formulazione esatta dell'hardener (HDI vs IPDI vs mix) non sempre è dichiarata nella scheda commerciale; va recuperata da SDS (sezione 3 di questo file).

URL utili:
- SprayMax product page: https://www.spraymax.com/en/products/2k-products/
- Peter Kwasny GmbH (produttore): https://www.peter-kwasny.de
- MIPA AG: https://www.mipa-paints.com

---

## 3. Compatibilità su PLA verniciato — rischio crazing e trip-coat

### A. Su PLA nudo
**Rischio reale di crazing/dissolvimento** se applicato a film spesso su PLA non protetto. Il solvente di trasporto (mix xilene + butil-acetato + acetone in alcuni casi) è aggressivo. **Mai applicare 2K direttamente su PLA**. Sempre con un primer di barriera in mezzo (filler primer Rust-Oleum o Tamiya Surface Primer).

### B. Su acrilico hobby (Vallejo, Citadel) curato
- Acrilico water-based curato 24-72 h → il 2K aderisce bene, ma il **primo passaggio deve essere "trip coat" / "mist coat"**: nebbiolina leggera a 30-40 cm di distanza, attendere 5 minuti che asciughi il solvente, poi mano completa.
- Saltare il mist coat = rischio "lifting" / "wrinkling" dell'acrilico (la lacca solvente del 2K rigonfia l'acrilico sottostante prima di sigillarlo).

### C. Su lacca acrilica spray (Tamiya TS, Mr. Hobby, Krylon)
- Compatibilità buona. Lacca su lacca aderisce per fusione superficiale parziale. Anche qui mist coat consigliato.

### D. Su epossidico (XTC-3D) o filler primer
- Compatibilità eccellente. Adesione meccanica + chimica solida.

### Trip-coat protocol (sintesi)
1. **Mist coat**: 1 secondo, 30 cm di distanza, copertura 30-50 % (deve sembrare "polveroso").
2. **Flash off**: 5-10 min in ambiente ventilato, 20 °C.
3. **Medium coat**: 2-3 secondi, 25 cm, copertura 80 %.
4. **Flash off**: 10-15 min.
5. **Wet coat**: passata lenta e regolare, 20-25 cm, "wet film" appena visibile (il pezzo deve riflettere). Evitare colatura.
6. Cura: 24-48 h a 20 °C in zona priva di polvere.

Fonti: discussione su AutoBody101 (https://www.autobody101.com), thread "SprayMax 2K over base coat" Refinish Network forum, video Bondoman "How to use SprayMax 2K" su YouTube.

---

## 4. Hard test — dati misurati (dove esistono) e claim datasheet

| Test | Risultato 1K Mr. Super Clear UV Cut | Risultato SprayMax 2K Glamour |
|---|---|---|
| **Pencil hardness (ASTM D3363)** | HB-F (hobby, stimato) | 2H-3H (datasheet SprayMax) |
| **Mohs (scratch test casa)** | ~2 (unghia segna leggermente) | ~3-4 (resiste a unghia, segna con moneta) [stima da confronti utenti, **da verificare**] |
| **Cross-hatch adhesion ASTM D3359** | [non pubblicato hobby] | Classe 4B-5B su substrato adeguato (datasheet) |
| **Resistenza benzina (1 min wipe)** | Aggredisce, opacizza | Nessun effetto |
| **Resistenza alcol IPA (1 min wipe)** | Opacizza | Nessun effetto |
| **Salt spray ASTM B117** | Non testato per uso hobby | 240 h+ su substrato metallico (dato body shop, non direttamente trasferibile a plastica) |
| **UV cabinet QUV** | [non pubblicato] | 500-1000 h con yellowing limitato (claim brand, **da verificare con report 3° parte**) |
| **Tg film finale** | ~40-55 °C | ~75-85 °C [stima letteratura] |

**Caveat onesto**: i numeri "hard test" sui 2K aerosol arrivano dal mondo automotive (substrato metallo verniciato). Su PLA verniciato — substrato meccanicamente più debole — il **collo di bottiglia non è il clear ma il PLA sottostante** (Tg 60 °C, modulo 3.5 GPa). Quindi il clear 2K **non rende il PLA indistruttibile**: rende lo strato superficiale molto più resistente di un 1K, ma il pezzo intero rimane vincolato alla termica del PLA.

---

## 5. Sicurezza casalinga — versione sintetica (dettagli in `03_safety_isocyanates_diy.md`)

- **Isocianati alifatici (HDI/IPDI)** = sensibilizzanti respiratori. Una singola esposizione massiva può innescare asma occupazionale cronica.
- **PPE minimo non negoziabile**:
  - Respiratore con **filtri A2-P3** combinati (esempio: 3M 6200/6300 + cartucce 6051 A1 o 6055 A2 + pre-filtri P3 5935).
  - **Meglio ancora**: full-face respirator (3M 6800, Sundström SR200) per protezione oculare.
  - Guanti nitrile, tuta usa-getta, ventilazione forzata.
- **Garage/esterno ventilato** dell'utente = condizione minima accettabile **se** c'è ricambio d'aria attivo (porta aperta + ventilatore in uscita). Mai box chiuso.
- Tempo permanenza isocianati in aria dopo spray: 15-60 min con ventilazione, ore senza.

> **Importante**: il filtro A2-P3 ha vita utile limitata (8 h di uso cumulativo o 6 mesi dall'apertura della cartuccia, la prima che scade). Le cartucce vanno sostituite anche se "sembrano OK".

---

## 6. Costo e ROI

| Voce | 1K Mr. Super Clear UV Cut | SprayMax 2K |
|---|---|---|
| Costo bomboletta | 14-18 € / 170 ml | 22-28 € / 400 ml |
| Costo per ml | ~0.10 €/ml | ~0.06 €/ml |
| Pezzi coperti (10-15 cm) per bomboletta | 8-12 | 6-10 |
| Costo per pezzo | ~1.50-2.00 € | ~2.50-4.00 € |
| Tempo cura per spedizione | 24-72 h | 24-48 h |
| Aggravio PPE | Maschera A1/A2 basic (~30 €) | Full kit A2-P3 (~80-150 € + ricariche) |

Costo aggiuntivo "tier above" su prodotto commerciale: **+1-2 €/pezzo + tempo gestione bomboletta + PPE**. Su un prodotto venduto >50 € il delta è trascurabile; su pezzi entry-level <20 € comincia a pesare.

---

## 7. Quando 2K vale davvero — decision tree pratico

```
Il pezzo verrà esposto a luce solare diretta (anche dietro vetro)?
├── SÌ → 2K (o almeno 1K UV Cut) obbligatorio
└── NO
    └── Sarà manipolato dal cliente (touchpoint, presa in mano)?
        ├── SÌ → 2K consigliato per resistenza graffio + sebo + sudore
        └── NO
            └── Pezzo display-only su mensola/scrivania?
                ├── SÌ → 1K Mr. Super Clear UV Cut sufficiente
                └── NO/Outdoor → 2K obbligatorio + considerare cambio materiale (ASA/PETG)
```

### Per il caso utente (entrambi gli usi, commerciale + personale, scale 3-40 cm)

- **Commerciale + scale 15-40 cm + touchpoint cliente**: 2K SprayMax giustificato. Premium look + durata percepita.
- **Commerciale display-only, scale 3-15 cm**: Mr. Super Clear UV Cut sufficiente, 2K è overkill (costo + complessità PPE non ripagati).
- **Personale display interno**: 1K più che adeguato.
- **Personale outdoor/balcone**: cambiare materiale (ASA) prima di pensare al 2K.

---

## 8. Riassunto operativo

| Domanda | Risposta sintetica |
|---|---|
| Quanto dura una bomboletta SprayMax 2K attivata? | 24-48 h |
| Copre quanti pezzi 15 cm? | 6-10 con tre mani |
| Si applica direttamente su PLA? | No, sempre con primer in mezzo |
| Trip coat necessario? | Sì, sempre sopra acrilico |
| Cura per movimentazione? | 24 h a 20 °C |
| Cura per spedizione? | 48-72 h prudenziali |
| Resistenza UV vs Mr. Super Clear UV Cut? | Migliore, ma differenza misurata richiede test (vedi `04_measurable_test_protocol.md`) |
| Sicurezza minima? | Garage ventilato + respiratore A2-P3 + guanti nitrile |
| Costo per pezzo aggiuntivo vs 1K? | +1-2 €/pezzo |

---

## 9. Fonti

- SprayMax 2K product / SDS: https://www.spraymax.com/en/products/2k-products/
- Peter Kwasny GmbH: https://www.peter-kwasny.de/en
- MIPA AG datasheet: https://www.mipa-paints.com
- Wurth 2K Klarlack: https://www.wuerth.it (codice prodotto variabile per regione)
- AutoBody101 forum, thread "SprayMax 2K experiences": https://www.autobody101.com
- Refinish Network forum: https://refinishnetwork.com
- YouTube — Bondoman, "SprayMax 2K Clearcoat Review": cercare canale ufficiale.
- YouTube — Mooresville Hot Rod, test 2K aerosol vs pistola HVLP.
- Wicks, Jones, Pappas, *Organic Coatings: Science and Technology* (Wiley) — riferimento chimica PU.
- 3M PPE selector: https://www.3m.com/3M/en_US/p/c/safety/respiratory-protection/
