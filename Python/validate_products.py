import pandas as pd
from pathlib import Path

# ============================================================
# HELIX PRODUCT VALIDATION ENGINE v1.0
# ============================================================

csv_path = Path(r"C:\Users\user\Desktop\Helix\Dataset\Raw\products.csv")

print("=" * 65)
print("          HELIX PRODUCT DATA QUALITY ENGINE")
print("=" * 65)

if not csv_path.exists():

    print("products.csv not found!")
    exit()

df = pd.read_csv(csv_path)

# ============================================================
# VALIDATIONS
# ============================================================

duplicate_product_ids = df["ProductID"].duplicated().sum()

duplicate_sku = df["SKU"].duplicated().sum()

missing_values = df.isnull().sum().sum()

negative_cost = (df["CostPrice"] <= 0).sum()

invalid_price = (
    df["SellingPrice"] <= df["CostPrice"]
).sum()

negative_reorder = (
    df["ReorderLevel"] < 0
).sum()

valid_status = {
    "Active",
    "Inactive",
    "Discontinued"
}

invalid_status = (
    ~df["ProductStatus"].isin(valid_status)
).sum()

# ============================================================
# REPORT
# ============================================================

print()

print("=" * 65)
print("              PRODUCT DATA QUALITY REPORT")
print("=" * 65)

print(f"Total Products            : {len(df)}")
print(f"Duplicate Product IDs     : {duplicate_product_ids}")
print(f"Duplicate SKU             : {duplicate_sku}")
print(f"Missing Values            : {missing_values}")
print(f"Negative Cost Price       : {negative_cost}")
print(f"Invalid Selling Price     : {invalid_price}")
print(f"Negative Reorder Level    : {negative_reorder}")
print(f"Invalid Product Status    : {invalid_status}")

print("=" * 65)

if (
    duplicate_product_ids == 0
    and duplicate_sku == 0
    and missing_values == 0
    and negative_cost == 0
    and invalid_price == 0
    and negative_reorder == 0
    and invalid_status == 0
):
    print("OVERALL STATUS            : PASS ✅")
else:
    print("OVERALL STATUS            : FAIL ❌")

print("=" * 65)