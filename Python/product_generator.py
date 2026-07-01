import random
import pandas as pd
from faker import Faker
from pathlib import Path
from product_master import PRODUCT_MASTER

fake = Faker()

# ============================================================
# CONFIGURATION
# ============================================================

NUMBER_OF_PRODUCTS = 100

# ============================================================
# PRODUCT TYPES
# ============================================================

PRODUCT_TYPES = {

    "Electronics": [
        "Laptop","Smartphone","Monitor","Keyboard","Mouse",
        "Printer","Earbuds","Smart Watch"
    ],

    "Furniture": [
        "Office Chair","Dining Table","Study Table",
        "Wardrobe","Bookshelf","Sofa"
    ],

    "Grocery": [
        "Rice","Coffee","Tea","Butter","Milk",
        "Sugar","Biscuits"
    ],

    "Fashion": [
        "T-Shirt","Jeans","Jacket",
        "Sneakers","Hoodie","Cap"
    ],

    "Sports": [
        "Football","Basketball",
        "Cricket Bat","Badminton Racket",
        "Yoga Mat"
    ],

    "Books": [
        "Python Guide","SQL Handbook",
        "Algorithms","Data Science",
        "Machine Learning"
    ],

    "Beauty": [
        "Face Wash","Shampoo",
        "Lipstick","Perfume",
        "Moisturizer"
    ],

    "Home": [
        "Pressure Cooker","Mixer",
        "Cookware Set","Water Bottle",
        "Vacuum Cleaner"
    ],

    "Toys": [
        "Building Blocks","Puzzle",
        "Remote Car","Doll",
        "Board Game"
    ],

    "Automotive": [
        "Engine Oil","Helmet",
        "Tyre","Seat Cover",
        "Car Wax"
    ]

}

# ============================================================
# CATEGORY PREFIX
# ============================================================

CATEGORY_PREFIX = {

    "CAT001":"ELE",
    "CAT002":"FUR",
    "CAT003":"GRO",
    "CAT004":"FAS",
    "CAT005":"SPO",
    "CAT006":"BOO",
    "CAT007":"BEA",
    "CAT008":"HOM",
    "CAT009":"TOY",
    "CAT010":"AUT"

}

# ============================================================
# GENERATE PRODUCTS
# ============================================================

products = []

for i in range(1, NUMBER_OF_PRODUCTS + 1):

    category_id = random.choice(list(PRODUCT_MASTER.keys()))

    category = PRODUCT_MASTER[category_id]["Category"]

    brand = random.choice(
        PRODUCT_MASTER[category_id]["Brands"]
    )

    product_type = random.choice(
        PRODUCT_TYPES[category]
    )

    product_name = f"{brand} {product_type}"

    product_id = f"PRD{i:06d}"

    sku = f"{CATEGORY_PREFIX[category_id]}-{brand[:3].upper()}-{i:06d}"

    cost_price = round(random.uniform(100,5000),2)

    selling_price = round(
        cost_price * random.uniform(1.15,1.60),
        2
    )

    reorder_level = random.randint(20,150)

    status = random.choices(
        ["Active","Inactive","Discontinued"],
        weights=[85,10,5]
    )[0]

    created_date = fake.date_between(
        start_date="-2y",
        end_date="today"
    )

    products.append({

        "ProductID":product_id,

        "CategoryID":category_id,

        "ProductName":product_name,

        "Brand":brand,

        "SKU":sku,

        "CostPrice":cost_price,

        "SellingPrice":selling_price,

        "ReorderLevel":reorder_level,

        "ProductStatus":status,

        "CreatedDate":created_date

    })

# ============================================================
# EXPORT
# ============================================================

df = pd.DataFrame(products)

print("\n========== FIRST 10 PRODUCTS ==========\n")

print(df.head(10))

print("\n=======================================\n")

print("Total Products Generated :", len(df))

output_path = Path(
    r"C:\Users\user\Desktop\Helix\Dataset\Raw\products.csv"
)

df.to_csv(output_path,index=False)

print("\nproducts.csv exported successfully!")