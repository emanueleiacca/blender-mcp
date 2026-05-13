# 05 - Errori comuni: diagnosi e prevenzione

Catalogo dei difetti tipici nella pittura spray di pezzi PLA, cause e rimedi.

## 5.1 Orange peel (buccia d'arancia)

Sintomo: superficie texturata simile a buccia di arancia (puntini/avvallamenti).

Cause possibili:
- Spruzzo da troppo lontano (>40 cm): le goccioline si "asciugano in aria" prima di toccare la superficie
- Vernice troppo viscosa (temperatura lattina bassa, <15 gradi C)
- Mano troppo sottile (atomizzazione frammentata)
- Umidita >70 percento
- Vernice agitata poco

Prevenzione:
- Distanza 20-30 cm
- Lattina a 20-22 gradi, agitazione 2 min
- RH 40-60 percento

Rimedio:
- Carteggiare zona affetta a 800-1200 grit dopo cura (24 h)
- Riapplicare 1 wet coat ravvicinata (20 cm) per "fondere" la pelle
- Se grave: stripping con isopropilico o stripper apposito e ricominciare

## 5.2 Runs / drips (colature)

Sintomo: gocce o "lacrime" sulla superficie verticale.

Cause:
- Spruzzo troppo vicino (<15 cm) o troppo prolungato sulla stessa zona
- Mano troppo pesante (wet coat invece di mist coat)
- Lattina troppo calda (>30 gradi)

Prevenzione:
- Rule of thumb: passata continua a velocita 30-40 cm/s, mai fermarsi
- Iniziare premere il bottone PRIMA del pezzo, rilasciare DOPO
- Mani sottili sovrapposte 50 percento

Rimedio:
- Se la goccia e' ancora bagnata: NON toccare. Lasciare colare e asciugare.
- Dopo cura completa: carteggio 600 -> 1200 -> 2000 con riapplicazione mano leggera

## 5.3 Fisheye (occhi di pesce)

Sintomo: piccoli crateri circolari nella vernice fresca, come se la vernice "respingesse" da puntini.

Causa primaria: contaminazione superficiale con silicone, oli, cere, o residui di rilascio stampante. Anche umidita estrema.

Su PLA Bambu A1 specifico: residui di lubrificante dei rod possono trasferirsi al pezzo via mani; sgrassare SEMPRE con IPA prima.

Prevenzione:
- Lavaggio sapone neutro + IPA 90+ percento, 2 cicli
- Maneggiare con guanti nitrile dopo sgrassaggio
- Pulire spray booth da residui WD-40 / silicone (mai usarli vicino)

Rimedio:
- Cura totale, carteggio 800, sgrassaggio profondo, riapplicare con additivo "fisheye eliminator" (poco usato hobby; piu' automotive)

## 5.4 Blooming / blushing (alone bianco)

Sintomo: pellicola lattiginosa/biancastra opacizzante, soprattutto sui colori scuri o sui clearcoat.

Causa: umidita >70 percento. Il solvente evaporando raffredda la superficie sotto il dew point; vapore acqueo condensa nella pellicola fresca.

Su pezzi PLA succede spesso in estate (cantina umida) o inverno (interno riscaldato vs esterno freddo).

Prevenzione:
- Misurare RH con igrometro economico (5 EUR su Amazon)
- Spray sotto 65 percento RH
- Mai spruzzare in giornate nebbiose o piovose
- Riscaldare leggermente il pezzo prima (asciugacapelli a 30 cm, NON oltre 40 gradi - PLA inizia a flettere a 55-60 gradi)

Rimedio:
- Se l'alone e' superficiale e fresco: clearcoat "retarder" (rallentante) o nebulizzazione di solvente puro per "fondere"
- In caso lieve: aspettare 24 h, talvolta l'alone svanisce con la cura
- Grave: stripping e refare

## 5.5 Primer che "bagna" / accentua le layer lines

Sintomo: dopo primer, le linee FDM sembrano peggio di prima.

Cause:
- Primer con solvente debole che non riempie ma "evidenzia"
- Primer troppo sottile / wash effect
- Layer lines erano gia profonde, nessun filler usato

Prevenzione: per Bambu A1 layer 0.16-0.28 mm, valutare sempre filler primer (Rust-Oleum Filler) o 2K filler airbrush (Vallejo Plastic Putty) prima del primer fine.

Rimedio: filler primer in 2-3 passate carteggiate, poi primer fine.

## 5.6 Scrostamento (paint flaking) / scarsa adesione su PLA

Sintomo: dopo 24 h, il primer viene via a scaglie con unghia o nastro.

Cause:
- PLA non sgrassato
- Primer water-based su superficie troppo liscia (PLA stirato a 0.08 mm o liscio per acetone/IPA polish)
- Cura insufficiente prima del topcoat
- Mismatch chimico (acrilico su lacca non curata = bleeding/lift)

Prevenzione:
- Sgrassaggio rigoroso
- Carteggiatura leggera 400 grit per "fare tooth" anche su zone gia lisce
- Cura primer 24 h prima del topcoat
- Test su zona nascosta

Rimedio: rimuovere a stripper (Simple Green per acrilici, isopropilico per alcuni primer), ricominciare con primer piu' aggressivo (Tamiya, Mr.Surfacer).

## 5.7 PLA che si crepa o si gonfia dopo il primer

Sintomo: micro-crack ("crackle") o gonfiore della superficie sotto primer.

Cause:
- Primer/lacca con solvente troppo aggressivo (alcuni Plastikote vecchi, vernici a base MEK, automotive 2K isocianati pesanti)
- Mano troppo carica = il solvente non evapora, attacca il PLA
- Pezzo ancora caldo dopo stampa (PLA piu' sensibile a stress termico residuo)

Prevenzione:
- Mai usare lacche celluloiche o stripper acetone-based su PLA
- Far riposare il pezzo 24 h dopo stampa
- Test di compatibilita su zona nascosta
- Mani SOTTILI (rispettare distanza)

Rimedio: nessuno; ricominciare. Lezione: il PLA tollera bene Tamiya, Mr. Hobby, Citadel, Rust-Oleum, Krylon, Montana, Vallejo. NON tollera bene primer "automotive 2K" pesanti, lacche celluloiche pure, smalti a base nitro vintage.

Riferimento solvent crazing su PLA: discussione su Prusa forum e Wevolver
(https://www.wevolver.com/article/acetone-pla).

## 5.8 Reazione con supporti residui / brim

Sintomo: in corrispondenza di punti di contatto supporti, la vernice si comporta diversamente (opaca, scrostata, lucida diversa).

Cause:
- Plastica leggermente fusa o sovra-estrusa al punto di contatto
- Residui di filamento poco compatto
- Differenza di rugosita

Prevenzione:
- Carteggiare pezzo ovunque a 400 prima del primer
- Tagliare via supporti con lama affilata e rifinire le cicatrici

## 5.9 Spitting (sputi della bomboletta)

Sintomo: la bomboletta espelle grumi o gocce grossolane invece di nebbia.

Cause:
- Nozzle ostruito da residui di vernice (tipico Montana Gold, Citadel, Tamiya dopo uso prolungato)
- Lattina quasi vuota
- Mancata agitazione (sedimentazione pigmento sul fondo)
- Capovolta troppo durante l'uso

Prevenzione:
- Capovolgere e spruzzare a vuoto per 2 sec a fine sessione (pulisce nozzle)
- Pulire nozzle con thinner o estrarlo e immergerlo
- Agitare 2 min + ogni 30 sec durante

Rimedio: sostituire nozzle (Montana, Krylon, Citadel vendono nozzle ricambio).

## 5.10 Tackiness persistente

Sintomo: dopo 24 h il pezzo e' ancora appiccicoso al tatto.

Cause:
- Mano troppo carica (solvente intrappolato)
- Temperatura bassa nella stanza
- Umidita alta che rallenta cura
- Topcoat incompatibile sopra primer non curato

Prevenzione:
- Mani sottili, attesa tra le mani
- Curare in stanza calda (22-25 gradi), bassa umidita
- Aspettare 5-7 giorni per cura piena su Rust-Oleum/Krylon su plastica

Rimedio: tempo + calore moderato (lampada a 40 cm, 30 gradi max). Se persiste oltre 7 giorni: stripping.

## 5.11 Tabella diagnosi rapida

| Sintomo | Causa piu' probabile | Quick fix |
|---|---|---|
| Buccia d'arancia | Distanza eccessiva | Avvicinare a 25 cm, riapplicare leggero |
| Colature | Troppo vicino / mano carica | Carteggio post-cura |
| Crateri circolari | Contaminazione silicone | Sgrassaggio + riapplicare |
| Alone bianco | Umidita >70 percento | Aspettare condizioni asciutte |
| Layer lines piu' visibili | Mancato filler primer | Filler primer + carteggio |
| Vernice via con unghia | Mancato sgrassaggio / cura | Stripping + restart |
| Crack/crackle PLA | Solvente troppo aggressivo | Cambiare primer |
| Sputi grumosi | Nozzle ostruito | Pulire/sostituire nozzle |
| Pezzo appiccicoso a 24 h | Mano carica + temp/umidita | Tempo + calore moderato |

## Fonti
- Eastwood, Fisheyes/Solvent Pop: https://www.eastwood.com/garage/how-to-prevent-and-fix-fisheyes-or-solvent-pop-in-paint-jobs/
- MIG Welding UK, Rectifying spray faults: https://www.mig-welding.co.uk/paint-faults.htm
- Sherwin-Williams, Fish Eyes: https://www.sherwin-williams.com/painting-contractors/products/resources/SW-ARTICLE-PRO-FISHEYES
- Paint Sprayer Zone, Fish eyes craters pinholes: https://paintsprayerzone.com/fish-eyes-craters-pinholes-differences/
- Tangible Day, Top 3 mistakes priming miniatures: https://tangibleday.com/mistakes-to-avoid-when-priming-miniatures-solutions/
- Wevolver, PLA and acetone smoothing: https://www.wevolver.com/article/acetone-pla
- Prusa Blog, chemical smoothing: https://blog.prusa3d.com/improve-your-3d-prints-with-chemical-smoothing_36268/
- Pinside, Rustoleum 2X problems: https://pinside.com/pinball/forum/topic/help-major-recurring-problem-with-rustoleum-2x
- CyPaint, fisheye/pinhole defects: https://cypaint.com/article/what-causes-fisheyes-and-pin-holes-in-paint
