import pandas as pd
from pathlib import Path

# ============================================================
# HELIX DATE DATA QUALITY ENGINE
# ============================================================

csv_path = (
    Path(__file__).resolve().parent.parent
    / "Dataset"
    / "Raw"
    / "dates.csv"
)

print("=" * 65)
print("             HELIX DATE DATA QUALITY ENGINE")
print("=" * 65)

if not csv_path.exists():
    print("dates.csv not found!")
    exit()

df = pd.read_csv(csv_path)

# ============================================================
# VALIDATIONS
# ============================================================

duplicate_dates = df["DateKey"].duplicated().sum()

missing_values = df.isnull().sum().sum()

invalid_month = (
    (df["MonthNumber"] < 1) |
    (df["MonthNumber"] > 12)
).sum()

invalid_quarter = (
    (df["QuarterNumber"] < 1) |
    (df["QuarterNumber"] > 4)
).sum()

invalid_week = (
    (df["WeekNumber"] < 1) |
    (df["WeekNumber"] > 53)
).sum()

# ============================================================
# REPORT
# ============================================================

print()

print("=" * 65)
print("                DATE DATA QUALITY REPORT")
print("=" * 65)

print(f"Total Dates             : {len(df)}")
print(f"Duplicate Date Keys     : {duplicate_dates}")
print(f"Missing Values          : {missing_values}")
print(f"Invalid Months          : {invalid_month}")
print(f"Invalid Quarters        : {invalid_quarter}")
print(f"Invalid Week Numbers    : {invalid_week}")

print("=" * 65)

if (
    duplicate_dates == 0
    and missing_values == 0
    and invalid_month == 0
    and invalid_quarter == 0
    and invalid_week == 0
):
    print("OVERALL STATUS          : PASS ✅")
else:
    print("OVERALL STATUS          : FAIL ❌")

print("=" * 65)