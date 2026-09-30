# Provenance — IMF BOP Goods Exports/Imports Extract

**Raw file:** `dataset_2026-09-16T07_46_47_931846777Z_DEFAULT_INTEGRATION_IMF_STA_BOP_21_0_0.csv`
**SHA-256:** `4996e9c9226c783df84876c1a1853fa444a7f6273d227857ca8b69d901711cfc`
**Status:** preserved exactly as uploaded — not modified, reshaped, rounded, or renamed.

## Independently confirmed directly from the file's own contents
- **Dataset/version:** `IMF.STA:BOP(21.0.0)` — same dataset as the already-verified current-account file
- **Indicator:** "Goods" (single value across all 6 rows) — confirms **goods only**, not goods-and-services
- **Accounting Entry:** "Credit/Revenue" (exports) and "Debit/Expenditure" (imports) — two rows per country, six rows total
- **Unit / Scale / Frequency:** US dollar / Millions / Quarterly
- **Series codes:**
  - Pakistan: `PAK.CD_T.G.USD.Q` (exports), `PAK.DB_T.G.USD.Q` (imports)
  - Vietnam: `VNM.CD_T.G.USD.Q` (exports), `VNM.DB_T.G.USD.Q` (imports)
  - Bangladesh: `BGD.CD_T.G.USD.Q` (exports), `BGD.DB_T.G.USD.Q` (imports)
- **Sign convention, inspected not assumed:** every value across all six series is positive — zero negative observations found. Exports and imports are both reported as positive magnitudes (credit and debit flows respectively), not as a signed net figure. Confirmed by direct inspection of all 198 non-missing data points, not inferred.
- **Coverage (independently recomputed):**
  - Pakistan (both): 2018-Q1–2026-Q2, 34/34, zero missing
  - Vietnam (both): 2018-Q1–2026-Q1, 33/34, missing `2026-Q2`
  - Bangladesh (both): 2018-Q1–2026-Q1, 33/34, missing `2026-Q2`
- **No duplicate series codes.**
- **Common three-country window: 2018-Q1–2026-Q1** — identical to the already-verified current-account window. Pakistan's 2026-Q2 retained for country-specific use only.

## Consistency check against the already-verified current-account series (sanity check, not a formal reconciliation)
2018-Q1 goods trade balance (exports minus imports) vs. the current-account balance already verified for the same quarter:
- Pakistan: goods balance −$7,793mn vs. CA −$4,395mn → +$3,398mn from non-goods items (services/income/transfers) — consistent with Pakistan's known reliance on remittance inflows to partly offset a larger goods deficit.
- Vietnam: goods balance +$4,860mn vs. CA +$3,028mn → −$1,832mn from non-goods items — consistent with Vietnam's FDI-heavy profile (foreign investors' profit repatriation typically shows up as a net outflow in the income account).
- Bangladesh: goods balance −$4,575mn vs. CA −$2,260mn → +$2,315mn from non-goods items — consistent with Bangladesh's remittance-dependent external sector.
All three are directionally sensible given each country's known economic structure. This is a plausibility check, not proof of exact accounting reconciliation (the current account also includes services and secondary income beyond just goods and remittances).

## Metadata caveats (documented, not blockers — same standard already applied to the current-account file)
1. **No explicit BPM6 tag** in this file's metadata. BPM6-consistency is inferred from the IMF BOP dataset's documented general methodology (post-2012 harmonization), not confirmed field-by-field in this specific file — same caveat as the current-account file.
2. **No explicit seasonally-adjusted/non-seasonally-adjusted field.** IMF's BOP is conventionally NSA at the international-compilation level — general practice, not a field-level confirmation in this file.

## Retrieval method
Downloaded manually by Ziba from data.imf.org's Balance of Payments (BOP) dataset — the goods sub-account (Credit and Debit entries separately), same dataset already used for current account. Not reconstructed, replaced, or supplemented from any secondary source.
