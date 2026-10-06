# Exchange-Rate Flexibility and External Adjustment: An Early Comparative Assessment of Bangladesh, Pakistan, and Vietnam

An applied empirical research note examining Bangladesh's exchange-rate and reserve pressure dynamics around its May 2025 move toward a more flexible exchange-rate arrangement, benchmarked against Pakistan and Vietnam, with a stylized four-quarter external-shock stress test.

## Research question

How did Bangladesh's exchange-rate and reserve pressure dynamics evolve around the May 2025 move toward a more flexible exchange-rate arrangement, and what does a simple external-shock stress test suggest about remaining vulnerabilities? This project
1) builds a verified three-country macroeconomic dataset
2) constructs a published Exchange Market Pressure (EMP) index 
3) Describes observed exchange-rate and reserve pressure around the reform
4) Applies a transparent mechanical stress test to assess how large plausible remittance, export, and import-price shocks would be relative to the latest observed external accounts.
**The project does not claim to measure every dimension of external-sector adjustment** (e.g., capital-flow composition or valuation effects are not covered); it is scoped specifically to exchange-rate/reserve pressure (via EMP) and a mechanical shock scenario (via the stress test).

## Why Bangladesh's May 2025 reform

Bangladesh Bank introduced a crawling-peg exchange-rate mechanism in May 2024, followed by a further move to a **more flexible exchange-rate arrangement — a crawling peg with band —** in **mid-May 2025**, under its IMF-supported financing program. This is a live, ongoing policy transition with limited existing empirical assessment, and it offers a natural case for descriptive external-sector analysis using standard IMF-style tools. 
**This reform is never described in this project as a free float or fully flexible exchange rate** — both the underlying IMF documentation and the observed data are explicit that it is a managed, step-like adjustment process.

## Countries covered

Bangladesh (focal case). Pakistan, and Vietnam were chosen to illustrate differences in exchange-rate management, external financing structure, reserve management, remittance dependence, and trade structure, not to imply structural similarity.

## Methodology

- **Exchange Market Pressure (EMP):** a standard, published two-component index (Kaminsky, Lizondo & Reinhart, 1998, *IMF Staff Papers*) combining monthly exchange-rate changes and reserve changes into a single pressure measure, weighted per country so that reserve volatility doesn't mechanically dominate the index. No policy-rate data is required or used. KLR's original crisis-dating threshold is **not** applied — the project uses the continuous index descriptively.
- **Gate 2 (descriptive event-window analysis):** compares Bangladesh's EMP in the 12 months before versus the 12 months after the reform, against its own full 2018–2026 history and against Pakistan and Vietnam over the identical calendar window.
- **Gate 3 (stress test):** a transparent, mechanical scenario — not a forecast — applying fixed shocks (remittances −10%, exports −5%, a global energy-price shock mechanically translated into a stylized +10% increase in import value) to the latest four observed quarters, reported as implied external-account deterioration.

## Data sources

All data is sourced directly from primary institutions and independently verified before use (full provenance in `RESEARCH_LEDGER.md` and `DATA_QA.md`):
- **IMF International Liquidity** — reserves excluding gold
- **IMF Exchange Rates (ER)** — nominal exchange rate, end-of-period
- **IMF Balance of Payments (BOP)** — current account, goods exports/imports
- **IMF World Economic Outlook (WEO)**, April 2026 vintage — GDP growth, CPI inflation (not used as reform-window evidence)
- **IMF Primary Commodity Price System (PCPS)** — global energy price index (external-shock proxy)
- **Bangladesh Bank** and **State Bank of Pakistan** — national monthly remittance releases


## Headline findings


- Bangladesh's mean EMP fell from **0.0072** in the 12 months before the reform to **−0.0060** in the 12 months after (full 2018–2026 historical mean: 0.0037), with volatility little changed. The reform month itself (May 2025, EMP 0.0190) was not unusually large relative to the preceding 12-month distribution.
- **Pakistan and Vietnam show the same directional decline in mean EMP over the identical calendar window** — Pakistan from −0.0023 to −0.0113, Vietnam from 0.0035 to 0.0000. **This is the project's central interpretive constraint: Bangladesh's pattern cannot be read as a causal estimate of the reform's effect**, since the same shift appears where no comparable reform occurred.
- A four-quarter stylized stress test implies combined external-account deterioration of approximately **−$12.3 billion** for Bangladesh and **−$11.9 billion** for Pakistan, and **−$70.6 billion** for Vietnam on a narrower two-shock basis (Vietnam's monthly national remittance data remain unresolved, so no remittance shock is applied there). These are mechanical scenario results, not reserve forecasts.

## Key limitations

- Descriptive, fixed-window comparison — no causal identification, no statistical significance test of the pre/post difference.
- Pakistan and Vietnam's comparative pattern (above) is the central caution on any Bangladesh-specific reading.
- A global energy-price spike falls inside the post-reform window, not disentangled here.
- Vietnam's nationwide monthly remittance data are unresolved; no data were fabricated or substituted to fill the gap.
- GDP growth and CPI inflation were excluded from reform-window evidence (Bangladesh's fiscal-year reporting convention and a WEO actual-vs-projection caveat on 2025–2026 make them unreliable for this specific comparison).
- External debt, REER, and policy interest rates were excluded from this project's scope by design.

**This analysis is descriptive and mechanical throughout — not causal, and the stress test is not a forecast.**

## Repository structure

```
/
├── README.md
├── RESEARCH_LEDGER.md          # full provenance and decision history for every data/methodology choice
├── DATA_QA.md                  # data-quality issue log
├── DATA_DICTIONARY.md          # variable-level definitions for the master dataset
├── FINAL_RESULTS_LOCKED.md     # locked numerical results (R-001 to R-008) — do not alter without a documented reason
├── REPRODUCIBILITY.md          # how to trace raw data -> paper
├── requirements.txt             # pinned Python package versions
├── LICENSE
├── paper/
│   ├── final_paper.md
│   └── figures/                # fig1-fig4 (referenced in the paper); fig5 (stress-test bar chart) generated but not used in the final paper, per RESEARCH_LEDGER.md D-024
├── policy_note/
│   └── policy_note.md
├── stress_test/
│   └── External_Stress_Test.xlsx   # formula-driven, auditable Excel reproduction of Gate 3
├── data/
│   ├── raw/                    # untouched, as downloaded, one subfolder per source with a PROVENANCE.md
│   └── derived/                # EMP series, master dataset, Gate 2/3 outputs — all reproducible from code/
├── code/                       # Python pipeline, numbered in execution order (01-06)
└── stata/
    └── 03_EMP.do                # reproducibility artifact; prepared and syntax-corrected but not independently executed — the Python implementation in code/01_calculate_emp.py is the accepted analytical implementation
```

## Reproducibility instructions

See `REPRODUCIBILITY.md` for the full pipeline trace and the tested Python version. In brief: `pip install -r requirements.txt`, then run `code/01_calculate_emp.py` through `code/06_build_excel_workbook.py` in order from the repository root; each script reads only already-verified files and writes to `data/derived/`, `paper/figures/`, or `stress_test/`. No step re-sources external data.
