import pandas as pd
from pathlib import Path

from Framework.database import get_connection
from Framework.etl_logger import ETLLogger

# ============================================================
# HELIX ORDER ETL LOADER
# ============================================================

logger = ETLLogger("Order ETL")

# ============================================================
# READ CSV
# ============================================================

csv_path = Path(__file__).resolve().parent.parent / "Dataset" / "Raw" / "orders.csv"

print(csv_path)
print(csv_path.exists())

df = pd.read_csv(csv_path)

df["OrderDate"] = pd.to_datetime(df["OrderDate"]).dt.strftime("%Y-%m-%d")
df["DeliveryDate"] = pd.to_datetime(df["DeliveryDate"]).dt.strftime("%Y-%m-%d")

print(f"\nOrders Found : {len(df)}")

connection = None
cursor = None

try:

    connection = get_connection()
    cursor = connection.cursor()

    query = """
    INSERT INTO Orders
    (
        OrderID,
        CustomerID,
        ProductID,
        Quantity,
        UnitPrice,
        DiscountPercent,
        OrderDate,
        DeliveryDate,
        OrderStatus
    )
    VALUES
    (%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """

    loaded = 0

    for _, row in df.iterrows():

        cursor.execute(
            query,
            (
                row["OrderID"],
                row["CustomerID"],
                row["ProductID"],
                row["Quantity"],
                row["UnitPrice"],
                row["DiscountPercent"],
                row["OrderDate"],
                row["DeliveryDate"],
                row["OrderStatus"]
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