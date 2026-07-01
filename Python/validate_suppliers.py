import pandas as pd
from pathlib import Path

# ============================================================
# HELIX SUPPLIER DATA QUALITY ENGINE
# ============================================================

csv_path = Path(
    r"C:\Users\user\Desktop\Helix\Dataset\Raw\suppliers.csv"
)

print("=" * 65)
print("          HELIX SUPPLIER DATA QUALITY ENGINE")
print("=" * 65)

if not csv_path.exists():

    print("suppliers.csv not found!")
    exit()

df = pd.read_csv(csv_path)

# ============================================================
# VALIDATIONS
# ============================================================

duplicate_supplier_ids = df["SupplierID"].duplicated().sum()

duplicate_emails = df["Email"].duplicated().sum()

duplicate_phones = df["Phone"].duplicated().sum()

missing_values = df.isnull().sum().sum()

invalid_rating = (
    (df["SupplierRating"] < 0) |
    (df["SupplierRating"] > 5)
).sum()

negative_leadtime = (
    df["LeadTimeDays"] < 0
).sum()

valid_status = {
    "Active",
    "Inactive"
}

invalid_status = (
    ~df["Status"].isin(valid_status)
).sum()

# ============================================================
# REPORT
# ============================================================

print()

print("=" * 65)
print("          SUPPLIER DATA QUALITY REPORT")
print("=" * 65)

print(f"Total Suppliers           : {len(df)}")
print(f"Duplicate Supplier IDs    : {duplicate_supplier_ids}")
print(f"Duplicate Emails          : {duplicate_emails}")
print(f"Duplicate Phones          : {duplicate_phones}")
print(f"Missing Values            : {missing_values}")
print(f"Invalid Ratings           : {invalid_rating}")
print(f"Negative Lead Time        : {negative_leadtime}")
print(f"Invalid Status            : {invalid_status}")

print("=" * 65)

if (
    duplicate_supplier_ids == 0
    and duplicate_emails == 0
    and duplicate_phones == 0
    and missing_values == 0
    and invalid_rating == 0
    and negative_leadtime == 0
    and invalid_status == 0
):
    print("OVERALL STATUS            : PASS ✅")
else:
    print("OVERALL STATUS            : FAIL ❌")

print("=" * 65)