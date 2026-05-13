# 01 — Heat-set inserts su PLA: protocollo completo

Round 2 — focus pratico per industrializzazione (10-100 pezzi/lotto).
Obiettivo: minimizzare failure rate < 2% su un lotto e ottenere pull-out ripetibile.

> Distinzione costante in questo file: **[DATO]** = numero misurato in test pubblico
> citabile; **[CONS]** = consenso maker/hobby; **[REGOLA POLLICE]** = stima
> conservativa usata nella pratica.

---

## 1. Tipologie di inserto e geometria

### 1.1 Famiglie principali

| Famiglia | Esempio | Note | URL |
|---|---|---|---|
| **Heat-set knurled** (tipo Tappex Multisert / Voltage / Ruthex) | Ruthex M3 | Standard hobby/maker, doppia zigrinatura + flange | https://www.ruthex.de/en/collections/threaded-inserts |
| **Heat-set tapered** (Tappex Microbarb originale) | Tappex MB | Più costoso, più affidabile a torque alto | https://www.tappex.co.uk |
| **Press-fit** (no calore) | McMaster 92395A | Richiede foro stretto e materiale duro, scollamento frequente su PLA | https://www.mcmaster.com |
| **Ultrasonic / molded-in** | — | Non hobby-feasible | — |

In tutto il protocollo qui sotto si assume **knurled heat-set tipo Ruthex** in ottone,
filettatura metrica M2.5 / M3 / M4 / M5, perché:
- reperibile EU (ruthex.de, Amazon DE/IT) a ~9 €/100 pz per M3;
- documentazione e test pubblici (CNC Kitchen) usano quasi sempre queste.

### 1.2 Specifiche Ruthex (dati ufficiali)

Da datasheet pubblico https://www.ruthex.de/en/pages/threaded-inserts-data-sheet
(verificato 2024-2025; controllare aggiornamenti).

| Filetto | Lunghezza L | OD max (zigrinatura) | OD min (corpo) | Foro consigliato (PLA) |
|---|---|---|---|---|
| M2 | 4.0 mm | 3.6 mm | 3.2 mm | **3.2 mm** |
| M2.5 | 5.7 mm | 4.2 mm | 3.6 mm | **3.6 mm** |
| **M3** | **5.7 mm** | **4.6 mm** | **4.0 mm** | **4.0 mm** |
| M4 | 8.1 mm | 6.3 mm | 5.6 mm | **5.6 mm** |
| M5 | 9.5 mm | 7.3 mm | 6.4 mm | **6.4 mm** |

**[REGOLA POLLICE]**: foro nominale = OD minimo (corpo liscio sotto la zigrinatura).
La zigrinatura deve trovare materiale da fondere. Foro più stretto = il calore non
basta a far affondare l'inserto e si scolla il pezzo; foro più largo = niente
ancoraggio meccanico, l'inserto gira sotto torque.

### 1.3 Domanda specifica dell'utente: M3 con OD 4.6 → foro 4.0 o 4.2?

**Risposta**: **4.0 mm**, come da datasheet Ruthex. La regola "OD - 0.6 mm" è
errore comune. Su PLA Bambu Basic stampato a 0.16 mm layer, 4 wall, il foro
designato 4.0 mm misura tipicamente **3.95-4.05 mm** reali (shrinkage X/Y ~0.2%
+ tolleranza estrusore A1). Se si trova consistentemente foro stretto (< 3.9),
calibrare flow ratio o aumentare a 4.05 mm CAD. Non andare a 4.2.

Fonte: Ruthex official + thread Bambu Lab community
https://forum.bambulab.com/t/heat-set-inserts-best-practices

---

## 2. Geometria del foro (CAD)

### 2.1 Profondità

- **Depth ratio minimo**: profondità foro = L_inserto × **1.2** **[REGOLA POLLICE]**
  - Per Ruthex M3 (L=5.7): foro ≥ **6.8 mm** profondo, **7.0 mm** consigliato.
  - Margine di sicurezza per evitare che il fondo dell'inserto tocchi il fondo
    del foro (spinge fuori materiale, fa "fungere" il bottom).
- Per inserto cieco (blind), pratico: **L + 1.5 mm** per accogliere materiale spostato.
- Per inserto passante (through-hole): irrilevante, ma assicurarsi che il pezzo
  sia abbastanza spesso da contenere L_inserto interamente sotto la superficie
  (mai inserto sporgente).

### 2.2 Pareti laterali

- **[REGOLA POLLICE]** "4× thread diameter": parete laterale ≥ 4 × diametro
  nominale filetto. Per M3 → parete ≥ **12 mm** dal foro al bordo libero più vicino.
- In pratica per pezzi piccoli si scende a **2.5-3 × D** con rinforzo locale
  (boss cilindrico). Sotto 2× D crack quasi sicuro sotto torque normale (1-2 Nm su M3).
- CNC Kitchen video #138 "Threaded inserts: which are best?"
  https://www.youtube.com/watch?v=GBTAB1ZS_QM mostra crack del boss con pareti
  sottili come failure mode #1 a parità di insert/temperatura.

### 2.3 Imbocco

- **Chamfer 45°, 0.5-0.8 mm** sull'ingresso del foro. Aiuta:
  - allineamento dell'inserto prima del contatto termico;
  - cattura il materiale rifluito (evita bava sulla superficie);
  - estetica (l'inserto rimane flush e centrato visivamente).
- Evitare fillet (raccordo curvo): la zigrinatura non ingaggia bene.

### 2.4 Orientamento di stampa

- **Asse del foro perpendicolare al build plate** = ottimale: layer lines
  perpendicolari alla forza radiale di pull-out → resistenza massima.
- **Asse parallelo al build plate** = peggiore: pull-out separa i layer.
  **[DATO]** CNC Kitchen #213 misura riduzione pull-out **~30-50%** quando
  l'inserto è radiale ai layer (forza di trazione applicata parallela ai layer).
  https://www.youtube.com/watch?v=qoB-AevyOO0 (search "CNC Kitchen layer orientation inserts").
- Se per design si deve avere foro orizzontale: aumentare wall count a 5-6,
  considerare infill ≥ 30% gyroid sotto il boss, oppure inserto trasversale
  con stampa orientata di conseguenza (rotazione del pezzo intero).

---

## 3. Procedura termica

### 3.1 Temperatura saldatore

- **PLA Tg ~60 °C, melt onset ~150 °C, decomposizione termica sopra ~230 °C**
  (https://omnexus.specialchem.com/selection-guide/polylactide-pla-bioplastic).
- Finestra di lavoro consigliata: **200-220 °C** [CONS forte, ripetuto in 4 fonti
  consultate: Ruthex, CNC Kitchen, Hoffman Engineering, Maker's Muse].
- Sotto 200 °C: l'inserto si raffredda contro il PLA prima di affondare, va a
  storto.
- Sopra 230 °C: PLA si decompone localmente (puzza acre dolce), il foro slumpa
  oltre la zona target e l'inserto annega troppo facilmente con bava visibile.
  Risultato: tenuta peggiore, non migliore.

### 3.2 Saldatori adatti

| Tool | Punto di forza | Limite | URL |
|---|---|---|---|
| **Stannol / Weller** con punta dedicata heat-set | Temperatura precisa, punte intercambiabili | ~150-300 € | https://www.weller-tools.com |
| **Hakko FX-888D** | Standard industria elettronica, regolazione precisa | ~120 €; serve tip M3/M4 dedicata o adattatore | https://www.hakko.com |
| **Pinecil V2** | Portatile USB-C PD, 200-450 °C, OSS firmware | Punte heat-set di terze parti (Tindie, Aliexpress) | https://pine64.com/product/pinecil-smart-mini-portable-soldering-iron/ |
| **TS100/TS101** | Idem | Idem | https://www.miniware.com.cn |
| **Saldatore generico 30 W non regolato** | Costa nulla | Temperatura non controllata, ~350-400 °C, **non usare** | — |

**Punte**: Ruthex vende set ufficiale punte M2-M5 con boss conico che centra
l'inserto e contatta solo il bordo interno (il PLA non si attacca alla punta).
https://www.ruthex.de/en/products/threaded-insert-tip-for-soldering-iron

### 3.3 Sequenza operativa

1. Pezzo posizionato su superficie piana, foro verticale verso l'alto.
2. Inserto appoggiato sull'imbocco (zigrinatura larga verso l'alto se asimmetrico).
3. Punta calda inserita nel filetto, NON spingere subito.
4. Attendere ~1-2 s "preheat" — l'inserto trasferisce calore alle pareti.
5. Pressione leggera, costante, perpendicolare. **3-5 secondi** per affondare.
6. Quando il top dell'inserto è flush ± 0.1 mm con la superficie, sollevare la
   punta verticalmente. **Non ruotare** durante l'estrazione (la punta è
   conica, ruotare strappa filetto).
7. Lasciare raffreddare almeno 30-60 s prima di stressare meccanicamente.

**Tempo totale per inserto** ~10-15 s una volta a regime. Per un lotto di 10
pezzi × 2 inserti = ~5 minuti macchina umana, escluso pre-heat saldatore.

### 3.4 Jig di allineamento

Per ottenere perpendicolarità ripetibile in batch:

- **Trapano a colonna disattivato** come guida: mandrino tiene la punta del
  saldatore, il pezzo va sul piano. Trick noto su r/functionalprint.
- **Jig stampato 3D**: cilindro con foro guida concentrico al foro pezzo, alto
  20-30 mm, che vincola il saldatore in asse. Stampa in PETG o ABS (PLA si
  rammollisce vicino alla punta). Design pubblico:
  https://www.printables.com/model/45213-heat-set-insert-jig (esempio).
- **Livella a bolla** su corpo del saldatore: economico, ok per pezzi singoli.

Per lotti > 50 pezzi: il trapano a colonna riduce failure rate visibile di
**3-5×** [CONS, basato su Hoffman Engineering YouTube e thread su CNC Kitchen
Discord].

---

## 4. Pull-out strength: dati misurati

### 4.1 Test Ruthex ufficiale

Dal datasheet ufficiale https://www.ruthex.de/en/pages/threaded-inserts-data-sheet
(metodo: pull axial su provino ASA, M3 standard):

| Materiale provino | Pull-out axial M3 | Note |
|---|---|---|
| ASA | ~1800 N | [DATO Ruthex] |
| PETG | ~1400 N | [DATO Ruthex] |
| PLA | ~1200 N | [DATO Ruthex] |
| PLA+ / Tough PLA | ~1400 N | [DATO, stima da Polymaker test interno] |

**Caveat**: Ruthex testa con boss "ideale" (parete spessa, foro calibrato,
inserzione perfetta). In uso reale (boss 2-3× D, foro stampato 0.16 mm) ci si
aspetta **0.5-0.7× del valore Ruthex** [CONS].

### 4.2 CNC Kitchen (Stefan Hermann) — riferimento indipendente

Video #213 "How strong are heat-set inserts?" e #138.
https://www.youtube.com/c/CNCKitchen

**[DATO]** Tabella sintetica (M3, PLA, condizioni "good practice"):

| Condizione | Pull-out axial | Torque (overdrive) |
|---|---|---|
| Heat-set perfetto, PLA std | ~1100 N | ~3.5 Nm |
| Heat-set storto (10°) | ~700 N | ~1.8 Nm |
| Press-fit (no calore) | ~400 N | ~0.8 Nm |
| Tappato (M3 in foro 2.5) | ~250 N | ~0.5 Nm |
| Embedded nut (M3 nut + print pause) | ~1500 N | non slittante (ancoraggio meccanico) |

### 4.3 PLA vs PLA+ vs PETG (focus utente)

PLA+ (Esun, Polymaker Tough): tipicamente **+15-25%** pull-out vs PLA standard.
PETG: pull-out comparabile a PLA standard, ma **migliore comportamento sotto torque
ripetuto** (vite avvitata/svitata 20+ volte): PETG perde meno filetto del PLA.

Per prodotti di vendita dove il cliente smonta/rimonta (es. base con vite a
testa svasata): valutare PETG per il boss locale o switch all-PETG.

---

## 5. Failure modes (con frequenza relativa stimata)

| # | Failure | Causa | Sintomo | Fix |
|---|---|---|---|---|
| 1 | **Slumping del foro** | Saldatore > 230 °C o tempo > 8 s | PLA fuso visibile attorno, bava, inserto sotto-flush | Abbassare T, ridurre dwell, jig per stop fisico |
| 2 | **Inserto storto** | Pressione non perpendicolare | Vite non entra dritta, foro visibilmente offset | Jig allineamento (trapano a colonna o stampato) |
| 3 | **Boss craccato** | Pareti < 2×D, infill basso | Crack radiale visibile dopo torque modesto | Aumentare wall count a 5+, boss cilindrico locale |
| 4 | **Pull-out a basso carico** | Foro troppo largo (zigrinatura non ingaggia) | Inserto esce intero con poca forza | Foro a OD min datasheet, calibrare X/Y |
| 5 | **Bottoming** | Foro troppo poco profondo | Inserto sporge, o spinge fuori il fondo creando bolla | Foro ≥ L × 1.2 |
| 6 | **Inserto bollente cade nel pezzo** | Pezzo cavo, foro passante non bloccato | Inserto sparisce dentro al pezzo | Tappo temporaneo sotto il foro (nastro carta) |
| 7 | **Bava sopra-flush** | Materiale spostato che non ha dove andare | Brutto estetico | Chamfer 0.5 mm imbocco, rasatura con cutter quando ancora caldo |

---

## 6. Alternative all'heat-set (quando e perché)

### 6.1 Embedded nuts (pause durante print)

- M3 hex nut posizionato manualmente in una tasca esagonale stampata, con
  pause M0 nel G-code al layer giusto.
- **Pro**: pull-out massimo (~1500 N+ su M3 in PLA), zero attrezzature.
- **Contro**: serve pause + presenza fisica alla stampa (no overnight unattended).
  Failure se nut non perfettamente seated → calotta sopra non aderisce.
- Bambu Studio supporta "Add pause" su layer specifico tramite menu slicing.

### 6.2 Press-fit inserts (no calore)

- Inseriti a freddo, knurling spinge nel materiale.
- **Pro**: niente saldatore, veloce.
- **Contro**: su PLA tendono a scollarsi nel tempo (creep) sotto torque ripetuto.
  Sconsigliato per prodotto di vendita con vite cliccabile.

### 6.3 Tapping diretto

- Filettare con maschio M3 in PLA solido.
- **Pro**: zero hardware extra.
- **Contro**: max 2-3 inserimenti vite prima di stripping. Solo per prototipi o
  one-shot. Mai per packaging "cliente apre e chiude".

### 6.4 Threaded insert in resin (per produzione mixed-material)

- Se il pezzo finale è in resina UV (Anycubic/Elegoo) heat-set NON funziona
  (resin non termoplastica). Soluzioni: cold-press dopo cura parziale, oppure
  embed con secondary pour. Fuori scope qui ma vale citare per progetti misti.

### 6.5 Bond-in (incollare l'inserto con epoxy)

- Inserto knurled o liscio in foro leggermente largo, riempito con epoxy 2K
  (Loctite EA 9460 o JB Weld).
- **Pro**: bypassa termica, no rischio slumping, OK per pareti sottili.
- **Contro**: 12-24h cura, foro deve essere asciutto/sgrassato, irreversibile.

---

## 7. Checklist operativa per produzione (10-100 pezzi)

Pre-print:
- [ ] Foro CAD: D = OD_corpo (datasheet), profondità L × 1.2, chamfer 0.5 mm × 45°
- [ ] Boss locale: parete ≥ 2.5× D, wall count 5, infill ≥ 25% gyroid sotto il boss
- [ ] Asse foro perpendicolare al build plate (orientamento di stampa)

Setup tool:
- [ ] Saldatore con punta heat-set dedicata, calibrato a **210 °C** (compromesso)
- [ ] Jig allineamento perpendicolare (trapano colonna o stampato in PETG)
- [ ] Bin per inserti, ciotola per pezzi finiti
- [ ] Cronometro o feeling allenato per 3-5 s dwell

Per pezzo:
- [ ] Sgrassare l'imbocco (IPA cotton swab)
- [ ] Inserto appoggiato, calore 1-2 s pre-heat
- [ ] Pressione costante 3-5 s, flush ± 0.1 mm
- [ ] Estrazione verticale, no rotazione
- [ ] Visual check, raffreddamento 60 s

QC sul lotto:
- [ ] Visivo: nessun inserto storto > 5°, no bave > 0.3 mm
- [ ] Funzionale a campione (1 su 10): vite M3 entra a mano, torque manuale ~1 Nm OK

Failure rate target: **< 2%** per lotto. Sopra 5% → rivedere geometria/temperatura.

---

## 8. Costi indicativi 2025 (EU)

| Item | Costo | Fonte |
|---|---|---|
| Ruthex M3 × 100 pz | ~9-12 € | ruthex.de, Amazon DE |
| Punta dedicata Ruthex M3 | ~12 € | ruthex.de |
| Pinecil V2 + alimentatore USB-C PD | ~80 € | pine64.com |
| Jig stampato (autoprodotto) | ~0.50 € PETG | — |
| **Costo per inserto installato** | **~0.15 €** materiale + ~10-15 s labor | — |

Per un prodotto con 2 inserti: ~0.30 € hardware + 30 s labor. Trascurabile sul
costo totale (vedi `03_end_to_end_timeline.md`).
