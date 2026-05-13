# 02 — Protezione UV per PLA

Il PLA è uno dei filamenti più sensibili all'UV tra le plastiche da stampa 3D. Per un prodotto **commerciale** che può finire su una scrivania accanto a una finestra, in vetrina, o (peggio) in esterno, la degradazione UV è una variabile critica per la durata percepita.

---

## 1. Cosa succede al PLA esposto a UV

Effetti documentati:

- **Ingiallimento** progressivo (cromoforo da fotossidazione della catena polimerica).
- **Infragilimento** (chain scission del backbone PLA): caduta dell'elongation at break, aumento della fragilità a impatto.
- **Microcracking superficiale** ("crazing") dopo settimane–mesi.
- **Perdita di brillantezza** della superficie (se non sigillata).
- **Calo della Tg** apparente e creep accelerato sotto carico statico.

Velocità approssimativa (esterno, latitudine sud Europa):
- 1–4 settimane: primo ingiallimento visibile su bianchi/naturali.
- 1–3 mesi: fragilità apprezzabile, microcracking.
- 6–12 mesi: pezzo strutturalmente compromesso.

In **interno dietro vetro** (vetro normale blocca gran parte dell'UV-B ma lascia passare UV-A): velocità ~1/5–1/10 dell'esterno. Comunque rilevante su orizzonte 1–3 anni.

---

## 2. Dati scientifici (autori / rivista / anno)

> Non cito stringhe URL specifiche dove non sono certo del DOI; fornisco autori e rivista per ricerca diretta su Google Scholar / ScienceDirect / MDPI.

- **Copinet, A. et al. (2004)**, "Effects of ultraviolet light (315 nm), temperature and relative humidity on the degradation of polylactic acid plastic films", *Chemosphere*. Mostra che UV + umidità accelera l'idrolisi del PLA in modo sinergico.
- **Sakai, W. et al. (2004–2005)**, lavori su fotodegradazione PLA — *Polymer Degradation and Stability*.
- **Rasselet, D. et al. (2014)**, "Oxidative degradation of polylactide (PLA) and its effects on physical and mechanical properties", *European Polymer Journal*. Documenta riduzione di Mw e proprietà meccaniche.
- **Bocchini, S. et al. (2010)**, "Polylactic acid and polylactic acid-based nanocomposite photooxidation", *Polymer Degradation and Stability* 95. Tracker FTIR della fotossidazione.
- **MDPI Polymers** ha numerose review libere: cercare "PLA photodegradation outdoor" + "PLA UV stabilizer" sul sito mdpi.com.
- **Islam, M.S. et al. (2022 ca.)** e review più recenti su biopolimer durability outdoor — *Polymers (MDPI)* e *Journal of Applied Polymer Science*.

Conclusione condivisa dalla letteratura: **il PLA puro non è adatto a uso esterno prolungato senza barriera UV**. Soluzioni: additivi (HALS, UV absorber tipo benzotriazoli) in compound, oppure barriera applicata superficialmente (clear coat con UV blocker / film).

---

## 3. Strategie di protezione UV applicabili a un prodotto stampato

### A. Clear coat con UV inhibitor

| Prodotto | UV protection dichiarata | Note |
|---|---|---|
| **Mr. Hobby Mr. Super Clear UV Cut** | Sì, dichiarata. Pensato per figure PVC/resina che ingialliscono. | Probabilmente il miglior compromesso hobby. |
| **Krylon UV-Resistant Clear Coat** | Sì, "UV resistant" sulla bomboletta. | Disponibile gloss e matte. Buona reperibilità US, meno EU. |
| **Rust-Oleum 2X UV Protectant Clear** | Sì. | Linea consumer, decente. |
| **Liquitex Soluvar Varnish (artistico)** | Buona resistenza UV per ambito quadri. | Removibile con white spirit (vantaggio restauro). |
| **2K Polyurethane automotive (Spies Hecker Permasolid 8800, Standox Standocryl, U-POL Clear)** | Sì, HALS + UV absorber industriale. | **Standard reale per durata anni.** |
| **Pledge / Future** | NO. Solo gloss leveling. | Non aggiunge protezione UV. |
| **Most acrylic hobby varnish (Vallejo, Citadel base)** | Non dichiarata o marginale. | Da non considerare per outdoor. |

Importante: anche un clear coat "UV resistant" **non rende il PLA indistruttibile** — riduce significativamente la velocità ma non azzera. Per un display in interno dietro vetro è sufficiente; per uso esterno prolungato il PLA è la materia prima sbagliata (preferire ASA, PETG o resine outdoor).

### B. Additivi UV nel filamento

- Alcuni filamenti vendono varianti "UV stable" (PolyMaker PolyLite ASA, ColorFabb nGen, Prusament PETG hanno migliore tenuta del PLA).
- Filamenti PLA "UV resistant" sono rari; quando dichiarati, attenzione al test third-party.
- Per prodotti commerciali outdoor, **passare ad ASA o PETG-CF** è più sensato che cercare di "salvare" un PLA.

### C. Pellicole protettive

- Pellicole adesive UV-blocking trasparenti (es. tipo per auto / vetrine museali) applicate sul **display case** invece che sul pezzo.
- Plexiglass / acrilico **UV-filtering** (es. Plexiglas Optical UV100) per cupole o teche.
- Vetro museale (Tru Vue Optium, ArtGlass UV) — costo alto ma standard musei.

### D. Posizionamento

- Mai luce diretta del sole, mai vicino a finestre south-facing senza filtro.
- LED freddi → meno UV di alogene/fluorescenti. Per display retail privilegiare LED neutri 4000 K.
- Per fotografia di prodotto preferire scatto rapido e poi storage in scatola al buio.

---

## 4. Soluzioni pro applicabili a un piccolo brand

Ordine di costo crescente:

1. **Krylon UV-Resistant Clear / Rust-Oleum 2X UV** — costo basso, miglioramento sensibile, applicazione spray semplice.
2. **Mr. Hobby Mr. Super Clear UV Cut** — costo medio, qualità superiore, ottimo controllo finish.
3. **Aerografo + Vallejo Mecha Varnish + display in teca con vetro/acrilico UV-filter** — combinato.
4. **2K SprayMax Clear (aerosol 2K)** — circa 25–35 €/bomboletta. Si attiva pungendo la base, ha vita ~48 h. Risultato vicino al body shop. **Obbligatorio respiratore A2/P3** (isocianati).
5. **Verniciatura in body shop esterno** con poliuretano 2K — 30–100 € a pezzo a seconda complessità. Per pezzi di pregio è la mossa che alza il prodotto di una categoria.

---

## 5. Test casalingo di stabilità UV

Per validare la propria pipeline:

- Stampare 3 provini identici.
- Coat 1 = nudo. Coat 2 = solo primer + acrilico. Coat 3 = primer + acrilico + clear coat UV.
- Esporre per 30/60/90 giorni in finestra south-facing.
- Confrontare con campione "control" tenuto in scatola.
- Misurare con smartphone: foto a luce controllata, confronto delta-E con app come "Color Grab" o spettrofotometro Nix (~100 €).

---

## 6. Fonti

- Google Scholar query suggerite: `"PLA" "UV degradation" outdoor`, `"polylactic acid" photodegradation HALS`, `PLA UV stabilizer benzotriazole`.
- ScienceDirect: *Polymer Degradation and Stability* (Elsevier) — più rilevante.
- MDPI *Polymers* — open access, molte review.
- All3DP, "Is PLA UV Resistant?" — articolo introduttivo consumer.
- Prusa Knowledge Base, sezione "Filament guide" — buone tabelle proprietà.
- Forum: r/3Dprinting thread storici "PLA outdoor longevity", risultati comunitari ripetuti.
- SprayMax 2K technical datasheet (peter-kwasny.de / spraymax.com).
- Tru Vue Optium e Plexiglas Optical UV100 — datasheet ufficiali.
