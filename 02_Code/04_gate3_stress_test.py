"""
04_gate3_stress_test.py

Gate 3: stylized, mechanical four-quarter external-shock stress test.
NOT a forecast. See STRESS_TEST.md for the full write-up, assumptions list,
and interpretation rules, and RESEARCH_LEDGER.md D-022 for the locked
results this script reproduces.

Baseline: latest common observed quarterly window, 2025-Q2 to 2026-Q1.
Locked shocks: remittances -10% (Bangladesh/Pakistan only), goods exports
-5% (all three), import-price +10% (global energy-price shock mechanically
applied as a stylized +10% increase in import value, real quantities held
constant — an imposed simplifying assumption, not an estimated pass-through
coefficient).

Input: data/derived/master_analytical_dataset.csv
Output: data/derived/gate3_stress_test.csv
"""
import pandas as pd

BASELINE_Q = ["2025-Q2", "2025-Q3", "2025-Q4", "2026-Q1"]
Q_MONTHS = {
    "2025-Q2": ["2025-M04", "2025-M05", "2025-M06"],
    "2025-Q3": ["2025-M07", "2025-M08", "2025-M09"],
    "2025-Q4": ["2025-M10", "2025-M11", "2025-M12"],
    "2026-Q1": ["2026-M01", "2026-M02", "2026-M03"],
}
COUNTRIES = ["BGD", "PAK", "VNM"]
NAMES = {"BGD": "Bangladesh", "PAK": "Pakistan", "VNM": "Vietnam"}
HORIZON_Q = 4

REMITTANCE_SHOCK = -0.10   # Bangladesh, Pakistan only
EXPORT_SHOCK = -0.05       # all three countries
IMPORT_PRICE_SHOCK = -0.10  # CA impact of a +10% stylized import-value increase


def get_baseline_sum(master, iso, var):
    sub = master[(master.country_iso3 == iso) & (master.variable_code == var) & (master.period.isin(BASELINE_Q))]
    assert len(sub) == 4, f"{iso} {var}: expected 4 baseline quarters, found {len(sub)}"
    return sub["value"].sum()


def get_remittance_baseline(master, iso):
    if iso == "VNM":
        return None  # UNRESOLVED — never fabricated or substituted
    rem = master[(master.country_iso3 == iso) & (master.variable_code == "remittances")].set_index("period")["value"]
    total = 0.0
    for months in Q_MONTHS.values():
        for m in months:
            if m not in rem.index:
                raise ValueError(f"Missing {iso} remittances for {m}")
            total += rem.loc[m]
    return total


def main():
    master = pd.read_csv("data/derived/master_analytical_dataset.csv")
    rows = []
    for iso in COUNTRIES:
        baseline_exports = get_baseline_sum(master, iso, "goods_exports")
        baseline_imports = get_baseline_sum(master, iso, "goods_imports")
        baseline_ca = get_baseline_sum(master, iso, "current_account_balance")
        baseline_rem = get_remittance_baseline(master, iso)

        remittance_shock = (REMITTANCE_SHOCK * baseline_rem) if baseline_rem is not None else None
        export_shock = EXPORT_SHOCK * baseline_exports
        import_price_shock = IMPORT_PRICE_SHOCK * baseline_imports

        scenarios = []
        if baseline_rem is not None:
            scenarios.append(("Remittance shock (-10%)", remittance_shock))
        scenarios.append(("Export shock (-5%)", export_shock))
        scenarios.append(("Import-price shock (+10% energy -> +10% import value)", import_price_shock))
        if baseline_rem is not None:
            scenarios.append(("Combined (remittance+export+import-price)",
                               remittance_shock + export_shock + import_price_shock))
        else:
            scenarios.append(("Combined (export+import-price only; remittance shock not applicable)",
                               export_shock + import_price_shock))

        for scen_name, shock_amt in scenarios:
            shocked_ca = baseline_ca + shock_amt
            rows.append(dict(
                country_iso3=iso, country_name=NAMES[iso],
                baseline_period=f"{BASELINE_Q[0]} to {BASELINE_Q[-1]} (4Q)", scenario=scen_name,
                baseline_exports=round(baseline_exports, 2), baseline_imports=round(baseline_imports, 2),
                baseline_current_account=round(baseline_ca, 2),
                baseline_remittances=round(baseline_rem, 2) if baseline_rem is not None else "N/A - UNRESOLVED",
                remittance_shock_amount=round(remittance_shock, 2) if (baseline_rem is not None and "Remittance" in scen_name) else
                    (round(remittance_shock, 2) if (baseline_rem is not None and "Combined" in scen_name and "remittance" in scen_name.lower()) else ("N/A" if baseline_rem is None else 0)),
                export_shock_amount=round(export_shock, 2) if ("Export" in scen_name or "Combined" in scen_name) else 0,
                import_price_shock_amount=round(import_price_shock, 2) if ("Import-price" in scen_name or "Combined" in scen_name) else 0,
                total_external_deterioration=round(shock_amt, 2),
                mechanically_shocked_current_account=round(shocked_ca, 2),
                horizon_quarters=HORIZON_Q,
            ))

    df = pd.DataFrame(rows)
    df.to_csv("data/derived/gate3_stress_test.csv", index=False)

    combined = df[df["scenario"].str.contains("Combined")]
    print("Combined-scenario results:")
    print(combined[["country_name", "total_external_deterioration", "mechanically_shocked_current_account"]].to_string(index=False))


if __name__ == "__main__":
    main()
