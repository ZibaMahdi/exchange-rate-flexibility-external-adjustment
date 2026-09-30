# RESEARCH_LEDGER.md

Running log of every claim, data-sourcing decision, and assumption made in this project. Every entry gets an ID. Nothing enters the paper, note, PowerPoint, or Excel model without an entry here.

---

## Standing Project Rules (permanent, apply from adoption forward)

**Rule: primary-source data acquisition.** For material external datasets, the researcher downloads the original data directly from the authoritative source and provides the untouched raw file to Claude. Claude may inspect and validate the uploaded file but must not reconstruct authoritative observations from search results, third-party aggregators, or inferred APIs when a direct source export is available. (Adopted following the reserve-variable verification — see the IMF International Liquidity extraction below for the case that motivated this rule.)

**Terminology rule:** "IMF IFS" is historical terminology. IMF's International Financial Statistics database has been retired and split into thematic dataflows; the reserves-relevant successor is **IMF International Liquidity (IL)**. Entries below written before this was discovered still say "IMF IFS" — left as-is for the audit trail, not corrected retroactively — but all current and future documentation should say **IMF International Liquidity (IL)** and cite exact series codes (e.g., `BGD.RXF11_REVS.USD.M`), not the historical name alone.

---

## Claims

**Claim ID: C-001**
**Claim:** Bangladesh Bank introduced a crawling peg exchange rate system in May 2024 (mid-rate BDT 117/USD, an interim IMF-linked arrangement), then moved to a more flexible "crawling peg with band" / market-based regime in mid-May 2025, which unlocked the fourth and fifth tranches of the IMF's $4.7bn ECF/EFF/RSF loan package.
**Source:** IMF, *Bangladesh: 2025 Article IV Consultation — Press Release, Staff Report, and Statement by the Executive Director*, IMF Staff Country Reports Vol. 2026, Issue 024 (published Jan 30, 2026), para. 8: "With the launch of a more flexible exchange rate arrangement in May 2025 ... In mid-May 2025, BB introduced the new crawling peg with the band regime..." — https://www.elibrary.imf.org/view/journals/002/2026/024/article-A001-en.xml
**Corroborating (non-primary) sources:** Bangladesh Bank press statement reporting, May 8, 2024 (Bloomberg, BSS); The Business Standard and The Daily Star reporting on the May 14, 2025 announcement.
**Status:** VERIFIED against an IMF primary source.
**Correction note:** the working characterization used earlier in this project ("shift toward a *fully flexible* exchange rate in May 2025") overstates what the primary source documents. The IMF's own language is "a more flexible exchange rate arrangement" implemented as a **crawling peg with band**, not a free float. The paper/note must use "more flexible" / "crawling peg with band," not "fully flexible" or "float," unless a later primary source (e.g., a subsequent Article IV report) documents a further move to full float.
**Action for Gate 2:** if possible, locate the actual Bangladesh Bank circular/press release from May 2025 to confirm the exact regime terminology BB itself used, as a second corroborating primary source alongside the IMF report.
**Standing rule (permanent, effective this entry forward):** always write "more flexible exchange-rate arrangement" / "crawling peg with band" for the May 2025 reform. Never "fully flexible," "free float," or "float," unless a later primary source explicitly documents that characterization.

---

## Status vocabulary (adopted from this point forward; earlier entries below are being reclassified into these four terms)

- **VERIFIED** — exact dataset/series has been inspected (not just located)
- **SOURCE IDENTIFIED** — official source located, but the actual series has not yet been inspected
- **UNRESOLVED** — a candidate source exists but comparability, coverage, or definition is uncertain
- **REJECTED** — a source/series was considered and rejected, with the reason stated

---

## Data-Sourcing Decisions (Gate 1 — Batch 1: Reserves, Exchange Rate, Remittances)

**Decision ID: D-000a — Attempted harmonized reserves series (per instruction, before falling back to national sources)**
**Candidate dataset:** IMF International Reserves and Foreign Currency Liquidity (IRFCL / "Reserves Data Template") — https://data.imf.org/en/datasets/IMF.STA:IRFCL
**Why it's a strong candidate:** IRFCL re-disseminates member countries' reserves data "in a common template and in a common currency (the U.S. dollar)," explicitly aligned with BPM6. This is the closest thing the IMF has to a conceptually harmonized cross-country reserves definition (Section I: "Official Reserve Assets and Other Foreign Currency Assets").
**Indicator (as documented, not yet confirmed in-portal):** Section I, "Official reserve assets," IRFCL dataset
**Unit:** USD (common currency, per template design)
**Frequency:** Monthly (SDDS-prescribed periodicity, no more than a one-month lag, for subscribing countries)
**Stock/flow:** Stock, end-of-period
**Country coverage — UNRESOLVED:** IRFCL is a *prescribed component of the SDDS* (Special Data Dissemination Standard). Only SDDS subscribers are obligated to report it monthly; e-GDDS participants (a lower, non-prescriptive tier) are not. I found indications that Pakistan and Vietnam both have e-GDDS-related metadata pages on the IMF's Dissemination Standards Bulletin Board (dsbb.imf.org), which would suggest e-GDDS rather than SDDS participation, but the DSBB's actual subscriber list is a JavaScript-rendered page my tools could not read — **I could not confirm SDDS/IRFCL participation for any of the three countries through search or fetch.**
**Status: SUPERSEDED — see "CURRENT FINAL DECISION — Reserve Variable" near the end of this file.** IRFCL country coverage for the three countries was never confirmed either way; the project routed around this open question entirely by using the **IMF International Liquidity (IL)** dataset instead (a different IMF product, confirmed usable via an actual downloaded file). This entry stays as history of a path that was tried and left open, not one that was resolved.

**Decision ID: D-001**
**Variable:** International reserves — Bangladesh
**Source:** Bangladesh Bank, Economic Data → Foreign Exchange Reserve (Monthly) — https://www.bb.org.bd/en/index.php/econdata/intreserve
**Frequency:** Monthly
**Unit:** USD million (BB reports "Reserves (Gross)")
**Status: SUPERSEDED by the Final Reserve Decision (see "CURRENT FINAL DECISION" near the end of this file).** Bangladesh Bank's own gross and BPM6-basis series remain valid for country-specific/descriptive use and as a validation cross-check (see the Jan 2026 discrepancy note below), but are **not** the series used for the cross-country/EMP common sample — that role is filled by IMF International Liquidity (IL), series `BGD.RXF11_REVS.USD.M`.
**Known complication (kept for history):** Bangladesh Bank and IMF report two different reserve figures — a **gross** reserves number and a lower **BPM6-basis** ("net"-adjusted) number (e.g., contemporaneous reporting shows gross reserves of ~$31.2bn vs. BPM6 reserves of ~$26.5bn in Dec 2025). Per your instruction, this is deliberately not being resolved in isolation — it depends on the D-000a outcome first.

**Decision ID: D-002**
**Variable:** International reserves — Pakistan
**Source:** State Bank of Pakistan, EasyData portal, "Gold and Foreign Exchange Reserves of Pakistan" — https://easydata.sbp.org.pk/ (dataset reference visible in portal URL: `TS_GP_EXT_PAKRES_M`)
**Frequency:** Weekly (SBP publishes a weekly reserves statement) and monthly (EasyData series)
**Unit:** USD million
**Status: SUPERSEDED by the Final Reserve Decision (see "CURRENT FINAL DECISION" near the end of this file).** SBP's own series remain valid for Pakistan-specific/descriptive use, but the cross-country/EMP common sample uses IMF International Liquidity (IL), series `PAK.RXF11_REVS.USD.M`, instead.
**Known complication (kept for history):** Pakistani reporting distinguishes "SBP-held reserves" from "total liquid reserves" (SBP + commercial banks). Must pick one and document why — SBP-held reserves is the more standard comparator to Bangladesh Bank's and SBV's central-bank-held reserves.

**Decision ID: D-003**
**Variable:** International reserves — Vietnam
**Source:** No suitable regularly downloadable SBV monthly reserve series has been located so far. Continuing to check SBV and IMF sources.
**Status: SUPERSEDED by the Final Reserve Decision (see "CURRENT FINAL DECISION" near the end of this file).** The "no Vietnam national series found" finding below remains valid history and explains why a national fallback wasn't available — but it's no longer a blocker, since Vietnam is covered by IMF International Liquidity (IL), series `VNM.RXF11_REVS.USD.M`, confirmed via an actual downloaded file (102/103 monthly observations, 2018-M01–2026-M06).
**Finding so far (kept for history):** I have not found a standing, downloadable reserves time series on the State Bank of Vietnam's own site through search. This is a statement about what my search has and hasn't turned up, not a claim about SBV's actual publication practices — I have not exhaustively browsed sbv.gov.vn's statistics section, and this needs a direct check (by me next session or by you) before concluding anything stronger. Reserves figures in Vietnamese/international press coverage are often attributed to brokerage estimates or one-off SBV statements rather than a cited standing table, and third-party aggregators (Trading Economics) list "IMF" as their source for Vietnam's reserves series — both are circumstantial, not confirmation of absence.
**Other candidate not yet checked:** NSO Vietnam's "Total international reserves of some countries and territories" table at https://www.nso.gov.vn/en/statistical-data/ — unclear if this covers Vietnam itself or is a comparator table of other countries; needs opening and checking, not assumed either way.
**Implication if no SBV/NSO series is confirmed:** Vietnam reserves would come from IMF IFS/COFER while Bangladesh's and Pakistan's come from national sources — a within-dataset inconsistency requiring explicit documentation, not silent handling.

**Decision ID: D-004 — SUPERSEDED, see D-013 below**
**Variable:** Official nominal exchange rate — all three countries
**Source (candidate, all three):** IMF International Financial Statistics, via the new IMF Data Portal (https://data.imf.org — legacy data.imf.org portal retired; IFS content now organized by topic dataset). Exact indicator ("Exchange Rates, National Currency per U.S. Dollar, Period Average" or similar) must be located and its indicator code recorded by whoever pulls the data, since the portal is filter-based rather than exposing a simple static series ID.
**National-source alternatives:** Bangladesh Bank Economic Data → Exchange Rate; SBP EasyData; Vietnam — no clear public SBV daily/monthly reference-rate table found yet, needs a follow-up check.
**Status: SUPERSEDED.** The IMF's exchange-rate dataset has been specifically identified as "Exchange Rates (ER)," `IMF.STA:ER` — see D-013 for the current, precise target. This entry's historical content is kept for the audit trail.
**Note (historical):** I could not verify an exact "series ID" string for IMF IFS exchange rate data through search alone — the portal requires interactive filtering (Dataset → Indicator → Country). Whoever pulls this data should screenshot/record the exact indicator name and code shown in the portal at download time, per DATA_QA.md.

**Decision ID: D-005a — Remittances, monthly (for high-frequency / post-May-2025 analysis)**
**Bangladesh — SOURCE IDENTIFIED, confirmed:** "Monthly data of Wage earner's remittance," Bangladesh Bank Economic Statistics — `https://www.bb.org.bd/en/index.php/econdata/wageremitance`. Live, specific page, consistently cited by independent sources (IOM, Financial Express) as the standard reference for this series.
**Pakistan — SOURCE IDENTIFIED, confirmed:** SBP publishes "Workers' Remittances" (raw and seasonally-adjusted separately) under its Economic Data section. Old direct paths (`sbp.org.pk/ecodata/homeremit.pdf`, `.../homeremmit/index2.asp`) exist in search results but, per the exports/imports lesson earlier this project, old `ecodata/*.pdf`-style links have been found stale before — Ziba to navigate via the live site menu rather than the old path directly.
**Vietnam — UNRESOLVED — no suitable nationwide monthly primary remittance series has been located so far in the main SBV/NSO statistical sources checked.** A second, focused search (per instruction) specifically checked: nationwide "kiều hối" reporting, SBV regional-branch releases, and BOP secondary-income/current-transfer publications. Findings:
  - SBV's Region 2 branch (`NHNN Chi nhánh Khu vực 2`) publishes **quarterly, Ho Chi Minh City–specific** remittance figures regularly (e.g., Q2 2026: $2.032bn to HCMC) — a real, recurring official release, just regional, not national, and quarterly, not monthly.
  - One academic source citing SBV directly (SBV 2022) gives a **multi-year cumulative national secondary-income/current-transfer total** (2016–2021Q3), not a regular published monthly/quarterly national time series.
  - CEIC/World Bank-sourced "BOP: Current Account: Personal Remittances" for Vietnam is explicitly **annual only** ("updated yearly"), consistent with everything else found about Vietnam remittances data.
  - Statista's own methodology notes state plainly that Vietnam "does not rely on IMF data" for remittances and is "one of the most difficult countries to track."
  - **This confirms the correction requested:** official Vietnamese remittance reporting does exist at other frequencies/geographies (regional quarterly, national annual/multi-year), so "no monthly national source exists" is not established — only that none has been located among the main statistical tables checked so far, at the specific monthly-national combination this project needs.
**Status: SOURCE IDENTIFIED for Bangladesh and Pakistan (pending file upload before VERIFIED). Vietnam: UNRESOLVED / NO SUITABLE NATIONWIDE MONTHLY PRIMARY SERIES LOCATED — not REJECTED.**
**Use case:** this monthly series — not the annual harmonized one below — is what feeds the Bangladesh reform-period analysis (Gate 5) and any monthly cross-country charting.
**Proposed fallback design for Vietnam (proposal only, not adopted — awaiting Ziba's decision):**
  1. Use Vietnam's annual national secondary-income/personal-remittances figure (SBV-sourced where available, World Bank WDI mirror otherwise) as annual-only descriptive/context material — explicitly labeled as annual, never blended into a monthly chart or table alongside Bangladesh/Pakistan's monthly data.
  2. HCMC quarterly regional data is not used as a substitute for the national figure anywhere (per instruction) — it may be mentioned qualitatively (e.g., "HCMC alone typically accounts for over half of national remittances") but never plotted or tabulated as if it were the national series.
  3. For Gate 6's remittance stress-test scenario specifically, either scope that scenario to Bangladesh/Pakistan only with Vietnam explicitly excluded and the reason stated, or apply the shock to Vietnam's annual figure separately with a clearly different, lower-frequency treatment — not decided, flagged for when Gate 6 is reached.

---

## Remittances — Bangladesh and Pakistan Verified (Vietnam remains open, see above)

**Bangladesh — manually extracted table, independently parsed and QA-checked (not trusted at face value):**
- **Source:** Bangladesh Bank, "Monthly Report on Workers' Remittance Inflows in Bangladesh — July, 2026," Table: "Month-wise Workers' Remittance Inflows FY 2014-15 to FY 2026-27." **This is a SOURCE-DERIVED DATA EXTRACT (manually copied from a PDF), not a native CSV/Excel export** — recorded as such per instruction, not treated as equivalent to the IL/ER portal downloads.
- **FY-total consistency check:** recomputed all 12 fiscal years' monthly sums against the table's own reported totals — every difference is ≤$0.02mn (rounding-level only). No transcription errors found at this check.
- **Anomaly found and flagged, not silently resolved:** a stray duplicate entry (`2858.76`, mislabeled `2025-2026`) appears at the end of the pasted table — the same value as FY2026-2027's correctly-placed July figure. Treated as a rendering duplicate of the single July 2026 observation, not a second data point; not confirmed against the source PDF directly. Full detail in `PROVENANCE.md`.
- **Calendar-month reconstruction:** FY → calendar-month conversion performed exactly as instructed (FY N-1/N July–Dec = calendar year N-1, Jan–Jun = calendar year N). Result: **103 consecutive monthly observations, Jan 2018–Jul 2026, zero missing, zero duplicates.**
- **Live-webpage discrepancy:** Ziba has stated the live BB "Monthly data of Wage earner's remittance" webpage shows slightly different values from this July 2026 PDF report. **Not independently verified this pass** (the live page's values were not in hand to compare) — recorded as Ziba's stated observation, not confirmed by Claude. **Per instruction, the July 2026 PDF report is the selected vintage for this project**, and this discrepancy is logged, not reconciled.
- **Status: VERIFIED** for Jan 2018–Jul 2026, as a source-derived extract (not a native export) — vintage explicitly the July 2026 PDF report.

**Pakistan — native SBP EasyData export, independently inspected:**
- **Series:** "Total Cash Worker Remittances," series key `TS_GP_BOP_WR_M.WR0010`, dataset "Country-wise Workers' Remittances," Million USD.
- **Coverage (independently recomputed):** 104/104 observations, Jan 2018–Aug 2026, zero missing, zero duplicates, all rows flagged "Normal" observation status.
- **Comparability caveat:** the series carries no explicit "seasonally adjusted" or "raw" label. Its absence of an "SA" marking is consistent with it being the raw series requested, but this is inferred, not confirmed — flagged in `PROVENANCE.md`.
- **Status: VERIFIED** for Jan 2018–Aug 2026 (one month ahead of Bangladesh's PDF-report vintage).

**Common Bangladesh–Pakistan window:** Jan 2018–Jul 2026 (Bangladesh's July 2026 PDF report is the binding constraint; Pakistan's Aug 2026 observation is retained for country-specific use only, same pattern as reserves/exchange rate). **Vietnam remains excluded from any common three-country monthly remittances table pending resolution above.**

**Raw files preserved:** `/data/raw/bd_remittances/` (reconstructed calendar series + full provenance including the original pasted table verbatim) and `/data/raw/pk_remittances/` (native CSV, SHA-256 checksummed), neither modified beyond the explicitly-instructed FY→calendar conversion for Bangladesh.

---

## Final Metadata Check — Pakistan Series Definition, and Bangladesh/Pakistan Comparability (one targeted search only, per instruction)

**Pakistan — is `WR0010`/"Total Cash Worker Remittances" the raw or seasonally-adjusted series?** Could not find an EasyData catalogue page stating this explicitly for the `WR0010` key itself. What the targeted search did establish: SBP's own site hosts **two distinctly-titled products** — plain "Workers' Remittances" (`sbp.org.pk/ecodata/homeremit.pdf`) and a separately-named **"Workers' Remittances - Seasonally Adjusted"** (`sbp.org.pk/ecodata/homeremmit/index2.asp` and `.../Remittance.pdf`). Our uploaded series' name, "Total Cash Worker Remittances," does not match the SA-labeled product's title — this is circumstantial support for it being the unadjusted series, not proof. **Status: still not fully confirmed; treat as "very likely unadjusted, not certain."**

**Pakistan — one real, dated definitional finding from the same source (`homeremit.pdf` footnotes):**
1. "The data of Workers' Remittances includes the conversions related to current transfers from Roshan Digital Accounts since September 2020."
2. "Data is based on original country of remitter from July, 2019."
Both are genuine, dated scope changes **within Pakistan's own series** — a real definitional widening starting Sept 2020, not something Bangladesh's series necessarily shares. This is a break to flag regardless of the BD/PK comparability question below.

**Definitions, as documented so far:**
- **Bangladesh Bank "Wage earner's remittance":** official monthly compilation of remittance inflows from Bangladeshi wage earners abroad, via the banking channel, published by BB's Statistics Department (Foreign Exchange Policy Department prior to June 2016). I did not find an equivalently detailed methodological footnote for Bangladesh in this pass (e.g., whether mobile-financial-service or digital-channel remittances are included/excluded, or since when) — this is an asymmetry in documentation depth, not evidence that BB's series lacks such detail, just that it wasn't found here.
- **SBP "Total Cash Worker Remittances":** cash current transfers from Pakistani workers abroad, banking-channel-recorded, with the confirmed Sept 2020 Roshan Digital Account inclusion and July 2019 country-of-remitter basis change noted above.

**Comparability assessment:** both series are official, central-bank-compiled, banking-channel cash remittance-inflow totals in USD, monthly — conceptually the same *kind* of measure, and reasonable to use as a cross-country remittance-inflow indicator for this project. They are **not confirmed identical in scope**: Pakistan's has a documented Sept 2020 widening (RDA inclusion) with no confirmed Bangladesh equivalent, and Bangladesh's own methodological detail wasn't found to the same depth this pass. Neither gap is large enough to reject the comparison, but neither is resolved — **flagged as an open comparability QA item, not silently assumed away.**

**Final status:** Bangladesh and Pakistan remittances remain **VERIFIED for observed coverage** (Jan 2018–Jul/Aug 2026 respectively, as already established) — **with a clearly separate, visible comparability/definition QA item open** (see DATA_QA.md) until a fuller methodological comparison (or official EasyData catalogue confirmation of `WR0010`) is available. **Vietnam remains UNRESOLVED** — no suitable nationwide monthly primary series located; unchanged this pass.

**Not proceeding to current account/BOP or any later variable.**

---

## CURRENT FINAL DECISION — Remittances (Gate 1 closed for this variable)

- **Bangladesh: VERIFIED, Jan 2018–Jul 2026.** Source-derived extract from Bangladesh Bank's July 2026 Monthly Report (not a native machine-readable export) — this label is permanent for this series, not a temporary caveat.
- **Pakistan: VERIFIED, Jan 2018–Aug 2026.** SBP EasyData, series key `TS_GP_BOP_WR_M.WR0010`.
- **Pakistan raw-vs-seasonally-adjusted classification: VERY LIKELY UNADJUSTED, NOT fully confirmed.** Retained permanently as a QA caveat, not resolved by assumption.
- **Bangladesh/Pakistan comparability:** sufficiently comparable for use as an official monthly remittance-inflow indicator (both are central-bank-compiled, banking-channel cash inflow totals in USD) — **not assumed definitionally identical.**
- **Pakistan methodological breaks, permanently documented:** July 2019 country-attribution basis change; September 2020 scope widening to include Roshan Digital Account conversions.
- **Vietnam: UNRESOLVED — no suitable nationwide monthly primary remittance series located.** HCMC regional data is never used as a national substitute. Vietnam's annual remittance figures are never placed into a monthly table.
- **This variable will not be reopened unless new primary evidence creates a material contradiction.**

---

**Decision ID: D-005b — Remittances, annual (for harmonized cross-country context only)**
**Source:** World Bank World Development Indicators, "Personal remittances, received" (current US$ and % of GDP) — **not** KNOMAD's bilateral remittance matrix, which is corridor-level (e.g., USA→Bangladesh) and the wrong granularity for this project. KNOMAD itself states it was "active from 2013 until 2024" and appears wound down as a standalone initiative.
**Status: SOURCE IDENTIFIED**
**Explicit constraint (per your instruction):** this annual series is for cross-country context/comparison tables only. It must **not** be substituted into the monthly post-May-2025 Bangladesh analysis just because it's more harmonized — that analysis uses D-005a.

---

## Data-Sourcing Decisions (Gate 1 — Batch 2: Current Account/BOP, Exports/Imports, External Debt)

**Decision ID: D-006 — SUPERSEDED, see D-014 below**
**Variable:** Current account balance / BOP — all three countries
**Bangladesh:** Bangladesh Bank Economic Data → "BOP, Export & Import" section (listed on bb.org.bd; exact sub-page URL not yet opened)
**Pakistan:** SBP Economic Data → External Sector → Balance of Payment, explicitly reported "as per BPM6" — direct PDF found at https://www.sbp.org.pk/ecodata/Balancepayment_BPM6.pdf
**Vietnam:** NSO Vietnam (formerly GSO), Statistical Data section — "Balance of payment by Classify, Balance of payment and Year" table at https://www.nso.gov.vn/en/statistical-data/
**Frequency:** Bangladesh and Pakistan appear to report monthly/cumulative BOP; Vietnam's NSO table frequency not yet confirmed (may be annual only)
**Status: SUPERSEDED.** This entry mixed the (separate) exports/imports finding in with BOP and predates the one-variable-at-a-time workflow. See D-014 for the current, focused current-account/BOP-only research.
**Positive finding (kept for history):** SBP explicitly labels its BOP data "as per BPM6," which is a good sign for comparability with Bangladesh Bank's data if BB does the same.
**Correction from direct verification (kept for history — this was actually about the exports/imports PDF, not BOP itself):** I fetched the SBP PDF link found via search (sbp.org.pk/ecodata/exp_import_BOP.pdf) directly, and it redirects to the SBP homepage rather than returning the PDF — meaning that specific link is stale/broken, likely from an old site structure. **Confirmed live alternative:** SBP's current site has a live "Economic Data" section at https://www.sbp.org.pk/economic-data. **Old ecodata/*.pdf paths should be treated as unreliable until re-confirmed; use sbp.org.pk/economic-data and easydata.sbp.org.pk going forward.**

---

## Current Account / BOP — One-Variable-at-a-Time Pass (Current)

**Decision ID: D-014 — Current account / Balance of Payments, source identification (Step 1)**

**Bangladesh:** Bangladesh Bank's own Statistics Department mandate (confirmed directly from BB's site) states its remit is *"to compile monthly Bangladesh Balance of Payments statistics in standard and analytic formats as per BPM-6 of IMF... to prepare and provide monthly data on import, export and BOP to IMF on regular basis."* This is a strong, specific confirmation that BB compiles **monthly, BPM6** BOP data. However, a third-party aggregator (CEIC) shows Bangladesh's BOP current-account balance as **monthly when denominated in BDT**, but **quarterly when denominated in USD** — a real discrepancy in frequency-by-currency that needs checking directly against BB's own publication once the file is in hand, not assumed.
**Pakistan:** SBP's own live site confirms a regularly-updated release: *"Summary of Balance of Payments BPM6 (Seasonally adjusted) for [month]"* — most recently "for Aug 26." This is **monthly, BPM6**. **Correction:** SBP's archive in fact shows **two** distinct monthly BPM6 BOP products — "Balance of Payments as per BPM6 – Seasonally Adjusted" and a separate **"Summary of Balance of Payments as per BPM6"** (non-seasonally-adjusted). The non-SA release does exist; my earlier statement that only the SA release was found is corrected. The non-SA release is the one to use as Pakistan's national monthly candidate — not the SA one.
**Vietnam:** confirmed via CEIC/Trading Economics that the **State Bank of Vietnam itself provides a quarterly Current Account Balance series**, BPM6 since 2012 (BPM5 before) — a real, specific, dated methodological break (BPM5→BPM6 in 2012) to log if the series is pulled back that far (irrelevant if we only need 2018 onward, but worth noting the vintage is post-2012-conversion throughout our sample). This is a meaningfully better starting position for Vietnam than reserves or remittances were — Vietnam is not obviously the hard case for this particular variable.

**Frequency comparability — the key finding for Step 4:** Bangladesh and Pakistan both have genuine **monthly** BPM6 releases; Vietnam's national release is **quarterly only**. This means **quarterly, not monthly, is the likely common frequency for any three-country BOP/current-account comparison** — the same structural pattern as several earlier variables (Vietnam is the binding constraint), just at a coarser frequency than reserves/exchange rate/remittances. Bangladesh's and Pakistan's monthly detail can still be used in their own country-specific sections, same pattern as before.

**IMF candidate:** the **IMF Balance of Payments (BOP)** dataset (`IMF.STA:BOP`, data.imf.org) is confirmed to exist, BPM6-consistent across ~204 economies, "quarterly and annual" in its own description — a plausible harmonized common-layer candidate, following the same pattern used successfully for reserves (IL) and exchange rate (ER). Not yet confirmed whether IMF's own BOP dataset actually carries observations for all three countries at quarterly frequency through the current sample — this needs the same kind of direct-file check as before, not assumed from the dataset's general description.

**Exact IMF indicator for current-account total — not confirmed remotely.** A targeted search found only the dataset's general description and the BPM6 hierarchical coding structure (aggregate + BOP-item + accounting-entry + sector + maturity codes), not a literal indicator string for "current account total, net." The portal's indicator selector is interactive/JS-rendered, same limitation as before. **This means the metadata check (definition, sign convention, unit, frequency) has to happen when Ziba actually selects the indicator in the portal — I cannot pre-verify it from here.** Instructions below tell Ziba what to check at that point rather than asserting a code I haven't seen.

**Status: SOURCE IDENTIFIED for all three countries.** Not VERIFIED — no file uploaded or inspected yet. Per instruction, only the IMF download is requested this turn; Bangladesh/Pakistan national files are not requested until the IMF file is inspected and its exact current-account series confirmed.

---

## IMF BOP File — Independently Inspected (A–N)

**A. Dataset name/version:** `IMF.STA:BOP(21.0.0)`
**B. Exact indicator/series name and code:** "Current account balance (credit less debit)," Accounting Entry "Net (credits less debits)" — series codes `PAK.NETCD_T.CAB.USD.Q`, `VNM.NETCD_T.CAB.USD.Q`, `BGD.NETCD_T.CAB.USD.Q`
**C. Definition:** headline current-account balance, credits minus debits — confirmed genuinely the total balance, not a subcomponent and not the "excluding exceptional financing" variant (that qualifier is absent from this file's INDICATOR field; only one series per country was returned, so there was no ambiguity to resolve between alternatives)
**D. Frequency:** Quarterly
**E. Unit:** US dollar, Millions
**F. Sign convention:** credits less debits — positive = surplus, negative = deficit. Confirmed consistent with the data itself: Pakistan predominantly negative (matches its well-known chronic deficits), Vietnam predominantly strongly positive (matches its export-surplus profile), Bangladesh mixed, trending toward near-zero/positive by 2026-Q1
**G. Flow vs. stock:** Flow (quarterly), as expected for a BOP current-account statement
**H. Seasonally adjusted vs. not:** **no explicit SA/NSA field in this file's metadata.** IMF's standard BOP presentation is conventionally NSA at the international-compilation level — this is general practice, not something confirmed field-by-field in this specific file. Flagged as open, not asserted as settled.
**I. First and last observation:** Pakistan 2018-Q1 (-4,394.60) to 2026-Q2 (-424.60); Vietnam 2018-Q1 (3,028.43) to 2026-Q1 (2,716.00); Bangladesh 2018-Q1 (-2,259.59) to 2026-Q1 (3.07)
**J. Number of observations:** Pakistan 34/34; Vietnam 33/34; Bangladesh 33/34
**K. Missing quarters:** Pakistan — none. Vietnam and Bangladesh — both missing `2026-Q2` only (a trailing-vintage lag, same pattern as every prior variable, just with Pakistan ahead this time instead of Bangladesh/Pakistan being ahead of Vietnam)
**L. Country coverage:** all three countries present, one series each, no ambiguity
**M. Common three-country coverage window: 2018-Q1 through 2026-Q1.** Pakistan's 2026-Q2 retained for country-specific use only, not part of the common panel
**N. Methodological breaks/revisions visible in metadata:** none flagged in the file itself (no BPM5/BPM6 tag, no revision marker present) — BPM6-consistency across all three is inferred from IMF's stated general practice of harmonizing all reported BOP data since 2012, not confirmed field-by-field in this file

## Frequency rule confirmed followed
This series remains quarterly — **not** converted to monthly. Bangladesh/Pakistan national monthly BOP data, if pursued later, will be sourced separately for country-specific detail and will **not** be mixed into this harmonized quarterly panel.

## Final status
**Current Account / BOP — IMF quarterly common layer: VERIFIED for 2018-Q1–2026-Q1**, across all three countries, on the confirmed headline "credit less debit" net balance, USD, quarterly. Raw file preserved unmodified at `/data/raw/imf_bop_current_account/` (SHA-256 in `PROVENANCE.md`).

**Recommended next step (not mandatory, your call):** a national cross-check is not required to call this VERIFIED — following the same precedent as reserves and exchange rate, where national sources served as a validation layer rather than a gate. If a cross-check is wanted: Bangladesh Bank's monthly BOP (aggregated to quarterly for comparison) or SBP's non-seasonally-adjusted "Summary of Balance of Payments as per BPM6" would be the candidates — neither has been downloaded yet, and neither is requested this turn per your instruction.

**Not proceeding to exports/imports, GDP, CPI, or any other variable.**

---

## CURRENT FINAL DECISION — Current Account / BOP (Gate 1 closed for this variable)

- **IMF dataset:** `IMF.STA:BOP(21.0.0)`
- **Series:** `BGD.NETCD_T.CAB.USD.Q`, `PAK.NETCD_T.CAB.USD.Q`, `VNM.NETCD_T.CAB.USD.Q`
- **Definition:** Current account balance (credit less debit); Accounting entry: Net (credits less debits)
- **Unit:** US dollar, millions. **Frequency:** Quarterly. **No monthly conversion performed or planned.**
- **Common sample: 2018-Q1 through 2026-Q1.** Bangladesh and Vietnam have no 2026-Q2 observation in the current vintage; Pakistan's 2026-Q2 is retained for country-specific use only, not part of the common three-country panel.
- **Documented metadata caveats (not blockers):**
  1. The file contains no explicit SA/NSA field.
  2. BPM6 consistency rests on the IMF BOP dataset's documented general methodology, not a field-level tag inside this specific CSV.
- **National Bangladesh Bank / SBP BOP releases are not required to close this variable.** They remain available as secondary cross-checks only if a substantive discrepancy arises later (e.g., during Gate 3 EMP construction or Gate 5's Bangladesh analysis) — not pursued proactively.
- **This variable will not be reopened unless new primary evidence creates a material contradiction.**

---

---

## Reserve-Source Verification Pass (focused task, per instruction)

**1. IRFCL direct check:** Attempted via web_search and web_fetch. data.imf.org's IRFCL pages are dataset-description pages, not queryable country tables through these tools — the actual country-selection interface is JavaScript-rendered and not readable this way. **I could not obtain per-country IRFCL observations, coverage dates, or confirm/deny country participation directly.** This remains genuinely UNRESOLVED, not assumed either way (per instruction 4) — it needs a human at the interactive portal.

**2. SBP archive check (three candidates you named):** I did not find "International Reserves and Foreign Currency Liquidity" or "Official Reserve Assets" as separately branded SBP products through search or direct site access. What exists is: (a) SBP's live homepage/economic-data snapshot, itemizing "SBP's Reserves," "Bank's Reserves," and "Total Reserves" (weekly), and (b) the EasyData portal series referenced by code `TS_GP_EXT_PAKRES_M` ("Gold and Foreign Exchange Reserves of Pakistan," monthly). These two look like the same underlying concept at different frequencies, not three distinct products — I did not find evidence of a separate, more BPM6-explicit "Official Reserve Assets" line distinct from these.

**3. Vietnam re-check (exact pages checked):**
- NSO Vietnam → Statistical Data → International Statistics tab → item "Total international reserves of some countries and territories" (https://www.nso.gov.vn/en/px-web?pxid=E1506). This resolves to an interactive PxWeb table (pxweb.nso.gov.vn/pxweb/en/International%20Statistics/...E15.06.px) which my tools can't extract values from, but the table's own title ("...of some countries and territories," matching the pattern of NSO's other comparative tables like "GDP of some countries and territories") strongly suggests this is a cross-country reference/context table, not Vietnam's own primary release.
- NSO Vietnam → Banking, insurance and State budget section — has Balance of Payments, credit, interest/exchange rate tables, but **no reserves line found** in that section specifically.
- SBV's own site (sbv.gov.vn/en) — its published statistical menu (repeated identically across several SBV pages I found) lists: CPI, Reserve requirement, Interest Rate, Money Market Operations, Open Market Operations, State Treasury bill auctions, Gold Auctions. **Foreign exchange reserves is not among SBV's own listed statistical categories** ("Reserve requirement" here means the bank reserve-requirement ratio, a different concept, not FX reserves).
- An SBV-published commentary piece on global FX reserves trends (found via search) cites the IMF's COFER data brief as its source when discussing reserves figures, rather than an SBV series — circumstantial but notable: SBV's own analysts appear to reach for IMF data on this topic too.
- **Conclusion, stated at the confidence level the evidence supports:** across these four specific checks, no dedicated, primary, Vietnam-specific monthly reserves release was found. This is stronger than the earlier "no suitable series located" note (more places checked, more consistently pointing the same way) but is still not a claim that SBV never publishes one anywhere — only that it wasn't found where a reserves release would be expected to be.

**4–5. Comparison table (reserves, per instruction 5):**

| Country | Source | Series/item | Definition | Frequency | Unit | Coverage | Methodological basis | Comparable across countries? | Decision |
|---|---|---|---|---|---|---|---|---|---|
| Bangladesh | Bangladesh Bank | Foreign Exchange Reserve (Monthly) — "Reserves (Gross)" | Gross FX reserves held by BB | Monthly | USD mn | Long run, not yet pulled | National; BB separately quotes a lower BPM6-basis figure elsewhere (different series, not this one) | Uncertain — depends on whether BB's BPM6 figure is itself a downloadable series (not yet checked) | Not yet decided |
| Pakistan | SBP (EasyData `TS_GP_EXT_PAKRES_M` + live economic-data page) | Gold and Foreign Exchange Reserves — split SBP-held / Bank / Total | Central-bank vs. total-system liquid FX reserves | Weekly (live) / Monthly (EasyData) | USD mn | Current + recent history confirmed live; full historical depth not yet pulled | National; explicitly holder-split | Uncertain — same gross-vs-narrower-basis ambiguity as Bangladesh | Not yet decided; SBP-held proposed as the closer analogue to BB's/SBV's central-bank concept |
| Vietnam | None found as a dedicated primary release (see checks above) | — | — | — | — | — | — | No | Not usable as a national primary source based on checks so far |
| All three | IMF, IFS "Total Reserves" (re-disseminated via World Bank WDI as "Total reserves (includes gold), current US$") | Total reserve assets | BPM6-consistent, common-currency (USD) presentation | Monthly (IFS) / Annual (WDI mirror) | USD | Near-universal — IFS covers ~194 countries/areas; independently, third-party aggregators (Trading Economics/CEIC) cite "IMF" as their source specifically for Vietnam's reserves figures, consistent with Vietnam being covered here even without its own national release | BPM6 | **Most likely candidate for a genuinely comparable series across all three** — but "near-universal coverage" is not the same as "confirmed observations for these three countries at the frequency/date range this project needs," which still requires an actual pull | Recommended candidate, not yet confirmed by inspection |

**6. Reserve definition choice: SUPERSEDED by Decision A/B below and the "CURRENT FINAL DECISION" section near the end of this file.** (Original text kept for history: "still not made, per instruction — this table is descriptive, not a decision. My read, for you to confirm or override: the IMF IFS/WDI 'Total Reserves' series is the strongest candidate for the comparison layer across all three countries... This is a recommendation, not a decision.")

---

## Final Reserve-Measure Comparison (superseding the recommendation above)

**Key finding before the table: WDI and IFS are not the same frequency, and not every "IMF reserves" product found on financial data platforms is the same underlying series.** Three distinct products surfaced this pass, and conflating them would be a real error:
- World Bank WDI's "Total reserves" mirror is explicitly **annual only** (DataBank metadata: "Annual 1960–2025"), regardless of methodology — this alone rules WDI out as the source for a 2018–2026 monthly analysis, confirming your instruction not to use it "merely because it's easier to download."
- IMF IFS's own "**Total Reserves excluding Gold**" line is confirmed **monthly** — verified directly (via FRED's re-dissemination, which cites "Source: International Monetary Fund / Release: International Financial Statistics / Frequency: Monthly") for the US, China, India, Indonesia, Turkey, South Korea, Iran, and the Euro Area. I did not find the exact ticker for Bangladesh, Pakistan, or Vietnam specifically — that's a real, stated gap, not an assumption either way.
- A third, different product exists and must **not** be confused with the above: FRED also hosts "Gross International Reserves Held by Central Bank for Pakistan" (PAKFAFARUSD), sourced from the IMF's **Middle East and Central Asia Regional Economic Outlook (REO)** — this is **annual**, and its own notes state "observations for the current and future years are projections." Treating this as observed data would silently inject IMF staff forecasts into what's supposed to be an empirical dataset. Rejected outright for this project.

| # | Item | Exact series/source | Frequency | Unit | Stock/end-period? | Gold included? | SDRs/IMF reserve position included? | Country coverage | Date coverage | Monthly obs. actually available? | Appropriate for EMP? |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | IMF IFS Total Reserves, incl. gold | IFS "Total Reserves" (WDI mirror: `FI.RES.TOTL.CD`) | WDI mirror: **annual only** confirmed; IFS-native frequency for this variant not separately confirmed | USD | Stock, end-period | Yes | Yes (non-gold components included, plus gold) | Near-universal | WDI: 1960–2025 | **No** (WDI annual) | Weaker — gold-price swings add noise unrelated to FX intervention |
| 2 | IMF IFS Total Reserves, excl. gold | IFS "Total Reserves excluding Gold" (FRED tickers e.g. `TRESEG[ISO2]M052N` USD / `M194N` SDR) | **Monthly — confirmed** for 8 comparable economies | USD mn or SDR mn (two unit variants exist) | Stock, end-period | No | Yes | Broad — not yet confirmed specifically for BGD/PAK/VNM tickers | Varies by country (e.g., Iran from 1983) | **Not yet confirmed for our 3 countries specifically** — real gap | **Best fit** — isolates reserve changes from gold valuation effects, which is what EMP wants |
| 3 | IMF IRFCL Official Reserve Assets | Section I, "Official reserve assets," IRFCL template | Monthly (SDDS-prescribed) for subscribers | USD (common currency) | Stock, end-period | Itemized separately (derivable either way) | Itemized separately | **SDDS subscribers only — BGD/PAK/VNM coverage still unconfirmed** (JS-rendered portal, not accessible to my tools) | From ~2000 for participants | Unknown for our 3 | Would be ideal (most granular) *if* coverage confirmed — coverage is the blocker |
| 4 | Bangladesh Bank reserves (gross/BPM6) | "Foreign Exchange Reserve (Monthly)" (gross); a separate BPM6-basis figure appears in BB/press releases, not confirmed as its own downloadable series | Monthly (gross, confirmed); BPM6 variant's own frequency unconfirmed | USD mn | Stock, end-period | Likely yes (gross); unclear for BPM6 variant | Unconfirmed | Bangladesh only | Long run, not yet pulled | Yes (gross) | Good for Bangladesh's own Gate 5 detail; not cross-country by itself |
| 5 | SBP reserves (SBP-held/Bank/Total) | "Gold and Foreign Exchange Reserves of Pakistan" | Weekly (live) / Monthly (EasyData) | USD mn | Stock, end-period | Yes, per series name | Unconfirmed | Pakistan only | Not yet pulled | Yes | Good for Pakistan's own detail; not cross-country by itself |
| 6 | Vietnam national reserve measure | **Not found** (see prior checks: NSO comparator table, no SBV-published series) | — | — | — | — | — | — | — | — | Not usable — no candidate exists to evaluate |

## Two Decisions

**Decision A — Cross-country descriptive comparison measure: (historical name "IMF IFS," current name IMF International Liquidity (IL)) "Reserves excluding gold."**
Chosen over the including-gold variant (removes gold-price valuation noise that has nothing to do with the countries' external positions), over IRFCL (coverage for our three countries was never confirmed — see D-000a, superseded), and over WDI (wrong frequency outright). This is a decision about *which series to target*, not a claim the data was in hand at the time: monthly observations for Bangladesh, Pakistan, and Vietnam were confirmed later via an actual downloaded file — **see "CURRENT FINAL DECISION" near the end of this file for the confirmed exact series codes.** Status at the time this was written: SOURCE IDENTIFIED (decided), not yet VERIFIED — **superseded; now VERIFIED for the 2018-M01–2026-M06 common sample.**

**Decision B — EMP reserve measure: also IMF International Liquidity (IL) "Reserves excluding gold" — same series, not a coincidence.**
I considered using each country's own national series instead (Bangladesh Bank / SBP) for the EMP calculation specifically, since national data is more operationally authentic and avoids any IMF re-dissemination lag. I'm not recommending that: using a different reserve basis for the EMP calculation than for the descriptive comparison tables would create exactly the kind of cross-file inconsistency ("why does Bangladesh's reserve level in Table 2 not match the number feeding the EMP chart in Figure 4") that an IMF reviewer would flag as sloppy, for a benefit (marginal timeliness) that doesn't matter much at monthly frequency. **Corrected justification (per instruction):** excluding gold does not "isolate market-pressure-driven reserve changes" — that overclaims. What it actually does is remove gold valuation/price effects, giving a cleaner reserve-asset measure for the EMP calculation. The excl.-gold series still contains reserve changes from multiple non-FX-intervention sources (SDR allocations, valuation of non-gold FX holdings, IMF reserve position changes, etc.) — it is cleaner, not clean. **This series is still not identical to Bangladesh Bank's BPM6 figure or any other national reserve figure — see the unreconciled validation discrepancies in the Final Decision section.**

**Status at the time this was written: PROVISIONAL — exact monthly observations pending inspection. Superseded — see "CURRENT FINAL DECISION" below.**

---

## Reserve Variable — Verification Attempt and Its Limits

**Terminology correction (important, found this pass):** "IMF IFS" is no longer fully accurate as a name. IMF's own data.imf.org documentation (COFER data page) states reserves data now sits in the **"International Liquidity" database (formerly International Financial Statistics)** — IFS as a single unified database has been retired and split into smaller thematic dataflows, confirmed independently via IMF-data R-package documentation ("The IMF has now retired IFS and split its contents across many smaller thematic data flows"). Going forward, this project should cite the source as **IMF International Liquidity database (successor to IFS)**, not "IMF IFS," for accuracy.

**Direct verification attempted, both blocked — stating this plainly rather than glossing over it:**
1. IMF's legacy REST API (`dataservices.imf.org/REST/SDMX_JSON.svc`) — fetch attempt returned **"ROBOTS_DISALLOWED": the site's robots.txt blocks automated access.** This is a real, demonstrated block, not an assumption.
2. IMF's current data.imf.org portal — as established in the reserves pass, the country/indicator selector is JavaScript-rendered and not readable by my tools.
**Conclusion: I cannot, with the tools available to me, directly query the IMF's own database and produce the observation-level detail requested (exact count, missing observations, first/last date, breaks).** This is a genuine capability limit, not a shortcut. Getting that detail requires either you querying data.imf.org's International Liquidity dataset directly (built for interactive human use), or a scripted pull from an environment not blocked by robots.txt — which runs into this project's own Python-deferral rule and would need your explicit call, not mine, to treat as an exception.

**What I could establish instead (circumstantial, not primary — labeled as such, not substituted for verification):**
- **Vietnam:** Trading Economics' monthly Vietnam "Foreign Exchange Reserves" series (1995–2025, monthly, USD million, e.g. $83,618.78mn Dec 2025) is tagged "source: IMF." Separately, Trading Economics' "International Reserves (excluding Gold)" page for Vietnam states explicitly: "data on international reserve assets refer to entries published in the world tables of the IMF's International Financial Statistics (IFS)." CEIC independently shows a Vietnam series "updated monthly, available from Jan 1995 to Jul 2025." Three independent redistributors pointing at IMF/IFS for monthly Vietnam data is meaningfully stronger evidence than one, but it is still secondary evidence, not an inspected primary file.
- **Bangladesh, national cross-check (instruction 5):** Bangladesh Bank's own recent press figures show its **gross** reserves and its **BPM6-basis** reserves as two regularly-reported numbers, not a one-off: e.g., Jan 2026 reporting shows gross $32.44bn vs. BPM6 $27.85bn same date; Feb 2026 reporting shows a further gross figure around $29–35bn range depending on source and method. This confirms the gross-vs-BPM6 gap is large (~$4–5bn), real, and current — reinforcing why the reserve-basis choice matters and can't be treated as a rounding issue.
- **Pakistan:** no new national cross-check performed this pass beyond what's already logged (SBP live split).

**Instruction 6 — the distinction, answered directly:**
> "Vietnam national monthly reserve series not located" — **supported**, per the SBV/NSO checks already logged.
> "Vietnam is not covered by IMF IFS [International Liquidity]" — **not supported; evidence points the other way.** Multiple independent secondary sources explicitly cite IMF/IMF IFS as their source for a monthly Vietnam reserves series going back to 1995. I have not personally inspected the IMF database to confirm this, but there is no basis to claim Vietnam is excluded from it.

**Instruction 9 — final statement on 2018–2026 sufficiency:** I **cannot yet confirm** sufficient coverage for all three countries, because I have not inspected the actual IMF dataset — only secondary evidence pointing toward likely monthly coverage for all three (strongest for Vietnam and the cross-country pattern generally, not yet specifically checked at the observation level for Bangladesh or Pakistan within International Liquidity specifically, since both have their own strong national series that made checking the IMF one less urgent so far). **The reserve variable stays PROVISIONAL, not VERIFIED, until this inspection actually happens** — which needs either your direct portal access or an agreed exception to the Python-deferral rule for a one-off data pull.

---

## Scoped Python Exception — IMF International Liquidity Extraction Attempt (Result: BLOCKED, not completed)

**Requested extraction:** Dataset International Liquidity (IL), indicator "Total Reserves minus Gold," series code `RAXG_USD`, USD millions, end-of-period reserve assets excluding gold, for Bangladesh/Pakistan/Vietnam, monthly, Jan 2018–latest.

**What actually happened:** the code-execution sandbox's network egress is restricted to a fixed allowlist (package registries — PyPI, npm, GitHub, etc. — and nothing else). A direct test confirmed this concretely rather than assuming it:
- `dataservices.imf.org` — DNS resolution failed outright (not even reachable).
- `data.imf.org`, `www.imf.org`, `sdmxcentral.imf.org` — all returned **HTTP 403**, with an explicit proxy header: `x-deny-reason: host_not_allowed`, body: *"Host not in allowlist: data.imf.org. Add this host to your network egress settings to allow access."*

**Conclusion: no data was retrieved. None of the following exist, because the extraction never ran:** no observations, no metadata file, no raw file in `/data/raw/imf_il_reserves/`. I am not fabricating placeholder values or a "plausible" coverage table — that would be inventing data, which is exactly what this project prohibits. This is a hard environment limitation, not a data-availability finding about Bangladesh, Pakistan, or Vietnam specifically.

**A. Exact series metadata:** requested, not obtained. What was requested is stated above (per your specification) — this is not IMF-confirmed metadata, just the request parameters.
**B. Coverage table:** cannot be produced — no observations returned.
**C. Raw-file location:** none created. `/data/raw/imf_il_reserves/` does not exist; I will not create an empty placeholder that could later be mistaken for "checked and empty."
**D. Validation comparison:** cannot be performed — nothing to compare against national/secondary sources yet.
**E. Unresolved discrepancy:** the extraction pipeline itself, not the data — the sandbox cannot reach any IMF domain (or, it turns out, any general external website — the allowlist is limited to software-package registries, so this isn't specific to the IMF).
**F. Yes/no conclusion on whether this series can serve as the project's common reserve measure: NOT YET DETERMINABLE — neither yes nor no.** The methodological case for it (from the earlier comparison table) is still the strongest of the candidates evaluated, but that is a design judgment, not a data-availability confirmation, and instruction 12 is explicit that VERIFIED requires the actual returned observations to support it.

**Status: remains PROVISIONAL — exact monthly observations pending inspection. Not VERIFIED, not REJECTED, not BLOCKED-as-in-abandoned — the data need is unchanged, only the retrieval method needs to change.**

**Realistic paths forward (for you to choose, not for me to pick):**
1. You retrieve the data.imf.org International Liquidity series for BGD/PAK/VNM (RAXG_USD, monthly, Jan 2018–latest) directly through the portal yourself and share the exported file — I can then read, validate, and log it without any further network access needed.
2. If this Claude environment has a network-egress setting you can edit (the proxy error message itself suggests this: "Add this host to your network egress settings to allow access"), enabling `data.imf.org` would let a future scoped script attempt this directly — I can't tell from here whether that setting is available to you in this product, so you'd need to check.

---

## CURRENT FINAL DECISION — Reserve Variable (supersedes all earlier reserve-sourcing entries above)

**This is the authoritative statement of the reserve variable's status. Earlier entries (D-000a, D-001, D-002, D-003, Decisions A/B, and the Batch-1/Batch-2 reserve discussion) are marked SUPERSEDED at their original locations and preserved for audit trail — they are not the current status.**

- **Dataset:** IMF International Liquidity (IL) — current name; "IMF IFS" is the historical name for this database, which has been retired and restructured (see Standing Project Rules at the top of this file).
- **Indicator:** Reserves excluding gold
- **Series:**
  - `BGD.RXF11_REVS.USD.M`
  - `PAK.RXF11_REVS.USD.M`
  - `VNM.RXF11_REVS.USD.M`
- **Common analytical sample: 2018-M01 through 2026-M06.**
- **July 2026 treatment:** Bangladesh and Pakistan both have a 2026-M07 observation and it is retained in the raw data for country-specific use, but it is **excluded from any three-country common-month analysis**, because Vietnam has no 2026-M07 observation in the current IMF International Liquidity Latest vintage.
- **No claim of identity with national figures:** the IMF IL series is **not** identical to Bangladesh Bank's BPM6 reserve figure, or to any other national reserve figure, and this project does not claim otherwise. Two validation discrepancies remain open and unreconciled (not silently smoothed over):
  - **Bangladesh, Jan 2026:** IMF IL = $26,241.80mn vs. Bangladesh Bank's own same-date figures (gross $32.44bn / BPM6-basis $27.85bn) — closest to BPM6, not identical.
  - **Vietnam, Dec 2025:** IMF IL = $85,580.37mn vs. Trading Economics' reported $83,618.78mn (~2.3% difference).
  - Neither will be reconciled unless primary-source documentation explaining the difference is obtained.
- **Raw file:** `/data/raw/imf_il_reserves/dataset_2026-09-12T19_47_51_749761953Z_DEFAULT_INTEGRATION_IMF_STA_IL_13_0_1.csv`, preserved unmodified (SHA-256 in `PROVENANCE.md`), downloaded directly by Ziba from the IMF portal per the Standing Project Rule above.
- **Status: VERIFIED for the 2018-M01–2026-M06 common sample.** Not verified/claimed beyond that window for the three-country comparison.

---

## Reserve Variable — Full Working History (detail behind the decision above)

**Raw file received and independently re-verified (not just taken on your summary):** I parsed the uploaded CSV directly and recomputed coverage myself rather than trusting the stated numbers at face value — they match exactly.

**Correction to earlier documentation (per instruction 6):** the actual downloadable series codes are **not** `RAXG_USD` as I had been documenting — they are `BGD.RXF11_REVS.USD.M`, `PAK.RXF11_REVS.USD.M`, `VNM.RXF11_REVS.USD.M` under dataset `IMF.STA:IL(13.0.1)`. All prior mentions of `RAXG_USD` in this project's documentation should be read as superseded by this entry; no IMF metadata I've seen establishes a mapping between that code and these actual series, so I'm not asserting one.

**Final verification table:**

| Country | Exact series code | First observation | Last available observation | # observations | Missing | Common-sample status |
|---|---|---|---|---|---|---|
| Bangladesh | `BGD.RXF11_REVS.USD.M` | 2018-M01 ($32,287.88mn) | 2026-M07 ($29,747.94mn) | 103/103 | 0 | Full range available; **truncated to 2026-M06 in the harmonized 3-country sample only** — July retained in country-specific raw data |
| Pakistan | `PAK.RXF11_REVS.USD.M` | 2018-M01 ($14,908.81mn) | 2026-M07 ($18,339.59mn) | 103/103 | 0 | Full range available; **truncated to 2026-M06 in the harmonized 3-country sample only** — July retained in country-specific raw data |
| Vietnam | `VNM.RXF11_REVS.USD.M` | 2018-M01 ($53,101.23mn) | 2026-M06 ($88,260.96mn) | 102/103 | 1 (`2026-M07`) | Defines the common-sample end point |

**A. Series metadata (confirmed from file):** Dataset `IMF.STA:IL(13.0.1)`; Indicator "Reserves excluding gold"; Unit "US dollar"; Scale "Millions"; Frequency "Monthly." Full detail, including what's independently re-derived vs. what rests on your portal-session account, is in `/data/raw/imf_il_reserves/PROVENANCE.md`.
**B. Coverage table:** above.
**C. Raw-file location:** `/data/raw/imf_il_reserves/dataset_2026-09-12T19_47_51_749761953Z_DEFAULT_INTEGRATION_IMF_STA_IL_13_0_1.csv`, preserved byte-for-byte (SHA-256 `d0e38...ffbd29f`, full hash in PROVENANCE.md), not modified.
**D. Validation comparison:**
  - Bangladesh 2026-M01: file = $26,241.80mn vs. previously-logged BB same-date figures (gross $32.44bn / BPM6 $27.85bn) — IL figure sits below both, closest to BPM6, gap not fully reconciled.
  - Vietnam 2025-M12: file = $85,580.37mn vs. previously-logged Trading Economics figure $83,618.78mn (~2.3% difference) — not reconciled.
  - Pakistan: no dated prior figure available to cross-check this pass.
**E. Unresolved discrepancies:** the two gaps above (Bangladesh vs. BB's own BPM6 figure; Vietnam vs. TE) are recorded, not silently smoothed over. Neither is large enough to doubt the file's validity, but neither is explained yet either.
**F. Conclusion: YES** — this series can serve as the project's common reserve measure, for the harmonized 2018-M01–2026-M06 window specifically.

**Decisions locked in, per your instructions:**
- Common three-country analytical sample: **2018-M01 through 2026-M06**.
- Bangladesh and Pakistan's July 2026 observations are preserved in the raw data and may appear in country-specific descriptive material, but do not enter any three-country comparison requiring a common month.
- Vietnam 2026-M07 recorded as **UNAVAILABLE in the current IMF Latest vintage** — not an error, not imputed, not interpolated.
- If a future IMF vintage adds Vietnam's July 2026 observation, that is a vintage update to be recorded going forward, not a retroactive edit of this raw-data record.

**Status: reserve variable is VERIFIED for the common analytical sample 2018-M01–2026-M06.** (2026-M07 remains available only for Bangladesh/Pakistan country-specific use, not as part of the verified common sample.)

**Still not started:** EMP construction, cleaning, or any other substantive analysis — this remains a source-verification step only, as instructed.

**Decision ID: D-007 — SUPERSEDED, see D-015 below**
**Variable:** Exports, imports (goods) — all three countries
**Bangladesh:** Bangladesh Bank Economic Data → "BOP, Export & Import"
**Pakistan:** **two competing official series exist** — (a) SBP's own "Exports/Imports as per BOP" (payments-record basis, direct PDF: https://www.sbp.org.pk/ecodata/exp_import_BOP.pdf) and (b) Pakistan Bureau of Statistics' customs-record trade statistics (https://www.pbs.gov.pk/external-trade-statistics/). SBP's own Monthly Statistical Bulletin explicitly cross-tabulates both bases against each other, confirming they are not identical.
**Vietnam:** NSO Vietnam, "Import export" section, monthly exports/imports value tables — https://www.nso.gov.vn/en/import-export/
**Status: SUPERSEDED.** See D-015 for the current, focused research under the one-variable-at-a-time workflow — the BOP-vs-customs question turns out to be an IMF-dataset-level distinction, not just a Pakistan-specific one.
**Kept for history:** SBP's own Monthly Statistical Bulletin cross-tabulates both trade bases against each other, confirming they are not identical for Pakistan specifically.

---

## Exports/Imports of Goods — One-Variable-at-a-Time Pass (Current)

**Decision ID: D-015 — Exports/imports of goods, source identification (Step 1)**

**The Pakistan SBP-vs-PBS distinction generalizes to an IMF-dataset-level choice, not just a Pakistan quirk.** Two separate IMF datasets exist, on two genuinely different conceptual bases:

1. **`IMF.STA:BOP`** — the same dataset already used and VERIFIED for current account. BOP's goods sub-account is compiled on a **change-of-ownership (BOP/payments) basis** — same conceptual family as SBP's "Exports/Imports as per BOP."
2. **`IMF.STA:ITG`** ("International Trade in Goods") — a **separate dataset**, compiled on a **customs/physical-border-crossing basis** (the IMTS framework) — same conceptual family as Pakistan Bureau of Statistics' customs data. IMF's own documentation states plainly: *"BOP-based statistics of trade in goods... are usually not comparable to IMTS-based merchandise trade data... due to differences in the concepts and definitions."* ITG provides FOB exports (`XG_FOB_USD`), and imports in both FOB (`MG_FOB_USD`) and CIF (`MG_CIF_USD`) variants — a further basis choice within ITG itself (FOB vs. CIF imports are not the same number either).

**This is not resolved silently.** Two real candidates, genuinely different:

| | IMF BOP (goods sub-account) | IMF ITG |
|---|---|---|
| Basis | Change-of-ownership (BOP/payments) | Customs/physical border-crossing (IMTS) |
| Frequency | Quarterly (matches our already-verified current account) | Reported as supporting monthly frequency generally (not yet confirmed specifically for BGD/PAK/VNM) |
| Consistency with current account | **Fully internally consistent** — same dataset, same BPM6 framework already verified | Not consistent with the BOP current-account figure already verified — a reviewer could reasonably ask why goods exports/imports don't reconcile to the current-account goods line |
| Matches which Pakistan national source | SBP's BOP-basis trade data | Pakistan Bureau of Statistics' customs data |

**Recommendation: use IMF BOP's goods sub-account as the harmonized three-country analytical layer**, prioritizing internal consistency with the already-verified current-account series over the frequency gain from ITG. This mirrors the project's established pattern (harmonized quarterly/monthly IMF common layer + national sources kept separate for country-specific higher-frequency detail) rather than introducing a second, differently-based IMF product into the core comparison. **This is a recommendation, not a unilateral decision — flagging it clearly since you asked not to resolve this silently.** If you'd rather prioritize monthly frequency over BOP-consistency, ITG is the alternative, with the explicit tradeoff that it won't reconcile against the current-account figure already locked in.

**Bangladesh:** Bangladesh Bank's "BOP, Export & Import" section (national candidate, not yet opened) — presumably BOP-basis given the section name, not yet confirmed monthly or quarterly.
**Vietnam:** NSO Vietnam's "Import export" monthly tables (national candidate) — basis not yet confirmed as BOP or customs.
**Pakistan:** unchanged from before — SBP (BOP-basis) vs. PBS (customs-basis) — now understood as mirroring the exact IMF BOP-vs-ITG distinction above, not a Pakistan-specific oddity.

**Status: SOURCE IDENTIFIED (IMF layer only, recommendation pending your confirmation).** National Bangladesh/Pakistan files **not requested yet**, per instruction, pending confirmation the harmonized-source investigation actually needs them.

---

## IMF BOP Goods Exports/Imports File — Independently Inspected

**Confirmed from the file itself (not assumed):**
- Dataset `IMF.STA:BOP(21.0.0)` — **same dataset as the already-verified current-account series**, confirming the recommendation to use the BOP layer for internal consistency was actually followed correctly in the download.
- Indicator: "Goods" — confirms **goods only**, not goods-and-services, and confirms this is the **BOP/change-of-ownership concept**, not IMF ITG/customs data (ITG was never queried for this file — only `IMF.STA:BOP` appears).
- Six series: Credit/Revenue (exports) and Debit/Expenditure (imports) for each of the three countries.

**Series codes, coverage, and missingness (independently recomputed):**

| Country | Series | Entry | Coverage | Obs. | Missing |
|---|---|---|---|---|---|
| Pakistan | `PAK.CD_T.G.USD.Q` | Exports (Credit) | 2018-Q1–2026-Q2 | 34/34 | None |
| Pakistan | `PAK.DB_T.G.USD.Q` | Imports (Debit) | 2018-Q1–2026-Q2 | 34/34 | None |
| Vietnam | `VNM.CD_T.G.USD.Q` | Exports (Credit) | 2018-Q1–2026-Q1 | 33/34 | `2026-Q2` |
| Vietnam | `VNM.DB_T.G.USD.Q` | Imports (Debit) | 2018-Q1–2026-Q1 | 33/34 | `2026-Q2` |
| Bangladesh | `BGD.CD_T.G.USD.Q` | Exports (Credit) | 2018-Q1–2026-Q1 | 33/34 | `2026-Q2` |
| Bangladesh | `BGD.DB_T.G.USD.Q` | Imports (Debit) | 2018-Q1–2026-Q1 | 33/34 | `2026-Q2` |

No duplicate series codes. No structural anomalies found in the common window.

**Sign convention — inspected, not assumed:** all 198 non-missing observations across all six series are **positive**. Exports and imports are both reported as positive magnitudes (their respective Credit/Debit flow sizes), not as a signed net balance. This was checked directly, not inferred from BOP conventions in general.

**Common three-country window: 2018-Q1–2026-Q1** — identical to the current-account window already verified. Pakistan's 2026-Q2 retained for country-specific use only, not part of the common panel.

**Consistency check against current account (plausibility, not formal reconciliation):** computed 2018-Q1 goods trade balance for each country and compared the gap against the already-verified current-account figure for the same quarter. All three gaps are directionally sensible given each country's known economic structure (Pakistan and Bangladesh: remittances partly offsetting a larger goods deficit; Vietnam: income-account outflows partly offsetting a larger goods surplus). Full figures in `PROVENANCE.md`. This confirms the two IMF BOP-sourced series are usable together consistently, as required.

**Metadata caveats, documented not blocking (same standard as current account):**
1. No explicit BPM6 tag in the file — inferred from IMF's general post-2012 harmonization practice, not confirmed field-by-field.
2. No explicit seasonally-adjusted/non-seasonally-adjusted field — IMF BOP is conventionally NSA at the international level; general practice, not a file-level confirmation.

**Nothing marked UNRESOLVED this pass** — no genuine ambiguity was found once the file was actually inspected (unlike, e.g., the Vietnam reserves search or the Pakistan remittances SA question). If this changes on closer inspection later, it will be logged, not smoothed over.

**Gate 1 status, per series:**
- Pakistan exports: **VERIFIED**, 2018-Q1–2026-Q2 (2026-Q2 outside common sample)
- Pakistan imports: **VERIFIED**, 2018-Q1–2026-Q2 (2026-Q2 outside common sample)
- Vietnam exports: **VERIFIED**, 2018-Q1–2026-Q1
- Vietnam imports: **VERIFIED**, 2018-Q1–2026-Q1
- Bangladesh exports: **VERIFIED**, 2018-Q1–2026-Q1
- Bangladesh imports: **VERIFIED**, 2018-Q1–2026-Q1
- **Overall: Exports/Imports of Goods — VERIFIED for the common three-country quarterly window 2018-Q1–2026-Q1**, on the IMF BOP goods sub-account (change-of-ownership basis), consistent with the current-account series.

No trade balances, growth rates, ratios, regressions, or stress-test calculations performed — Gate 1 only, as instructed. Raw file preserved unmodified at `/data/raw/imf_bop_goods_trade/` (SHA-256 in `PROVENANCE.md`).

**Not proceeding to GDP or CPI.**

**Decision ID: D-008 — OMITTED BY DESIGN (permanent scope change)**
**Variable:** External debt
**Status: OMITTED BY DESIGN.** Removed from the project's variable scope by explicit instruction — not necessary for the core research question, and removing it keeps the project focused and avoids unnecessary comparability problems. **Not to be reintroduced without explicit instruction.** (Historical note, kept for the record: prior status was UNRESOLVED / NOT YET ATTEMPTED, with World Bank IDS and IMF external debt statistics identified as candidate sources — this research was never completed and is now moot.)

---

## Data-Sourcing Decisions (Gate 1 — Batch 3, partial: REER, Policy Rate; GDP/Inflation deferred)

**Decision ID: D-009 — OMITTED BY DESIGN (permanent scope change)**
**Variable:** REER
**Status: OMITTED BY DESIGN.** Removed from the project's variable scope by explicit instruction. **Not to be reintroduced without explicit instruction.** (Historical note, kept for the record: prior status was REJECTED as originally specified — at least three non-comparable REER series were found for Bangladesh alone, different base years/baskets, a genuine comparability failure consistent with the research design's own drop-if-incomparable rule. The scope removal supersedes even the "pending a re-scoped version" possibility that was left open before.)

**Decision ID: D-010 — OMITTED BY DESIGN (permanent scope change)**
**Variable:** Policy rate
**Status: OMITTED BY DESIGN.** Removed from the project's variable scope by explicit instruction. **Not to be reintroduced without explicit instruction.** (Historical note, kept for the record: Bangladesh and Pakistan candidates were identified — BB repo rate, SBP Policy Rate — Vietnam's equivalent was never confirmed. This research was never completed and is now moot.)

**GDP growth, inflation (CPI):** still in scope (retained per this turn's variable list) — deferred, not yet sourced. Next up after current account/BOP and exports/imports, per the standing order.

**Decision ID: D-011 — Vietnam exchange rate (following up the earlier "not yet located" gap) — folded into D-013**
**Finding:** SBV sets and announces a daily "central rate" (formerly "reference exchange rate") for VND/USD under a standing decision framework (historically Decision 2730/QD-NHNN; trading band has changed over time, from ±3% historically to ±5% currently per recent reporting), confirmed consistently across many independent news reports (Vietnam News Agency/Vietnam+, SGGP) spanning 2016–2026. This is a real, standing daily SBV publication, not a one-off — much stronger footing than the reserves search.
**Status: kept as a national/descriptive-layer candidate.** The harmonized cross-country layer now goes through IMF ER (D-013) instead; this SBV finding remains useful for Bangladesh-style national cross-checks and the Bangladesh/Vietnam reform-period narrative, not superseded so much as reassigned to a supporting role.

**Decision ID: D-013 — Official nominal exchange rate, one-variable-at-a-time pass (current)**
**Primary source selected:** IMF **Exchange Rates (ER)** dataset — `IMF.STA:ER`, https://data.imf.org/en/datasets/IMF.STA:ER. Per IMF's own dataset description: "historical exchange rate data between the US Dollar, Special Drawing Rights (SDR), Euro, and various national currencies. It includes both period average and end-of-period exchange rates." This is the current-portal home for what used to be an IFS exchange-rate indicator (IFS is retired, per the Standing Project Rules terminology note).
**National-source alternatives (descriptive/cross-check role only, same pattern as reserves):** Bangladesh Bank Economic Data → Exchange Rate; SBP EasyData; SBV's daily central-rate publication (D-011).
**Status: SOURCE IDENTIFIED.** Not VERIFIED — no file has been uploaded or inspected yet. Full request specification and download instructions given to Ziba this turn (see chat); awaiting the uploaded CSV before proceeding to Step 3/4/5 of the one-variable-at-a-time workflow.

**File uploaded and independently inspected (Step 3/4/5 complete):**

| Country | Series code | Variant | First obs. | Last available | # obs. | Missing | Note |
|---|---|---|---|---|---|---|---|
| Bangladesh | `BGD.XDC_USD.EOP_RT.M` | End-of-period | 2018-M01 (82.9) | 2026-M08 (123.0) | 104/104 | 0 | Full coverage, ahead of the other two |
| Bangladesh | `BGD.XDC_USD.PA_RT.M` | Period average | 2018-M01 (82.82) | 2026-M08 (123.10) | 104/104 | 0 | Full coverage |
| Pakistan | `PAK.XDC_USD.EOP_RT.M` | End-of-period | 2018-M01 (110.56) | 2026-M07 (277.74) | 103/104 | `2026-M08` | Expected trailing lag only |
| Pakistan | `PAK.XDC_USD.PA_RT.M` | Period average | 2018-M01 (110.55) | 2026-M07 (277.90) | 103/104 | `2026-M08` | Expected trailing lag only |
| Vietnam | `VNM.XDC_USD.EOP_RT.M` | End-of-period | 2018-M01 (22,441) | 2026-M06 (25,206) | 102/104 | `2026-M07`, `2026-M08` | Trailing lag, consistent with the reserves finding |
| Vietnam | `VNM.XDC_USD.PA_RT.M` | Period average | 2018-M01 (22,410.65) | 2026-M06 (25,168.38) | 101/104 | **`2025-M08` (internal), `2026-M07`, `2026-M08`** | **Genuine internal gap, not just a trailing lag — flagged, not reconciled** |

**Comparability check (Step 4):** identical definition ("Domestic currency per US Dollar") and unscaled "Units" across all three countries, under one dataset/methodology (`IMF.STA:ER(4.0.1)`) — a cleaner comparability picture than reserves had (no gross-vs-BPM6-style multiple bases here, since IMF publishes one FX-rate concept per variant). Values are economically plausible on their face (Pakistan's PKR depreciation from ~110 to ~278/USD, Bangladesh's BDT from ~83 to ~123/USD, Vietnam's VND from ~22,400 to ~25,200/USD all match well-known depreciation patterns over this period) — not independently verified against a national source this pass, but nothing looks anomalous.

**Common three-country sample:** confirms the same end-date convention already set for reserves — **2018-M01 through 2026-M06** — since that's Vietnam's last available month for both variants. Bangladesh's and Pakistan's more recent months are retained for country-specific use, not used in three-country comparisons, matching the reserves precedent exactly.

**Flagged, not resolved:** Vietnam's period-average series has an unexplained gap at 2025-M08 specifically, inside the common sample window, that its own end-of-period series does not have. No interpolation performed. If period-average is the variant Gate 3 ends up needing for EMP, this gap will need an explicit, documented decision at that point (drop the month for all three countries, use end-of-period instead, or something else) — not resolved now, not imputed.

**Status — recorded separately per variant, not blended:**
- **End-of-period: VERIFIED for the common three-country sample 2018-M01–2026-M06.** No missing observations within that window for any of the three countries.
- **Period-average: VERIFIED for the common three-country sample 2018-M01–2026-M06 WITH ONE INTERNAL MISSING OBSERVATION: Vietnam, 2025-M08.** This is genuinely missing — not interpolated, backfilled, estimated, or silently dropped. Any later use of period-average rates must flag this explicitly and must not let software default it to zero or carry-forward the prior month. The eventual EMP methodology (Gate 3, not decided here) will determine whether that means using end-of-period instead, excluding 2025-M08 consistently across all three countries, or another explicit handling — no decision made yet.
- **Default for descriptive exchange-rate charts: end-of-period**, unless the research design later establishes a specific reason to use period-average.

Raw file preserved at `/data/raw/imf_er_exchange_rate/` (SHA-256 in `PROVENANCE.md`), not modified.

**Not started:** EMP construction, cleaning, or any substantive analysis.

**Decision ID: D-012 — GDP growth and inflation (CPI), all three countries — deferred item, addressed at low confidence-effort per standing prioritization**
**Bangladesh:** Bangladesh Bureau of Statistics (BBS) — national CPI/GDP; cross-check via IMF WEO
**Pakistan:** Pakistan Bureau of Statistics (PBS) — national CPI/GDP; cross-check via IMF WEO
**Vietnam:** NSO Vietnam (already found generally — nso.gov.vn) — national CPI/GDP; cross-check via IMF WEO
**Status: PARTIALLY SUPERSEDED — GDP growth portion now closed, see D-016.** CPI portion remains SOURCE IDENTIFIED at the institution level only, not yet pursued under the one-variable-at-a-time workflow.

---

## GDP Growth — Verified and Closed

**Decision ID: D-016 — GDP growth, IMF WEO verification**
- **Dataset:** `IMF.RES:WEO(9.0.0)`, **April 2026 vintage**
- **Series:** `BGD.NGDP_RPCH.A`, `PAK.NGDP_RPCH.A`, `VNM.NGDP_RPCH.A`
- **Definition:** Annual real GDP growth, percent change
- **Coverage:** 2018–2026 present, no missing observations (9/9 for each country)
- **Fiscal-year convention:** Bangladesh and Pakistan's national accounts use a **July–June fiscal year**; Vietnam follows the **calendar-year** convention — affects how the "2025"/"2026" column labels should be read for Bangladesh and Pakistan specifically.
- **Actual vs. projection:** WEO documentation states **2026–27 figures are projections**. Per-country "last data update" notes exist in the online WEO database but were not independently retrieved for these three countries specifically.
- **No observations overwritten or altered.** Raw file preserved exactly as downloaded at `/data/raw/imf_weo_gdp_growth/` (SHA-256 in `PROVENANCE.md`).
- **For substantive historical analysis: 2025–2026 are flagged as non-historical/latest-vintage observations, pending more precise country-level classification, and must not be treated as realized outcomes** until that classification is resolved.

**Status: VERIFIED for data coverage and definition, with an explicit ACTUAL-VS-PROJECTION METADATA CAVEAT** (covering 2025–2026, and the Bangladesh/Pakistan fiscal-year labeling question). Not fully resolved history — the caveat travels with the series wherever it's used.

**GDP Gate 1 closed.** Not proceeding to CPI.

---

## CPI Inflation — Verified and Closed

**Decision ID: D-017 — CPI inflation, IMF WEO verification**
- **Dataset:** `IMF.RES:WEO(9.0.0)`, **April 2026 vintage** (same vintage as GDP growth)
- **Series:** `BGD.PCPIPCH.A`, `PAK.PCPIPCH.A`, `VNM.PCPIPCH.A`
- **Indicator (exact label):** "All Items, Consumer price index (CPI), Period average, percent change"
- **Definition:** Annual period-average CPI inflation, percent change
- **Coverage:** 2018–2026, 9/9 observations for each country, no missing observations, no duplicate series
- **Raw file preserved unchanged and checksummed** at `/data/raw/imf_weo_cpi_inflation/` (SHA-256 in `PROVENANCE.md`)

**Actual-vs-projection caveat: deliberately NOT copied over from GDP.** GDP growth (same WEO vintage) carries an explicit caveat for 2025–2026; this series does not inherit it. No direct evidence — a field in this file, or CPI-specific WEO documentation — was found supporting that caveat for CPI. If evidence for it surfaces later, it gets added explicitly at that point, not assumed by analogy to GDP.

**Status: VERIFIED for data definition and coverage.**

**CPI Gate 1 closed.** Not proceeding to any other variable.

---

## Master Analytical Dataset — Constructed (Decision ID: D-018)

Built from already-verified raw/derived files only, no new sourcing. Long/tidy format (`data/derived/master_analytical_dataset.csv`), one row per country×variable×period, native frequency preserved (monthly/quarterly/annual coexist without forced alignment). Companion files: `DATA_DICTIONARY.md`, `data/derived/master_qa_summary.csv`.

- **Monthly:** reserves excl. gold, EOP exchange rate, remittances (BGD/PAK only — Vietnam has zero rows, UNRESOLVED, not fabricated), EMP (CALCULATED, copied unmodified from the already-accepted `emp_klr_two_component.csv` — alpha NOT recomputed here)
- **Quarterly:** current account balance, goods exports, goods imports
- **Annual:** GDP growth, CPI inflation
- **Excluded by design:** external debt, REER, policy rate

**QA: zero duplicate (country, variable, period) rows; zero missing values (rows only exist where a real observation does).** Every row tagged `SOURCE` or `CALCULATED`, and `in_common_window` flags whether it falls inside that variable's already-established three-country common window.

**Stata status recorded per instruction:** `03_EMP.do` was prepared and syntax-corrected but **not independently executed** — the Python calculation remains the accepted EMP implementation; the do-file is a reproducibility artifact only, not validated code.

**Remaining gaps that block later analysis:** Vietnam monthly remittances (UNRESOLVED); GDP growth 2025–2026 actual-vs-projection status (unresolved at country level); Bangladesh/Pakistan fiscal-year vs. Vietnam calendar-year GDP labeling (unreconciled); Pakistan remittances raw/SA classification ("very likely," unconfirmed); KLR reserve-concept alignment (strong evidence, not ironclad). Full detail in `DATA_QA.md`.

No regressions, causal inference, stress testing, or substantive interpretation performed.

---

## Import-Price / External-Shock Proxy — Verified (Decision ID: D-019)

**Source:** IMF Primary Commodity Price System (PCPS), `IMF.RES:PCPS(9.0.0)`, series `G001.PNRG.INDEX.M` — "Energy index, Commodity price index, Index, 2016=100." Country field "World" — a single global series, deliberately not country-specific, per the recommendation that a common international benchmark is more defensible than three separately-constructed national import-price indices.

**Independently confirmed from the file (not assumed):**
- Frequency: Monthly. Unit: Index, 2016=100. Data transformation: Index (not pre-transformed into percent change).
- Coverage: 2018-M01–2026-M08, **104/104 observations, zero missing.**
- Plausibility: minimum (55.89) falls exactly at 2020-M04, matching the well-documented COVID-19 oil-price collapse; maximum (376.41) falls at 2022-M08, matching the well-documented post-Russia-Ukraine-invasion energy-price spike. Not formal validation, but a meaningful internal-consistency signal.

**Status: VERIFIED for data definition and coverage.** Raw file preserved unmodified at `/data/raw/imf_pcps_energy_price/` (SHA-256 in `PROVENANCE.md`).

**Not yet added to the master analytical dataset, and not used in any stress test, regression, or interpretation** — this closes the source-verification step only, per standing instruction. External debt, REER, policy rate, Vietnam remittances, Pakistan's remittance raw-vs-SA classification, Stata reproducibility, and the locked EMP methodology were not reopened or reworked.

---

## Master Analytical Dataset — Energy Price Index Added (Decision ID: D-020)

Added the already-verified IMF PCPS Energy Index (D-019) to `data/derived/master_analytical_dataset.csv` as `energy_price_index`, with `country_iso3 = "WLD"` — a single global series, not replicated or assigned per-country, and not merged into any quarterly/annual variable. Monthly frequency preserved exactly as in the raw file.

**Before/after row count:** 1,481 → 1,585 (+104, matching the energy series' full 2018-M01–2026-M08 coverage exactly).

**QA performed:**
- Zero duplicate (country, variable, period) keys after the addition.
- Zero missing observations within the energy series (104/104).
- All nine previously-verified variables' (country, variable) observation counts confirmed **unchanged** by direct comparison against the pre-update dataset.
- Confirmed no excluded variable (external debt, REER, policy rate) is present in the updated dataset.

`DATA_DICTIONARY.md` updated with the new variable's row, explicitly described as a global shock proxy rather than a country-specific import-price index. `data/derived/master_qa_summary.csv` regenerated to include it.

No stress testing, regressions, event studies, interpretation, or paper drafting performed.

---

## Gate 2 — Descriptive Assessment of Bangladesh's May 2025 Reform (Decision ID: D-021)

**Scope: descriptive only.** No causal inference, regression, forecasting, or stress testing performed. All figures trace directly to `data/derived/emp_klr_two_component.csv` (locked EMP calculation, not recomputed, alpha not touched) and `data/derived/master_analytical_dataset.csv` (verified master dataset). No new data sourced, no raw files modified, no new variables added.

**Windows used (fixed, not adjusted for results):** Pre-reform = 2024-M05–2025-M04 (12 months); Reform month = 2025-M05; Post-reform = 2025-M06–2026-M05 (12 months); Full historical benchmark = 2018-M02–2026-M06 (101 months).

**Institutional wording maintained:** "more flexible exchange-rate arrangement" / "crawling peg with band" throughout — never "free float" or "fully flexible." Reform date treated as mid-May 2025.

**Key descriptive findings (non-causal language used throughout the full report):**
- Bangladesh's post-reform EMP mean (-0.0060) is below its pre-reform mean (0.0072) and the full-historical mean (0.0037); SD is comparable to the full-historical SD.
- May 2025 itself is not an outlier relative to the pre-reform distribution (z = 0.41).
- Bangladesh's largest-ever EMP value (2024-M05, pre-reform) and smallest-ever value (2025-M06, immediately post-reform) both fall inside this event window — flagged as a timing coincidence, not causal evidence.
- **Pakistan and Vietnam show the same pre-to-post directional decline in mean EMP over the identical calendar window** — logged explicitly as a reason for caution against attributing Bangladesh's pattern to its reform specifically.
- Post-reform EMP movement is descriptively driven more by the reserve-change component than the exchange-rate component.
- A global energy-price spike (2026-M03 onward) falls inside the post-reform window — logged as a potential confounding external condition, not incorporated into the EMP calculation itself.

**Deliverables produced:**
- `data/derived/gate2_event_window_summary.csv` (Table A/B source — EMP, %Δe, %Δr, %Δremittances across all windows, all three countries)
- `data/derived/gate2_bangladesh_monthly.csv` (Table C — Bangladesh monthly detail, 2024-M05–2026-M05)
- `data/derived/gate2_comparative_emp.csv` (Table B)
- `GATE2_ANALYSIS.md` (full write-up, limitations section included)
- Four inline visualizations (Bangladesh EMP full history with reform marked; Bangladesh exchange-rate and reserves as separate panels, not dual-axis; comparative 3-country EMP; global energy-price index)

**Verification performed before finalizing:** spot-checked multiple output values directly against the source files (BGD 2025-M05 EMP, BGD 2025-M05 remittances, energy index 2026-M03) — all matched exactly. No raw files modified. Locked EMP values and alpha not recomputed. No new variables added to the master dataset.

**Limitations logged in full in `GATE2_ANALYSIS.md`** — most importantly: no statistical test of the pre/post difference, Pakistan/Vietnam showing the same directional shift, the 2026-M03 energy-price spike as a potential confound, GDP/CPI deliberately excluded from this window's evidence, Vietnam remittances still unresolved.

**Not proceeding to stress testing or paper drafting.**

---

## Gate 3 — Stylized Four-Quarter External-Shock Stress Test (Decision ID: D-022)

**Scope: mechanical scenario exercise only.** No regression, causal inference, forecasting, or machine learning. No new data sourced — every input traces to `data/derived/master_analytical_dataset.csv`. No raw file modified. No excluded variable (external debt, REER, policy rate) introduced.

**Baseline:** 2025-Q2 through 2026-Q1 (4 quarters, the latest common observed quarterly window), applied identically to all three countries. Exports/imports/current-account baselines are the sum of the four quarterly observations; Bangladesh/Pakistan remittance baselines are the sum of the twelve corresponding monthly observations (a Gate-3-specific aggregation, not written back into the master dataset).

**Locked shocks:** remittances −10% (BGD/PAK only), goods exports −5% (all three), import-price +10% global energy shock (all three), combined = sum of applicable shocks.

**Import-price transmission assumption, stated explicitly before calculation:** real import quantities held constant; a +10% global energy-price shock is applied as a stylized +10% increase in the value of goods imports, entering the external balance as a −10% × baseline-imports impact. Documented as an imposed simplifying assumption, not an estimated pass-through coefficient — the PCPS series remains a global, non-country-specific shock proxy.

**Results (total 4-quarter external-account deterioration, combined scenario):** Bangladesh −$12,258.14mn (shocked CA −$12,097.13mn); Pakistan −$11,850.34mn (shocked CA −$11,400.35mn); Vietnam −$70,616.15mn on a **narrower two-shock combined** (export + import-price only — no remittance shock; shocked CA −$39,593.15mn). Vietnam's remittance shock is marked N/A, not fabricated or substituted from HCMC/annual data, per instruction.

**Reserve interpretation deliberately not modeled:** results are reported only as cumulative external-account deterioration ("external financing pressure implied"), explicitly not translated into a reserve-loss figure — financing, exchange-rate adjustment, capital flows, valuation effects, and policy response are all unmodeled and stated as such.

**QA performed:** all baseline figures traced directly to the master dataset; all four scenario calculations independently re-verified at full floating-point precision (combined = exact sum of individual shocks, zero discrepancy, for all three countries); confirmed no raw file modified; confirmed no excluded variable present; confirmed the 4-quarter horizon applied identically across countries and variables.

**Deliverables:** `data/derived/gate3_stress_test.csv`, `STRESS_TEST.md` (full assumptions list and two presentation tables — Bangladesh; Pakistan/Vietnam with only data-supported shocks).

**Language used throughout:** "mechanically implies," "under the stated assumptions," "stylized scenario," "external financing pressure." Never "forecast," "predicted," "expected reserve loss," or claims about what the economy "will" do.

**Not proceeding to paper or policy note drafting.**

---

## Final Research Synthesis — Paper, Policy Note, and Locked Results (Decision ID: D-023)

Gates 1–3 closed. No new data sourced, no regressions/causal identification added, EMP methodology and stress-test assumptions unaltered, Stata not revisited, no excluded variable (external debt/REER/policy rate) reintroduced. All content drawn only from `master_analytical_dataset.csv`, `GATE2_ANALYSIS.md`, `STRESS_TEST.md`, and this ledger.

**Deliverables produced:**
- `paper/final_paper.md` — 11-section research paper (title, abstract, introduction, institutional context, data/methodology, descriptive evidence, cross-country comparison, stress test, limitations, conclusion, references), with 5 figures in `paper/figures/` (Bangladesh EMP full history with reform marked; exchange rate/reserves as separate panels; comparative 3-country EMP with Pakistan scale caveat noted; global energy index; stress-test bar chart)
- `policy_note/IMF_style_policy_note.md` — 2-page structure (key message, what changed, what the data show, stress-test takeaway, vulnerabilities/policy implications, causality caveat)
- `FINAL_RESULTS_LOCKED.md` — eight locked result blocks (R-001 through R-008) covering the EMP reform-window summary, EMP extremes, reserve/FX reform detail, cross-country comparison (with the Pakistan/Vietnam comparator constraint locked alongside it, not separable), the stress test, the EMP methodology specification, institutional terminology, and the permanently excluded variables — plus an explicit change-log protocol for any future revision

**Interpretive discipline maintained throughout both documents:** "coincided with," "is consistent with," "descriptively," "mechanically implies" used throughout; "the reform caused/reduced/stabilized" never asserted as a finding. The Pakistan/Vietnam comparator pattern is presented as a central limitation in both the paper (Section 5, restated in Section 7) and the policy note (stated in four separate places: key message, what the data show, vulnerabilities, and its own dedicated caveat section) — not a buried footnote.

**No new analytical gate created**, per instruction. This closes the project's core analytical workflow; only the GitHub repository packaging, data dictionary finalization, and any interview-preparation work (Gates 9–10 in the original workflow) remain outside what was requested this turn.

---

## Editorial Corrections to Paper and Policy Note (Decision ID: D-024)

Wording-only corrections per instruction — no calculation, data, methodology, stress-test assumption, table value, or locked result changed:
1. "not an outlier by conventional standards" / "not statistically unusual" → "not unusually large relative to the preceding 12-month empirical distribution" (removes implied hypothesis test).
2. Relative causal-plausibility phrasing ("at least as plausible/relevant") → "cannot be disentangled from common external conditions" (paper Section 5/Conclusion; policy note).
3. "market-clearing pricing/adjustment" → "consistent with the documented crawling-peg-with-band arrangement," with an explicit statement that no counterfactual market-clearing rate is inferred.
4. "financing gap" (stress-test context) → "mechanically implied external-account deterioration" / "cumulative external-account deterioration."
5. Figure 3 regenerated as three small-multiple panels (independent y-axis per country) so Bangladesh and Vietnam are no longer visually compressed by Pakistan's scale — replaces the single shared-axis chart.
6. Figure 5 (stress-test bar chart) removed from the paper's narrative and figure list; the underlying PNG, `STRESS_TEST.md`, and `gate3_stress_test.csv` are untouched; Table 4 (already in the paper) remains the sole presentation of the stress-test results.

All five locked results (R-001–R-005) and every numerical value in `FINAL_RESULTS_LOCKED.md` are unchanged.

---

## Excel Stress-Test Workbook (Decision ID: D-025)

`stress_test/External_Stress_Test.xlsx` created — a genuinely auditable, fully formula-driven reproduction of Gate 3, not a static table paste. Six sheets: README, Inputs, Scenarios, Calculations, Summary, QA_Checks. No new data sourced, no assumption changed, no result altered, no excluded variable (external debt/REER/policy rate — confirmed absent by direct search of every cell) introduced, no macros/VBA, no reserve-loss figure.

**Build note, disclosed rather than hidden:** an initial version of the Calculations sheet had an off-by-one row-reference error (shock-percentage formulas pointed one row above the actual Scenarios-linked percentages), which produced a "REVIEW REQUIRED" result and visibly wrong shock amounts (e.g., Bangladesh's remittance shock showing $0 instead of a deterioration). This is exactly the kind of error the QA_Checks sheet exists to catch, and it did — the error was found and fixed before delivery, not after.

**Post-fix verification (LibreOffice recalculation, zero formula errors, 109 formulas):**
- All 30 QA_Checks formulas return PASS; overall cell reads "ALL CHECKS PASSED"
- Bangladesh combined deterioration: -$12,258.14mn (exact match to locked R-005); shocked CA -$12,097.13mn
- Pakistan combined deterioration: -$11,850.34mn; shocked CA -$11,400.35mn
- Vietnam combined deterioration (export + import-price only, remittance shock correctly rendered as text "N/A", never 0): -$70,616.15mn; shocked CA -$39,593.15mn
- All baseline inputs verified against `gate3_stress_test.csv`; all locked results verified against `FINAL_RESULTS_LOCKED.md` R-005 — all PASS

**Auditability features:** Scenario assumption cells (remittance/export/energy shock %, import-price transmission/pass-through rate, horizon) are isolated, yellow-highlighted, and editable; every downstream calculation is a formula referencing them or the Inputs sheet, not a hardcoded number; the energy shock (+10%) and its transmission rate (100%) are shown as separate multiplying cells rather than a single opaque "-10%" import-price shock figure.

`FINAL_RESULTS_LOCKED.md` was not modified.

---

## GitHub Repository Packaging (Decision ID: D-026)

Final repository structure assembled: `README.md`, `LICENSE` (MIT for original code/writing; explicit carve-out stating it does not cover third-party IMF/Bangladesh Bank/SBP data), `REPRODUCIBILITY.md`, and a new `code/` folder (six numbered Python scripts, `01_calculate_emp.py` through `06_build_excel_workbook.py`) reproducing the full pipeline that was previously run ad hoc in-session.

**Verification performed, not assumed:** each of the six scripts was executed in an isolated test directory against the already-delivered raw files, and its output was diffed or spot-checked against the already-delivered derived files.
- `01_calculate_emp.py`: `emp_klr_two_component.csv` byte-for-byte identical; `emp_qa_summary.csv` identical after one added column.
- `02_build_master_dataset.py`: identical except floating-point representation noise at the 12th–16th significant digit (immaterial at any reported precision) and one corrected file-path string in a notes column; `master_qa_summary.csv` exactly identical. One bug found and fixed during testing (missing "WLD" entity in the country-name lookup, and three per-country loops incorrectly iterating over all four entities instead of the three actual countries).
- `03_gate2_analysis.py` and `04_gate3_stress_test.py`: key outputs (Bangladesh EMP window means; all three countries' combined stress-test deterioration and shocked CA) matched `FINAL_RESULTS_LOCKED.md` exactly.
- `06_build_excel_workbook.py`: rebuilt workbook recalculates with zero formula errors and QA_Checks reads "ALL CHECKS PASSED," matching the already-delivered workbook's values exactly.

**Final consistency checks (per instruction), all passed:**
- Every file path referenced in `README.md` exists in the delivered tree.
- No occurrence of "free float" or "fully flexible" describing the reform anywhere in `README.md`, `REPRODUCIBILITY.md`, `paper/final_paper.md`, or `policy_note/IMF_style_policy_note.md` except as explicit negations ("never described as," "not characterized as").
- No "forecast" claim about the stress test anywhere except explicit negations ("not a forecast," "not reserve forecasts").
- No stale Figure 5 reference in the paper; README's repository-structure note correctly documents that Figure 5 exists in `paper/figures/` but is not used in the final paper (per D-024), rather than omitting it silently.
- No claim anywhere that Stata was executed successfully — `REPRODUCIBILITY.md` states plainly that `03_EMP.do` was not independently executed.

**No genuinely obsolete or duplicate files found in the delivered tree** requiring removal. `paper/figures/fig5_stress_test.png` is retained deliberately, consistent with the explicit commitment already logged in D-024 not to delete it.

`FINAL_RESULTS_LOCKED.md` was not modified. No new analysis, data sourcing, methodology change, or locked-result change was performed — this entry documents packaging and verification only.

---

## Reproducibility Cleanup (Decision ID: D-027)

Reproducibility-only changes, no research result/methodology/data/assumption/figure/paper/locked-result change:

1. **`requirements.txt` added** — pandas==3.0.2, numpy==2.4.4, matplotlib==3.10.8, openpyxl==3.1.5, pinned to the tested environment. `datetime`/`statistics` correctly excluded (standard library).
2. **`REPRODUCIBILITY.md` states the tested Python version (3.12.3)** and references `requirements.txt`.
3. **`code/06_build_excel_workbook.py` modified** so the Inputs sheet's quarterly/monthly line items are read from `data/derived/master_analytical_dataset.csv`, and the QA_Checks sheet's reference values are read from `data/derived/gate3_stress_test.csv`, at build time — replacing Python constants that had been retyped by hand from those files. The Excel workbook's structure, formulas, sheet layout, and locked results are unchanged.
4. **Full six-script pipeline re-run end to end in a clean isolated environment** after the change. All results matched exactly: `emp_klr_two_component.csv` and `gate3_stress_test.csv` byte-for-byte identical to the previously-delivered files; `master_analytical_dataset.csv` identical aside from floating-point noise at the 12th–16th significant digit and one already-logged cosmetic path correction; rebuilt Excel workbook recalculates with zero formula errors across 109 formulas and QA_Checks reads "ALL CHECKS PASSED" (zero FAILs) — Bangladesh combined deterioration −$12,258.14mn (shocked CA −$12,097.13mn), Pakistan −$11,850.34mn (shocked CA −$11,400.35mn), Vietnam −$70,616.15mn two-shock basis (shocked CA −$39,593.15mn), all matching `FINAL_RESULTS_LOCKED.md` R-005 exactly.
5. **README research-question wording narrowed**: "How did Bangladesh's external-sector adjustment evolve" → "How did Bangladesh's exchange-rate and reserve pressure dynamics evolve," with an added explicit sentence stating the project does not claim to measure every dimension of external-sector adjustment (e.g., capital-flow composition, valuation effects are out of scope). This is a README-only wording change; the paper's own title and text were not touched.
6. **No new dependencies added** beyond what the six scripts already required.

`FINAL_RESULTS_LOCKED.md` was not modified.

---

## Workbook Corrections from User's Direct Inspection (Decision ID: D-028)

User inspected `06_build_excel_workbook.py` directly and identified four issues. All four were evaluated as sound before executing, per standing instruction to check the user's logic first:

1. **Horizon miscategorized as an editable assumption.** Correct catch: horizon=4 quarters is a fixed methodological parameter (the Inputs sheet's baseline is built from a specific hard-coded set of 4 quarters/12 months) — changing the horizon cell alone would not actually change which observations are pulled, so presenting it with the same yellow/editable styling as the genuine shock assumptions was misleading about the workbook's actual interactivity. Fixed: horizon cell now grey-filled, black font, with explanatory text stating it is fixed and shown for reference only; the Scenarios-sheet header note now clarifies only the shock assumptions are editable. Value (4) and all calculations unchanged.
2. **Excel README wording inconsistency.** The workbook's own research-question text still said "external-sector adjustment" after the repository README was already corrected to "exchange-rate and reserve pressure dynamics" (D-027). Fixed for consistency; paper title/content untouched.
3. **QA Section 8 wording overstated the read mechanism.** The workbook reads its reference values from `gate3_stress_test.csv`, not by parsing `FINAL_RESULTS_LOCKED.md` directly — the old header ("Locked final results match FINAL_RESULTS_LOCKED.md R-005") could be misread as a direct file-level read. Reworded to "Workbook results match the verified Gate 3 reference values (from gate3_stress_test.csv, consistent with FINAL_RESULTS_LOCKED.md R-005)," preserving the R-005 label as context rather than as a claimed read source.
4. **Hard-coded Inputs QA row ranges (optional robustness cleanup).** QA checks 1 and 2 previously used literal row-range strings (e.g., "Inputs!B6:B9") duplicating positions already known from `inputs_rows`. Replaced with ranges derived arithmetically from `inputs_rows` (quarterly blocks = total_row−4 to total_row−1; remittance blocks = total_row−12 to total_row−1) — same effective ranges, no longer independently hard-coded.

**Full six-script pipeline re-run end to end in a clean isolated environment after all four changes.** Results: zero formula errors across 109 formulas; QA_Checks reads "ALL CHECKS PASSED" with zero FAILs; all locked Gate 3 values unchanged and confirmed exact (Bangladesh −$12,258.14mn / −$12,097.13mn; Pakistan −$11,850.34mn / −$11,400.35mn; Vietnam −$70,616.15mn / −$39,593.15mn); `emp_klr_two_component.csv` and `gate3_stress_test.csv` byte-for-byte identical to the previously-delivered files. No methodology, data, or locked-result change. `FINAL_RESULTS_LOCKED.md` not modified.

---

## Final Workbook Freeze (Decision ID: D-029)

Three presentation/QA fixes, evaluated as sound before executing:

1. **Calculations!D13 (Vietnam remittance shock %) changed from -10.0% to text "N/A".** Real inconsistency: the dollar shock amount (D18) already correctly showed "N/A" for Vietnam, but the percentage assumption row above it (D13) was still displaying the -10% Bangladesh/Pakistan assumption via a formula applied uniformly across all three columns — implying Vietnam had a remittance-shock rate assigned to it when it doesn't receive this shock at all. Fixed by writing D13 as literal text "N/A" instead of a formula reference to the shared assumption cell; B13/C13 unchanged.
2. **New QA check 3b added**, verifying Calculations!D13 is text "N/A" (ISTEXT, exact match, NOT ISNUMBER) — companion to the existing check 3 (which covers the dollar-amount row), so the percentage-row fix is itself verified, not just asserted.
3. **Summary sheet columns B and C widened** (16→28, 18→40) so scenario labels ("Import-price shock only," etc.) and the "Mechanically shocked current account" header display in full.
4. **Full six-script pipeline re-run end to end in a clean isolated environment.** Zero formula errors; QA_Checks reads "ALL CHECKS PASSED" across 31 checks (30 + the new 3b), zero FAILs; all locked Gate 3 values confirmed unchanged (Bangladesh −$12,258.14mn/−$12,097.13mn; Pakistan −$11,850.34mn/−$11,400.35mn; Vietnam −$70,616.15mn/−$39,593.15mn); `emp_klr_two_component.csv` and `gate3_stress_test.csv` byte-for-byte identical to the previously-delivered files. No data, methodology, assumption, or locked-result change. `FINAL_RESULTS_LOCKED.md` not modified.

**This is the final freeze of `stress_test/External_Stress_Test.xlsx` and `code/06_build_excel_workbook.py`, per instruction — no further changes unless a new substantive error is found.**
