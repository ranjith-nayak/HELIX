import pandas as pd
import mysql.connector
from pathlib import Path

from Framework.etl_logger import ETLLogger

# ============================================================
# HELIX CUSTOMER ETL LOADER
# ============================================================

logger = ETLLogger("Customer ETL")

# ============================================================
# READ CSV
# ============================================================

csv_path = Path(__file__).resolve().parent.parent / "Dataset" / "Raw" / "customers.csv"

print(csv_path)
print(csv_path.exists())

df = pd.read_csv(csv_path)

# ============================================================
# DATE CONVERSION
# ============================================================

df["DateOfBirth"] = pd.to_datetime(
    df["DateOfBirth"],
    dayfirst=True
).dt.strftime("%Y-%m-%d")

df["RegistrationDate"] = pd.to_datetime(
    df["RegistrationDate"],
    dayfirst=True
).dt.strftime("%Y-%m-%d")

print(f"\nCustomers Found : {len(df)}")

# ============================================================
# MYSQL CONNECTION
# ============================================================

connection = None
cursor = None

try:

    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Ranjith@123",
        database="AstraNova_OLTP"
    )

    cursor = connection.cursor()

    # ============================================================
    # INSERT QUERY
    # ============================================================

    query = """
    INSERT INTO Customer
    (
        CustomerID,
        SegmentID,
        FirstName,
        LastName,
        Email,
        Phone,
        DateOfBirth,
        Gender,
        RegistrationDate,
        Status
    )
    VALUES
    (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """

    loaded = 0

    # ============================================================
    # LOAD DATA
    # ============================================================

    for _, row in df.iterrows():

        cursor.execute(
            query,
            (
                row["CustomerID"],
                row["SegmentID"],
                row["FirstName"],
                row["LastName"],
                row["Email"],
                row["Phone"],
                row["DateOfBirth"],
                row["Gender"],
                row["RegistrationDate"],
                row["Status"]
            )
        )

        loaded += 1

    connection.commit()

 # ============================================================
    # SUCCESS REPORT
    # ============================================================

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