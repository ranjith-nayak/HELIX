import random
import pandas as pd
from pathlib import Path

# ============================================================
# LOAD MASTER DATA
# ============================================================

product_path = Path(__file__).resolve().parent.parent / "Dataset" / "Raw" / "products.csv"
supplier_path = Path(__file__).resolve().parent.parent / "Dataset" / "Raw" / "suppliers.csv"

products = pd.read_csv(product_path)
suppliers = pd.read_csv(supplier_path)

# ============================================================
# CONFIGURATION
# ============================================================

NUMBER_OF_INVENTORY = 300

inventory = []

# ============================================================
# GENERATE INVENTORY
# ============================================================

for i in range(1, NUMBER_OF_INVENTORY + 1):

    product = products.sample(1).iloc[0]
    supplier = suppliers.sample(1).iloc[0]

    quantity = random.randint(0, 500)

    reorder = random.randint(20, 80)

    maximum = random.randint(300, 700)

    unit_cost = round(
        float(product["CostPrice"]),
        2
    )

    if quantity == 0:
        status = "Out of Stock"
    elif quantity <= reorder:
        status = "Low Stock"
    else:
        status = "In Stock"

    inventory.append({

        "InventoryID": f"INV{i:06d}",

        "ProductID": product["ProductID"],

        "SupplierID": supplier["SupplierID"],

        "QuantityInStock": quantity,

        "ReorderPoint": reorder,

        "MaximumStockLevel": maximum,

        "UnitCost": unit_cost,

        "LastRestockDate": pd.Timestamp.today().normalize() - pd.Timedelta(days=random.randint(1, 90)),

        "Status": status

    })

# ============================================================
# DATAFRAME
# ============================================================

df = pd.DataFrame(inventory)

print("\n========== FIRST 10 INVENTORY RECORDS ==========\n")

print(df.head(10))

print("\n===============================================")

print(f"\nTotal Inventory Records : {len(df)}")

# ============================================================
# EXPORT CSV
# ============================================================

output_path = Path(__file__).resolve().parent.parent / "Dataset" / "Raw" / "inventory.csv"

df.to_csv(output_path, index=False)

print("\ninventory.csv exported successfully!")