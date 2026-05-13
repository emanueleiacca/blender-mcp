# 08 — A/B testing & analytics DIY

**Obiettivo**: validare ipotesi pricing/photo/title con strumenti free, evitando "feeling" e raccogliendo dati misurati. Setup zero-cost replicabile su Etsy e Shopify.

> Caveat metodologico: indie maker raramente ha sample size sufficiente per significatività statistica (servono >300 visit per leg per p<0.05 su differenze 10–20%). Usiamo "directional A/B" = trend chiaro a occhio anche se non scientifico.

---

## 1. Strumenti analytics free

### 1.1 Etsy

- **Etsy Stats**: built-in, https://www.etsy.com/your/shops/me/stats. Free.
  - Daily/weekly/monthly visits, favorites, orders, revenue.
  - Source breakdown: Etsy search, Etsy ads, social, direct.
  - Per-listing performance.
- **Etsy Search Analytics** (in Stats): keyword usate dai visitatori per trovare ogni listing.

### 1.2 Shopify

- **Shopify Reports** native (free su tutti i piani): traffic source, conversion, products, customers.
- **Google Analytics 4** (free, https://analytics.google.com): connessione via tag.
- **Google Search Console** (free): query keyword Google reali che portano al tuo sito.
- **Hotjar free** (https://www.hotjar.com/, 35 daily sessions): heatmap + session recording.
- **Microsoft Clarity** (https://clarity.microsoft.com/): 100% free, no limit sessions, heatmap + recording. **Migliore alternativa free a Hotjar 2024–2025**.

### 1.3 Social

- **Instagram Insights**: native business account, free.
- **TikTok Analytics**: native, free.
- **Pinterest Analytics**: native business account, free.
- **Meta Business Suite**: aggregato IG+FB, free.

### 1.4 Email

- **MailerLite / Kit / Mailchimp dashboards**: open rate, CTR, conversion (se UTM tagged).

---

## 2. Setup tracking minimo

### 2.1 UTM tagging

Per misurare quale canale converte, tagga **ogni link verso Etsy/Shopify** con UTM parameters.

Template: 
```
https://www.etsy.com/listing/123456789?utm_source=instagram&utm_medium=bio&utm_campaign=reel_marmorino_dec24
```

**Tool free**: **Google URL Builder** https://ga-dev-tools.google/campaign-url-builder/

Compila:
- `utm_source`: instagram / tiktok / pinterest / newsletter
- `utm_medium`: bio / story / reel / email
- `utm_campaign`: campaign-name-month-year

Etsy mostra source in Stats > Traffic. Shopify + GA4 mostra in Acquisition.

### 2.2 Google Search Console setup (Shopify)

1. Crea account: https://search.google.com/search-console
2. Aggiungi property "URL prefix" con dominio Shopify.
3. Verifica tramite HTML tag o file (Shopify supporta entrambi).
4. Dopo 1–2 settimane: vedi query Google reali → reverse-engineer keyword nuove.

### 2.3 Microsoft Clarity setup (Shopify)

1. https://clarity.microsoft.com → crea progetto.
2. Aggiungi script tag al theme Shopify (`<head>`).
3. Dopo 48h: heatmap + recording.
4. **Cosa cercare**: dove click rage / scroll incompleti / abbandono cart.

---

## 3. A/B testing su Etsy (limitato ma possibile)

Etsy **non supporta A/B test nativo**. Workaround:

### 3.1 Test sequenziale (single-listing)

Cambia **una variabile per volta** ogni 1–2 settimane. Pre-condizioni:
- Volume listing stabile (>15 visit/settimana).
- Stagionalità neutralizzata (non test in dicembre vs gennaio).

| Variabile | Periodo test | Cosa misurare |
|---|---|---|
| **Thumbnail (foto 1)** | 1 settimana A, 1 settimana B | CTR (visit/impression), conversion |
| **Title** | 2 settimane A, 2 settimane B | Search impression rank, conversion |
| **Price** | 1 settimana A, 1 settimana B | Conversion rate (a parità di visit) |
| **Description** | 2 settimane | Conversion |

### 3.2 Test parallelo (multi-listing simili)

Crea 2 listing **diversi** per stesso prodotto con variabile diversa:
- Listing A: prezzo €75
- Listing B: prezzo €95

**Caveat**: Etsy può penalizzare "duplicate listing" 2023+. Mitigation: differenziare leggermente (set vs singolo, dimensione, finitura).

### 3.3 Esempio test: thumbnail hero shot

- **Variante A** (settimana 1): hero shot scuro drammatica.
- **Variante B** (settimana 2): hero shot lifestyle (in casa).
- **Misura**: CTR (visit / impression).
- **Sample minimo**: ~100 impression/settimana per leg per trend chiaro.

Etsy Stats > Listing > "Search analytics" mostra impression + visit.

---

## 4. A/B testing su Shopify

### 4.1 Strumenti

| Tool | Free tier | Note |
|---|---|---|
| **Google Optimize** | Era free, **deprecato Sep 2023** | Non più disponibile |
| **VWO Free** | 50k visitors/mese free | Generoso, A/B + heatmap |
| **Convert.com** | 14 day trial | A/B avanzato |
| **Shopify native split test (theme)** | Free | Limitato a theme variants |
| **GA4 A/B custom** | Free | Setup manuale tramite custom dimensions |
| **Microsoft Clarity** | Free | NO A/B, ma sessione recording per qualitative |

**Raccomandazione piccolo brand**: **VWO Free** + **Microsoft Clarity**.

### 4.2 Test prioritari per Shopify

1. **Product page price test** (€75 vs €95).
2. **CTA button color** ("Add to cart" red vs black vs accent brand).
3. **Photo order** (hero first vs lifestyle first).
4. **Description length** (short vs long storytelling).
5. **Free shipping threshold** (€80 vs €100 vs €120).

### 4.3 Significatività statistica

Per indie maker con <1000 visit/mese, la **significatività statistica** è quasi sempre fuori portata. Use:
- **Directional trend**: 1 leg vince con >20% gap su 50+ conversion → vai con quello.
- **Long-running test**: lascia il test 4+ settimane prima di concludere.
- **Effect size > noise**: se differenza <10%, ignorare (probabilmente noise).

Calculator significatività: https://www.evanmiller.org/ab-testing/sample-size.html

---

## 5. Pricing A/B specifico

### 5.1 Setup (Etsy)

Approccio sequenziale 4 settimane:

| Settimana | Prezzo | Misura |
|---|---:|---|
| 1 | €80 | Baseline visit + conversion |
| 2 | €100 | Stesso |
| 3 | €120 | Stesso |
| 4 | €80 | Baseline retest (controllo stagionalità) |

**Output**: tabella conversion rate × prezzo → revenue per visit (RPV).
- €80: 100 visit, 5% conv = 5 sale × 80 = **400 €/100 visit**
- €100: 100 visit, 3% conv = 3 sale × 100 = **300 €/100 visit**
- €120: 100 visit, 2% conv = 2 sale × 120 = **240 €/100 visit**
→ **€80 vince in RPV**.

In altri casi:
- €80: 5% × 80 = 400
- €100: 4.5% × 100 = **450 €** ← winner
- €120: 3% × 120 = 360
→ **€100 vince**, perché conv drop solo del 10% con prezzo +25%.

### 5.2 Test bundle vs singolo

- Settimana 1: solo listing singolo €80.
- Settimana 2: aggiungi listing bundle 2 pcs €130.
- Misura: AOV totale store.

---

## 6. Foto A/B (highest ROI test)

### 6.1 Su Etsy

- Cambia **1° foto (thumbnail)** ogni 7 giorni.
- Misura **CTR = visit / impression**.
- Etsy Stats > Listing > Search Visibility.

### 6.2 Variabili photo da testare

1. **Background color** (white vs scuro vs lifestyle).
2. **Angle** (frontal vs 3/4 vs dall'alto).
3. **Lighting** (soft diffuso vs drammatico laterale).
4. **Composition** (pezzo solo vs con prop di scala).
5. **Crop** (full pezzo vs detail macro).

Tipicamente **drammatica/dark background** vince thumbnail vs **white box**: contrast cattura attenzione scroll. **[stima consensus Etsy forum]**, da verificare.

---

## 7. Tracking dashboard fai-da-te

Google Sheet semplice, aggiornato settimanalmente:

| Settimana | Listing | Visit | Impression | CTR | Conv | Revenue | Note |
|---|---|---:|---:|---:|---:|---:|---|
| W1 | Marmorino 12cm | 45 | 1200 | 3.75% | 2 | 160 € | Hero shot scuro |
| W2 | Marmorino 12cm | 52 | 1300 | 4.00% | 3 | 240 € | Hero shot lifestyle |

Aggiungere colonne per source (IG, TikTok, organic Etsy, Pinterest) → vedi quale canale converte meglio per ogni SKU.

**Tool free per dashboard**:
- Google Sheets nativo.
- **Looker Studio** (Google Data Studio, free, https://lookerstudio.google.com/): collega GA4 + Sheets → dashboard visivo gratis.

---

## 8. Qualitative analytics: capire il "perché"

Dati quantitativi (visit, conv) dicono **cosa** succede. Per capire **perché**:

### 8.1 Microsoft Clarity session recording

- Vedi 10–20 session rec/settimana di visitor che NON hanno comprato.
- Look for: dove scroll-stop, dove rage-click, dove abbandona.
- **Insight tipici**: "tutti scrollano fino a foto 5 e poi escono" → foto 5 è il break.

### 8.2 Customer feedback

- **Email a clienti** dopo 14 gg ordine: "che cosa ti ha convinto a comprare? cosa quasi ti ha fatto rinunciare?"
- Response rate ~15–25%. 5 risposte = oro.

### 8.3 Review reverse-engineering

Leggi review proprie + competitor. Quali parole ricorrono? "Texture incredibile" / "Più piccolo del previsto" / "Spedizione veloce". → usa nel titolo/description.

---

## 9. KPI dashboard mensile minimo

Track ogni mese, 30 min lavoro:

| Metrica | Sorgente | Target sano mese 6 |
|---|---|---|
| Etsy visit | Etsy Stats | Crescente MoM |
| Etsy conversion rate | Etsy Stats | 1–3% (benchmark Etsy 2024) |
| Etsy revenue | Etsy Stats | Definisci tu |
| Shopify visit (if active) | GA4 | Crescente |
| Shopify conv rate | Shopify Reports | 0.5–2% (più basso di Etsy) |
| Instagram follower | IG Insights | +5–15% MoM |
| Reel reach medio | IG Insights | Stabile o crescente |
| Pinterest impressions | Pinterest Analytics | Crescente |
| Email subscriber | Mailchimp/Kit | +10–30 nuovi/mese |
| Email open rate | Email tool | 25–40% (benchmark 2024) |
| Email CTR | Email tool | 2–5% |
| Repeat customer % | Etsy/Shopify | >15% dopo mese 6 |

**Benchmark fonte**: Mailchimp benchmarks https://mailchimp.com/resources/email-marketing-benchmarks/, Etsy seller forum consensus.

---

## 10. Errori comuni A/B

- **Test troppo brevi**: 3 giorni → noise. Minimo 7 gg.
- **Test multipli simultanei**: cambi foto + prezzo + title same time → non sai cosa ha mosso.
- **Sample troppo piccolo**: 20 visit/leg = puro caso.
- **Stagionalità non controllata**: novembre vs gennaio = diversi mondi.
- **Confirmation bias**: cerchi solo dati che confermano l'ipotesi → ignora controprova.

---

## 11. Tabella ROI test prioritari

| Test | Effort setup | Effort run | Costo | Uplift potenziale |
|---|---|---|---|---|
| Thumbnail A/B | 30 min/cambio | 1 settimana attesa | 0 | +10–30% CTR |
| Title A/B | 15 min | 2 settimane | 0 | +5–15% impression |
| Price A/B | 5 min | 4 settimane | 0 | +10–25% RPV |
| Description rewrite | 1 h | 2 settimane | 0 | +5–15% conv |
| Bundle test | 30 min new listing | 2 settimane | 0 | +20–40% AOV |
| Photo order A/B | 10 min | 1 settimana | 0 | +5–15% conv |
| Free ship threshold | 5 min | 4 settimane | 0 | +10–20% AOV |

---

## 12. Fonti

- **Etsy Seller Handbook**, sezione Stats: https://www.etsy.com/seller-handbook
- **Microsoft Clarity**: https://clarity.microsoft.com/
- **VWO**: https://vwo.com/
- **Google Analytics 4**: https://analytics.google.com/
- **Looker Studio**: https://lookerstudio.google.com/
- **Evan Miller A/B sample size calculator**: https://www.evanmiller.org/ab-testing/sample-size.html
- **Mailchimp Email Benchmarks**: https://mailchimp.com/resources/email-marketing-benchmarks/
- **Shopify Reports**: https://help.shopify.com/en/manual/reports-and-analytics
- **Pat Flynn** Smart Passive Income (analytics episodes).
- Reddit r/Etsy, r/Shopify (analytics threads).
