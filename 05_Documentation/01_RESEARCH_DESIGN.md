# 01_RESEARCH_DESIGN.md

**Status: DRAFT — awaiting review and explicit "GATE PASSED"**
**Gate: 0 (Research Design)**

---

## 1. Title

**Exchange-Rate Flexibility and External Adjustment: An Early Comparative Assessment of Bangladesh, Pakistan, and Vietnam**

## 2. Research Question

**Main question:**
How has Bangladesh's external-sector adjustment evolved following the May 2025 move toward greater exchange-rate flexibility, and how does that adjustment compare with Pakistan and Vietnam during recent external stress episodes?

**Subquestions:**

1. How have Bangladesh's exchange market pressure (EMP), reserve levels, and current account balance moved since May 2025, relative to the pre-reform trend?
2. How does the scale and composition of Bangladesh's post-2025 external adjustment compare with Pakistan's adjustment during its 2022–23 balance-of-payments/reserve crisis, and with Vietnam's adjustment during its most comparable recent stress episode?
3. To what extent do structural differences — remittance dependence, reserve buffers, exchange-rate regime, trade/FDI structure — plausibly explain differences in how the three countries absorbed external shocks? (Explanatory, not causal.)
4. Under plausible remittance, import-price, and export shocks, how much additional external financing pressure would each country face today, and how does current reserve coverage compare across the three?

## 3. Country-Selection Rationale

- **Bangladesh (focal case):** Site of the May 2025 reform (move toward a crawling-peg/more flexible framework — exact classification to be confirmed against an IMF or Bangladesh Bank primary source at Gate 1). Also connects to your bKash/financial-sector background.
- **Pakistan (comparator):** History of periodic BOP and reserve crises, heavy IMF program engagement, a managed exchange-rate regime with a documented parallel-market premium, and — like Bangladesh — significant remittance dependence. Useful contrast on *how much stress* a broadly similar remittance-dependent, import-reliant economy has absorbed.
- **Vietnam (comparator):** Different exchange-rate management approach (managed/crawling band around a reference rate), an export-manufacturing/FDI-driven external sector rather than remittance-driven, and a different reserve-management history. Useful contrast on *structural type*, not a stress-severity match.

**Explicit framing:** the three countries are not structurally identical and the project will not imply they are. The comparison is meant to illustrate differences in exchange-rate management, external financing structure, reserve management, remittance dependence, and trade structure — not to benchmark Bangladesh against equivalent cases.

## 4. Sample Period & Frequency

**Proposed default (OPEN DECISION — see §12.1):** monthly data from **January 2018** through the latest available observation (expected ~mid-2026), with selected annual series (GDP growth, external debt stock) extended back to **2015** for trend/context charts only, not for the core EMP calculation window.

**Frequency by variable type (not forced into a single frequency — this asymmetry will be documented, not silently resolved):**
- Monthly: nominal exchange rate, international reserves
- Quarterly: current account, BOP components, external debt (where available quarterly)
- Annual: GDP growth; policy rate only if a genuinely comparable series exists

## 5. Provisional Variable List

**External sector**
- International reserves (gross, USD)
- Exports, imports (goods, USD)
- Current account balance
- External debt stock — **conditional**: include only if a consistently defined, comparable series exists across all three countries (to be confirmed at Gate 1); otherwise treated qualitatively in text, not as a chart variable

**External financing / shock exposure**
- Remittances (USD)
- FDI — **conditional**, included only if it adds genuine explanatory value to the comparison (per your Vietnam-vs-remittance-economy rationale)
- One commodity/import-price shock proxy (e.g., an import price or fuel price index — exact series to be confirmed at Gate 1)

**Exchange rate**
- Official nominal exchange rate (local currency/USD)
- REER — **conditional**: include only if one source (IMF or BIS) covers all three countries consistently over the sample window; otherwise dropped and noted as a limitation

**Domestic macro**
- Inflation (CPI)
- GDP growth
- Policy/interest rate — **conditional**, only if definitions are genuinely comparable across the three central banks

This is a deliberately small variable set. No variable is added because it "looks interesting" — each has a direct role in the EMP calculation, the adjustment narrative, or the stress-test model.

## 6. Candidate IMF / Official Datasets

To be confirmed with exact series IDs, table names, and access dates at **Gate 1** (this is a plan, not a verified source list):

- **IMF International Financial Statistics (IFS)** — exchange rates, reserves, core monetary aggregates
- **IMF Balance of Payments / IIP statistics** — current account, external debt
- **IMF World Economic Outlook (WEO) database** — GDP growth, inflation, cross-check aggregates
- **Bangladesh Bank** — reserves, exchange rate, remittances (national primary source)
- **State Bank of Pakistan** — reserves, exchange rate, remittances (national primary source)
- **State Bank of Vietnam / Vietnam General Statistics Office** — reserves, exchange rate (national primary source)
- **World Bank KNOMAD** — remittances (standard cross-country remittances source; may be preferred over IMF for this variable)
- **BIS effective exchange rate statistics** — candidate REER source if IMF's REER coverage is inconsistent across the three countries

I will not assume any of these are automatically harmonized across countries — definitions, units, and coverage get checked variable-by-variable at Gate 1/2.

## 7. EMP Methodology — Research Plan (not a final selection)

This project will use one specific, cited, published Exchange Market Pressure methodology — not a self-invented index. At **Gate 3**, before any implementation, I will:

1. Identify the exact published specification and provide a full citation
2. Explain each component and the mathematical formula
3. Explain the weighting scheme and its rationale
4. Explain sign conventions and interpretation
5. State the methodology's assumptions
6. Identify any adaptation required for this three-country dataset, and distinguish clearly between the original published methodology and our adaptation

**Candidate methodologies to investigate and verify against primary sources (economics literature — not yet confirmed, not yet a citation):**
- Girton & Roper (1977) — the original EMP index
- Weymark (1995) — a commonly used EMP variant with explicit reserve/exchange-rate/interest-rate weighting
- Eichengreen, Rose & Wyplosz (1996) — EMP index widely used in currency-crisis literature

None of these is selected yet. At Gate 3, one will be chosen, the primary published source located and cited properly, and you will verify it before implementation begins.

## 8. Bangladesh Reform-Period Framework

- Defined pre-reform period: observations before May 2025
- Reform/transition point: May 2025 (exact date and regime description to be confirmed against an IMF or Bangladesh Bank primary source at Gate 1)
- Post-reform observation window: May 2025 through the latest available data (~12–16 months — explicitly a short window)
- **Framing constraint:** this is an *early assessment*, not a causal evaluation. Language will use "early assessment," "observed post-reform dynamics," "associated with," "consistent with" — never "the reform caused/increased/improved" unless the evidence genuinely supports it (which a ~14-month window generally cannot).
- The short post-reform period is treated as a primary limitation of the project, stated explicitly wherever post-reform results are presented.

## 9. Stress-Test Framework

Excel-based scenario model with four illustrative shocks (clearly labeled as assumptions, not forecasts):
- Remittance shock: −10%
- Import-price shock: +10%
- Export shock: −5%
- Combined shock (all three simultaneously)

Outputs: adjusted remittances/exports/imports, external financing pressure, reserve impact, reserve/import coverage — each traceable to an observed baseline value plus a documented, visible assumption.

## 10. Key Limitations (to carry through to the paper's Limitations section)

- Short post-reform window for Bangladesh (~12–16 months) — precludes causal or long-run conclusions
- The three countries are structurally different; cross-country comparison illustrates contrast, not equivalence
- Parallel/kerb-market FX premia in Bangladesh and Pakistan are not modeled; official rates may understate underlying market pressure during segmented-FX periods — stated explicitly, not papered over
- Small cross-sectional N (3 countries) rules out formal panel econometrics; analysis stays descriptive/comparative by design
- Frequency mismatches across variables and sources (monthly vs. quarterly vs. annual)
- Data vintage/revision risk in real-time macro series

## 11. Preliminary Deliverables

- GitHub repository (`/data/raw`, `/data/cleaned`, `/data/derived`, `/stata`, `/excel`, `/figures`, `/paper`, `/policy_note`, `/presentation`)
- Research paper (8–12 pages)
- 2-page analytical/policy note
- 5-slide PowerPoint briefing
- Excel stress-testing model
- Reproducible Stata `.do` files
- Data dictionary
- `DATA_QA.md`
- `RESEARCH_LEDGER.md`
- `FINAL_RESULTS_LOCKED`
- Optional small Python component (only after all substantive work is complete)

---

## 12. Open Decisions Requiring Your Input

**12.1 — Sample period start year.** I've proposed January 2018 (monthly) with annual context data back to 2015. Reasonable, but the real constraint is each central bank's data availability, which I haven't checked yet. Confirm this as a working default, or tell me if you have a reason to prefer a different anchor (e.g., 2015 for a longer pre-reform baseline).

**12.2 — Vietnam's comparator stress episode.** For a roughly contemporaneous cross-country stress backdrop, I'd propose Vietnam's 2022–23 VND depreciation episode (associated with the global Fed-tightening/dollar-strength cycle) as the comparator, run alongside Pakistan's 2022–23 BOP crisis. Note this is a much milder episode for Vietnam than Pakistan's genuine crisis — the point of including it is structural contrast (resilience/exposure), not severity-matching. Confirm this framing, or propose an alternative Vietnam episode (e.g., 2015's one-off devaluation).

**12.3 — REER, external debt, FDI, policy rate (the four "conditional" variables in §5).** I'd rather confirm data availability/comparability at Gate 1 before committing to any of these, rather than guess now. Are you comfortable with that — i.e., these get decided one gate later, with a clear rule (include only if genuinely comparable, else drop with a documented reason) rather than a decision today?

**12.4 — Deadline.** Your notes mention Monday as a self-imposed, flexible target. Given the gate structure above, Gate 0–2 alone (design + data acquisition + cleaning) is unlikely to comfortably finish by Monday if done properly. Confirm you're treating Monday as soft, not a hard constraint I should be optimizing against.

---

**Next step:** review this document, resolve §12.1–12.4 (a short reply is fine — I don't need essays), and reply **"GATE PASSED"** when you're ready for me to move to Gate 1 (data acquisition and provenance). I won't start any data collection or coding before that.
