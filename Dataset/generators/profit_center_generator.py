"""
===========================================================
Project : Global Sales Intelligence Platform
Author  : Carine Kuimi
Purpose : Generate Profit Center Master Data
===========================================================
"""

import os
import pandas as pd

from config import OUTPUT_FOLDER


def generate_profit_centers():

    profit_centers = [

        {
            "Profit_Center_ID": 1,
            "Profit_Center_Name": "Consumer Electronics",
            "Business_Unit": "Electronics"
        },

        {
            "Profit_Center_ID": 2,
            "Profit_Center_Name": "Office Furniture",
            "Business_Unit": "Furniture"
        },

        {
            "Profit_Center_ID": 3,
            "Profit_Center_Name": "Office Supplies",
            "Business_Unit": "Office Supplies"
        },

        {
            "Profit_Center_ID": 4,
            "Profit_Center_Name": "Software Solutions",
            "Business_Unit": "Software"
        },

        {
            "Profit_Center_ID": 5,
            "Profit_Center_Name": "Professional Services",
            "Business_Unit": "Services"
        },

        {
            "Profit_Center_ID": 6,
            "Profit_Center_Name": "Accessories",
            "Business_Unit": "Accessories"
        }

    ]

    df = pd.DataFrame(profit_centers)

    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    output_path = os.path.join(
        OUTPUT_FOLDER,
        "profit_centers.csv"
    )

    df.to_csv(
        output_path,
        index=False,
        encoding="utf-8"
    )

    print(f"{len(df)} profit centers generated.")

    print(f"Saved to {output_path}")

if __name__ == "__main__":
    generate_profit_centers()