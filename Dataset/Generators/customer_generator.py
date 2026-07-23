"""
===========================================================
Project : Global Sales Intelligence Platform
Author  : Carine Kuimi
Purpose : Generate Customer Master Data
===========================================================
""" 

import os
import random

import pandas as pd
from faker import Faker

from config import NUM_CUSTOMERS, OUTPUT_FOLDER

fake = Faker()

# ----------------------------------------------------------
# Countries and Cities
# ----------------------------------------------------------

COUNTRIES = {
    "Germany": [
        "Berlin",
        "Munich",
        "Hamburg",
        "Cologne",
        "Frankfurt"
    ],
    "France": [
        "Paris",
        "Lyon",
        "Marseille"
    ],
    "Spain": [
        "Madrid",
        "Barcelona"
    ],
    "Italy": [
        "Milan",
        "Rome"
    ],
    "Netherlands": [
        "Amsterdam"
    ],
    "Belgium": [
        "Brussels"
    ],
    "Austria": [
        "Vienna"
    ],
    "Switzerland": [
        "Zurich"
    ]
}

# ----------------------------------------------------------
# Customer Types
# ----------------------------------------------------------

CUSTOMER_TYPES = [
    "Company",
    "Individual"
]

# ----------------------------------------------------------
# Customer Segments
# ----------------------------------------------------------

SEGMENTS = [
    "Consumer",
    "Corporate",
    "Small Business"
]

# ----------------------------------------------------------
# Industries
# ----------------------------------------------------------

INDUSTRIES = [
    "Retail",
    "Manufacturing",
    "IT",
    "Healthcare",
    "Finance",
    "Telecommunications",
    "Education",
    "Logistics"
]


def generate_customers():

    customers = []

    for customer_id in range(1, NUM_CUSTOMERS + 1):

        country = random.choice(list(COUNTRIES.keys()))

        city = random.choice(COUNTRIES[country])

        customer = {

            "Customer_ID": customer_id,

            "Customer_Name": fake.company(),

            "Customer_Type": random.choice(CUSTOMER_TYPES),

            "Industry": random.choice(INDUSTRIES),

            "Segment": random.choice(SEGMENTS),

            "Country": country,

            "City": city,

            "Postal_Code": fake.postcode(),

            "Registration_Date": fake.date_between(
                start_date="2022-01-01",
                end_date="2025-12-31"
            ),

            "Region_ID": random.randint(1, 20)

        }

        customers.append(customer)

    df = pd.DataFrame(customers)

    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    output_path = os.path.join(
        OUTPUT_FOLDER,
        "customers.csv"
    )

    df.to_csv(
        output_path,
        index=False,
        encoding="utf-8"
    )

    print(f"{len(df)} customers generated.")

    print(f"Saved to {output_path}")
