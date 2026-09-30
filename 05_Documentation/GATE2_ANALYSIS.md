# GATE2_ANALYSIS.md — Descriptive Assessment of Bangladesh's May 2025 Exchange-Rate Reform

**Status: descriptive only. No causal inference, regression, forecasting, or stress testing performed.** Every number in this document traces directly to `data/derived/emp_klr_two_component.csv` (the already-locked EMP calculation) or `data/derived/master_analytical_dataset.csv` (the verified master dataset) — nothing was resourced, recomputed from raw files, or altered. The EMP methodology and its country-specific alpha values were not touched.

**Institutional wording used throughout:** the May 2025 change is referred to as a "more flexible exchange-rate arrangement" / "crawling peg with band," not a free float or fully flexible regime, per the locked terminology. The reform date is treated as **mid-May 2025**, with **May 2025** as the calendar reform month for window construction.

## Window design (fixed, not adjusted for results)

- **Pre-reform:** May 2024 – April 2025 (12 months)
- **Reform month:** May 2025
- **Post-reform:** June 2025 – May 2026 (12 months)
- **Full historical benchmark:** 2018-M02 – 2026-M06 (101 months, the full common EMP sample)

## A. Bangladesh reform-window summary

| Variable | Window | N | Mean | Median | SD | Min | Max |
|---|---|---|---|---|---|---|---|
| EMP | Pre-reform | 12 | 0.0072 | 0.0054 | 0.0284 | -0.0259 | 0.0814 |
| EMP | Reform month | 1 | 0.0190 | — | — | 0.0190 | 0.0190 |
| EMP | Post-reform | 12 | -0.0060 | -0.0009 | 0.0175 | -0.0539 | 0.0114 |
| EMP | Full historical | 101 | 0.0037 | 0.0020 | 0.0160 | -0.0539 | 0.0814 |
| %Δ exchange rate | Pre-reform | 12 | 0.88% | 0.00% | 2.03% | 0.00% | 7.00% |
| %Δ exchange rate | Reform month | 1 | 0.74% | — | — | 0.74% | 0.74% |
| %Δ exchange rate | Post-reform | 12 | -0.01% | 0.00% | 0.30% | -0.80% | 0.40% |
| %Δ reserves | Pre-reform | 12 | 1.00% | -1.83% | 8.75% | -7.45% | 17.36% |
| %Δ reserves | Reform month | 1 | -7.21% | — | — | -7.21% | -7.21% |
| %Δ reserves | Post-reform | 12 | 3.64% | 2.23% | 10.39% | -7.85% | 32.75% |
| %Δ remittances | Pre-reform | 12 | 3.87% | 9.20% | 17.11% | -24.61% | 30.38% |
| %Δ remittances | Reform month | 1 | 7.89% | — | — | 7.89% | 7.89% |
| %Δ remittances | Post-reform | 12 | 1.88% | -1.94% | 11.96% | -16.76% | 24.27% |

**Largest/smallest Bangladesh EMP observations:**
- Pre-reform: max **+0.0814 (2024-M05)**; min **-0.0259 (2024-M12)**.
- Post-reform: max **+0.0114 (2025-M07)**; min **-0.0539 (2025-M06)**.

Two things worth flagging descriptively, without drawing a causal line: **2024-M05's EMP value is also the largest in the entire 2018–2026 sample**, occurring almost exactly one year before the reform date — a period that also coincides with the earlier crawling-peg introduction logged in the ledger (Claim C-001). **2025-M06's EMP value is also the smallest in the entire sample**, occurring the month immediately after the reform. Both are notable coincidences in timing, not evidence of what caused them.

**Is May 2025 itself unusual relative to the pre-reform distribution?** May 2025's EMP (0.0190) sits **0.41 standard deviations above the pre-reform mean** — not an extreme value by conventional standards (a threshold of ±2 or ±3 SD is typically used to call something "unusual," per the KLR crisis-threshold tradition that is explicitly not being applied here). Descriptively, the reform month itself does not stand out as an outlier against the preceding year.

**Post-reform distribution vs. full historical distribution:** Bangladesh's post-reform EMP mean (-0.0060) is below both its pre-reform mean (0.0072) and the full historical mean (0.0037), while its standard deviation (0.0175) is close to the full-historical standard deviation (0.0160) — descriptively consistent with somewhat lower average pressure post-reform, without a large change in volatility. This is an observed pattern in the data, not a causal claim about the reform's effect.

## B. Bangladesh vs. Pakistan vs. Vietnam — EMP summary

| Country | Pre-reform mean (SD) | Reform month | Post-reform mean (SD) | Full historical mean (SD) |
|---|---|---|---|---|
| Bangladesh | 0.0072 (0.0284) | 0.0190 | -0.0060 (0.0175) | 0.0037 (0.0160) |
| Pakistan | -0.0023 (0.0159) | -0.0288 | -0.0113 (0.0205) | 0.0069 (0.0597) |
| Vietnam | 0.0035 (0.0053) | 0.0015 | 0.0000 (0.0039) | 0.0004 (0.0052) |

**An important caution this table itself surfaces:** all three countries show a pre-to-post decline in mean EMP over this identical calendar window — not just Bangladesh. Pakistan's and Vietnam's means also fall (Pakistan: -0.0023 → -0.0113; Vietnam: 0.0035 → 0.0000). Since Pakistan and Vietnam had no comparable exchange-rate reform in this window, **this shared pattern across all three countries is a reason for caution, not a reason to attribute Bangladesh's shift to its reform** — it may partly reflect common external conditions (see the energy-price context below) rather than anything Bangladesh-specific. Pakistan's EMP is also an order of magnitude more volatile than Bangladesh's or Vietnam's throughout the full sample (full-historical SD of 0.0597 vs. 0.016 and 0.005 respectively) — a scale difference worth keeping in mind when comparing the three visually.

## C. Bangladesh monthly detail, 2024-M05 through 2026-M05

Full table in `data/derived/gate2_bangladesh_monthly.csv` (25 rows: month, EMP, %Δ exchange rate, %Δ reserves, remittances level, energy price index level, period label). Two patterns worth surfacing descriptively:

1. **Reserves jumped from $19.0bn (2025-M05) to $25.2bn (2025-M06)** — a one-month increase of +32.75%, the largest in Bangladesh's entire sample — coinciding with, not necessarily caused by, the reform month.
2. **The global energy price index rose sharply in 2026-M03** (from ~159 to 242, a jump not matched by anything in Bangladesh's own reserve or exchange-rate data that month) and stayed elevated through 2026-M05. This is presented as external context only — the data show this external condition existed during the later post-reform window, without claiming it explains any particular Bangladesh observation.

## Distinguishing the four components (per instruction)

1. **Observed exchange-rate adjustment:** Bangladesh's EOP rate moved from ~117.7 (2024-M05) to ~122.75 (2026-M05) — most of the adjustment happened in discrete steps before and around the reform month (117.7→120→122 across mid-2024 to early 2025), with the rate essentially flat (122.6–122.9) for the twelve months after May 2025. This step-like pattern is consistent with the "crawling peg with band" description rather than continuous free-floating adjustment — an observation about the data's shape, not an assessment of the regime's design.
2. **Reserve accumulation/depletion:** reserves were roughly flat-to-declining pre-reform (~$17.4–20.6bn range) and higher and more variable post-reform (~$23.2–28.4bn range), with the single large jump noted above.
3. **Residual EMP after the reserve component:** EMP's post-reform decline (see Table A) is driven more by the reserve-change term than by exchange-rate changes, since %Δe was small and stable post-reform (mean -0.01%, SD 0.30%) while %Δr was larger and more variable (mean 3.64%, SD 10.39%) — descriptively, most of the post-reform EMP movement is coming from the reserves side of the index, not the exchange-rate side.
4. **External energy-price conditions:** covered in the energy-price chart and the 2026-M03 spike noted above — presented as contextual background, not incorporated into the EMP calculation itself (per the locked methodology, EMP uses only reserves and exchange rate).

**A large EMP value is not being read as a currency crisis indicator here** — KLR's 3-standard-deviation crisis threshold was deliberately not applied (per your standing instruction), and no month in this analysis is labeled a "crisis."

## Visualizations produced (rendered inline in chat, data sourced from the files above)

1. Bangladesh EMP, 2018-M02–2026-M06, full historical series, with the May 2025 reform month labeled on the x-axis.
2. Bangladesh exchange rate (EOP) and reserves, shown as **two separate panels** (not a dual-axis chart, per instruction), 2024-M05–2026-M05.
3. Comparative EMP, Bangladesh/Pakistan/Vietnam, 2018-M02–2026-M06 — note Pakistan's much larger scale compresses the visual comparison with the other two countries.
4. Global energy price index, 2018-M02–2026-M06, same window as the EMP series for direct visual reference.

## Limitations affecting interpretation (explicit, not buried)

- **This is a fixed 12-month/12-month window comparison with no statistical test of whether the pre/post difference is distinguishable from ordinary month-to-month variation** — the SDs reported are descriptive, not standard errors of an estimated effect.
- **Pakistan and Vietnam show the same directional EMP shift over the identical calendar window**, which weakens any temptation to read Bangladesh's shift as reform-specific without further work (a proper before/after design would need a comparison group correction, which this descriptive pass does not attempt).
- **The global energy-price spike in 2026-M03 falls inside the post-reform window** and could confound any later attempt to attribute the whole post-reform period's EMP behavior to the exchange-rate regime change alone.
- **GDP and CPI were not used as reform-window evidence**, per instruction — Bangladesh's fiscal-year convention and the WEO actual-vs-projection caveat on 2025–2026 would have made them unreliable for this specific window anyway.
- **Vietnam's remittances remain unresolved** — no three-country remittance comparison was attempted for this reason, only Bangladesh's own remittance pattern was examined.
- **KLR's reserve-concept alignment (IFS line 1L.d vs. our IMF IL series) remains "strong evidence, not ironclad"** — inherited from Gate 1, not re-litigated here.
- **None of this establishes causality.** Every finding above is a description of what the data show over these fixed windows, not an estimate of the reform's effect.
