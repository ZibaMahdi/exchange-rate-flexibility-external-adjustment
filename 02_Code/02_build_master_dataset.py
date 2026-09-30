"""
02_build_master_dataset.py

Builds the project's master analytical dataset from already-verified raw
files and the locked EMP calculation (run 01_calculate_emp.py first). Long/
tidy format: one row per (country, variable, period), so monthly, quarterly,
and annual variables coexist without forcing a shared calendar. See
DATA_DICTIONARY.md for full variable definitions and RESEARCH_LEDGER.md for
source provenance.

Inputs (raw, read-only):
    data/raw/imf_il_reserves/...        (reserves excluding gold, monthly)
    data/raw/imf_er_exchange_rate/...   (exchange rate, EOP + period-average, monthly)
    data/raw/bd_remittances/...         (Bangladesh remittances, source-derived extract)
    data/raw/pk_remittances/...         (Pakistan remittances, native export)
    data/raw/imf_bop_current_account/...
    data/raw/imf_bop_goods_trade/...
    data/raw/imf_weo_gdp_growth/...
    data/raw/imf_weo_cpi_inflation/...
    data/raw/imf_pcps_energy_price/...  (global energy-price proxy, not country-specific)
    data/derived/emp_klr_two_component.csv  (from 01_calculate_emp.py)

Output:
    data/derived/master_analytical_dataset.csv
    data/derived/master_qa_summary.csv

Deliberate omissions, not oversights:
    - Vietnam has NO remittances rows (nationwide monthly data UNRESOLVED —
      never fabricated, never substituted from regional/annual sources).
    - External debt, REER, and policy rate are OMITTED BY DESIGN and do not
      appear anywhere in this pipeline.
"""
import pandas as pd

COUNTRIES = ["BGD", "PAK", "VNM"]
NAMES = {"BGD": "Bangladesh", "PAK": "Pakistan", "VNM": "Vietnam",
         "WLD": "World (global series, not country-specific)"}
COMMON_M = ("2018-M01", "2026-M06")
COMMON_Q = ("2018-Q1", "2026-Q1")
COMMON_A = ("2018", "2026")

rows = []


def add_row(iso, var_code, var_label, freq, period, value, unit, vtype, source, in_common, status, notes=""):
    rows.append(dict(country_iso3=iso, country_name=NAMES[iso], variable_code=var_code,
                      variable_label=var_label, frequency=freq, period=period, value=value,
                      unit=unit, value_type=vtype, source=source, in_common_window=in_common,
                      status=status, notes=notes))


def main():
    # ---- 1. Reserves excluding gold (monthly, SOURCE) ----
    il = pd.read_csv("data/raw/imf_il_reserves/dataset_2026-09-12T19_47_51_749761953Z_DEFAULT_INTEGRATION_IMF_STA_IL_13_0_1.csv", dtype=str, encoding="utf-8-sig")
    meta_il = ["DATASET", "SERIES_CODE", "OBS_MEASURE", "COUNTRY", "INDICATOR", "UNIT", "FREQUENCY", "SCALE"]
    time_il = [c for c in il.columns if c not in meta_il]
    for iso in COUNTRIES:
        row = il[il["SERIES_CODE"] == f"{iso}.RXF11_REVS.USD.M"].iloc[0]
        for m in time_il:
            v = row[m]
            if pd.isna(v) or str(v).strip() == "":
                continue
            add_row(iso, "reserves_excl_gold", "International reserves excluding gold", "Monthly", m,
                    float(v), "USD million", "SOURCE", "IMF International Liquidity (IL), RXF11_REVS.USD.M",
                    COMMON_M[0] <= m <= COMMON_M[1], "VERIFIED")

    # ---- 2. Exchange rate, EOP only (monthly, SOURCE) ----
    er = pd.read_csv("data/raw/imf_er_exchange_rate/dataset_2026-09-13T15_34_30_478901807Z_DEFAULT_INTEGRATION_IMF_STA_ER_4_0_1.csv", dtype=str, encoding="utf-8-sig")
    meta_er = ["DATASET", "SERIES_CODE", "OBS_MEASURE", "COUNTRY", "INDICATOR", "TYPE_OF_TRANSFORMATION", "FREQUENCY", "SCALE"]
    time_er = [c for c in er.columns if c not in meta_er]
    for iso in COUNTRIES:
        row = er[er["SERIES_CODE"] == f"{iso}.XDC_USD.EOP_RT.M"].iloc[0]
        for m in time_er:
            v = row[m]
            if pd.isna(v) or str(v).strip() == "":
                continue
            add_row(iso, "exchange_rate_eop", "Nominal exchange rate, end-of-period (local currency per USD)", "Monthly", m,
                    float(v), "LCU per USD", "SOURCE", "IMF Exchange Rates (ER), XDC_USD.EOP_RT.M",
                    COMMON_M[0] <= m <= COMMON_M[1], "VERIFIED")

    # ---- 3. Remittances (monthly, SOURCE) — Bangladesh and Pakistan only ----
    bd_rem = pd.read_csv("data/raw/bd_remittances/bd_remittances_calendar_2018_onward.csv")
    for _, r in bd_rem.iterrows():
        period_str = f"{int(r['calendar_year'])}-M{int(r['calendar_month']):02d}"
        add_row("BGD", "remittances", "Workers'/wage-earner remittance inflows", "Monthly", period_str,
                float(r["value"]), "USD million", "SOURCE",
                "Bangladesh Bank, Monthly Report on Workers' Remittance Inflows, July 2026 "
                "(source-derived extract from PDF, not a native export)",
                COMMON_M[0] <= period_str <= COMMON_M[1], "VERIFIED",
                notes="Source-derived extract, not native machine-readable file")

    pk_rem = pd.read_csv("data/raw/pk_remittances/pk_workers_remittances_easydata.csv")
    pk_rem["date"] = pd.to_datetime(pk_rem["Observation Date"], format="%d-%b-%Y")
    for _, r in pk_rem.iterrows():
        period_str = f"{r['date'].year}-M{r['date'].month:02d}"
        add_row("PAK", "remittances", "Workers'/wage-earner remittance inflows", "Monthly", period_str,
                float(r["Observation Value"]), "USD million", "SOURCE",
                "SBP EasyData, TS_GP_BOP_WR_M.WR0010 (Total Cash Worker Remittances)",
                COMMON_M[0] <= period_str <= COMMON_M[1], "VERIFIED",
                notes="Raw/non-seasonally-adjusted status: very likely, not fully confirmed")
    # Vietnam: no rows added, deliberately. See RESEARCH_LEDGER.md / DATA_QA.md.

    # ---- 4. EMP (monthly, CALCULATED — from 01_calculate_emp.py, not recomputed here) ----
    emp = pd.read_csv("data/derived/emp_klr_two_component.csv")
    for _, r in emp.iterrows():
        add_row(r["country_iso3"], "EMP_klr", "Exchange Market Pressure index (KLR 1998 two-component)", "Monthly",
                r["month"], float(r["EMP_CALCULATED"]), "Index (unitless)", "CALCULATED",
                "Calculated from IMF IL reserves-excl-gold and IMF ER EOP exchange rate "
                "(see RESEARCH_LEDGER.md and stata/03_EMP.do)",
                True, "VERIFIED (locked methodology, not recomputed here)")

    # ---- 5. Current account balance (quarterly, SOURCE) ----
    meta_bop = ["DATASET", "SERIES_CODE", "OBS_MEASURE", "COUNTRY", "BOP_ACCOUNTING_ENTRY", "INDICATOR", "UNIT", "FREQUENCY", "SCALE"]
    ca = pd.read_csv("data/raw/imf_bop_current_account/dataset_2026-09-16T07_28_55_668351590Z_DEFAULT_INTEGRATION_IMF_STA_BOP_21_0_0.csv", dtype=str, encoding="utf-8-sig")
    time_bop = [c for c in ca.columns if c not in meta_bop]
    for iso in COUNTRIES:
        row = ca[ca["SERIES_CODE"] == f"{iso}.NETCD_T.CAB.USD.Q"].iloc[0]
        for q in time_bop:
            v = row[q]
            if pd.isna(v) or str(v).strip() == "":
                continue
            add_row(iso, "current_account_balance", "Current account balance (credit less debit, net)", "Quarterly", q,
                    float(v), "USD million", "SOURCE", "IMF BOP(21.0.0), NETCD_T.CAB.USD.Q",
                    COMMON_Q[0] <= q <= COMMON_Q[1], "VERIFIED")

    # ---- 6. Goods exports/imports (quarterly, SOURCE) ----
    tr = pd.read_csv("data/raw/imf_bop_goods_trade/dataset_2026-09-16T07_46_47_931846777Z_DEFAULT_INTEGRATION_IMF_STA_BOP_21_0_0.csv", dtype=str, encoding="utf-8-sig")
    time_tr = [c for c in tr.columns if c not in meta_bop]
    for iso in COUNTRIES:
        exp_row = tr[tr["SERIES_CODE"] == f"{iso}.CD_T.G.USD.Q"].iloc[0]
        imp_row = tr[tr["SERIES_CODE"] == f"{iso}.DB_T.G.USD.Q"].iloc[0]
        for q in time_tr:
            ve, vi = exp_row[q], imp_row[q]
            in_common = COMMON_Q[0] <= q <= COMMON_Q[1]
            if pd.notna(ve) and str(ve).strip() != "":
                add_row(iso, "goods_exports", "Exports of goods (credit)", "Quarterly", q, float(ve),
                        "USD million", "SOURCE", "IMF BOP(21.0.0), CD_T.G.USD.Q", in_common, "VERIFIED")
            if pd.notna(vi) and str(vi).strip() != "":
                add_row(iso, "goods_imports", "Imports of goods (debit)", "Quarterly", q, float(vi),
                        "USD million", "SOURCE", "IMF BOP(21.0.0), DB_T.G.USD.Q", in_common, "VERIFIED")

    # ---- 7. GDP growth (annual, SOURCE) ----
    meta_weo = ["DATASET", "SERIES_CODE", "OBS_MEASURE", "COUNTRY", "INDICATOR", "FREQUENCY", "SCALE"]
    gdp = pd.read_csv("data/raw/imf_weo_gdp_growth/dataset_2026-09-16T18_52_19_183124519Z_DEFAULT_INTEGRATION_IMF_RES_WEO_9_0_0.csv", dtype=str, encoding="utf-8-sig")
    time_weo = [c for c in gdp.columns if c not in meta_weo]
    for iso in COUNTRIES:
        row = gdp[gdp["SERIES_CODE"] == f"{iso}.NGDP_RPCH.A"].iloc[0]
        for y in time_weo:
            v = row[y]
            if pd.isna(v) or str(v).strip() == "":
                continue
            add_row(iso, "gdp_growth", "Real GDP growth, annual percent change", "Annual", y, float(v), "Percent",
                    "SOURCE", "IMF WEO(9.0.0) April 2026 vintage, NGDP_RPCH.A", COMMON_A[0] <= y <= COMMON_A[1],
                    "VERIFIED (with ACTUAL-VS-PROJECTION caveat for 2025-2026; BGD/PAK fiscal-year convention)")

    # ---- 8. CPI inflation (annual, SOURCE) ----
    cpi = pd.read_csv("data/raw/imf_weo_cpi_inflation/dataset_2026-09-17T07_49_32_818648537Z_DEFAULT_INTEGRATION_IMF_RES_WEO_9_0_0.csv", dtype=str, encoding="utf-8-sig")
    time_weo2 = [c for c in cpi.columns if c not in meta_weo]
    for iso in COUNTRIES:
        row = cpi[cpi["SERIES_CODE"] == f"{iso}.PCPIPCH.A"].iloc[0]
        for y in time_weo2:
            v = row[y]
            if pd.isna(v) or str(v).strip() == "":
                continue
            add_row(iso, "cpi_inflation", "CPI inflation, period-average, annual percent change", "Annual", y,
                    float(v), "Percent", "SOURCE", "IMF WEO(9.0.0) April 2026 vintage, PCPIPCH.A",
                    COMMON_A[0] <= y <= COMMON_A[1], "VERIFIED (no actual/projection caveat applied - no direct evidence found)")

    # ---- 9. Global energy-price index (monthly, SOURCE, WORLD — not country-specific) ----
    meta_pcps = ["DATASET", "SERIES_CODE", "OBS_MEASURE", "COUNTRY", "INDICATOR", "DATA_TRANSFORMATION", "FREQUENCY", "SCALE"]
    pcps = pd.read_csv("data/raw/imf_pcps_energy_price/dataset_2026-09-19T08_32_32_873152583Z_DEFAULT_INTEGRATION_IMF_RES_PCPS_9_0_0.csv", dtype=str, encoding="utf-8-sig")
    time_pcps = [c for c in pcps.columns if c not in meta_pcps]
    row = pcps.iloc[0]
    for m in time_pcps:
        v = row[m]
        if pd.isna(v) or str(v).strip() == "":
            continue
        add_row("WLD", "energy_price_index",
                "Global energy price index (fuel commodity price index) - external shock proxy",
                "Monthly", m, float(v), "Index, 2016=100", "SOURCE",
                "IMF Primary Commodity Price System (PCPS), G001.PNRG.INDEX.M",
                COMMON_M[0] <= m <= COMMON_M[1], "VERIFIED",
                notes="Global proxy for import-price/external shock; not a country-specific import-price index; "
                      "do not merge mechanically into country-level or quarterly/annual variables")

    master = pd.DataFrame(rows).sort_values(["frequency", "variable_code", "country_iso3", "period"]).reset_index(drop=True)
    master.to_csv("data/derived/master_analytical_dataset.csv", index=False)

    qa = master.groupby(["variable_code", "frequency", "country_iso3"]).agg(
        n_obs=("value", "count"), first_period=("period", "min"), last_period=("period", "max")
    ).reset_index()
    qa.to_csv("data/derived/master_qa_summary.csv", index=False)

    print(f"Master dataset built: {master.shape[0]} rows, {master['variable_code'].nunique()} variables, "
          f"{master['country_iso3'].nunique()} country/entity codes.")
    print("Vietnam remittances rows (should be 0):", len(master[(master.country_iso3 == "VNM") & (master.variable_code == "remittances")]))


if __name__ == "__main__":
    main()
