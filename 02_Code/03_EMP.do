*==============================================================================
* 03_EMP.do
* Constructs the KLR (1998) two-component Exchange Market Pressure (EMP) index
* for Bangladesh, Pakistan, and Vietnam.
*
* INPUTS (raw, unmodified — read-only):
*   data/raw/imf_il_reserves/dataset_2026-09-12T19_47_51_749761953Z_..._IL_13_0_1.csv
*   data/raw/imf_er_exchange_rate/dataset_2026-09-13T15_34_30_478901807Z_..._ER_4_0_1.csv
*
* OUTPUT (derived — never overwrites raw):
*   data/derived/emp_klr_two_component_stata.csv
*   data/derived/emp_qa_summary_stata.csv
*
* METHODOLOGY: Kaminsky, Lizondo & Reinhart (1998), "Leading Indicators of
* Currency Crises," IMF Staff Papers 45(1), 1-48 — two-component EMP index,
* country-specific standard-deviation weighting, no interest-rate term
* (policy rate omitted by project design). KLR's 3-SD crisis threshold is
* NOT applied here — this do-file produces the continuous EMP series only.
*
* SCOPE: Gate 1/3 EMP construction only. No interpretation, no regressions,
* no event studies, no stress tests. Bangladesh's May 2025 reform is not
* discussed in this file.
*
* Target: Stata MP 14.1, macOS. Unchanged from the prior version:
* KLR two-component formula, EOP exchange rate, reserves excluding gold,
* common sample 2018-M01-2026-M06, country-specific alpha, no 3-SD threshold.
*==============================================================================

clear all
set more off
version 14.1

* ---- 0. Paths ----
* Set this to the project's actual root directory before running — e.g.:
*   cd "/Users/ziba/fx-adjustment-comparative-study"
* then leave ROOT as "." below. A relative path only works if Stata's
* current working directory is the project root when this do-file runs.
global ROOT    "."
global RAW_IL  "$ROOT/data/raw/imf_il_reserves/dataset_2026-09-12T19_47_51_749761953Z_DEFAULT_INTEGRATION_IMF_STA_IL_13_0_1.csv"
global RAW_ER  "$ROOT/data/raw/imf_er_exchange_rate/dataset_2026-09-13T15_34_30_478901807Z_DEFAULT_INTEGRATION_IMF_STA_ER_4_0_1.csv"
global DERIVED "$ROOT/data/derived"

cap mkdir "$DERIVED"

*==============================================================================
* 1. IMPORT AND RESHAPE - RESERVES (IMF IL, "Reserves excluding gold")
*
* FIX: the month-column headers in the raw CSV ("2018-M01", "2018-M02", ...)
* are not valid Stata variable names (they start with a digit and contain a
* hyphen), so Stata's import auto-sanitizes them into names that cannot be
* predicted reliably in advance — the original "reshape long v" call assumed
* they were already named "v...", which they are not. Fix: rename the month
* columns to a clean, predictable "v1 v2 v3 ..." stub by POSITION (not by
* guessing their sanitized names), then reconstruct the true "YYYY-Mxx"
* label from that position afterward, since both raw files' month columns
* start at 2018-M01 and run contiguously with no gaps in the column headers
* themselves (any missing DATA within that range is a blank cell, not a
* missing column — this was already confirmed during Gate 1 verification).
*==============================================================================
import delimited "$RAW_IL", clear varnames(1) stringcols(_all)

* Keep only the three locked series codes
keep if inlist(series_code, "BGD.RXF11_REVS.USD.M", "PAK.RXF11_REVS.USD.M", "VNM.RXF11_REVS.USD.M")

gen country_iso3 = substr(series_code, 1, 3)

* Identify the month columns by elimination (whatever Stata named them,
* this returns them in original column order, which is chronological)
ds country_iso3 series_code dataset obs_measure country indicator unit frequency scale, not
local monthvars `r(varlist)'
local nmonths : word count `monthvars'
di as text "IL file: `nmonths' month columns found (expect 103, 2018-M01 to 2026-M07)"

* Rename them to a clean v1..v_N stub, preserving column order
local i = 1
foreach v of local monthvars {
    rename `v' v`i'
    local i = `i' + 1
}

reshape long v, i(country_iso3) j(monthnum)
rename v reserves_usd_mn_SOURCE
destring reserves_usd_mn_SOURCE, replace force

* Reconstruct "YYYY-Mxx" from position, since column 1 = 2018-M01
gen year_r  = 2018 + floor((monthnum - 1) / 12)
gen mon_r   = mod(monthnum - 1, 12) + 1
gen month_str = string(year_r) + "-M" + string(mon_r, "%02.0f")
drop year_r mon_r monthnum

* Keep only the common window 2018-M01 through 2026-M06
keep if month_str >= "2018-M01" & month_str <= "2026-M06"

tempfile reserves
save `reserves'

*==============================================================================
* 2. IMPORT AND RESHAPE - EXCHANGE RATE (IMF ER, End-of-Period)
* Same fix applied as in Section 1.
*==============================================================================
import delimited "$RAW_ER", clear varnames(1) stringcols(_all)

* Keep ONLY the End-of-Period series (locked decision — not Period-Average)
keep if inlist(series_code, "BGD.XDC_USD.EOP_RT.M", "PAK.XDC_USD.EOP_RT.M", "VNM.XDC_USD.EOP_RT.M")

gen country_iso3 = substr(series_code, 1, 3)

ds country_iso3 series_code dataset obs_measure country indicator type_of_transformation frequency scale, not
local monthvars `r(varlist)'
local nmonths : word count `monthvars'
di as text "ER file: `nmonths' month columns found (expect 104, 2018-M01 to 2026-M08)"

local i = 1
foreach v of local monthvars {
    rename `v' v`i'
    local i = `i' + 1
}

reshape long v, i(country_iso3) j(monthnum)
rename v exchange_rate_eop_SOURCE
destring exchange_rate_eop_SOURCE, replace force

gen year_r  = 2018 + floor((monthnum - 1) / 12)
gen mon_r   = mod(monthnum - 1, 12) + 1
gen month_str = string(year_r) + "-M" + string(mon_r, "%02.0f")
drop year_r mon_r monthnum

keep if month_str >= "2018-M01" & month_str <= "2026-M06"

tempfile fx
save `fx'

*==============================================================================
* 3. MERGE RESERVES AND EXCHANGE RATE
*==============================================================================
use `reserves', clear
merge 1:1 country_iso3 month_str using `fx', assert(match) nogenerate

* ---- QA CHECK: completeness before any calculation (Step 2 of spec) ----
by country_iso3: gen n_months = _N
by country_iso3: egen n_miss_r = total(missing(reserves_usd_mn_SOURCE))
by country_iso3: egen n_miss_e = total(missing(exchange_rate_eop_SOURCE))
quietly summarize n_months
di as text "Months per country: " r(min) " to " r(max) " (expect 102 for all three)"
quietly count if n_miss_r > 0 | n_miss_e > 0
if r(N) > 0 {
    di as error "STOP - QA FAILURE: missing reserves or exchange-rate observations in common window"
    exit 459
}
di as result "QA PASSED: all three countries have complete inputs for 2018-M01 to 2026-M06"

* Convert month_str "YYYY-Mxx" into a proper monthly date for sorting/lagging
gen year = real(substr(month_str, 1, 4))
gen mon  = real(substr(month_str, 7, 2))
gen month_date = ym(year, mon)
format month_date %tm

drop year mon n_months n_miss_r n_miss_e
sort country_iso3 month_date

tempfile merged
save `merged'

*==============================================================================
* 4. STEP 1 (of locked spec): MONTH-OVER-MONTH PERCENTAGE CHANGES
*==============================================================================
use `merged', clear
by country_iso3 (month_date): gen pct_change_exchange_rate_CALCULATED = ///
    (exchange_rate_eop_SOURCE - exchange_rate_eop_SOURCE[_n-1]) / exchange_rate_eop_SOURCE[_n-1]

by country_iso3 (month_date): gen pct_change_reserves_CALCULATED = ///
    (reserves_usd_mn_SOURCE - reserves_usd_mn_SOURCE[_n-1]) / reserves_usd_mn_SOURCE[_n-1]

* First month per country (2018-M01) has no prior month — pct changes are
* missing by construction, not an error. Drop it: EMP starts 2018-M02.
by country_iso3 (month_date): drop if _n == 1

* ---- QA CHECK: no divide-by-zero / non-finite values ----
quietly count if missing(pct_change_exchange_rate_CALCULATED) | missing(pct_change_reserves_CALCULATED)
if r(N) > 0 {
    di as error "STOP - QA FAILURE: missing percentage-change values after the first-month drop"
    exit 459
}
di as result "QA PASSED: no missing/non-finite percentage changes"

*==============================================================================
* 5. STEP 3 (of locked spec): COUNTRY-SPECIFIC ALPHA
*    alpha_i = sd(%Delta e_i) / sd(%Delta r_i), full common window 2018-M02-2026-M06
*==============================================================================
by country_iso3: egen sd_e = sd(pct_change_exchange_rate_CALCULATED)
by country_iso3: egen sd_r = sd(pct_change_reserves_CALCULATED)
gen alpha_CALCULATED = sd_e / sd_r
drop sd_e sd_r

*==============================================================================
* 6. STEP 4 (of locked spec): EMP CALCULATION
*    EMP_i,t = %Delta e_i,t - alpha_i * %Delta r_i,t
*==============================================================================
gen EMP_CALCULATED = pct_change_exchange_rate_CALCULATED - alpha_CALCULATED * pct_change_reserves_CALCULATED

* ---- QA CHECK: expected sample bounds (Step 5 of locked spec) ----
local expected_first = ym(2018,2)
local expected_last  = ym(2026,6)
di as text "Expected first EMP month: " %tm `expected_first' " | Expected last EMP month: " %tm `expected_last'
di as text "Actual bounds per country (verify these match the expected values above):"
tabstat month_date, by(country_iso3) stat(min max) format(%tm)

*==============================================================================
* 7. QA SUMMARY TABLE (Step 6 of locked spec)
*==============================================================================
preserve
    collapse (mean) mean_EMP=EMP_CALCULATED (sd) sd_EMP=EMP_CALCULATED ///
             (min) min_EMP=EMP_CALCULATED (max) max_EMP=EMP_CALCULATED ///
             (first) alpha=alpha_CALCULATED (count) n_obs=EMP_CALCULATED, ///
             by(country_iso3)
    list, clean
    export delimited using "$DERIVED/emp_qa_summary_stata.csv", replace
restore

*==============================================================================
* 8. SAVE DERIVED DATASET - never overwrites raw files
*==============================================================================
order country_iso3 month_str month_date reserves_usd_mn_SOURCE exchange_rate_eop_SOURCE ///
      pct_change_exchange_rate_CALCULATED pct_change_reserves_CALCULATED ///
      alpha_CALCULATED EMP_CALCULATED

export delimited using "$DERIVED/emp_klr_two_component_stata.csv", replace

di as result "=============================================================="
di as result "EMP construction complete. KLR 3-SD crisis threshold NOT applied."
di as result "No interpretation, regressions, or event studies performed."
di as result "=============================================================="
