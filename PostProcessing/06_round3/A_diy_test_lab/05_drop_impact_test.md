# 05 — Drop weight impact test (resistenza urto)

> **TL;DR**: lasciar cadere oggetti di peso noto da altezza progressiva
> rivela la **soglia di crack/chip** del tuo coating + PLA. Costo: €0.
> Replica brutalmente il "Gardner impact test" da laboratorio (€2000).

Risolve un gap implicito: i test 01-04 misurano adesione/colore/idrofobicità
ma **non robustezza meccanica**. Un cliente che fa cadere un pezzo da 50 cm
sul tavolo è la realtà; qui simuli prima della spedizione.

---

## 5.1 Concetto: energia di impatto

Energia cinetica di un oggetto che cade:
```
E = m × g × h
```
dove m = massa (kg), g = 9.81 m/s², h = altezza (m).

| Oggetto | Massa | Energia a 10cm | a 30cm | a 50cm |
|---|---|---|---|---|
| Moneta 1€ | 7.5g | 0.0074 J | 0.022 J | 0.037 J |
| Moneta 2€ | 8.5g | 0.0083 J | 0.025 J | 0.042 J |
| Vite M6×20 | ~6g | 0.0059 J | 0.018 J | 0.029 J |
| Bullone M10×30 | ~30g | 0.029 J | 0.088 J | 0.147 J |
| Pesetto bilancia 50g | 50g | 0.049 J | 0.147 J | 0.245 J |
| Martello piccolo 200g | 200g | 0.20 J | 0.59 J | 0.98 J |

Per riferimento, **Gardner impact test ASTM D2794** misura in inch-pounds:
1 in-lb ≈ 0.113 J. Coating "buono" per applicazioni decor: resiste a
**~0.5-1 J** senza crepa.

ASTM D2794 spec (reverse impact): https://www.astm.org/d2794-93r19.html

---

## 5.2 Setup laboratorio del povero — €0-5

| Item | Costo | Note |
|---|---|---|
| Bilancia cucina | €5-10 (Brico, Lidl) | per pesare oggetti di prova |
| Righello/metro | €1 (già hai) | misura altezza caduta |
| Smartphone slow-mo | €0 | filma impatto a 240/960 fps |
| Provini standard | €1 filamento | piastrine PLA 25×25×3mm |
| Tappetino "drop zone" | €0 | superficie dura (tavolo) o mezzo-dura (libro spesso) → vedi §5.3 |
| Tubo guida verticale (opzionale) | €2 | tubo PVC Brico 16mm, evita rimbalzo laterale del peso che falsa l'altezza |

**Totale: €3-8** (la bilancia è la vera spesa, ma vedila come investimento generale).

---

## 5.3 Configurazione test

### Variante A — "Pezzo cade sul tavolo"
Replica scenario reale: cliente fa cadere oggetto. Provino in caduta
libera da altezza H sopra una **superficie standardizzata** (tavolo,
pavimento ceramica, marmo).

**Problema**: il "danno" dipende sia dal coating che dal substrato
sottostante (PLA si frattura) → misuri robustezza del **pezzo intero**, non
del solo coating.

### Variante B — "Peso cade sul pezzo" (più scientifico)
Provino fermo sul tavolo. Lasci cadere peso noto da altezza H sopra il
provino. Coating dovrebbe assorbire/riflettere l'urto.

Setup:
- Provino su tappetino di gomma (3mm spessore, da Brico €2/m²) per
  attutire e isolare l'urto sul coating, NON sul PLA che fessura.
- Tubo guida PVC 16mm sospeso verticale sopra il provino, scala mm marcata
  con pennarello.
- Lasci cadere peso (bullone, vite) dentro il tubo da altezza progressiva.

Variante B è il tuo "Gardner povero". Più consistente.

---

## 5.4 Procedura

1. **Prepara provini**: 2 repliche per trattamento (ne distruggi alcuni).
2. **Test progressivo**: 10 cm → 20 cm → 30 cm → 50 cm → 80 cm.
3. Per ogni altezza:
   - Lascia cadere peso dentro il tubo guida.
   - Osserva (smartphone slow-mo se vuoi vedere il primo impatto).
   - Esamina coating con luce radente:
     - **Nessun segno**: pass, continua altezza superiore.
     - **Indentazione visibile**: pass borderline, nota altezza.
     - **Crack stellato dal punto impatto**: fail.
     - **Chip (frammento staccato)**: fail catastrofico.
   - Foto macro post-impatto.
4. Soglia: **prima altezza che produce crack o chip** = "drop threshold" del coating.
5. **Ripeti 3 volte** con stesso peso, stessa altezza, su 3 provini diversi
   → riduci varianza (drop test è rumoroso, ±20% facile).

---

## 5.5 Scoring proposto

| Drop threshold (con peso 8.5g moneta 2€) | Score | Significato |
|---|---|---|
| <10 cm crepa | 1 | Coating fragilissimo, NON spedire |
| 10-20 cm crepa | 2 | Marginal, OK indoor delicato |
| 20-30 cm crepa | 3 | Standard hobby OK |
| 30-50 cm crepa | 4 | Commerciale Etsy-grade |
| >50 cm tiene | 5 | Robusto, kid-friendly |

---

## 5.6 Test matrix consigliato

| ID | Trattamento | Soglia attesa |
|---|---|---|
| I0 | PLA Bambu Basic nudo | 30-50 cm (PLA è abbastanza tenace) |
| I1 | + Pledge | 30-50 cm (Pledge sottile, non cambia molto) |
| I2 | + MaxMeyer Trasparente Lucido | 30-50 cm |
| I3 | + Mr. Super Clear UV Cut | 30-50 cm |
| I4 | + Plasti-kote primer + bianco + clear | 20-40 cm (primer + bianco aggiunge spessore = più potenziale chipping) |
| I5 | + SprayMax 2K (riferimento R2-A) | 50-80 cm (2K è elastico) |

**Insight chiave**: il drop test spesso rivela che **lo strato spesso non
sempre è il più robusto**. Stratificazioni multi-coat (primer + base + clear)
con tempi cura inadeguati possono delaminare. Test ti dice se la tua "torta"
ha buona coesione strato-strato.

---

## 5.7 Test correlato — "thumb fingernail flick"

Versione even more brutal: piega l'unghia indietro, rilasciala come uno
schiocco sopra il coating. Equivale a impatto ~50-100mN, area piccolissima.

- **Nessun segno**: 5/5.
- **Suono "ticking" più sordo del controllo**: leggero ammaccamento (4/5).
- **Segno visibile**: 2-3/5.
- **Chip immediato**: 1/5.

Replicabile in 10 secondi su un provino qualunque. **Non rigoroso** ma
indicativo. Vedi anche `06_thumb_roll_and_tactile.md`.

---

## 5.8 Bias

1. **Rimbalzo del peso**: cadendo nel tubo può rimbalzare e colpire 2-3
   volte. Usa tubo lungo che catturi il peso dopo primo impatto, o stoppa
   manualmente.
2. **Punto di impatto**: il peso colpisce sempre nello stesso punto del
   provino → fatica accumulata. Sposta provino tra altezze, o usa zone
   diverse del provino.
3. **Substrato (tavolo)**: tavolo rigido vs molle → energia trasmessa diversa.
   Usa **sempre stessa base** (es. pannello MDF 20mm su pavimento).
4. **Geometria peso**: bullone con punta = stress concentrato; moneta
   piatta = stress distribuito. Risultati diversi. **Standardizza un singolo
   peso per tutti i test**.
5. **Temperatura**: PLA fragile a <15°C (sotto Tg). Coating idem. Testa a
   20-25°C.

---

## 5.9 Tempo & costo

- **Setup**: €3-8.
- **Per altezza × provino**: 30 sec + foto. Test completo a 5 altezze: ~5
  min/provino + foto.
- **6 trattamenti × 3 repliche**: ~100 min.

---

## 5.10 Fonti

- ASTM D2794 Reverse Impact: https://www.astm.org/d2794-93r19.html
- Gardner impact tester (commerciale): https://www.gardco.com/
- Energia cinetica formula: https://en.wikipedia.org/wiki/Kinetic_energy
- Project Farm "Hardest spray paint impact" — channel:
  https://www.youtube.com/@ProjectFarm
- AvE drop test methodology (philosophical):
  https://www.youtube.com/@arduinoversusevil2025
- r/3Dprinting durability tests: https://www.reddit.com/r/3Dprinting/
