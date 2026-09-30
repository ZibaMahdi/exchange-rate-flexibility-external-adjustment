# STRESS_TEST.md — Gate 3: Stylized Four-Quarter External-Shock Scenario

**This is a transparent mechanical scenario exercise, not a forecast.** Nothing in this document predicts what will happen. Every number is the arithmetic result of applying a stated, fixed percentage shock to an observed historical baseline — "mechanically implies," not "is expected to." No regression, causal inference, forecasting, or machine learning was used. No new data was sourced. The verified master dataset (`data/derived/master_analytical_dataset.csv`) is the only input.

## Baseline

**Baseline period: 2025-Q2 through 2026-Q1 (4 quarters)** — the latest available common observed quarterly window, since the common quarterly sample ends at 2026-Q1. Applied identically to all three countries. Baseline values for exports, imports, and the current account are the **sum of the four quarterly observations** — a cumulative 4-quarter total, matching the 4-quarter horizon of the shocks applied to it. Remittance baselines (Bangladesh, Pakistan) are the sum of the twelve corresponding monthly observations (April 2025–March 2026), aggregated from the verified monthly master data — this quarterly aggregation is a Gate-3-specific calculation, not a change to the master dataset itself.

| Country | Baseline exports | Baseline imports | Baseline current account | Baseline remittances |
|---|---|---|---|---|
| Bangladesh | $42,477.21mn | $66,593.96mn | $161.01mn | $34,748.87mn |
| Pakistan | $30,913.00mn | $62,457.00mn | $449.98mn | $40,589.86mn |
| Vietnam | $494,755.00mn | $458,784.00mn | $31,023.00mn | **N/A — UNRESOLVED, not fabricated** |

## Mechanical transmission assumption for the import-price shock — stated explicitly, before any calculation

The global energy-price proxy (IMF PCPS Energy Index) is a **global shock indicator, not a country-specific import-price index**. The scenario does **not** claim that a 10% global energy-price increase translates one-for-one into a 10% increase in any country's actual import bill — that would require an estimated pass-through coefficient, which this project does not have and is not attempting to estimate here.

**The assumption actually used, stated as a simplifying scenario choice, not an estimate:** real import quantities are held constant, and a +10% global energy-price shock is applied as a **stylized +10% increase in the value of goods imports**. This is a deliberately simple, transparent assumption chosen for illustrative purposes — it is not a pass-through estimate, not a modeled elasticity, and not a claim about how much of each country's import basket is actually energy.

## Scenario mechanics (signs kept explicit throughout)

- **Remittance shock:** −10% × baseline remittances → a negative external-account impact (fewer inflows)
- **Export shock:** −5% × baseline goods exports → a negative external-account impact (less export revenue)
- **Import-price shock:** a +10% stylized increase in import value, which **enters the external balance as a −10% × baseline imports impact** (higher import cost worsens the current account) — the value increase and its balance impact are two sides of the same assumption, shown separately below to avoid ambiguity
- **Combined:** the sum of the applicable individual shocks

## Table 1 — Bangladesh

| Scenario | Remittance shock | Export shock | Import-price shock | Total external-account deterioration | Baseline CA | Mechanically shocked CA |
|---|---|---|---|---|---|---|
| Remittance shock (−10%) | −$3,474.89mn | — | — | −$3,474.89mn | $161.01mn | −$3,313.88mn |
| Export shock (−5%) | — | −$2,123.86mn | — | −$2,123.86mn | $161.01mn | −$1,962.85mn |
| Import-price shock (+10% energy → +10% import value) | — | — | −$6,659.40mn | −$6,659.40mn | $161.01mn | −$6,498.39mn |
| **Combined (all three)** | −$3,474.89mn | −$2,123.86mn | −$6,659.40mn | **−$12,258.14mn** | $161.01mn | **−$12,097.13mn** |

## Table 2 — Pakistan and Vietnam (only shocks supported by verified data)

| Country | Scenario | Remittance shock | Export shock | Import-price shock | Total deterioration | Baseline CA | Mechanically shocked CA |
|---|---|---|---|---|---|---|---|
| Pakistan | Remittance shock (−10%) | −$4,058.99mn | — | — | −$4,058.99mn | $449.98mn | −$3,609.00mn |
| Pakistan | Export shock (−5%) | — | −$1,545.65mn | — | −$1,545.65mn | $449.98mn | −$1,095.67mn |
| Pakistan | Import-price shock | — | — | −$6,245.70mn | −$6,245.70mn | $449.98mn | −$5,795.72mn |
| Pakistan | **Combined (all three)** | −$4,058.99mn | −$1,545.65mn | −$6,245.70mn | **−$11,850.34mn** | $449.98mn | **−$11,400.35mn** |
| Vietnam | Export shock (−5%) | N/A | −$24,737.75mn | — | −$24,737.75mn | $31,023.00mn | $6,285.25mn |
| Vietnam | Import-price shock | N/A | — | −$45,878.40mn | −$45,878.40mn | $31,023.00mn | −$14,855.40mn |
| Vietnam | **Combined (export + import-price only — no remittance shock)** | N/A | −$24,737.75mn | −$45,878.40mn | **−$70,616.15mn** | $31,023.00mn | **−$39,593.15mn** |

**Vietnam's remittance shock was not computed and is not shown as zero or blank-filled — it is marked N/A because no verified monthly baseline exists.** No symmetric remittance scenario was forced onto Vietnam, per instruction. Vietnam's "combined" scenario is explicitly narrower (two shocks, not three) than Bangladesh's and Pakistan's, and is labeled as such everywhere it appears — never presented as directly comparable to the other two countries' three-shock combined figure without that caveat.

## Reserve interpretation — deliberately not modeled

**No reserve forecast is produced.** What this scenario mechanically implies is a **cumulative deterioration in the external balance over 4 quarters** — the "total external-account deterioration" figures above. Whether or how this would actually translate into reserve losses depends on financing flows, exchange-rate adjustment, capital account movements, valuation effects, and policy response — **none of which are modeled in this exercise.** Reporting a reserve-loss number would require assumptions about all of those channels that this project has not made and is not making here. The external financing pressure implied by the scenario is the deterioration figure itself, not a reserve number.

## Assumptions imposed rather than estimated (explicit list)

1. **The ±10%/−5% shock magnitudes themselves** are stated, illustrative scenario inputs, not estimated from data or historical shock distributions.
2. **The import-price transmission assumption** (a 10% global energy-price shock ⇒ a 10% increase in the *value* of total goods imports, real quantities held constant) is a simplifying scenario choice, not an estimated pass-through elasticity, and does not account for each country's actual energy share of imports.
3. **No financing response, exchange-rate adjustment, or policy reaction is modeled** — the "mechanically shocked current account" assumes everything else held constant, which is not realistic and is not claimed to be.
4. **The 4-quarter baseline is a simple sum of quarterly flows**, not seasonally adjusted, not annualized via any other convention, and not smoothed.
5. **Vietnam's remittance shock is omitted, not approximated** — no HCMC regional or annual figure was substituted, per instruction.
6. **The energy-price shock is applied identically (+10%) to all three countries** despite them having different energy-import shares — this is a stated simplification, not a claim that all three countries are equally exposed.
7. **This is a mechanical, mutually-exclusive-scenario exercise, not a joint probability model** — the "combined" scenario simply sums the three individual shocks; it does not model any interaction or correlation between them.

## QA performed before finalizing

- **Baseline traceability:** every baseline figure (exports, imports, current account, remittances) was computed directly from `data/derived/master_analytical_dataset.csv` by summing the exact four (or twelve, for remittances) verified rows for the stated period — no intermediate manual entry.
- **Arithmetic verification:** all four scenario calculations (remittance, export, import-price, combined) were independently re-verified at full floating-point precision — confirmed the combined shock equals the exact sum of the individual applicable shocks for all three countries, and the shocked current account equals baseline plus the combined shock, with zero discrepancy.
- **No raw file modified.** Only the already-verified, already-finalized master dataset was read.
- **No excluded variable introduced** — external debt, REER, and policy rate do not appear anywhere in this scenario.
- **4-quarter horizon applied consistently** — the same 2025-Q2–2026-Q1 window was used as the baseline period for every country and every variable in this exercise.
