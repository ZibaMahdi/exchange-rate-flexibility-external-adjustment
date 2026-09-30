# DATA_QA.md

Source-level and definitional issues identified so far. This is not a QA log of cleaned data yet (that starts at Gate 2, once we actually have files in /data/raw) — this is a running log of provenance-stage issues discovered while identifying sources at Gate 1.

---

## Permanent Scope Change — Three Variables Removed
**External debt, policy rate, and REER are OMITTED BY DESIGN** as of this instruction — not to be sourced, downloaded, analyzed, or revisited unless explicitly reinstated. Reason given: not necessary for the core research question, and removing them keeps the project focused and avoids unnecessary comparability problems (REER in particular had already surfaced a real comparability failure — see RESEARCH_LEDGER.md D-009, historical). Retained variable list: international reserves, nominal exchange rate, remittances, current account balance, exports, imports, GDP growth, CPI inflation, and an import-price/external-shock proxy for the stress-test component.

## Issue Log

**Issue 1 — Bangladesh reserves: gross vs. BPM6 basis — RESOLVED for the common/EMP variable, one open sub-item remains**
Bangladesh Bank publishes both a gross foreign exchange reserves figure and a lower figure computed under the IMF's BPM6 methodology. These differ materially (e.g., ~$31.2bn gross vs. ~$26.5bn BPM6 as of Dec 2025). **Resolved for cross-country/EMP purposes:** this project uses IMF International Liquidity (IL), not either Bangladesh Bank series, for the common reserve variable — see RESEARCH_LEDGER.md "CURRENT FINAL DECISION — Reserve Variable." This sidesteps the gross-vs-BPM6 choice for the harmonized layer entirely. **Still open, lower priority:** if Bangladesh's own country-specific section (Gate 5) wants to additionally present BB's national figure for local color, gross-vs-BPM6 still needs a pick at that point — not urgent, and not a blocker for anything else. **Kept open, not reconciled:** the IMF IL figure and BB's own BPM6 figure are close but not identical (Jan 2026: $26,241.80mn IL vs. $27.85bn BB-BPM6) — a real, logged, unexplained discrepancy, not evidence against using IL.

**Issue 2 — Pakistan reserves: SBP-held vs. total liquid reserves — RESOLVED for the common/EMP variable**
SBP reporting distinguishes reserves held by the central bank from total liquid foreign reserves (SBP + commercial banks). These are materially different figures. **Resolved for cross-country/EMP purposes:** this project uses IMF International Liquidity (IL), series `PAK.RXF11_REVS.USD.M`, not either SBP series, for the common reserve variable — see RESEARCH_LEDGER.md "CURRENT FINAL DECISION — Reserve Variable." SBP's own series remain available for Pakistan-specific descriptive detail only, not decided.

**Issue 3 — Vietnam reserves: no suitable regularly downloadable SBV monthly series located — RESOLVED via IMF International Liquidity**
No suitable, regularly downloadable State Bank of Vietnam reserves series was located through search — this remains true and is kept as history (see RESEARCH_LEDGER D-003, superseded). **No longer a blocker:** Vietnam is covered by IMF International Liquidity, series `VNM.RXF11_REVS.USD.M`, confirmed via an actual downloaded file (102/103 monthly observations, 2018-M01–2026-M06; no 2026-M07 in the current Latest vintage). The common three-country reserve variable uses this series for all three countries, not a mix of national-plus-IMF sources, so the earlier concern about within-dataset inconsistency (two countries national, one IMF) doesn't apply — all three now use the same IL series.

**Issue 6 — Pakistan: two non-identical official trade-data bases**
Pakistan has two official exports/imports series that are not identical: the State Bank of Pakistan's BOP/payments-record basis, and the Pakistan Bureau of Statistics' customs-record basis. SBP's own Monthly Statistical Bulletin cross-tabulates both, confirming a real gap between them. This is the same category of problem as Issue 1 (Bangladesh reserves basis) and Issue 2 (Pakistan reserves basis) — a definitional choice needed before these numbers can be compared to Bangladesh and Vietnam. Proposed default: BOP/payments basis, for consistency with the EMP/current-account framework — not yet confirmed as a decision.

**Issue 4 — IMF exchange-rate dataset: End-of-period VERIFIED clean; Period-average VERIFIED with one flagged internal gap**
The IMF Exchange Rates (ER) dataset (`IMF.STA:ER`) has been downloaded and independently inspected. Bangladesh and Pakistan have clean coverage (Pakistan missing only the most recent month, 2026-M08, an expected lag). **End-of-period: VERIFIED for 2018-M01–2026-M06, no missing observations.** **Period-average: VERIFIED for the same window, but with Vietnam's 2025-M08 genuinely missing** — a gap in the middle of the series, not a trailing lag, and not to be interpolated, backfilled, or silently dropped. Default for descriptive charts is end-of-period unless the research design later specifies otherwise; whether period-average is usable for EMP (and how 2025-M08 is handled if so) is a Gate 3 decision, not made yet. Common three-country sample end-date confirmed as 2026-M06, consistent with the reserves variable.

**Issue 5 — KNOMAD wind-down**
The World Bank's KNOMAD initiative (historically the go-to remittances data source in academic/policy work) describes itself as "active from 2013 until 2024" on its own site, i.e. no longer an ongoing program. Its bilateral remittance matrix is also the wrong granularity for this project (corridor-level, not national totals). This project should use national central-bank remittance series (confirmed available for Bangladesh; Pakistan and Vietnam not yet checked) plus World Bank World Development Indicators ("Personal remittances, received") as the aggregate cross-country comparator, not KNOMAD directly.

---

## Status vocabulary
See RESEARCH_LEDGER.md — every source/decision now carries one of: VERIFIED, SOURCE IDENTIFIED, UNRESOLVED, REJECTED. Nothing moves from SOURCE IDENTIFIED to VERIFIED without an actual downloaded file being inspected (per standing instruction — no exceptions for convenience).

## Issue 7 — Common three-country monthly sample ends 2026-M06, not 2026-M07
The common three-country monthly analytical sample ends in 2026-M06 because Vietnam has no 2026-M07 observation in the current IMF International Liquidity Latest vintage. Bangladesh and Pakistan both have a 2026-M07 observation (confirmed directly from the raw file); Vietnam's series stops at 2026-M06 (102/103 observations, independently recomputed from the file, not merely asserted). Bangladesh's and Pakistan's July 2026 values are retained in the raw data and may be used in country-specific descriptive material, but must not enter any three-country comparison requiring a common observation month. If a future IMF vintage adds a Vietnam July 2026 observation, that is a vintage update to be recorded prospectively — it does not retroactively change this raw-data record.

## Issue 8 — Bangladesh remittances: manually-extracted source, one flagged (unresolved) table anomaly
Bangladesh's remittance series came from a manually-extracted PDF table (Bangladesh Bank's July 2026 Monthly Report), not a native data-portal export — this distinction is preserved in `RESEARCH_LEDGER.md` and `PROVENANCE.md`. FY-total consistency checks passed (all differences ≤$0.02mn, rounding-level). One stray duplicate entry in the pasted table (`2858.76`, mislabeled FY "2025-2026") was treated as a rendering duplicate of the correctly-placed July 2026 figure, not confirmed against the source PDF — flagged, not silently resolved. Ziba has separately noted the live BB webpage shows slightly different values than this PDF report; not independently verified, and the PDF report is the selected vintage per explicit instruction. Any future reconciliation attempt should be logged as a vintage comparison, not a silent correction.

## Issue 9 — Pakistan remittances: raw-vs-seasonally-adjusted label not explicitly confirmed
The uploaded SBP EasyData series ("Total Cash Worker Remittances," `TS_GP_BOP_WR_M.WR0010`) carries no explicit "seasonally adjusted" or "raw" label in its metadata. Treated as the raw series (as requested) based on the absence of an "SA" marking, which is an inference, not a confirmed fact — noted in `PROVENANCE.md` for future reference if this needs firming up.

## Issue 10 — Bangladesh/Pakistan remittances: comparability not fully confirmed (open, not blocking)
A targeted check found SBP hosts two distinctly-titled products — plain "Workers' Remittances" and a separately-named "Workers' Remittances - Seasonally Adjusted" — supporting (not proving) that our series (`WR0010`, "Total Cash Worker Remittances") is the unadjusted one. Separately confirmed: Pakistan's series definition **widened in September 2020** to include Roshan Digital Account conversions, and its country-attribution basis changed in **July 2019** — both genuine, dated, Pakistan-specific definitional changes. No equivalent methodological detail was found for Bangladesh's "Wage earner's remittance" in this pass (an asymmetry in documentation depth, not evidence of a gap in BB's own methodology notes). Both series are conceptually similar (official, banking-channel, cash remittance-inflow totals in USD) but **not confirmed identical in scope**. VERIFIED status for observed coverage stands; this comparability question stays open and visible rather than assumed resolved.

## Master Analytical Dataset — Constructed

`data/derived/master_analytical_dataset.csv` (long/tidy format, **1,585 rows** as of the energy-price-index addition: country/global × variable × period, native frequency preserved — monthly, quarterly, and annual variables coexist without forced alignment) and its companion `DATA_DICTIONARY.md` and `data/derived/master_qa_summary.csv` are now built from already-verified raw/derived files only. Zero duplicate (country, variable, period) combinations; zero missing values (rows are only added when a real observation exists — no placeholder/invented rows). Vietnam's remittances have **zero rows in the master dataset**, deliberately — this reflects the genuine absence of data rather than an oversight, and is documented in the data dictionary and the gaps list below. The global energy price index (`energy_price_index`) was added with `country_iso3 = "WLD"` — a single shared series, not replicated across countries or merged into any quarterly/annual variable.

**Stata note (per instruction):** the Python EMP calculation remains the accepted implementation. `stata/03_EMP.do` was prepared and syntax-corrected but has **not** been independently executed — it is not represented as validated code, only as a prepared reproducibility artifact.

### Remaining data gaps that genuinely block later analysis
1. **Vietnam monthly national remittances — UNRESOLVED.** No nationwide monthly primary series located. Blocks any monthly three-country remittances comparison or a symmetric remittance-shock stress test across all three countries (Gate 6 will need an explicit, separately-documented design choice here, not a default).
2. **GDP growth 2025–2026 actual-vs-projection status — not resolved to the country level.** Blocks treating those two years as confirmed historical outcomes in the Bangladesh reform-period narrative or any descriptive trend claim spanning them.
3. **Bangladesh/Pakistan fiscal-year vs. Vietnam calendar-year labeling for GDP growth — not reconciled.** Blocks any GDP-growth comparison that assumes all three countries' "2025" or "2026" columns refer to the same 12-month window.
4. **Pakistan's raw-vs-seasonally-adjusted remittances classification — "very likely," not confirmed.** Lower priority than 1–3, but should be resolved before remittances feature in any precise cross-country monthly comparison.
5. **KLR reserve-concept alignment (IFS line 1L.d vs. our IMF IL "reserves excluding gold") — strong convergent evidence, not a single ironclad citation.** Doesn't block using the EMP series, but should be tightened before the paper states the two are equivalent as a matter of fact.

Nothing else identified this pass blocks proceeding — the current-account/exports/imports quarterly window and the monthly reserves/exchange-rate/EMP window are both clean and fully verified for their respective common samples.

## Not Yet Done (do not treat silence as "no issues")
- **Reserves, exchange rate, and Bangladesh/Pakistan remittances are VERIFIED** via actual inspected files. Vietnam remittances remain UNRESOLVED (no suitable nationwide monthly series located; fallback design proposed but not adopted — see RESEARCH_LEDGER.md D-005a).
- IRFCL harmonized-reserves country coverage — moot for reserves (IL used instead); not pursued further.
- Current account/BOP and exports/imports sources found in Batch 2 — not yet inspected against an actual file.
- External debt, GDP, inflation, policy rate, REER sourcing not yet attempted.
- Pakistan trade-basis choice (SBP BOP-basis vs. PBS customs-basis) not yet decided — unrelated to reserves/exchange rate/remittances, still open.
