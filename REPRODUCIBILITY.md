# REPRODUCIBILITY.md

## Environment

Tested with **Python 3.12.3**. Package versions are pinned to the tested environment in `requirements.txt` (pandas, numpy, matplotlib, openpyxl); install with `pip install -r requirements.txt`. `datetime` and `statistics`, also used by the pipeline, are Python standard-library modules and require no separate installation.

## Primary-source data acquisition rule (standing project rule)

For material external datasets, the researcher downloads the original data directly from the authoritative source and provides the untouched raw file for inspection. Every file in `data/raw/` was acquired this way — Claude never reconstructed, replaced, or supplemented observations from search results, third-party aggregators, or inferred APIs when a direct source export was available. This rule is recorded in full in `RESEARCH_LEDGER.md`.

## Raw data is preserved unchanged

Every subfolder under `data/raw/` contains the file exactly as downloaded, plus a `PROVENANCE.md` documenting its source, retrieval context, SHA-256 checksum, and independently-verified coverage. **No script in `code/` ever writes to `data/raw/`.** The one exception — Bangladesh's remittances, which came from a manually-transcribed PDF table rather than a native export — is explicitly labeled as a "source-derived extract" throughout, not treated as equivalent to a native machine-readable file, and its provenance file preserves the original pasted table verbatim.

## EMP implementation: Python is the accepted implementation; Stata is a reproducibility artifact

`code/01_calculate_emp.py` is the accepted analytical implementation of the KLR (1998) two-component EMP index. It was verified via two independent calculation paths (vectorized NumPy/pandas and a manual loop using Python's `statistics` module) that matched to floating-point precision when the methodology was locked.

`stata/03_EMP.do` implements the identical, locked specification and was syntax-corrected for execution in Stata MP 14.1 on macOS, but **it has not been independently executed**. It is included as a reproducibility artifact for readers who want a Stata-native version of the pipeline, not as validated code — per this project's own standing rule, code is never described as "working" until it has actually been run and its output confirmed. If you run it and it reproduces the numbers in `FINAL_RESULTS_LOCKED.md`, that is worth recording in `RESEARCH_LEDGER.md` as a new verification event; until then, treat it as unverified.

## The Excel stress test is formula-driven, not a static export

`stress_test/External_Stress_Test.xlsx` (built by `code/06_build_excel_workbook.py`) recomputes the Gate 3 stress test from its own Inputs and Scenarios sheets using live formulas — nothing in the Calculations, Summary, or QA_Checks sheets is a pasted number. Opening the workbook and changing a Scenarios assumption cell (e.g., the export shock percentage) will recalculate every downstream figure automatically. The workbook's own QA_Checks sheet cross-verifies its output against `data/derived/gate3_stress_test.csv` and `FINAL_RESULTS_LOCKED.md` and reports "ALL CHECKS PASSED" — this is described in `RESEARCH_LEDGER.md` D-025, including a row-reference bug the QA_Checks sheet itself caught during construction and that was fixed before delivery.

## Full pipeline trace: raw data → master dataset → EMP → Gate 2 → Gate 3 → paper/policy note

Run from the repository root, in order:

1. **`code/01_calculate_emp.py`**
   Reads `data/raw/imf_il_reserves/` and `data/raw/imf_er_exchange_rate/`.
   Writes `data/derived/emp_klr_two_component.csv`, `data/derived/emp_qa_summary.csv`.

2. **`code/02_build_master_dataset.py`**
   Reads every folder under `data/raw/` plus `data/derived/emp_klr_two_component.csv`.
   Writes `data/derived/master_analytical_dataset.csv` (the single long/tidy panel — native frequency preserved, monthly/quarterly/annual variables coexist without forced alignment) and `data/derived/master_qa_summary.csv`.

3. **`code/03_gate2_analysis.py`**
   Reads `data/derived/master_analytical_dataset.csv` and `data/derived/emp_klr_two_component.csv`.
   Writes `data/derived/gate2_event_window_summary.csv`, `data/derived/gate2_comparative_emp.csv`, `data/derived/gate2_bangladesh_monthly.csv` — the descriptive event-window results underlying `GATE2_ANALYSIS.md`.

4. **`code/04_gate3_stress_test.py`**
   Reads `data/derived/master_analytical_dataset.csv`.
   Writes `data/derived/gate3_stress_test.csv` — the stylized shock scenarios underlying `STRESS_TEST.md`.

5. **`code/05_make_figures.py`**
   Reads `data/derived/emp_klr_two_component.csv` and `data/derived/master_analytical_dataset.csv`.
   Writes Figures 1–4 to `paper/figures/`, used directly in `paper/final_paper.md`.

6. **`code/06_build_excel_workbook.py`**
   Reads `data/derived/master_analytical_dataset.csv` (for the Inputs sheet's individual quarterly/monthly line items) and `data/derived/gate3_stress_test.csv` (for the QA_Checks sheet's reference values) — nothing in this script is a hard-coded analytical constant duplicated by hand; if either source file changes and this script is re-run, the workbook regenerates in step with it. Builds and saves `stress_test/External_Stress_Test.xlsx`. Recalculate afterward (e.g. with a LibreOffice-based recalculation tool) to populate formula values and confirm QA_Checks reads "ALL CHECKS PASSED."

**`paper/final_paper.md`** and **`policy_note/IMF_style_policy_note.md`** are written documents synthesizing the outputs of steps 1–6; they are not generated by a script, and their numerical content is fixed to `FINAL_RESULTS_LOCKED.md`.

## Verification performed during packaging

Each script above was re-run in an isolated test environment against the already-delivered raw files and its output compared against the previously-delivered derived files. `01_calculate_emp.py`, `02_build_master_dataset.py`, `03_gate2_analysis.py`, and `04_gate3_stress_test.py` reproduced their target outputs exactly (aside from floating-point representation noise at the 12th–16th significant digit in a small number of master-dataset cells, far beyond any figure's reporting precision, and one deliberately corrected file-path string in a notes column). `06_build_excel_workbook.py` reproduced a workbook with identical computed values and an identical "ALL CHECKS PASSED" result.

**Re-verified after `06_build_excel_workbook.py` was changed to read its Inputs-sheet and QA-reference values from `data/derived/master_analytical_dataset.csv` and `data/derived/gate3_stress_test.csv` at build time, instead of from hard-coded constants:** the full six-script pipeline was re-run end to end in a clean environment. All locked results matched exactly — Bangladesh combined deterioration −$12,258.14mn (shocked CA −$12,097.13mn), Pakistan −$11,850.34mn (shocked CA −$11,400.35mn), Vietnam −$70,616.15mn on the two-shock basis (shocked CA −$39,593.15mn) — and QA_Checks read "ALL CHECKS PASSED" with zero FAILs and zero formula errors across 109 formulas.

## What this project does not do

No causal inference, regression, or forecasting appears anywhere in this pipeline. External debt, REER, and policy rate are excluded from every script and every document by design. No script fabricates or imputes a missing observation (Vietnam's remittances, most notably, are absent by design — zero rows, never a zero value).
