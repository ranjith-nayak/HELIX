import pandas as pd
from pathlib import Path

# ============================================================
# HELIX DATE DIMENSION GENERATOR
# ============================================================

start_date = "2023-01-01"
end_date = "2027-12-31"

dates = pd.date_range(start=start_date, end=end_date)

df = pd.DataFrame()

df["DateKey"] = dates.strftime("%Y%m%d").astype(int)

df["FullDate"] = dates

df["DayNumber"] = dates.day

df["DayName"] = dates.day_name()

df["MonthNumber"] = dates.month

df["MonthName"] = dates.month_name()

df["QuarterNumber"] = dates.quarter

df["YearNumber"] = dates.year

df["WeekNumber"] = dates.strftime("%V").astype(int)

print("\n========== FIRST 10 DATES ==========\n")

print(df.head(10))

print("\n===================================")

print(f"\nTotal Dates Generated : {len(df)}")

# ============================================================
# EXPORT CSV
# ============================================================

output_path = (
    Path(__file__).resolve().parent.parent
    / "Dataset"
    / "Raw"
    / "dates.csv"
)

df.to_csv(output_path, index=False)

print("\ndates.csv exported successfully!")