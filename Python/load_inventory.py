import pandas as pd
from pathlib import Path

from Framework.database import get_connection
from Framework.etl_logger import ETLLogger

# ============================================================
# HELIX INVENTORY ETL LOADER
# ============================================================

logger = ETLLogger("Inventory ETL")

# ============================================================
# READ CSV
# ============================================================

csv_path = Path(__file__).resolve().parent.parent / "Dataset" / "Raw" / "inventory.csv"

print(csv_path)
print(csv_path.exists())

df = pd.read_csv(csv_path)

df["LastRestockDate"] = pd.to_datetime(
    df["LastRestockDate"]
).dt.strftime("%Y-%m-%d")

print(f"\nInventory Records Found : {len(df)}")

connection = None
cursor = None

try:

    connection = get_connection()
    cursor = connection.cursor()

    query = """
    INSERT INTO Inventory
    (
        InventoryID,
        ProductID,
        SupplierID,
        QuantityInStock,
        ReorderPoint,
        MaximumStockLevel,
        UnitCost,
        LastRestockDate,
        Status
    )
    VALUES
    (%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """

    loaded = 0

    for _, row in df.iterrows():

        cursor.execute(
            query,
            (
                row["InventoryID"],
                row["ProductID"],
                row["SupplierID"],
                row["QuantityInStock"],
                row["ReorderPoint"],
                row["MaximumStockLevel"],
                row["UnitCost"],
                row["LastRestockDate"],
                row["Status"]
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