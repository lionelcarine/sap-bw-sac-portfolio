"""
===========================================================
Project : Global Sales Intelligence Platform
Author  : Carine Kuimi
Purpose : Generate Product Master Data
===========================================================
"""

import os
import random
import pandas as pd

from config import NUM_PRODUCTS, OUTPUT_FOLDER

# ----------------------------------------------------------
# Product Categories
# ----------------------------------------------------------

CATEGORIES = {

    "Electronics": [
        "Laptop",
        "Desktop PC",
        "Monitor",
        "Keyboard",
        "Mouse",
        "Printer",
        "Tablet",
        "Smartphone"
    ],

    "Furniture": [
        "Office Chair",
        "Desk",
        "Cabinet",
        "Bookshelf",
        "Conference Table"
    ],

    "Office Supplies": [
        "Notebook",
        "Paper",
        "Pen",
        "Folder",
        "Stapler"
    ],

    "Accessories": [
        "USB Cable",
        "Docking Station",
        "Headset",
        "Backpack",
        "Power Bank"
    ],

    "Software": [
        "ERP License",
        "CRM License",
        "Database License",
        "Security Suite",
        "Analytics Suite"
    ],

    "Services": [
        "Consulting",
        "Training",
        "Installation",
        "Support",
        "Cloud Migration"
    ]

}

# ----------------------------------------------------------
# Brands
# ----------------------------------------------------------

BRANDS = [

    "SAP",
    "Dell",
    "HP",
    "Lenovo",
    "Microsoft",
    "Apple",
    "Logitech",
    "Cisco",
    "Asus",
    "Samsung"

]

SUPPLIERS = [

    "Tech Solutions GmbH",
    "Global IT Distribution",
    "Business Systems AG",
    "Smart Office Europe",
    "Digital Warehouse Ltd",
    "NextGen Technologies",
    "EuroTech Supply"

]

PRODUCT_STATUS = [

    "Active",
    "Active",
    "Active",
    "Active",
    "Discontinued"

]


def generate_products():

    products = []

    product_id = 1

    while product_id <= NUM_PRODUCTS:

        category = random.choice(list(CATEGORIES.keys()))

        product_name = random.choice(CATEGORIES[category])

        brand = random.choice(BRANDS)

        cost = round(random.uniform(20, 900), 2)

        margin = random.uniform(1.20, 1.80)

        price = round(cost * margin, 2)

        product = {

            "Product_ID": product_id,

            "Product_Name": f"{brand} {product_name}",

            "Category": category,

            "Subcategory": product_name,

            "Brand": brand,

            "Unit_Cost": cost,

            "Standard_Price": price,

            "Supplier": random.choice(SUPPLIERS),

            "Product_Status": random.choice(PRODUCT_STATUS),

            "Profit_Center_ID": random.randint(1, 6)

        }

        products.append(product)

        product_id += 1

    df = pd.DataFrame(products)

    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    output_path = os.path.join(

        OUTPUT_FOLDER,

        "products.csv"

    )

    df.to_csv(

        output_path,

        index=False,

        encoding="utf-8"

    )

    print(f"{len(df)} products generated.")

    print(f"Saved to {output_path}")
