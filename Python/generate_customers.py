from faker import Faker
import random
import pandas as pd

# ------------------------------------------------------------------
# Initialize Faker
# ------------------------------------------------------------------

fake = Faker("en_IN")

# ------------------------------------------------------------------
# Configuration
# ------------------------------------------------------------------

NUMBER_OF_CUSTOMERS = 10

EMAIL_DOMAINS = [
    "gmail.com",
    "outlook.com",
    "yahoo.com",
    "icloud.com",
    "proton.me"
]

SEGMENTS = ["SEG001", "SEG002", "SEG003", "SEG004", "SEG005"]
SEGMENT_WEIGHTS = [45, 35, 15, 3, 2]

STATUS = [
    "Prospect",
    "Active",
    "Loyal",
    "Dormant",
    "Inactive",
    "Blocked"
]

STATUS_WEIGHTS = [45, 30, 10, 8, 5, 2]

# ------------------------------------------------------------------
# Generate Customer ID
# ------------------------------------------------------------------

def customer_id(number):
    return f"CUS{number:06d}"

# ------------------------------------------------------------------
# Customer List
# ------------------------------------------------------------------

customers = []

# ------------------------------------------------------------------
# Generate Customers
# ------------------------------------------------------------------

for i in range(1, NUMBER_OF_CUSTOMERS + 1):

    first_name = fake.first_name()
    last_name = fake.last_name()

    customer = {

        "CustomerID": customer_id(i),

        "SegmentID": random.choices(
            SEGMENTS,
            weights=SEGMENT_WEIGHTS
        )[0],

        "FirstName": first_name,

        "LastName": last_name,

        "Email": f"{first_name.lower()}.{last_name.lower()}{random.randint(100,999)}@{random.choice(EMAIL_DOMAINS)}",

        "Phone": f"{random.choice(['6','7','8','9'])}{random.randint(100000000,999999999)}",

        "DateOfBirth": fake.date_of_birth(
            minimum_age=18,
            maximum_age=65
        ),

        "Gender": random.choice(
            ["Male", "Female"]
        ),

        "RegistrationDate": fake.date_between(
            start_date="-3y",
            end_date="today"
        ),

        "Status": random.choices(
            STATUS,
            weights=STATUS_WEIGHTS
        )[0]

    }

    customers.append(customer)

# ------------------------------------------------------------------
# Create DataFrame
# ------------------------------------------------------------------

df = pd.DataFrame(customers)

# ------------------------------------------------------------------
# Display Output
# ------------------------------------------------------------------

print("\n========== FIRST 5 CUSTOMERS ==========\n")
print(df.head())

print("\n=======================================\n")

print(f"Total Customers Generated : {len(df)}")

# ------------------------------------------------------------------
# Export CSV
# ------------------------------------------------------------------

df.to_csv("customers.csv", index=False)

print("\ncustomers.csv exported successfully!")