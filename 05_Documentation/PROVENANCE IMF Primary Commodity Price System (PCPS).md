# Provenance — IMF Primary Commodity Price System (PCPS) Energy Index Extract

**Raw file:** `dataset_2026-09-19T08_32_32_873152583Z_DEFAULT_INTEGRATION_IMF_RES_PCPS_9_0_0.csv`
**SHA-256:** `771bbcd4813696975101c565813b2892274d5b68edaaa2d2406b2b2ab8189a76`
**Status:** preserved exactly as uploaded — not modified, reshaped, rounded, or renamed.

## Confirmed from the file
- **Dataset/version:** `IMF.RES:PCPS(9.0.0)`
- **Series code:** `G001.PNRG.INDEX.M` — `G001` denotes a global/world entity code, not a specific country, consistent with this being deliberately a **common, non-country-specific** proxy
- **Country field:** "World"
- **Indicator:** "Energy index, Commodity price index, Index, 2016=100"
- **Data transformation:** Index (not a percent-change or other derived transform)
- **Frequency / Unit / Scale:** Monthly / Index, 2016=100 / Units
- **Coverage:** 2018-M01 through 2026-M08, **104/104 observations, zero missing**. Single row (one global series — no per-country breakdown needed or expected).

## Plausibility check (not a formal validation, but a strong internal-consistency signal)
- **Minimum: 55.89 at 2020-M04** — matches the globally well-documented COVID-19 oil-price collapse (April 2020, the month WTI crude briefly traded negative).
- **Maximum: 376.41 at 2022-M08** — matches the well-documented energy-price spike following Russia's invasion of Ukraine (February 2022), which peaked in mid-to-late 2022.
- Values moderate substantially by 2025 (e.g., 157.86 at 2025-M09), consistent with widely reported post-2022 energy-price normalization.

These are not proof of correctness on their own, but the series behaves exactly as the well-known global energy-price history would predict, which is a meaningful corroboration.

## Status
**VERIFIED for data definition and coverage.** No missing values, no duplicates (trivially, given a single global series), no anomalies found.

## Retrieval method
Downloaded manually by Ziba from the IMF's Primary Commodity Price System (PCPS) portal. Not reconstructed, replaced, or supplemented from any secondary source.

## Not yet done
This series has not been added to the master analytical dataset, and no stress-test, regression, or interpretive use has been made of it — this file covers source verification only, per standing instruction.
