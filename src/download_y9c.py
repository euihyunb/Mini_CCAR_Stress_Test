"""
Download FR Y-9C filings for a single holding company.

Covers 2005 Q1 through 2021 Q1, hosted by the Federal Reserve Bank of Chicago
as consolidated quarterly files for all holding companies.

Filings from 2021 Q2 onward are served by the National Information Center,
which applies CAPTCHA-based bot protection and returns HTTP 403 to
programmatic requests. Those 19 filings are retrieved through a browser; see
data/raw/y9c/README.md.

Run from the repository root:
    python src/download_y9c.py
"""

import time
from pathlib import Path

import requests

rssd = 1037003  # M&T Bank Corporation

chicago_url = (
    "https://www.chicagofed.org/~/media/others/banking/"
    "financial-institution-reports/bhc-data/bhcf{yy}{mm}.csv"
)

sample_start = (2005, 1)
sample_end = (2021, 1)  # last quarter hosted by the Chicago Fed

out_dir = Path("data") / "raw" / "y9c"
pause_seconds = 1.0

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    )
}


def quarters(start, end):
    """Yield (year, quarter) pairs from start to end inclusive."""
    year, quarter = start
    while (year, quarter) <= end:
        yield year, quarter
        quarter += 1
        if quarter > 4:
            year, quarter = year + 1, 1


def quarter_end_month(quarter):
    return quarter * 3


def chicago_target(year, quarter):
    yy = f"{year % 100:02d}"
    mm = f"{quarter_end_month(quarter):02d}"
    return chicago_url.format(yy=yy, mm=mm), f"bhcf{yy}{mm}.csv"


def download(url, path):
    if path.exists():
        return "skipped"

    response = requests.get(url, headers=headers, timeout=120)
    if response.status_code != 200:
        return f"failed ({response.status_code})"

    path.write_bytes(response.content)
    return f"{len(response.content):,} bytes"


def main():
    out_dir.mkdir(parents=True, exist_ok=True)

    for year, quarter in quarters(sample_start, sample_end):
        url, filename = chicago_target(year, quarter)
        result = download(url, out_dir / filename)
        print(f"{year}Q{quarter}  {filename:16s}  {result}")

        if result != "skipped":
            time.sleep(pause_seconds)


if __name__ == "__main__":
    main()