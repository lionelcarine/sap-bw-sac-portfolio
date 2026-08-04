"""
===========================================================
Project : Global Sales Intelligence Platform
Author  : Carine Kuimi
Purpose : Generate Cost Center Master Data
===========================================================
"""

import os
import pandas as pd

from config import OUTPUT_FOLDER


def generate_cost_centers():

    cost_centers = [

        {
            "Cost_Center_ID": 1,
            "Cost_Center_Name": "Sales Germany",
            "Department": "Sales",
            "Budget": 500000
        },

        {
            "Cost_Center_ID": 2,
            "Cost_Center_Name": "Marketing Europe",
            "Department": "Marketing",
            "Budget": 350000
        },

        {
            "Cost_Center_ID": 3,
            "Cost_Center_Name": "Finance",
            "Department": "Finance",
            "Budget": 250000
        },

        {
            "Cost_Center_ID": 4,
            "Cost_Center_Name": "IT Services",
            "Department": "IT",
            "Budget": 600000
        },

        {
            "Cost_Center_ID": 5,
            "Cost_Center_Name": "Human Resources",
            "Department": "HR",
            "Budget": 180000
        },

        {
            "Cost_Center_ID": 6,
            "Cost_Center_Name": "Supply Chain",
            "Department": "Operations",
            "Budget": 450000
        },

        {
            "Cost_Center_ID": 7,
            "Cost_Center_Name": "Customer Service",
            "Department": "Support",
            "Budget": 220000
        },

        {
            "Cost_Center_ID": 8,
            "Cost_Center_Name": "Corporate Management",
            "Department": "Management",
            "Budget": 800000
        }

    ]

    df = pd.DataFrame(cost_centers)

    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    output_path = os.path.join(
        OUTPUT_FOLDER,
        "cost_centers.csv"
    )

    df.to_csv(
        output_path,
        index=False,
        encoding="utf-8"
    )

    print(f"{len(df)} cost centers generated.")

    print(f"Saved to {output_path}")