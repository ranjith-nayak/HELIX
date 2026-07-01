import random
import pandas as pd
from pathlib import Path
from faker import Faker

fake = Faker()

# ============================================================
# LOAD MASTER DATA
# ============================================================

base_path = Path(__file__).resolve().parent.parent / "Dataset" / "Raw"

customers = pd.read_csv(base_path / "customers.csv")
products = pd.read_csv(base_path / "products.csv")
inventory = pd.read_csv(base_path / "inventory.csv")

# ============================================================
# CONFIGURATION
# ============================================================

NUMBER_OF_ORDERS = 1000

orders = []

statuses = [
    "Pending",
    "Processing",
    "Shipped",
    "Delivered",
    "Cancelled"
]

status_weights = [
    5,
    10,
    20,
    60,
    5
]

# ============================================================
# GENERATE ORDERS
# ============================================================

for i in range(1, NUMBER_OF_ORDERS + 1):

    customer = customers.sample(1).iloc[0]

    product = products.sample(1).iloc[0]

    quantity = random.randint(1, 10)

    discount = random.choice([0, 5, 10, 15, 20])

    order_date = fake.date_between(
        start_date="-2y",
        end_date="today"
    )

    delivery_date = (
        pd.to_datetime(order_date)
        + pd.Timedelta(days=random.randint(2, 10))
    )

    status = random.choices(
        statuses,
        weights=status_weights
    )[0]

    orders.append({

        "OrderID": f"ORD{i:06d}",

        "CustomerID": customer["CustomerID"],

        "ProductID": product["ProductID"],

        "Quantity": quantity,

        "UnitPrice": product["SellingPrice"],

        "DiscountPercent": discount,

        "OrderDate": order_date,

        "DeliveryDate": delivery_date.date(),

        "OrderStatus": status

    })

# ============================================================
# DATAFRAME
# ============================================================

df = pd.DataFrame(orders)

print("\n========== FIRST 10 ORDERS ==========\n")

print(df.head(10))

print("\n=====================================")

print(f"\nTotal Orders Generated : {len(df)}")

# ============================================================
# EXPORT CSV
# ============================================================

output_path = base_path / "orders.csv"

df.to_csv(output_path, index=False)

print("\norders.csv exported successfully!")