import pandas as pd
from pathlib import Path

# ============================================================
# HELIX ORDER DATA QUALITY ENGINE
# ============================================================

csv_path = Path(__file__).resolve().parent.parent / "Dataset" / "Raw" / "orders.csv"

print("=" * 65)
print("              HELIX ORDER DATA QUALITY ENGINE")
print("=" * 65)

if not csv_path.exists():
    print("orders.csv not found!")
    exit()

df = pd.read_csv(csv_path)

# ============================================================
# VALIDATIONS
# ============================================================

duplicate_orders = df["OrderID"].duplicated().sum()

missing_values = df.isnull().sum().sum()

negative_quantity = (df["Quantity"] <= 0).sum()

negative_price = (df["UnitPrice"] <= 0).sum()

invalid_discount = (
    (df["DiscountPercent"] < 0) |
    (df["DiscountPercent"] > 100)
).sum()

valid_status = {
    "Pending",
    "Processing",
    "Shipped",
    "Delivered",
    "Cancelled"
}

invalid_status = (
    ~df["OrderStatus"].isin(valid_status)
).sum()

# ============================================================
# REPORT
# ============================================================

print()

print("=" * 65)
print("                ORDER DATA QUALITY REPORT")
print("=" * 65)

print(f"Total Orders             : {len(df)}")
print(f"Duplicate Order IDs      : {duplicate_orders}")
print(f"Missing Values           : {missing_values}")
print(f"Invalid Quantity         : {negative_quantity}")
print(f"Invalid Unit Price       : {negative_price}")
print(f"Invalid Discount         : {invalid_discount}")
print(f"Invalid Status           : {invalid_status}")

print("=" * 65)

if (
    duplicate_orders == 0
    and missing_values == 0
    and negative_quantity == 0
    and negative_price == 0
    and invalid_discount == 0
    and invalid_status == 0
):
    print("OVERALL STATUS           : PASS ✅")
else:
    print("OVERALL STATUS           : FAIL ❌")

print("=" * 65)