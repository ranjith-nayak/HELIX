import pandas as pd
import mysql.connector
from pathlib import Path

from Framework.etl_logger import ETLLogger

# ============================================================
# HELIX PRODUCT ETL LOADER
# ============================================================

logger = ETLLogger("Product ETL")

# ============================================================
# READ CSV
# ============================================================

csv_path = Path(__file__).resolve().parent.parent / "Dataset" / "Raw" / "products.csv"

print(csv_path)
print(csv_path.exists())

df = pd.read_csv(csv_path)

print(f"\nProducts Found : {len(df)}")

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
    INSERT INTO Product
    (
        ProductID,
        CategoryID,
        ProductName,
        Brand,
        SKU,
        CostPrice,
        SellingPrice,
        ReorderLevel,
        ProductStatus,
        CreatedDate
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
                row["ProductID"],
                row["CategoryID"],
                row["ProductName"],
                row["Brand"],
                row["SKU"],
                row["CostPrice"],
                row["SellingPrice"],
                row["ReorderLevel"],
                row["ProductStatus"],
                row["CreatedDate"]
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