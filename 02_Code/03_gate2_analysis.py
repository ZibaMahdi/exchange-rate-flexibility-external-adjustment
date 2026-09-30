"""
03_gate2_analysis.py

Gate 2: descriptive (non-causal) event-window analysis of Bangladesh's
May 2025 exchange-rate reform, with Pakistan and Vietnam as comparative
context over the identical calendar windows. See GATE2_ANALYSIS.md for the
full write-up and interpretation, and RESEARCH_LEDGER.md D-021 for the
locked findings this script reproduces.

Windows (fixed, not adjusted for results):
    Pre-reform:  2024-M05 to 2025-M04 (12 months)
    Reform month: 2025-M05
    Post-reform: 2025-M06 to 2026-M05 (12 months)
    Full historical: 2018-M02 to 2026-M06 (101 months)

Inputs: data/derived/master_analytical_dataset.csv, data/derived/emp_klr_two_component.csv
Outputs: data/derived/gate2_event_window_summary.csv
         data/derived/gate2_comparative_emp.csv
         data/derived/gate2_bangladesh_monthly.csv
"""
import pandas as pd
import numpy as np

PRE = [f"2024-M{m:02d}" for m in range(5, 13)] + [f"2025-M{m:02d}" for m in range(1, 5)]
REFORM = ["2025-M05"]
POST = [f"2025-M{m:02d}" for m in range(6, 13)] + [f"2026-M{m:02d}" for m in range(1, 6)]
NAMES = {"BGD": "Bangladesh", "PAK": "Pakistan", "VNM": "Vietnam"}


def stats(series):
    s = series.dropna()
    if len(s) == 0:
        return dict(n=0, mean=np.nan, median=np.nan, sd=np.nan, min=np.nan, max=np.nan)
    return dict(n=len(s), mean=s.mean(), median=s.median(),
                sd=s.std(ddof=1) if len(s) > 1 else np.nan, min=s.min(), max=s.max())


def main():
    master = pd.read_csv("data/derived/master_analytical_dataset.csv")
    emp_detail = pd.read_csv("data/derived/emp_klr_two_component.csv")

    windows = [("Pre-reform (2024-M05 to 2025-M04)", PRE),
               ("Reform month (2025-M05)", REFORM),
               ("Post-reform (2025-M06 to 2026-M05)", POST),
               ("Full historical (2018-M02 to 2026-M06)", None)]

    rows_a = []
    for iso in NAMES:
        df_c = emp_detail[emp_detail["country_iso3"] == iso].set_index("month")
        for wname, wlist in windows:
            sub = df_c if wlist is None else df_c.loc[df_c.index.intersection(wlist)]
            for varname, col in [("EMP_klr", "EMP_CALCULATED"),
                                  ("pct_change_exchange_rate", "pct_change_exchange_rate_CALCULATED"),
                                  ("pct_change_reserves", "pct_change_reserves_CALCULATED")]:
                rows_a.append(dict(country_iso3=iso, country_name=NAMES[iso], window=wname, variable=varname,
                                    **stats(sub[col])))

    # Remittance % change — Bangladesh and Pakistan only (Vietnam has no data)
    rem = master[master["variable_code"] == "remittances"]
    for iso in ["BGD", "PAK"]:
        sub_rem = rem[rem["country_iso3"] == iso].sort_values("period").set_index("period")["value"]
        pct_rem = sub_rem.pct_change()
        for wname, wlist in windows:
            sub = pct_rem if wlist is None else pct_rem.loc[pct_rem.index.intersection(wlist)]
            rows_a.append(dict(country_iso3=iso, country_name=NAMES[iso], window=wname,
                                variable="pct_change_remittances", **stats(sub)))

    event_window_summary = pd.DataFrame(rows_a)
    event_window_summary.to_csv("data/derived/gate2_event_window_summary.csv", index=False)

    comparative_emp = event_window_summary[event_window_summary["variable"] == "EMP_klr"].reset_index(drop=True)
    comparative_emp.to_csv("data/derived/gate2_comparative_emp.csv", index=False)

    # Bangladesh monthly detail, 2024-M05 to 2026-M05
    window_months = PRE + REFORM + POST
    bgd_detail = emp_detail[emp_detail["country_iso3"] == "BGD"].set_index("month")
    rem_bgd = master[(master["variable_code"] == "remittances") & (master["country_iso3"] == "BGD")].set_index("period")["value"]
    energy = master[master["variable_code"] == "energy_price_index"].set_index("period")["value"]

    rows_c = []
    for m in window_months:
        rows_c.append(dict(
            month=m,
            EMP=bgd_detail.loc[m, "EMP_CALCULATED"] if m in bgd_detail.index else np.nan,
            pct_change_exchange_rate=bgd_detail.loc[m, "pct_change_exchange_rate_CALCULATED"] if m in bgd_detail.index else np.nan,
            pct_change_reserves=bgd_detail.loc[m, "pct_change_reserves_CALCULATED"] if m in bgd_detail.index else np.nan,
            remittances_usd_mn=rem_bgd.loc[m] if m in rem_bgd.index else np.nan,
            energy_price_index=energy.loc[m] if m in energy.index else np.nan,
            period_label=("Pre-reform" if m in PRE else ("Reform month" if m in REFORM else "Post-reform")),
        ))
    pd.DataFrame(rows_c).to_csv("data/derived/gate2_bangladesh_monthly.csv", index=False)

    print("Gate 2 analysis complete: event-window summary, comparative EMP, and Bangladesh monthly detail written.")


if __name__ == "__main__":
    main()
