# Data Sources

All inputs to this project are publicly available. Raw files are not committed
to this repository. This document records the source, vintage, and retrieval
path for each input so that the dataset can be reconstructed independently.

Retrieval dates are recorded because federal agencies revise published files.
Where a file has a version or release date, it is stated.

The Federal Reserve publishes stress test materials on two dates each year.
Scenarios and methodology are released in February, at the start of the
exercise. Results are released in June. This project uses the February
scenario file as input and the June results file as the benchmark.
---

## 1. Supervisory scenario

**Purpose:** Provides the nine-quarter macroeconomic paths that drive loss and
revenue projections.

| Field | Value |
|---|---|
| Publisher | Board of Governors of the Federal Reserve System |
| Document | 2026 Stress Test Scenarios |
| Release date | February 4, 2026 |
| Scenario used | Severely adverse, domestic variables |
| Horizon | 2026 Q1 through 2028 Q1 |
| Retrieved | Not yet retrieved |
| Local path | `data/raw/fed_scenarios/` |

Source: https://www.federalreserve.gov/publications/files/2026-final-supervisory-stress-test-scenarios-20260204.pdf

Notes: The Board finalized the 2026 scenarios on February 4, 2026, and at the
same time voted to maintain existing stress test capital requirements pending
consideration of public feedback on proposed changes to the framework.

---

## 2. Bank regulatory filings

**Purpose:** Provides the starting balance sheet, capital position, and the
historical panel used to estimate loss and revenue models.

| Field | Value |
|---|---|
| Publisher | Federal Financial Institutions Examination Council / Federal Reserve |
| Report form | FR Y-9C, Consolidated Financial Statements for Holding Companies |
| Institution | M&T Bank Corporation |
| RSSD ID | To be confirmed |
| Starting balance sheet | 2025 Q4 |
| Historical panel | To be determined |
| Retrieved | Not yet retrieved |
| Local