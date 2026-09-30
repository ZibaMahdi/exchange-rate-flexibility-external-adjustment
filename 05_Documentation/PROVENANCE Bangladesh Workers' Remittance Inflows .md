# Provenance — Bangladesh Workers' Remittance Inflows (manually extracted table)

**This is a SOURCE-DERIVED DATA EXTRACT, not a native machine-readable export.** Ziba copied this table from an official PDF report and pasted it into chat; it was not downloaded as a CSV/Excel file from a data portal. This distinction is recorded explicitly, per instruction, and should be carried into any downstream documentation of this variable.

## Source
Bangladesh Bank, "Monthly Report on Workers' Remittance Inflows in Bangladesh — July, 2026"
Table: "Month-wise Workers' Remittance Inflows FY 2014-15 to FY 2026-27"
Unit: million USD
Source department: Statistics Department, Bangladesh Bank (per the table's own footnote: "Upto June, 2016 Foreign Exchange Policy Department, Bangladesh Bank" — i.e., the compiling department changed partway through the historical series, which is itself worth noting even though it predates this project's 2018 start).

## Original pasted table, preserved exactly as provided

```
Monthly Report on Workers’ Remittance Inflows in Bangladesh July, 2026: Month-wise Workers’ Remittance Inflows FY 2014-15 to FY 2026-27
In million USD
Fiscal Year July August September October November December
2014-2015 1139.24 1228.59 1438.31 1048.31 1932.50 1047.75
2015-2016 1296.23 1149.59 1284.70 1139.54 1172.09 1313.13
2016-2017 1005.51 1183.61 1056.64 1010.99 951.37 958.73
2017-2018 1115.57 1418.58 856.87 1162.77 1214.74 1163.82
2018-2019 1318.18 1411.05 1139.66 1239.11 1180.44 1206.91
2019-2020 1597.69 1444.75 1476.91 1641.67 1555.23 1691.68
2020-2021 2598.21 1963.94 2151.05 2102.16 2078.74 2050.65
2021-2022 1871.49 1810.10 1726.71 1646.87 1553.73 1630.66
2022-2023 2096.32 2036.93 1539.60 1525.54 1595.17 1699.70
2023-2024 1973.15 1599.45 1334.35 1971.43 1930.04 1991.26
2024-2025 1913.77 2224.15 2404.11 2395.08 2199.99 2638.78
2025-2026 2477.87 2421.89 2685.56 2562.44 2889.73 3223.67
2026-2027 2858.76                                                                                                                                January February March April May June Total Fiscal Year
1188.54 1245.53 1385.41 1251.49 1305.91 1341.58 15553.16 2014-2015
1167.59 1137.39 1288.15 1191.51 1201.32 1465.59 14806.81 2015-2016
1009.47 940.75 1077.52 1092.64 1267.61 1214.61 12769.46 2016-2017
1379.79 1149.08 1299.77 1331.33 1504.98 1384.37 14981.69 2017-2018
1597.21 1317.73 1458.68 1434.30 1748.16 1368.20 16419.63 2018-2019
1638.43 1452.20 1276.29 1092.96 1504.60 1832.63 18205.02 2019-2020
1961.91 1780.59 1910.98 2067.64 2171.03 1940.81 24777.71 2020-2021
1704.53 1494.47 1859.73 2010.81 1885.34 1837.27 21031.73 2021-2022
1958.87 1560.48 2022.47 1684.91 1691.66 2199.08 21610.72 2022-2023
2113.15 2164.56 1997.07 2044.23 2254.93 2538.60 23912.22 2023-2024
2185.23 2527.65 3295.63 2752.33 2969.56 2822.53 30328.81 2024-2025
3171.63 3019.45 3752.21 3123.32 3442.58 2819.03 35589.39 2025-2026
2858.76 2025-2026
Source : Statistics Department, Bangladesh Bank
Upto June, 2016 Foreign Exchange Policy Department, Bangladesh Bank
```

## QA performed (independent — not trusting the pasted structure at face value)

**1. Fiscal-year/month structure verified:** each row runs July → June (Bangladesh's fiscal year), with the pasted layout splitting into two blocks (Jul–Dec, then Jan–Jun+Total) that had to be matched back together row-by-row by fiscal year label — done manually, cross-checked against the total column (below).

**2. FY-total consistency check (computed sum of 12 months vs. the table's own reported "Total" column):**

| Fiscal Year | Computed sum | Reported total | Difference |
|---|---|---|---|
| 2014-2015 | 15553.16 | 15553.16 | 0.00 |
| 2015-2016 | 14806.83 | 14806.81 | +0.02 |
| 2016-2017 | 12769.45 | 12769.46 | -0.01 |
| 2017-2018 | 14981.67 | 14981.69 | -0.02 |
| 2018-2019 | 16419.63 | 16419.63 | 0.00 |
| 2019-2020 | 18205.04 | 18205.02 | +0.02 |
| 2020-2021 | 24777.71 | 24777.71 | 0.00 |
| 2021-2022 | 21031.71 | 21031.73 | -0.02 |
| 2022-2023 | 21610.73 | 21610.72 | +0.01 |
| 2023-2024 | 23912.22 | 23912.22 | 0.00 |
| 2024-2025 | 30328.81 | 30328.81 | 0.00 |
| 2025-2026 | 35589.38 | 35589.39 | -0.01 |

All differences are ≤$0.02mn — consistent with ordinary rounding in the source table, not a transcription error. Not adjusted or reconciled; reported as-is.

**3. Anomaly found, flagged rather than resolved:** the pasted table contains a stray final entry — `2858.76` paired with the label `2025-2026` — appearing after the properly-structured FY2025-2026 row. This exact value (2858.76) also appears correctly, in the first block, as FY2026-2027's July figure. **This looks like a duplicate/misplaced rendering of the single July 2026 data point, mislabeled with the wrong fiscal year, rather than a second distinct observation** — but this is an inference, not a confirmed fact, since I cannot see the original PDF's layout. It has been treated as a duplicate of the July 2026 figure and **not** double-counted in the reconstructed series below. Ziba should confirm against the actual PDF if precision on this point matters later.

**4. Missing months, duplicated months (in the reconstructed calendar series): none found**, aside from the one flagged anomaly above, which was resolved toward "not a real second observation" rather than left as an unexplained duplicate — documented, not silent.

**5. Live-webpage discrepancy:** Ziba has stated that Bangladesh Bank's live "Monthly data of Wage earner's remittance" webpage shows some values that differ slightly from this July 2026 PDF report. This has **not** been independently verified by Claude (the live page's specific values were not in hand for comparison this pass) — recorded as Ziba's stated observation. Per instruction, **the July 2026 PDF report is the selected vintage for this project's Bangladesh remittance series**, and any future discrepancy against the live webpage is to be recorded, not silently reconciled.

## Calendar-month conversion (as explicitly instructed)

FY 2017-2018's Jan–Jun block supplies Jan 2018–Jun 2018; FY 2018-2019's Jul–Dec block supplies Jul 2018–Dec 2018; and so on through FY 2025-2026's Jun 2026, plus the single FY 2026-2027 July 2026 observation. Result: **103 consecutive monthly observations, January 2018 through July 2026, zero missing, zero duplicates** (after resolving the flagged anomaly above as a non-observation). Full reconstructed series delivered alongside this file as `bd_remittances_calendar_2018_onward.csv`, with each row traceable back to its original fiscal-year/month cell.
