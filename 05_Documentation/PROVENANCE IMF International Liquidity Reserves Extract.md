# Provenance — IMF International Liquidity Reserves Extract

**Raw file:** `dataset_2026-09-12T19_47_51_749761953Z_DEFAULT_INTEGRATION_IMF_STA_IL_13_0_1.csv`
**SHA-256:** `d0e38cfbee99f6a78a84fea69e11d837cf998151955616916ab339c88ffbd29f`
**Status:** preserved exactly as uploaded — not modified, reshaped, rounded, or renamed. Copied byte-for-byte; checksum above can be used to confirm this at any later point.

## What is independently confirmed directly from the file's own contents (re-derived by Claude, not just taken from Ziba's summary)
- **Dataset/version tag (from file):** `IMF.STA:IL(13.0.1)`
- **Indicator (from file):** "Reserves excluding gold"
- **Unit / Scale / Frequency (from file):** US dollar / Millions / Monthly
- **Exact series codes (from file):**
  - Bangladesh: `BGD.RXF11_REVS.USD.M`
  - Pakistan: `PAK.RXF11_REVS.USD.M`
  - Vietnam: `VNM.RXF11_REVS.USD.M`
- **Coverage (independently recomputed from the file, not assumed):**
  - Bangladesh: 2018-M01 through 2026-M07, 103/103 observations, 0 missing
  - Pakistan: 2018-M01 through 2026-M07, 103/103 observations, 0 missing
  - Vietnam: 2018-M01 through 2026-M06, 102/103 observations, missing exactly `2026-M07`

## What rests on Ziba's own account of the IMF portal session (not independently verifiable from the CSV's contents alone)
- **Vintage selected: "Latest"** — this is a portal UI selection, not a field encoded in the CSV's data rows.
- **"Vietnam also has no 2026-M07 observation in the IMF portal's individual series search"** — this is consistent with what the CSV itself shows (the same gap), which corroborates it, but the individual-series-search check itself was performed by Ziba directly in the portal, not something Claude can independently re-verify without portal access.
- **Retrieval date:** taken from the timestamp embedded in the original filename (`2026-09-12T19:47:51.749761953Z`); not independently confirmed against an IMF server timestamp.

## Retrieval method (per the scoped exception)
Downloaded manually by Ziba directly from the IMF data.imf.org portal (not via API — the automated extraction attempt was blocked by this environment's network egress restrictions, logged separately in RESEARCH_LEDGER.md). This file is the authoritative raw source for the reserve variable per Ziba's explicit instruction; it has not been reconstructed, replaced, or supplemented with FRED/CEIC/Trading Economics/WDI data.

## Cross-checks performed against previously logged secondary/national figures (validation only — raw file was not altered)
- **Bangladesh, 2026-M01:** file shows $26,241.80mn. Previously logged (RESEARCH_LEDGER, from a Jan 8, 2026 BSS article) Bangladesh Bank's own same-date figures: gross $32.44bn, BPM6-basis $27.85bn. The IMF IL figure sits below both, closest to (but not identical to) the BPM6 figure — consistent with excluding-gold being a stricter cut than BPM6-basis alone. Gap not fully reconciled; recorded as a discrepancy, not silently smoothed over.
- **Vietnam, 2025-M12:** file shows $85,580.37mn. Previously logged Trading Economics figure for the same month (tagged "source: IMF" on their site) was $83,618.78mn — a ~2.3% difference. Possible causes not confirmed: different revision vintage, or TE's plain "Foreign Exchange Reserves" page not being the exact same series as IL's "Reserves excluding gold." Recorded as an open, unresolved discrepancy.
- **Pakistan:** no directly-dated cross-check was available from prior logged sources this pass; not compared.
