# _next_questions — A_diy_test_lab (round 3 → round 4 spunti)

Spunti emersi durante la stesura del lab DIY. Da approfondire in round 4
con altri test, ricerca, o esecuzione effettiva del protocollo 14gg.

---

## Validation / esecuzione protocollo

### 1. **Eseguire effettivamente il protocollo 14gg**
Tutto il round 3 è "ricetta". Round 4 dovrebbe essere "ho cucinato e questo
è il piatto": eseguire il protocollo, riportare numeri **veri** in
`07_excel_template_radar.md` sostituendo l'esempio fittizio.

### 2. **Cross-validation R3 povero vs R2 ufficiale**
Eseguire **stesso test set** una volta col kit povero (€2.50 cross-hatch) e
una volta col kit Elcometer 107 + Tesa 4651 (€80) per misurare il **delta
di accuracy**. Output: "il kit povero diverge da quello ufficiale di X
punti su Y trattamenti" → quantifica il trade-off.

### 3. **Inter-operator reliability**
Far eseguire stesso test a 3 persone diverse, misurare la varianza
operatore. Quanto cambia il risultato thumb roll tra famigliari? Tactile
rank tra amici? Output: errore "operatore" da sottrarre al segnale.

---

## Test aggiuntivi che il R3 NON copre

### 4. **Gloss meter cinese €40 Aliexpress**
Spettrofotometro gloss a 60° → misura Gloss Units. Quantifica "quanto lucido"
oggettivamente. Connessione `_next_questions.md` E_diy_budget #11.
Cerca: https://www.aliexpress.com/wholesale?SearchText=gloss+meter+60

### 5. **Profilometro DIY laser**
Smartphone + laser pointer + setup triangolazione → micro-rugosità misurata
in µm. Vedi paper "DIY profilometer with smartphone" su Google Scholar.
Alternativa al tactile rank quando vuoi numero, non solo ordinamento.

### 6. **Spectrophotometer pocket DIY** (Public Lab)
Public Lab DIY spectrometer kit (€25) + smartphone:
https://publiclab.org/wiki/spectrometry
Misura assorbimento UV nel coating → conferma "ha davvero UV blockers?".

### 7. **Test "lavabilità" — spugna abrasiva ASTM D2486**
Ciclatore "wash test" DIY con motorino di una vecchia macchinetta usa-getta
+ Arduino + spugna. Conta N passate prima del breakdown coating.

### 8. **Test "termico real-world auto"**
Provini in auto al sole d'estate per 1 settimana, T misurata con
termoigrometro Aliexpress €8. Conferma trade-off PLA Tg 60°C in R2-A §7.

### 9. **Salt spray DIY (ASTM B117 povero)**
Vasca chiusa con nebulizzatore + acqua salata 5% → 100h test "ambiente
costiero" per pezzi venduti in zone mare. Costo: <€20.

### 10. **Test "abrasione carta vetrata su rotante"**
Trapano Brico (€20 Lidl/Parkside) + disco gomma + carta vetrata 600 →
misuratore di durabilità coating semi-quantitativo. Conta secondi prima
del breakdown.

---

## Refinement metodologico

### 11. **Bias removal automatico Excel template**
Aggiungere al template `07` formule per **z-score normalization** invece di
min-max. Output più resistente ai outlier.

### 12. **App "Color Grab" calibration session**
Sequenza standard di 3 patch ColorChecker da fotografare ogni sessione →
calibrazione auto. Procedure step-by-step. Convergenza ΔE con calibrazione.

### 13. **Replicabilità inter-batch**
Fa il protocollo 14gg una volta a Marzo (RH bassa, T 20°C), una volta a
Luglio (RH alta, T 30°C). Confronta. Il workflow funziona estate vs
inverno? Quali parametri cambiare?

### 14. **Cross-hatch su superfici curve**
Il test 01 funziona solo su piatti. Per pezzi curvi serve adattamento. Test:
provino piatto del stesso batch dà gli stessi risultati di un patch curvo
piccolo? O serve test dedicato?

### 15. **Smartphone different brands → bias colore**
Stesso provino fotografato con Samsung S20 vs iPhone 13 vs Xiaomi → quanto
differiscono i ΔE letti? Output: "scelgo uno smartphone per tutto il
protocollo" o "uso solo uno specifico modello".

---

## Connessione con R2 ancora aperta

### 16. **Validare il Preval sprayer Pledge** (R2-E _next #5)
Includere T_Preval nei test 14gg. Confronto "Pledge pennello" vs "Pledge
Preval spray" → veridicità claim "spray gloss €0.05/pezzo".

### 17. **Validare Lidl Crelando = Vallejo Studio?** (R2-E _next #18)
Test 01+02+04 con T_Crelando come trattamento extra. Conferma o smentisce
hypothesis "Crelando Lidl = Vallejo Studio fornitore comune".

### 18. **Validare cera Kiwi + Pledge layering** (R2-E _next #13)
Aggiungere T_KiwiPledge → test 03 water bead per verificare se la cera
intrappolata sotto Pledge dura.

---

## Round 5+ idee

### 19. **A/B test cliente reale**
Vendere 20 pezzi col workflow validato R3, 20 pezzi col workflow attuale
non-validato. Track reviews/return rate Etsy. Differenza percepita?

### 20. **YouTube post "I tested 6 PLA coatings DIY style"**
Content marketing della stessa ricerca: monetizza il protocollo come
contenuto. Project Farm-style video. ROI: traffico al brand Etsy.

### 21. **Citizen science co-test**
Distribuire il protocollo a 10 makers IT, raccogliere risultati aggregati.
Più data, più decisioni informate. FabLab + r/3Dprinting community.

### 22. **Test "alimentare-safe" decoupage**
Pledge + sigillante chiaro + cera alimentare → uno strato che reggerebbe
contatto con alimenti secchi (pane, frutta da decor)? Vedi _next E_diy #12.

### 23. **Cabinet UV "vero" cinese €100-200**
Aliexpress vende mini UV cabinet hobby per resin curing. Test: irradiance
reale misurata con UV sensor €15 — è davvero meglio della lampada €20
solitaria? Trade-off costo vs riproducibilità.

### 24. **Estensione test multi-substrato**
Stessi 6 trattamenti su PETG, ABS, ASA, PLA-CF. Workflow validato R3 per
PLA Bambu Basic; in futuro brand può espandere a altri filamenti.
