import pandas as pd
from pathlib import Path
import re

# ============================================================
# HELIX CUSTOMER DATA VALIDATION ENGINE v1.0
# ============================================================

# Dataset Location
csv_path = Path(r"C:\Users\user\Desktop\Helix\Dataset\Raw\customers.csv")

print("=" * 65)
print("        HELIX CUSTOMER DATA QUALITY ENGINE")
print("=" * 65)

# ------------------------------------------------------------
# Load Dataset
# ------------------------------------------------------------

if not csv_path.exists():
    print("ERROR : customers.csv not found")
    print(csv_path)
    exit()

df = pd.read_csv(csv_path)

print(f"\nDataset Loaded Successfully")
print(f"Total Records : {len(df)}")

# ------------------------------------------------------------
# Duplicate Validation
# ------------------------------------------------------------

duplicate_ids = df["CustomerID"].duplicated().sum()
duplicate_emails = df["Email"].duplicated().sum()
duplicate_phones = df["Phone"].duplicated().sum()

# ------------------------------------------------------------
# Missing Values
# ------------------------------------------------------------

missing_values = df.isnull().sum().sum()

# ------------------------------------------------------------
# Customer ID Validation
# Format : CUS000001
# ------------------------------------------------------------

customer_pattern = r"^CUS\d{6}$"

invalid_customer_ids = (
    ~df["CustomerID"]
    .astype(str)
    .str.match(customer_pattern)
).sum()

# ------------------------------------------------------------
# Segment Validation
# ------------------------------------------------------------

valid_segments = {
    "SEG001",
    "SEG002",
    "SEG003",
    "SEG004",
    "SEG005"
}

invalid_segments = (
    ~df["SegmentID"].isin(valid_segments)
).sum()

# ------------------------------------------------------------
# Gender Validation
# ------------------------------------------------------------

valid_gender = {
    "Male",
    "Female"
}

invalid_gender = (
    ~df["Gender"].isin(valid_gender)
).sum()

# ------------------------------------------------------------
# Status Validation
# ------------------------------------------------------------

valid_status = {
    "Prospect",
    "Active",
    "Loyal",
    "Dormant",
    "Inactive",
    "Blocked"
}

invalid_status = (
    ~df["Status"].isin(valid_status)
).sum()

# ------------------------------------------------------------
# Email Validation
# ------------------------------------------------------------

email_pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

invalid_email = (
    ~df["Email"]
    .astype(str)
    .str.match(email_pattern)
).sum()

# ------------------------------------------------------------
# Phone Validation
# ------------------------------------------------------------

phone_pattern = r'^[6-9]\d{9}$'

invalid_phone = (
    ~df["Phone"]
    .astype(str)
    .str.match(phone_pattern)
).sum()

# ------------------------------------------------------------
# Report
# ------------------------------------------------------------

print("\n")
print("=" * 65)
print("              CUSTOMER DATA QUALITY REPORT")
print("=" * 65)

print(f"Total Records              : {len(df)}")
print(f"Duplicate Customer IDs     : {duplicate_ids}")
print(f"Duplicate Emails           : {duplicate_emails}")
print(f"Duplicate Phones           : {duplicate_phones}")
print(f"Missing Values             : {missing_values}")
print(f"Invalid Customer IDs       : {invalid_customer_ids}")
print(f"Invalid Segment IDs        : {invalid_segments}")
print(f"Invalid Emails             : {invalid_email}")
print(f"Invalid Phone Numbers      : {invalid_phone}")
print(f"Invalid Gender             : {invalid_gender}")
print(f"Invalid Status             : {invalid_status}")

print("=" * 65)

if (
    duplicate_ids == 0
    and duplicate_emails == 0
    and duplicate_phones == 0
    and missing_values == 0
    and invalid_customer_ids == 0
    and invalid_segments == 0
    and invalid_email == 0
    and invalid_phone == 0
    and invalid_gender == 0
    and invalid_status == 0
):
    print("OVERALL STATUS             : PASS ✅")
else:
    print("OVERALL STATUS             : FAIL ❌")

print("=" * 65)