"""
05_make_figures.py

Generates the five figures used in paper/final_paper.md, from already-
verified derived data only. No new analysis. Figure 3 is deliberately
built as three small-multiple panels (independent y-axis per country) so
Pakistan's much larger EMP range does not visually compress Bangladesh's
and Vietnam's series.

Inputs: data/derived/emp_klr_two_component.csv, data/derived/master_analytical_dataset.csv
Outputs: paper/figures/fig1_bgd_emp.png
         paper/figures/fig2_bgd_fx_reserves.png
         paper/figures/fig3_comparative_emp.png
         paper/figures/fig4_energy_index.png
"""
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

plt.rcParams.update({"font.size": 10, "figure.dpi": 150})
REFORM_DATE = datetime(2025, 5, 1)


def month_to_date(m):
    y, mm = m.split("-M")
    return datetime(int(y), int(mm), 1)


def main():
    emp = pd.read_csv("data/derived/emp_klr_two_component.csv")
    master = pd.read_csv("data/derived/master_analytical_dataset.csv")

    # ---- Figure 1: Bangladesh EMP full history, May 2025 marked ----
    bgd = emp[emp.country_iso3 == "BGD"].sort_values("month").copy()
    bgd["date"] = bgd["month"].apply(month_to_date)
    fig, ax = plt.subplots(figsize=(9, 4))
    ax.plot(bgd["date"], bgd["EMP_CALCULATED"], color="#1f4e79", linewidth=1.2)
    ax.axhline(0, color="grey", linewidth=0.6)
    ax.axvline(REFORM_DATE, color="#c00000", linestyle="--", linewidth=1.2, label="May 2025 reform")
    ax.set_title("Figure 1. Bangladesh EMP (KLR two-component index), 2018-M02 to 2026-M06")
    ax.set_ylabel("EMP index")
    ax.legend(loc="upper left")
    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    fig.tight_layout()
    fig.savefig("paper/figures/fig1_bgd_emp.png")
    plt.close(fig)

    # ---- Figure 2: BGD exchange rate and reserves, two separate panels ----
    window = bgd[(bgd["month"] >= "2024-M05") & (bgd["month"] <= "2026-M05")]
    fig, axes = plt.subplots(2, 1, figsize=(9, 6), sharex=True)
    axes[0].plot(window["date"], window["exchange_rate_eop_SOURCE"], color="#1f4e79", marker="o", markersize=3)
    axes[0].axvline(REFORM_DATE, color="#c00000", linestyle="--", linewidth=1.2)
    axes[0].set_title("Figure 2a. Bangladesh nominal exchange rate (EOP), around the reform")
    axes[0].set_ylabel("BDT per USD")
    axes[1].plot(window["date"], window["reserves_usd_mn_SOURCE"], color="#2e7d32", marker="o", markersize=3)
    axes[1].axvline(REFORM_DATE, color="#c00000", linestyle="--", linewidth=1.2, label="May 2025 reform")
    axes[1].set_title("Figure 2b. Bangladesh international reserves excluding gold, around the reform")
    axes[1].set_ylabel("USD million")
    axes[1].legend(loc="upper left")
    axes[1].xaxis.set_major_locator(mdates.MonthLocator(interval=3))
    axes[1].xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))
    plt.setp(axes[1].get_xticklabels(), rotation=45, ha="right")
    fig.tight_layout()
    fig.savefig("paper/figures/fig2_bgd_fx_reserves.png")
    plt.close(fig)

    # ---- Figure 3: comparative EMP, small multiples (independent y-axis per country) ----
    colors = {"BGD": "#1f4e79", "PAK": "#c00000", "VNM": "#2e7d32"}
    labels = {"BGD": "Bangladesh", "PAK": "Pakistan", "VNM": "Vietnam"}
    fig, axes = plt.subplots(3, 1, figsize=(9, 8), sharex=True)
    for ax, iso in zip(axes, ["BGD", "PAK", "VNM"]):
        sub = emp[emp.country_iso3 == iso].sort_values("month").copy()
        sub["date"] = sub["month"].apply(month_to_date)
        ax.plot(sub["date"], sub["EMP_CALCULATED"], color=colors[iso], linewidth=1.1)
        ax.axhline(0, color="grey", linewidth=0.6)
        ax.axvline(REFORM_DATE, color="black", linestyle=":", linewidth=1.0)
        ax.set_title(labels[iso], loc="left", fontsize=10)
        ax.set_ylabel("EMP index")
    axes[0].set_title("Figure 3. Comparative EMP: Bangladesh, Pakistan, Vietnam (2018-M02 to 2026-M06)\n"
                       "Small-multiple panels, each with its own y-axis scale, so Bangladesh and Vietnam are not\n"
                       "visually compressed by Pakistan's larger range. Dotted line = May 2025.\nBangladesh",
                       loc="left", fontsize=10)
    axes[-1].xaxis.set_major_locator(mdates.YearLocator())
    axes[-1].xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    fig.tight_layout()
    fig.savefig("paper/figures/fig3_comparative_emp.png")
    plt.close(fig)

    # ---- Figure 4: global energy price index ----
    energy = master[master.variable_code == "energy_price_index"].sort_values("period").copy()
    energy = energy[(energy["period"] >= "2018-M02") & (energy["period"] <= "2026-M06")]
    energy["date"] = energy["period"].apply(month_to_date)
    fig, ax = plt.subplots(figsize=(9, 4))
    ax.plot(energy["date"], energy["value"], color="#7b3f00", linewidth=1.2)
    ax.axvline(REFORM_DATE, color="black", linestyle=":", linewidth=1.0, label="May 2025 (Bangladesh reform)")
    ax.set_title("Figure 4. Global energy price index, 2018-M02 to 2026-M06 (external context)")
    ax.set_ylabel("Index, 2016=100")
    ax.legend(loc="upper left")
    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    fig.tight_layout()
    fig.savefig("paper/figures/fig4_energy_index.png")
    plt.close(fig)

    print("Figures 1-4 written to paper/figures/. (Figure 5, a stress-test bar chart, was dropped from the paper's "
          "final figure list in favor of Table 4 — see RESEARCH_LEDGER.md D-024 — and is not regenerated here.)")


if __name__ == "__main__":
    main()
