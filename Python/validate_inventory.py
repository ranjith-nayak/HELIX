import pandas as pd
from pathlib import Path

# ============================================================
# HELIX INVENTORY DATA QUALITY ENGINE
# ============================================================

csv_path = Path(__file__).resolve().parent.parent / "Dataset" / "Raw" / "inventory.csv"

print("=" * 65)
print("          HELIX INVENTORY DATA QUALITY ENGINE")
print("=" * 65)

if not csv_path.exists():
    print("inventory.csv not found!")
    exit()

df = pd.read_csv(csv_path)

# ============================================================
# VALIDATIONS
# ============================================================

duplicate_inventory = df["InventoryID"].duplicated().sum()

missing_values = df.isnull().sum().sum()

negative_quantity = (df["QuantityInStock"] < 0).sum()

negative_reorder = (df["ReorderPoint"] < 0).sum()

negative_maximum = (df["MaximumStockLevel"] < 0).sum()

invalid_unit_cost = (df["UnitCost"] < 0).sum()

valid_status = {
    "In Stock",
    "Low Stock",
    "Out of Stock"
}

invalid_status = (~df["Status"].isin(valid_status)).sum()

# ============================================================
# REPORT
# ============================================================

print()

print("=" * 65)
print("          INVENTORY DATA QUALITY REPORT")
print("=" * 65)

print(f"Total Inventory Records : {len(df)}")
print(f"Duplicate Inventory IDs : {duplicate_inventory}")
print(f"Missing Values          : {missing_values}")
print(f"Negative Quantity       : {negative_quantity}")
print(f"Negative Reorder Point  : {negative_reorder}")
print(f"Negative Maximum Stock  : {negative_maximum}")
print(f"Invalid Unit Cost       : {invalid_unit_cost}")
print(f"Invalid Status          : {invalid_status}")

print("=" * 65)

if (
    duplicate_inventory == 0
    and missing_values == 0
    and negative_quantity == 0
    and negative_reorder == 0
    and negative_maximum == 0
    and invalid_unit_cost == 0
    and invalid_status == 0
):
    print("OVERALL STATUS          : PASS ✅")
else:
    print("OVERALL STATUS          : FAIL ❌")

print("=" * 65)