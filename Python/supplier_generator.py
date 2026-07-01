import random
import pandas as pd
from faker import Faker
from pathlib import Path

from supplier_master import SUPPLIER_COMPANIES

fake = Faker()

# ============================================================
# CONFIGURATION
# ============================================================

NUMBER_OF_SUPPLIERS = 50

# ============================================================
# GENERATE SUPPLIERS
# ============================================================

suppliers = []

categories = list(SUPPLIER_COMPANIES.keys())

for i in range(1, NUMBER_OF_SUPPLIERS + 1):

    category = random.choice(categories)

    supplier_name = random.choice(
        SUPPLIER_COMPANIES[category]
    )

    supplier = {

        "SupplierID": f"SUP{i:06d}",

        "SupplierName": supplier_name,

        "ContactPerson": fake.name(),

        "Email": f"contact{i}@{supplier_name.lower().replace(' ','').replace('.','')}.com",

        "Phone": fake.msisdn()[:10],

        "City": fake.city(),

        "State": fake.state(),

        "Country": "India",

        "SupplierRating": round(
            random.uniform(3.5,5.0),1
        ),

        "LeadTimeDays": random.randint(2,20),

        "Status": random.choices(
            ["Active","Inactive"],
            weights=[90,10]
        )[0],

        "CreatedDate": fake.date_between(
            start_date="-3y",
            end_date="today"
        )

    }

    suppliers.append(supplier)

# ============================================================
# DATAFRAME
# ============================================================

df = pd.DataFrame(suppliers)

print("\n========== FIRST 10 SUPPLIERS ==========\n")

print(df.head(10))

print("\n========================================")

print(f"\nTotal Suppliers Generated : {len(df)}")

# ============================================================
# EXPORT CSV
# ============================================================

output_path = Path(
    r"C:\Users\user\Desktop\Helix\Dataset\Raw\suppliers.csv"
)

df.to_csv(output_path,index=False)

print("\nsuppliers.csv exported successfully!")