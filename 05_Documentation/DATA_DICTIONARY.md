# DATA_DICTIONARY.md — Master Analytical Dataset

Covers `data/derived/master_analytical_dataset.csv`. This dataset is **long/tidy format** — one row per (country, variable, period) — deliberately, so that monthly, quarterly, and annual variables coexist without forcing any of them onto a shared calendar. A `frequency` column and a `period` column (format varies by frequency: `"2018-M01"`, `"2018-Q1"`, `"2018"`) identify each observation's native cadence. Columns `value_type` (SOURCE vs. CALCULATED) and `in_common_window` (whether the observation falls inside the already-established three-country common window for that variable) are included on every row.

## Monthly variables

| Variable code | Definition | Source | Unit | Coverage (per country) | Status |
|---|---|---|---|---|---|
| `reserves_excl_gold` | International reserves excluding monetary gold | IMF International Liquidity (IL), series `{ISO3}.RXF11_REVS.USD.M` | USD million | BGD 2018-M01–2026-M07; PAK 2018-M01–2026-M07; VNM 2018-M01–2026-M06 | VERIFIED. Common 3-country window: 2018-M01–2026-M06. |
| `exchange_rate_eop` | Nominal exchange rate, end-of-period, local currency per USD | IMF Exchange Rates (ER), series `{ISO3}.XDC_USD.EOP_RT.M` | LCU per USD | BGD 2018-M01–2026-M08; PAK 2018-M01–2026-M07; VNM 2018-M01–2026-M06 | VERIFIED. Common 3-country window: 2018-M01–2026-M06. Period-average variant exists and was verified separately but is **not** included here — only EOP, per the locked EMP specification. |
| `remittances` | Workers'/wage-earner remittance inflows | Bangladesh: Bangladesh Bank, *Monthly Report on Workers' Remittance Inflows, July 2026* (source-derived extract from a PDF table, **not** a native machine-readable export). Pakistan: SBP EasyData, `TS_GP_BOP_WR_M.WR0010` ("Total Cash Worker Remittances"). | USD million | BGD 2018-M01–2026-M07; PAK 2018-M01–2026-M08 | VERIFIED for Bangladesh and Pakistan. **Vietnam: no rows — UNRESOLVED, no suitable nationwide monthly primary series located (see gaps list below).** Pakistan's raw-vs-seasonally-adjusted classification remains "very likely unadjusted, not fully confirmed." |
| `EMP_klr` | Exchange Market Pressure index, KLR (1998) two-component specification | **CALCULATED** from `reserves_excl_gold` and `exchange_rate_eop` — see `RESEARCH_LEDGER.md` and `stata/03_EMP.do` for the locked methodology | Index (unitless) | BGD/PAK/VNM 2018-M02–2026-M06 (101 obs each) | VERIFIED per the locked, already-accepted Python implementation. **Not recomputed here — values copied directly from `data/derived/emp_klr_two_component.csv`.** |
| `energy_price_index` | **Global** energy (fuel) commodity price index — external shock proxy, not a country-specific import-price series | IMF Primary Commodity Price System (PCPS), series `G001.PNRG.INDEX.M` | Index, 2016=100 | Single global series (`country_iso3 = "WLD"`), 2018-M01–2026-M08 (104 obs) | VERIFIED. **Deliberately not assigned per-country or merged into any country-level, quarterly, or annual variable** — it exists in the dataset as one series shared across the whole panel, to be applied explicitly (not silently) wherever the eventual stress-test design calls for it. |

## Quarterly variables

| Variable code | Definition | Source | Unit | Coverage (per country) | Status |
|---|---|---|---|---|---|
| `current_account_balance` | Current account balance (credit less debit, net) | IMF BOP(21.0.0), series `{ISO3}.NETCD_T.CAB.USD.Q` | USD million | BGD 2018-Q1–2026-Q1; PAK 2018-Q1–2026-Q2; VNM 2018-Q1–2026-Q1 | VERIFIED. Common 3-country window: 2018-Q1–2026-Q1. |
| `goods_exports` | Exports of goods (credit), BOP/change-of-ownership basis | IMF BOP(21.0.0), series `{ISO3}.CD_T.G.USD.Q` | USD million | BGD 2018-Q1–2026-Q1; PAK 2018-Q1–2026-Q2; VNM 2018-Q1–2026-Q1 | VERIFIED. Common 3-country window: 2018-Q1–2026-Q1. |
| `goods_imports` | Imports of goods (debit), BOP/change-of-ownership basis | IMF BOP(21.0.0), series `{ISO3}.DB_T.G.USD.Q` | USD million | BGD 2018-Q1–2026-Q1; PAK 2018-Q1–2026-Q2; VNM 2018-Q1–2026-Q1 | VERIFIED. Common 3-country window: 2018-Q1–2026-Q1. |

## Annual variables

| Variable code | Definition | Source | Unit | Coverage (per country) | Status |
|---|---|---|---|---|---|
| `gdp_growth` | Real GDP growth, annual percent change | IMF WEO(9.0.0), April 2026 vintage, series `{ISO3}.NGDP_RPCH.A` | Percent | BGD/PAK/VNM 2018–2026 (9 obs each) | VERIFIED for coverage/definition, **with an explicit ACTUAL-VS-PROJECTION METADATA CAVEAT for 2025–2026**, and a fiscal-year (Bangladesh/Pakistan, July–June) vs. calendar-year (Vietnam) labeling difference not resolved further. |
| `cpi_inflation` | CPI inflation, period-average, annual percent change | IMF WEO(9.0.0), April 2026 vintage, series `{ISO3}.PCPIPCH.A` | Percent | BGD/PAK/VNM 2018–2026 (9 obs each) | VERIFIED for coverage/definition. **The GDP growth actual-vs-projection caveat is deliberately not applied here** — no direct evidence was found to support extending it to CPI. |

## Explicitly excluded from this dataset (by design, not oversight)
External debt, REER, and policy rate — OMITTED BY DESIGN per the project's permanent scope decision; not sourced, not included, not to be reintroduced without explicit instruction.

## Source vs. Calculated
Every row is tagged `SOURCE` or `CALCULATED` in the `value_type` column. Only `EMP_klr` is `CALCULATED` — everything else is a directly-sourced observation from a verified raw file, unmodified beyond the already-documented, explicitly-instructed transformations (Bangladesh's fiscal-year-to-calendar-month conversion, logged in full in `data/raw/bd_remittances/PROVENANCE.md`).
