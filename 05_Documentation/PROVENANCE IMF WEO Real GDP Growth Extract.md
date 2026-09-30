# Provenance — IMF WEO Real GDP Growth Extract

**Raw file:** `dataset_2026-09-16T18_52_19_183124519Z_DEFAULT_INTEGRATION_IMF_RES_WEO_9_0_0.csv`
**SHA-256:** `08a34fdc744d47dad27faecec677a62cc29fdbf478e8c91133a0849dfbb81fbf`
**Status:** preserved exactly as uploaded — not modified, reshaped, rounded, or renamed. No observations overwritten or altered.

## Confirmed from the file
- **Dataset/version:** `IMF.RES:WEO(9.0.0)` — **April 2026 vintage** (confirmed via IMF's own WEO Database Appendix: estimates/projections based on statistical information through April 1, 2026)
- **Series codes:** `BGD.NGDP_RPCH.A`, `PAK.NGDP_RPCH.A`, `VNM.NGDP_RPCH.A`
- **Indicator:** "Gross domestic product (GDP), Constant prices, Percent change" — Annual real GDP growth, percent change
- **Coverage:** 2018–2026, 9/9 observations for all three countries, zero missing, zero duplicates

## Fiscal-year vs. calendar-year convention
Bangladesh and Pakistan's national accounts use a **July–June fiscal year**; Vietnam follows the **calendar-year** convention. This affects how the file's "2025"/"2026" column labels should be read for Bangladesh and Pakistan specifically — not resolved further this pass, flagged for whenever these figures are actually used in analysis.

## Actual vs. projection
Per WEO documentation, **2026–27 figures are projections**. Per-country "last data update" notes (referenced in IMF's Database Appendix as existing in the online WEO database) were not independently retrieved for Bangladesh, Pakistan, or Vietnam specifically. **2025 and 2026 are flagged as non-historical/latest-vintage observations, not treated as realized outcomes, pending more precise country-level classification** — this is a metadata caveat, not a resolved fact for every year in that range.

## Status
**VERIFIED for data coverage and definition.** Carries an explicit **ACTUAL-VS-PROJECTION METADATA CAVEAT** covering 2025–2026 (and, for Bangladesh/Pakistan, the fiscal-year labeling question) — not to be treated as fully resolved history until addressed directly.

## Retrieval method
Downloaded manually by Ziba from data.imf.org's WEO dataset. Not reconstructed, replaced, or supplemented from any secondary source.
