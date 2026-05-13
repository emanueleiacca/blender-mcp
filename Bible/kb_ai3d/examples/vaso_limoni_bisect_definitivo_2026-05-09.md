# Esempio: Vaso limoni — bisect definitivo (KISS principle)

**Data**: 2026-05-09 (continuazione del case 2026-05-08)
**Soggetto**: Lo stesso vaso limoni del 2026-05-08 (vedi `vaso_limoni_2026-05-08.md` per setup)
**Materiale**: Gesso
**Stato**: ✅ **RISOLTO** dopo iterazione multi-strategia

---

## Contesto

L'output Hi3D 2.1 del 2026-05-08 era un blob lavorabile (decorazione corretta) ma con:
- Fondo non perfettamente piatto
- Base inclinata (~5° di tilt)
- Apertura superiore "blob" (mancata struttura)

## Tentativi falliti (lezione KISS)

### Tentativo 1 — Snap vertices to plane

```python
# Selezionato edge loop inferiore → snap a Z=0
```

**Risultato**: ❌ ha distorto la geometria. **User feedback**: "ti sembra la base di un vaso questa? deve essere circolare"

### Tentativo 2 — Delete bottom + fill

```python
# Delete bottom verts → fill new face
```

**Risultato**: ❌ fill ha creato N-gon distorto, non circolare

### Tentativo 3 — Fan triangulation

```python
# Fan triangulation da centroide
```

**Risultato**: ❌ ancora geometria irregolare

### Tentativo 4 — RITORNO al primo approccio (KISS)

**User feedback**: "torniamo alla prima soluzione"

```python
# Bisect singolo Z=4.98 (5mm sopra bbox_z_min)
# keep upper portion
# fill flat con grid_fill (max 8 edges)
```

**Risultato**: ✅ **FUNZIONA**

## Codifica nella KB (Regola 34 KISS)

**Regola 34 TESTING_LOG**: per fix base inclinata/spuria, **un singolo bisect Z=epsilon** è quasi sempre superiore a snap/delete/fan triangulation. KISS — non complicare ciò che funziona.

## Indicator post-bisect (Regola 35)

Dopo bisect, eseguire MCP `analyze_mesh_for_print` → metric `fill_islands_count`:
- **fill_islands_count = 1**: base perfettamente connessa, bisect riuscito ✅
- **fill_islands_count > 1**: ci sono cavità residue interne → seguire con `Mesh → Clean Up → Fill Holes`

Su vaso limoni post-bisect: `fill_islands_count = 1` ✅

## Output finale

- Polycount: 450k (post-decimate)
- Watertight: ✅
- `bbox_z_min = 0` ✅ (Regola 36)
- `contact_points_count = 1` (bottom flat, 1 contact area) ✅

## Stampa A1

- Layer 0.16 mm
- Orient: bottom flat a Z=0
- Supporti: tree organic 30° per limoni in overhang
- Brim: 5 mm
- Tempo: ~6h per 140mm height
- Risultato: ottimo. Cordone intrecciato visibile, limoni 3D ok, base perfettamente piatta

## Lezioni codificate

- ✅ **Regola 34 — KISS principle**: bisect singolo > tentativi sofisticati
- ✅ **Regola 35 — fill_islands_count** come quality indicator post-bisect
- ✅ **Vaso limoni 2-day saga** è il case study di riferimento per soggetti "structurally occluded"
- ⚠️ Snap/delete/fan triangulation = trappola — sembrano flessibili ma distorgono geometria circolare

## Cross-reference

- Regole 34, 35, 36 TESTING_LOG
- `examples/vaso_limoni_2026-05-08.md` (setup giorno 1)
- `tools/hitem3d-2.1.md` § 10.1 (soggetto cavo)
