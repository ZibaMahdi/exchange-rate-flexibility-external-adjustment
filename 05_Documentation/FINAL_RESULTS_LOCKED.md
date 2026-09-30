# FINAL_RESULTS_LOCKED.md

**Status: LOCKED.** These are the project's final approved numerical results as of Gate 3 completion and paper/policy-note drafting. Future work must treat these as fixed unless a material error is discovered. If a result must change: identify the affected result ID below, explain why, rerun only the affected calculation, update `RESEARCH_LEDGER.md`, invalidate downstream outputs (paper, policy note, any figure derived from the changed number), and explicitly note the change here — never silently substitute a new number.

All results below trace to `data/derived/emp_klr_two_component.csv`, `data/derived/master_analytical_dataset.csv`, `data/derived/gate2_event_window_summary.csv`, and `data/derived/gate3_stress_test.csv`. Full provenance for every underlying input is in `RESEARCH_LEDGER.md` and `DATA_QA.md`.

---

## R-001 — Bangladesh EMP, reform-window summary
- Pre-reform mean (2024-M05–2025-M04, n=12): **0.0072** (SD 0.0284)
- May 2025 (reform month): **0.0190**
- Post-reform mean (2025-M06–2026-M05, n=12): **−0.0060** (SD 0.0175)
- Full historical mean (2018-M02–2026-M06, n=101): **0.0037** (SD 0.0160)
- Source: `gate2_event_window_summary.csv`, variable `EMP_klr`, country BGD

## R-002 — Bangladesh EMP extremes (full sample)
- Largest: **+0.0814, May 2024** (pre-reform)
- Smallest: **−0.0539, June 2025** (post-reform)
- Source: `emp_klr_two_component.csv`, country BGD

## R-003 — Bangladesh reserve/exchange-rate reform-window detail
- June 2025 reserve change: **+32.75%** (from ~$19.0bn to ~$25.2bn), the largest monthly reserve increase in Bangladesh's sample
- Post-reform mean %Δ exchange rate: **−0.01%** (SD 0.30%)
- Post-reform mean %Δ reserves: **+3.64%** (SD 10.39%)
- Source: `gate2_bangladesh_monthly.csv`, `emp_klr_two_component.csv`

## R-004 — Cross-country EMP comparison (identical calendar windows)
| Country | Pre-reform mean (SD) | May 2025 | Post-reform mean (SD) | Full historical mean (SD) |
|---|---|---|---|---|
| Bangladesh | 0.0072 (0.0284) | 0.0190 | −0.0060 (0.0175) | 0.0037 (0.0160) |
| Pakistan | −0.0023 (0.0159) | −0.0288 | −0.0113 (0.0205) | 0.0069 (0.0597) |
| Vietnam | 0.0035 (0.0053) | 0.0015 | 0.0000 (0.0039) | 0.0004 (0.0052) |

**Locked interpretive constraint attached to R-004: all three countries decline from pre- to post-reform. This comparator pattern must always be reported alongside R-001, never omitted, in any future use of R-001.**
Source: `gate2_comparative_emp.csv`

## R-005 — Four-quarter stylized stress test (baseline 2025-Q2–2026-Q1)
| Country | Baseline CA ($mn) | Combined deterioration ($mn) | Shocked CA ($mn) | Shocks included |
|---|---|---|---|---|
| Bangladesh | 161.0 | −12,258.14 | −12,097.13 | Remittance −10%, Export −5%, Import-price +10% |
| Pakistan | 449.98 | −11,850.34 | −11,400.35 | Remittance −10%, Export −5%, Import-price +10% |
| Vietnam | 31,023.0 | −70,616.15 | −39,593.15 | Export −5%, Import-price +10% **only** (no remittance shock) |

**Locked constraint: Vietnam's figure must never be presented alongside Bangladesh's/Pakistan's without noting it reflects two shocks, not three.**
Source: `gate3_stress_test.csv`

## R-006 — EMP methodology (locked, not to be altered without explicit instruction)
- Specification: Kaminsky, Lizondo & Reinhart (1998) two-component EMP, EMP = %Δe − α·%Δr
- α computed per country, full common sample 2018-M02–2026-M06 (standard-deviation ratio)
- α values: Bangladesh 0.161305; Pakistan 0.307318; Vietnam 0.146898
- Exchange rate: IMF ER, end-of-period (not period-average). Reserves: IMF International Liquidity, excluding gold
- KLR's 3-SD crisis threshold NOT applied
- Source: `RESEARCH_LEDGER.md` D-013 through D-018; `03_EMP.do` (prepared, not independently executed — Python implementation is the accepted one)

## R-007 — Institutional/terminology facts (locked)
- Bangladesh Bank introduced a crawling peg in May 2024; a further "more flexible exchange-rate arrangement" (crawling peg with band) in mid-May 2025
- Never described as a free float or fully flexible regime
- Source: IMF 2025 Article IV Consultation staff report (Claim C-001, `RESEARCH_LEDGER.md`)

## R-008 — Variables permanently excluded from this project (OMITTED BY DESIGN)
External debt, REER, policy rate. Not reintroduced anywhere in the paper, policy note, or this locked-results file.

---

## Deliverables produced from these locked results
- `paper/final_paper.md` (with figures in `paper/figures/`)
- `policy_note/IMF_style_policy_note.md`
- `GATE2_ANALYSIS.md`, `STRESS_TEST.md` (source analyses)
- `RESEARCH_LEDGER.md`, `DATA_QA.md` (full provenance)

## Change log
*(empty — no changes made since locking)*
