import pandas as pd
from pathlib import Path

from Framework.database import get_connection
from Framework.etl_logger import ETLLogger

# ============================================================
# HELIX DATE ETL LOADER
# ============================================================

logger = ETLLogger("Date ETL")

# ============================================================
# READ CSV
# ============================================================

csv_path = (
    Path(__file__).resolve().parent.parent
    / "Dataset"
    / "Raw"
    / "dates.csv"
)

print(csv_path)
print(csv_path.exists())

df = pd.read_csv(csv_path)

df["FullDate"] = pd.to_datetime(
    df["FullDate"]
).dt.strftime("%Y-%m-%d")

print(f"\nDates Found : {len(df)}")

connection = None
cursor = None

try:

    connection = get_connection()
    cursor = connection.cursor()

    query = """
    INSERT INTO DimDate
    (
        DateKey,
        FullDate,
        DayNumber,
        DayName,
        MonthNumber,
        MonthName,
        QuarterNumber,
        YearNumber,
        WeekNumber
    )
    VALUES
    (%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """

    loaded = 0

    for _, row in df.iterrows():

        cursor.execute(
            query,
            (
                int(row["DateKey"]),
                row["FullDate"],
                int(row["DayNumber"]),
                row["DayName"],
                int(row["MonthNumber"]),
                row["MonthName"],
                int(row["QuarterNumber"]),
                int(row["YearNumber"]),
                int(row["WeekNumber"])
            )
        )

        loaded += 1

    connection.commit()

    logger.success(
        records_read=len(df),
        records_loaded=loaded
    )

    print("\nDatabase Updated Successfully!")

except Exception as e:

    logger.failure(e)

finally:

    if cursor:
        cursor.close()

    if connection:
        connection.close()