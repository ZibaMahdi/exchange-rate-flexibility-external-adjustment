# Provenance — IMF Balance of Payments (BOP) Current Account Extract

**Raw file:** `dataset_2026-09-16T07_28_55_668351590Z_DEFAULT_INTEGRATION_IMF_STA_BOP_21_0_0.csv`
**SHA-256:** `f7c682cd4fc2a6328cb628a82a634692aa63d7a8cad08319c25da71ff332c29d`
**Status:** preserved exactly as uploaded — not modified, reshaped, rounded, or renamed.

## Independently confirmed directly from the file's own contents
- **Dataset/version:** `IMF.STA:BOP(21.0.0)`
- **Indicator:** "Current account balance (credit less debit)"
- **BOP Accounting Entry:** "Net (credits less debits)"
- **Unit / Scale / Frequency:** US dollar / Millions / Quarterly
- **Series codes:**
  - Pakistan: `PAK.NETCD_T.CAB.USD.Q`
  - Vietnam: `VNM.NETCD_T.CAB.USD.Q`
  - Bangladesh: `BGD.NETCD_T.CAB.USD.Q`
- **Coverage (independently recomputed):**
  - Pakistan: 2018-Q1 – 2026-Q2, **34/34, zero missing**
  - Vietnam: 2018-Q1 – 2026-Q1, 33/34, missing `2026-Q2`
  - Bangladesh: 2018-Q1 – 2026-Q1, 33/34, missing `2026-Q2`
- **Common three-country window: 2018-Q1 – 2026-Q1.** Pakistan's 2026-Q2 is retained for country-specific use only, not part of the common quarterly panel — same pattern established for reserves/exchange rate/remittances, just with Pakistan (not Vietnam) as the one ahead this time.

## Definition check (per instruction — not assumed from the requested label)
- **Genuinely the headline balance, not a subcomponent or the "excluding exceptional financing" variant:** confirmed — the file's own INDICATOR field reads "Current account balance (credit less debit)," with no "excluding exceptional financing" qualifier, and only one series per country was returned (no competing alternatives bundled in to choose between).
- **Sign convention:** credits less debits — positive = surplus, negative = deficit. Consistent with the data itself: Pakistan is predominantly negative (matches its well-documented chronic current-account deficits), Vietnam is predominantly strongly positive (matches its export-surplus profile), Bangladesh is mixed with a shift toward near-zero/positive by 2026-Q1 (consistent with the post-reform external-adjustment narrative this project is investigating — noted as a pattern in the raw data, not yet interpreted or attributed to the reform).
- **Quarterly flow, not a stock:** confirmed by FREQUENCY field and BOP's inherent nature as a flow statement.
- **USD:** confirmed by UNIT field.
- **Seasonally adjusted vs. not:** **no explicit SA/NSA field exists in this file's metadata.** IMF's standard BOP presentation is conventionally reported on an NSA (raw) basis at the international-compilation level — noted here as general practice, not as something this specific file confirms directly. Flagged as an open point, not asserted as fact.
- **BPM6-consistent for all three countries:** not explicitly tagged in this file (no BPM5/BPM6 field), but consistent with IMF's post-2012 practice of harmonizing all reported BOP data to BPM6 (per the "IMF.STA:BOP" dataset's own general description found during source identification) — an inference from IMF's stated general practice, not a field-level confirmation in this file.

## Retrieval method
Downloaded manually by Ziba from data.imf.org's Balance of Payments (BOP) dataset, per the indicator/accounting-entry combination confirmed in chat ("Current account balance (credit less debit)" / "Net (credits less debits)"). Not reconstructed, replaced, or supplemented from WDI, FRED, Trading Economics, CEIC, national sources, or search-result values, per standing project rule.
