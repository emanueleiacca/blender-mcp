# Next questions — Round 3

Domande emerse durante questa indagine pipeline industriale che meritano un
prossimo deep-dive.

---

## A. Misurazione (gap scientifico)

1. ★ **Time-tracking reale di un primo lotto pilota da 10 pezzi**: stopwatch
   su ogni fase, comparare con la stima di `03_end_to_end_timeline.md`. Dove si
   è sotto-stimato/sovra-stimato?
2. ★ **Pull-out test fai-da-te**: bilancia digitale + cavo + bottiglia con
   acqua per misurare pull-out di Ruthex M3 in Bambu Basic. Protocollo
   replicabile per validare i numeri Ruthex/CNC Kitchen sul setup reale
   dell'utente.
3. **Ironing su Bambu Basic White**: test Ra strumentato locale con
   profilometro a basso costo (Rauheitsprüfer DIN tipo TR200, ~300 €) o
   surrogate (high-res macro foto + diffuse reflectance smartphone).
4. **Failure rate effettivo heat-set su lotto 50**: tracking pezzo per pezzo
   per identificare il 5% di failure.

---

## B. Approfondimenti specifici heat-set

5. **Effetto chamfer/fillet imbocco** sulla pull-out: comparare 0 / 0.5 / 1.0
   mm chamfer.
6. **Inserto storto recuperabile**: si può riscaldare e raddrizzare, o va
   scartato?
7. **Inserti in alluminio vs ottone**: differenze pratiche su PLA?
8. **Boss design ottimale**: cilindrico semplice vs con costole vs con tasca
   esagonale di rinforzo. Test CNC Kitchen riproducibile?
9. **Embedded nut con pause M0** in Bambu Studio: workflow concreto e jig di
   posizionamento del dado. Confronto pull-out vs heat-set.

---

## C. Ironing avanzato

10. **Ironing su walls**: workaround creativi (rotazione del pezzo per stampare
    la faccia critica come top, poi ironing). Casi reali sul forum Bambu?
11. **Ironing + chimica**: top con ironing poi etile acetato vapor → effetto
    "vetrificato"? Esistono test?
12. **Combo ironing + Pledge Floor Care** (trick Round 1) per finitura
    porcellana senza vernice: foto reali e Ra misurata.

---

## D. Batch processing avanzato

13. **Print farm minima 2-3 Bambu A1**: ROI reale, gestione (network printing,
    monitor via Home Assistant?), spazio richiesto.
14. **Spray booth DIY documentato**: piano costruttivo passo-passo con filtri,
    ventola PC, scarico, costo finale e foto.
15. **Tracking SKU/lotto con QR code stampato sul fondo del pezzo**: workflow
    per non perdere identificazione su 50+ pezzi simili.
16. **Drying rack timer e automazione**: stoplight LED che indica "primer
    pronto sand" basato su timer Raspberry Pi.
17. **Ergonomia e burnout**: 4-6 h consecutive di sanding → tunnel carpale.
    Best practice (guanti, postura, breaks)?

---

## E. Pricing e mercato

18. ★ **Test A/B di pricing reale Etsy**: stesso prodotto a 80 / 110 / 140 €
    su listing diversi (paesi diversi per non viololare ToS), tracking
    conversion rate.
19. **Wholesale vs DTC**: vale aprire wholesale per gift shops indipendenti?
    MOQ tipici, condizioni.
20. **Instagram drop model** (release windowed, scarsità) per piccoli maker:
    case study reali con dati conversion.
21. **VAT/IVA per maker EU che vendono su Etsy**: regime forfettario IT,
    soglia 85k €, OSS one-stop-shop per EU cross-border. Riferimento commerciale.
22. **Tax planning maker hobbyist Italia**: quando obbligatorio aprire P.IVA?

---

## F. Outsourcing specifico

23. **JLCPCB FDM PLA quality reale 2025**: ordinare campione di 2-3 pezzi e
    documentare qualità (layer lines, dimensional accuracy, color) vs Bambu A1
    in-house.
24. **Servizi italiani di stampa 3D B2C**: alternative a Sculpteo/Craftcloud
    con sede IT (3DZ, 3DiTaly, Replica Plastica)?
25. **Painter italiani su commission**: lista verificata (IG, Etsy), tariffe
    tipiche per pezzo decor 12 cm finitura porcellana.
26. **Foto outsource**: prove pratiche Soona / Pulpix / fotografo locale
    Bologna-Milano, qualità output, ROI vs in-house setup permanente.

---

## G. Crossover Round 3

27. ★ **Brand book / visual identity** per piccolo brand 3D maker: template
    minimo (logo, palette, font, packaging mockup) costo zero o ~100 €
    freelancer.
28. **Storytelling per Etsy listing**: paper/data su cosa converte (about,
    process video, behind-the-scenes).
29. **Community / Discord / IG strategy**: dove postare per esposizione gratis
    (r/PrintedMinis, Bambu showcase, IG hashtag stack).
30. **Lo "stack legale" per maker IT che vendono online**: P.IVA forfettario,
    fattura elettronica, IVA OSS, gestionale (Fatture in Cloud, Aruba).
