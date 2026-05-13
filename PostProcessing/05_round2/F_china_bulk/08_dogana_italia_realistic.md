# 08 — Dogana Italia 2025-2026: realistico per import CN

Sintesi operativa per piccolo brand IT che importa dalla Cina. Tasse, soglie, codici, tempi, rischi.

> Verificare sempre regole aggiornate su <https://www.adm.gov.it> (Agenzia Dogane e Monopoli) e <https://taxation-customs.ec.europa.eu>.

---

## A. Soglie e regime IVA 2025-2026 (regole 1° luglio 2021 + aggiornamenti)

| Valore ordine extra-UE | Cosa pago |
|------------------------|-----------|
| Qualsiasi (anche €1) | **IVA 22%** sempre dovuta — abolita franchigia €22 |
| ≤ €150 | IVA 22% + handling corriere SE no IOSS; **niente IVA fisica in dogana SE venditore è IOSS** (Aliexpress, Amazon, eBay attivi IOSS) |
| > €150 | IVA 22% + **dazio doganale** in base codice TARIC + handling corriere/sdoganamento + eventuale storage |

### A.1 IOSS — perché Aliexpress è "magico"

**IOSS (Import One-Stop-Shop)** è il regime UE 2021: il venditore extra-UE riscuote IVA al checkout e la versa periodicamente. Vantaggi:
- Pacco entra UE **senza dogana fisica visibile** (procedura semplificata).
- No handling fee corriere.
- Costo finale = prezzo + spedizione, già IVA inclusa.

Si applica solo a ordini **≤ €150 totale (merce, spedizione esclusa)**. Sopra €150, IOSS non vale → si torna alla dogana classica.

Aliexpress, Wish, Amazon CN sellers, Temu sono **tutti IOSS** sotto soglia. **Alibaba.com NO** (è B2B, non rientra).

---

## B. Dazi doganali per categoria — TARIC sintesi

| Categoria | Codice TARIC (esempio) | Dazio UE | Note |
|-----------|--------------------------|----------|------|
| **Filamento PLA monofilo 1.75/2.85 mm** | 3916.91.00 | **6.5%** | Per peso > 1 kg |
| **Vernici / coating preparations** | 3208.90.91 / 3208.90.19 | **6.5%** | Coatings solvent-based |
| **Vernici waterborne** | 3209.10.00 | **6.5%** | Acrilici |
| **Pigmenti in polvere** | 3204 / 3206 / 3207 | **0-6%** | Variabile, alcuni esenti |
| **Pennelli artistici** | 9603.30.10 | **3.7%** | Per pittura artistica |
| **Bombolette spray aerosol (paint)** | 3208.90.91 + classe IMDG 2.1 | **6.5% + procedura mer pericolosa** | Spedizione mare obbligatoria |
| **Imballaggi carton (mailer box stampati)** | 4819.10.00 / 4819.20.00 | **0%** | Esente UE |
| **Tissue paper stampata** | 4811.49.00 / 4823.90 | **0%** | Esente |
| **Sticker / etichette adesive** | 4821.10.10 (carta) / 3919.90 (plastica) | **0-6.5%** | Adesivi plastica 6.5% |
| **Foam EVA insert** | 3921.13.10 / 3921.19 | **6.5%** | Plastica espansa |
| **Airbrush + spruzzatori** | 8424.20.00 | **1.7%** | Apparecchi spruzzo |
| **Compressori piccoli (< 30 kg)** | 8414.80.22 / 8414.40 | **2.2%** | — |
| **Saldatori elettrici** | 8515.11.00 / 8515.19 | **2.7%** | Per heat-set |
| **Heat-set inserts (filettati ottone)** | 7415.39.00 | **3.7%** | Bulloneria ottone non standard |
| **Inserti M3 standard** | 7318.16.91 | **3.7%** | Dadi standard |
| **Light tent / softbox** | 9405.40.99 | **2.7%** | Apparecchi illuminazione |
| **Tripod fotografico** | 9620.00.00 | **2.7%** | Treppiedi |

### B.1 Calcolo landed cost esempio

Ordine Alibaba 500 mailer box custom = $400 + freight $300 = $700 (~€650).

| Voce | Importo |
|------|---------|
| Merce (CIF, valore dichiarato) | €650 |
| Dazio (HS 4819 → 0%) | €0 |
| IVA 22% su (merce + dazio) | €143 |
| Handling DHL sdoganamento | €18-25 |
| **TOTALE LANDED** | **€811-818** |
| Costo unitario | €1.62 / box |

Con sample iniziale ($50 + $40 ship + €20 IVA) → ~€110 sample + 6-9 settimane lead time.

---

## C. Under-declaration — il rischio nascosto del DDP cinese

Quando un fornitore cinese spedisce in DDP a basso costo, **molto spesso sotto-dichiara il valore** della merce per ridurre IVA pagata in dogana. Conseguenze:

1. **Se la dogana IT controlla a campione** (frequente per pallet pesanti, ricorrenti destinatari): chiede valore reale (con la fattura proforma o dati di pagamento). Se non corrisponde → **accertamento**, multa 100-200% IVA evasa + interessi.
2. **Stesso destinatario ricorrente**: Agenzia Dogane sviluppa profilo statistico. Se sotto-dichiari sistematicamente, scatta audit.
3. **Per P.IVA**: l'azienda è responsabile finale dei tributi. Anche se il forwarder cinese ha "fatto i magheggi", la P.IVA italiana paga.

### C.1 Difesa

- **Richiedere fattura commerciale completa** al fornitore (Trade Assurance la genera automaticamente).
- **Confrontare** dichiarazione doganale (codice MRN, ricevibile dal corriere) con la fattura tua.
- Se sotto-dichiarazione: contestare al fornitore + se necessario pagare integrazione IVA spontaneamente (tutela P.IVA).
- **Preferire** spedizione **DAP / FOB** con sdoganamento da forwarder IT con cui hai contratto trasparente.

---

## D. Tempi sdoganamento Italia 2025-2026

| Punto ingresso | Specialità | Tempi sdoganamento (giorni) |
|----------------|-----------|------------------------------|
| **Milano Malpensa (MXP)** | Air cargo, express courier hub | 1-3 gg (corrieri), 2-5 gg (cargo) |
| **Roma Fiumicino (FCO)** | Air cargo, express courier hub centro-sud | 1-3 gg (corrieri), 2-5 gg (cargo) |
| **Bologna BLQ** | Air cargo growing, express | 1-3 gg |
| **Genova porto** | Sea container Asia-Med, LCL/FCL leader | 5-10 gg sdoganamento porto |
| **La Spezia porto** | Container traffic alternativa Genova | 5-10 gg |
| **Trieste porto** | Sea Asia via Suez emergent, gateway Centroeuropa | 5-10 gg |
| **Gioia Tauro porto** | Hub Sud, transhipment | 7-15 gg |

**Trick**: per pacchi piccoli da Aliexpress / Choice / Premium, il punto di ingresso è gestito automaticamente (di solito Milano Malpensa). Per LCL mare bulk si sceglie in base a vicinanza warehouse — per Italia Nord, **Genova/La Spezia**; per Centro/Sud, **Gioia Tauro/Trieste**.

---

## E. Spedizioni con corriere espresso — addebiti

| Corriere | Sdoganamento per import CN | Handling/anticipo IVA-dazio |
|----------|-----------------------------|------------------------------|
| **DHL Express** | Standard | €11-18 + 2.5% del totale IVA+dazio (minimo €11) |
| **UPS** | Standard | €15-25 advancement fee |
| **FedEx / TNT** | Standard | €15-25 |
| **Aramex** | Per piccoli | €10-18 |
| **Poste Italiane (per pacchi standard non-express)** | Per ordini posta cinese tipica | €7.50 fisso |
| **GLS, Bartolini ricezione finale** | Solo distribuzione, NO sdoganamento | — |

---

## F. P.IVA italiana: cosa cambia

Per piccolo brand commerciale **già con P.IVA**:

1. **Iscrivere REX o EORI**: gratuito, obbligatorio per import/export business. Si fa online su agenziadoganemonopoli.gov.it. Codice EORI = "IT" + P.IVA.
2. **Fattura commerciale CN**: deve essere intestata alla P.IVA italiana, codice EORI in evidenza.
3. **Recupero IVA**: l'IVA pagata in dogana è **detraibile** se la merce è inerente all'attività (sì per packaging, filamento, vernici, tools commerciali). Si annota in registro acquisti, si recupera nella liquidazione IVA.
4. **Dazi**: NON sono detraibili (sono "costo"), ma deducibili come spese aziendali ai fini IRES/IRPEF.
5. **Reverse charge**: NON si applica all'import extra-UE (è solo per acquisti intra-UE). L'IVA si paga effettivamente al momento sdoganamento.
6. **Modelli Intrastat**: NON si fanno per import extra-UE (sono solo intra-UE). Si fanno solo i modelli doganali standard (DAU + bolla doganale).

### F.1 Consiglio P.IVA

Tenere un **commercialista** che conosca import/export è la differenza tra "risparmio 50%" reale e "casino fiscale con multe". Per piccolo brand, costa €600-1500/anno e si ripaga subito.

---

## G. Cosa controlla la dogana IT su import CN

Profilo di rischio comune (esperienza brand 2024-2025):

| Categoria | Probabilità controllo | Cosa controllano |
|-----------|------------------------|-------------------|
| Aliexpress small parcel <€80 | 1-3% | Random, valore + descrizione |
| Aliexpress €80-150 | 5-10% | IOSS validity, descrizione |
| Alibaba DHL Express pallet | 15-25% | Fattura, peso, valore, classificazione |
| LCL container | 25-50% | Tutto, AQL su campione |
| Bombolette spray import privato | **80-100%** | IMDG, SDS, CLP, REACH — molti fermi |
| Vernici / chemicals bulk | 30-60% | SDS, REACH, classificazione |
| Cosmetici / food contact | 60-90% | Severissimo, spesso bloccato |

### G.1 Documenti da avere SEMPRE pronti per ispezione

1. Fattura commerciale (commercial invoice) — valore reale.
2. Packing list (quantità per box).
3. Bill of Lading o Air Waybill.
4. Certificate of Origin (form A) — riduce dazio per alcuni paesi (CN non gode di preferenza generalizzata UE dopo 2014, ma il certificate aiuta classificazione).
5. SDS / Safety Data Sheet (per chemicals).
6. Test report REACH (per chemicals).
7. CE / EN certificate (per PPE, apparecchi elettrici).

---

## H. Categorie a rischio dogana alto (evitare o gestire con cura)

| Categoria | Perché alto rischio |
|-----------|----------------------|
| **Bombolette spray** | Merce pericolosa IMDG 2.1, CLP, REACH, IATA aereo vietato |
| **Vernici industriali solvent-based bulk** | REACH, dazio 6.5%, CLP etichettatura IT obbligatoria |
| **Isocianati (2K primer auto)** | Sostanza preoccupazione molto elevata REACH, autorizzazione specifica |
| **Pigmenti con Pb/Cd/Cr-VI** | Banditi/limitati REACH, rischio sequestro |
| **PPE certificati (FFP3, occhiali sicurezza)** | Richiede marcatura CE valida, EN149 |
| **Apparecchi elettrici (compressori, saldatori, ring light)** | Marcatura CE, dichiarazione conformità EMC/LVD richiesta |
| **Giocattoli / oggetti per bambini** | EN71, marcatura CE, severissimo |
| **Cosmetici, prodotti food contact** | Normative dedicate, autorizzazioni Ministero Salute |

### H.1 Per piccolo brand commerciale 3D-print

L'utente fa **oggetti d'arredo / decorativi adulti** in PLA. NON soggetti a:
- EN71 (giocattoli) — a meno che li venda esplicitamente come tali.
- Food contact — a meno che siano contenitori cibo.
- Cosmetic regulation — irrilevante.

Quindi nessuno di questi rischi alti, a meno di entrare in quei mercati.

---

## I. Riferimenti

- ADM Italia: <https://www.adm.gov.it>
- TARIC EU: <https://ec.europa.eu/taxation_customs/dds2/taric/taric_consultation.jsp>
- Calcolatore dazi UE: <https://trade.ec.europa.eu/access-to-markets/it>
- IOSS info venditore: <https://vat-one-stop-shop.ec.europa.eu/import-one-stop-shop-ioss_en>
- REACH ECHA database: <https://echa.europa.eu>
- EORI numero (verifica): <https://ec.europa.eu/taxation_customs/dds2/eos/eori_validation.jsp>
