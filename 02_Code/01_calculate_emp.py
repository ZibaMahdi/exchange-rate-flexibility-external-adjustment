"""
01_calculate_emp.py

Constructs the KLR (1998) two-component Exchange Market Pressure (EMP) index
for Bangladesh, Pakistan, and Vietnam. This is the LOCKED methodology for
this project (see RESEARCH_LEDGER.md D-013 through D-018) — do not change
the formula, the exchange-rate series choice (end-of-period, not
period-average), or the alpha-estimation window without updating the ledger.

Inputs (raw, read-only — never modified):
    data/raw/imf_il_reserves/dataset_2026-09-12T19_47_51_749761953Z_..._IL_13_0_1.csv
    data/raw/imf_er_exchange_rate/dataset_2026-09-13T15_34_30_478901807Z_..._ER_4_0_1.csv

Outputs (derived):
    data/derived/emp_klr_two_component.csv
    data/derived/emp_qa_summary.csv

Methodology: EMP_i,t = %Delta(e_i,t) - alpha_i * %Delta(r_i,t), where alpha_i
is the ratio of the standard deviation of exchange-rate changes to the
standard deviation of reserve changes, estimated separately for each country
over the full common sample (2018-M01 to 2026-M06). KLR's 3-standard-deviation
crisis threshold is NOT applied — this script produces the continuous index
only. See STRESS_TEST.md and the paper for the full citation and rationale.

This script computes the index via two independent paths (vectorized
NumPy/pandas, and a manual loop using Python's `statistics` module) and
asserts they match to floating-point precision, reproducing the verification
already performed when this methodology was locked.
"""
import pandas as pd
import numpy as np
import statistics as pystat

IL_PATH = "data/raw/imf_il_reserves/dataset_2026-09-12T19_47_51_749761953Z_DEFAULT_INTEGRATION_IMF_STA_IL_13_0_1.csv"
ER_PATH = "data/raw/imf_er_exchange_rate/dataset_2026-09-13T15_34_30_478901807Z_DEFAULT_INTEGRATION_IMF_STA_ER_4_0_1.csv"
COMMON_SAMPLE = ("2018-M01", "2026-M06")
COUNTRIES = ["BGD", "PAK", "VNM"]


def load_series():
    il = pd.read_csv(IL_PATH, dtype=str, encoding="utf-8-sig")
    er = pd.read_csv(ER_PATH, dtype=str, encoding="utf-8-sig")
    meta_il = ["DATASET", "SERIES_CODE", "OBS_MEASURE", "COUNTRY", "INDICATOR", "UNIT", "FREQUENCY", "SCALE"]
    time_cols = [c for c in il.columns if c not in meta_il]
    months = [c for c in time_cols if COMMON_SAMPLE[0] <= c <= COMMON_SAMPLE[1]]

    r_series, e_series = {}, {}
    for iso in COUNTRIES:
        r_row = il[il["SERIES_CODE"] == f"{iso}.RXF11_REVS.USD.M"].iloc[0]
        e_row = er[er["SERIES_CODE"] == f"{iso}.XDC_USD.EOP_RT.M"].iloc[0]
        r_series[iso] = r_row[months].astype(float).reset_index(drop=True)
        e_series[iso] = e_row[months].astype(float).reset_index(drop=True)

        # Completeness check before any calculation, per project QA discipline
        assert r_series[iso].isna().sum() == 0, f"{iso} reserves has missing values in the common window"
        assert e_series[iso].isna().sum() == 0, f"{iso} exchange rate has missing values in the common window"

    return months, r_series, e_series


def compute_emp_dual_path(r, e):
    """Two independent implementations; must match to floating-point precision."""
    # Path A: vectorized
    pct_de_a = (e[1:] - e[:-1]) / e[:-1]
    pct_dr_a = (r[1:] - r[:-1]) / r[:-1]
    alpha_a = np.std(pct_de_a, ddof=1) / np.std(pct_dr_a, ddof=1)
    emp_a = pct_de_a - alpha_a * pct_dr_a

    # Path B: manual loop, independent standard-deviation implementation
    pct_de_b, pct_dr_b = [], []
    for t in range(1, len(e)):
        pct_de_b.append((e[t] - e[t - 1]) / e[t - 1])
        pct_dr_b.append((r[t] - r[t - 1]) / r[t - 1])
    alpha_b = pystat.stdev(pct_de_b) / pystat.stdev(pct_dr_b)
    emp_b = [pct_de_b[i] - alpha_b * pct_dr_b[i] for i in range(len(pct_de_b))]

    max_diff = max(abs(a - b) for a, b in zip(emp_a, emp_b))
    assert max_diff < 1e-9, f"Dual-path EMP calculation mismatch: {max_diff}"
    assert abs(alpha_a - alpha_b) < 1e-9, "Dual-path alpha mismatch"

    return pct_de_a, pct_dr_a, alpha_a, emp_a


def main():
    months, r_series, e_series = load_series()
    emp_months = months[1:]  # first month has no prior period to difference against

    rows, qa_rows = [], []
    names = {"BGD": "Bangladesh", "PAK": "Pakistan", "VNM": "Vietnam"}
    for iso in COUNTRIES:
        r = r_series[iso].values
        e = e_series[iso].values
        pct_de, pct_dr, alpha, emp = compute_emp_dual_path(r, e)

        for t, m in enumerate(emp_months):
            rows.append(dict(
                country_iso3=iso, country_name=names[iso], month=m,
                reserves_usd_mn_SOURCE=r[t + 1], exchange_rate_eop_SOURCE=e[t + 1],
                pct_change_exchange_rate_CALCULATED=pct_de[t],
                pct_change_reserves_CALCULATED=pct_dr[t],
                alpha_CALCULATED=alpha, EMP_CALCULATED=emp[t],
            ))
        emp_arr = np.array(emp)
        qa_rows.append(dict(
            country=names[iso], country_iso3=iso, alpha=round(alpha, 6),
            mean_EMP=round(emp_arr.mean(), 6), sd_EMP=round(emp_arr.std(ddof=1), 6),
            min_EMP=round(emp_arr.min(), 6), min_EMP_date=emp_months[emp_arr.argmin()],
            max_EMP=round(emp_arr.max(), 6), max_EMP_date=emp_months[emp_arr.argmax()],
            n_obs=len(emp_arr),
        ))

    pd.DataFrame(rows).to_csv("data/derived/emp_klr_two_component.csv", index=False)
    pd.DataFrame(qa_rows).to_csv("data/derived/emp_qa_summary.csv", index=False)
    print(f"EMP calculated for {len(COUNTRIES)} countries, {len(emp_months)} months each "
          f"({emp_months[0]} to {emp_months[-1]}). Dual-path verification passed.")


if __name__ == "__main__":
    main()
