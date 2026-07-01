import pandas as pd
from pathlib import Path

from Framework.database import get_connection
from Framework.etl_logger import ETLLogger

# ============================================================
# HELIX SUPPLIER ETL LOADER
# ============================================================

logger = ETLLogger("Supplier ETL")

csv_path = Path(__file__).resolve().parent.parent / "Dataset" / "Raw" / "suppliers.csv"

print(csv_path)
print(csv_path.exists())

df = pd.read_csv(csv_path)

df["CreatedDate"] = pd.to_datetime(
    df["CreatedDate"]
).dt.strftime("%Y-%m-%d")

print(f"\nSuppliers Found : {len(df)}")

connection = None
cursor = None

try:

    connection = get_connection()
    cursor = connection.cursor()

    query = """
    INSERT INTO Supplier
    (
        SupplierID,
        SupplierName,
        ContactPerson,
        Email,
        Phone,
        City,
        State,
        Country,
        SupplierRating,
        LeadTimeDays,
        Status,
        CreatedDate
    )
    VALUES
    (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """

    loaded = 0

    for _, row in df.iterrows():

        cursor.execute(
            query,
            (
                row["SupplierID"],
                row["SupplierName"],
                row["ContactPerson"],
                row["Email"],
                row["Phone"],
                row["City"],
                row["State"],
                row["Country"],
                row["SupplierRating"],
                row["LeadTimeDays"],
                row["Status"],
                row["CreatedDate"]
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