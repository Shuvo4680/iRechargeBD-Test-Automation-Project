"""
Lightweight CSV/Excel data reader for data-driven tests.

Kept dependency-free (csv module) by default; swap in openpyxl/pandas
if you move to true .xlsx test data files.
"""
import csv
import os

TEST_DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "test_data")


def read_csv(filename: str):
    """
    Reads a CSV file from test_data/ and returns a list of dicts,
    one per row, keyed by the header row.
    """
    path = os.path.join(TEST_DATA_DIR, filename)
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return [row for row in reader]
