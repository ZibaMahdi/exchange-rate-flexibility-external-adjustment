# Provenance — IMF Exchange Rates (ER) Extract

**Raw file:** `dataset_2026-09-13T15_34_30_478901807Z_DEFAULT_INTEGRATION_IMF_STA_ER_4_0_1.csv`
**SHA-256:** `9fc7cb1051150b322fec4a6ac132f671da9c9e5aea952285d6a92d1becf91491`
**Status:** preserved exactly as uploaded — not modified, reshaped, rounded, or renamed.

## Independently confirmed directly from the file's own contents
- **Dataset/version tag:** `IMF.STA:ER(4.0.1)`
- **Indicator:** "Domestic currency per US Dollar" (both variants)
- **Unit / Scale / Frequency:** Units (unscaled) / — / Monthly
- **Six rows = 3 countries × 2 indicator variants:**
  - `PAK.XDC_USD.PA_RT.M` (Period average) and `PAK.XDC_USD.EOP_RT.M` (End-of-period)
  - `VNM.XDC_USD.EOP_RT.M` and `VNM.XDC_USD.PA_RT.M`
  - `BGD.XDC_USD.EOP_RT.M` and `BGD.XDC_USD.PA_RT.M`
- **Coverage (independently recomputed):**
  - Bangladesh (both variants): 2018-M01 – 2026-M08, **104/104, zero missing**
  - Pakistan (both variants): 2018-M01 – 2026-M07, 103/104, missing only `2026-M08` (latest month not yet published — expected lag)
  - Vietnam, End-of-period: 2018-M01 – 2026-M06, 102/104, missing `2026-M07` and `2026-M08`
  - **Vietnam, Period-average: 2018-M01 – 2026-M06, 101/104, missing `2025-M08` in addition to `2026-M07`/`2026-M08`**

## Flagged finding — genuine internal gap, not just a trailing-edge lag
Vietnam's **period-average** rate is missing **2025-M08** specifically — a gap in the middle of an otherwise-continuous series, not the "latest month not yet published" pattern seen everywhere else in this project so far. Vietnam's **end-of-period** rate has no such gap. This is recorded as an unexplained break, not smoothed over, imputed, or assumed to be a simple reporting lag. No interpolation performed or planned.

## Retrieval method
Downloaded manually by Ziba from the IMF data.imf.org "Exchange Rates (ER)" dataset portal, per the scoped download instructions given in chat (countries: Bangladesh/Pakistan/Viet Nam; both End-of-period and Period-average indicators; monthly; 2018-01–latest; Latest vintage; CSV export). Not reconstructed, replaced, or supplemented from any secondary source, per standing project rule.
