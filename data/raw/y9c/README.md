# FR Y-9C filings

Raw filings for M&T Bank Corporation, RSSD 1037003. Not committed to the
repository.

## Coverage

| Period | Source | Retrieval |
|---|---|---|
| 2005 Q1 to 2021 Q1 | Federal Reserve Bank of Chicago | `python src/download_y9c.py` |
| 2021 Q2 to 2025 Q4 | National Information Center | Manual, see below |

## Chicago Federal Reserve

Consolidated quarterly files covering all holding companies. Wide format, one
row per institution, item codes as column headers. The second row of each file
is a separator line and must be skipped when reading.

Files are named `bhcf{YY}{MM}.csv` where MM is the quarter-end month.

## National Information Center

The NIC Financial Data Download applies CAPTCHA-based bot protection.
Programmatic requests return HTTP 403 regardless of headers or session
handling, so these filings are retrieved through a browser.

1. Go to the NIC Financial Data Download page
2. Select report type FR Y-9C and institution RSSD 1037003
3. Download the CSV for each quarter from 2021 Q2 through 2025 Q4
4. Save to this directory without renaming

Files are named `FRY9C_1037003_{YYYYMMDD}.csv`. Long format, one row per line
item, with an item code, description, and value.

## Format difference

The two sources use different layouts. Notebook 03 reads each with a separate
loader and reconciles them at the 2021 Q1 to Q2 boundary.