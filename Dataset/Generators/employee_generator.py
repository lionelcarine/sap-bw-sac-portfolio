"""
===========================================================
Project : Global Sales Intelligence Platform
Author  : Carine Kuimi
Purpose : Generate Employee Master Data
===========================================================
"""

import os
import random
from datetime import date, timedelta
import pandas as pd
from faker import Faker

from config import NUM_EMPLOYEES, OUTPUT_FOLDER

fake = Faker()

DEPARTMENTS = [
    "Sales",
    "Marketing",
    "Finance",
    "IT",
    "Operations",
    "HR",
    "Supply Chain",
    "Customer Service"
]

POSITIONS = {
    "Sales": [
        "Sales Manager",
        "Sales Representative",
        "Account Manager"
    ],
    "Marketing": [
        "Marketing Specialist",
        "Marketing Manager"
    ],
    "Finance": [
        "Financial Analyst",
        "Controller"
    ],
    "IT": [
        "Data Analyst",
        "Data Engineer",
        "BI Developer",
        "System Administrator"
    ],
    "Operations": [
        "Operations Manager",
        "Operations Specialist"
    ],
    "HR": [
        "HR Specialist",
        "HR Manager"
    ],
    "Supply Chain": [
        "Supply Chain Analyst",
        "Logistics Coordinator"
    ],
    "Customer Service": [
        "Customer Support Specialist"
    ]
}


def generate_employees():

    employees = []

    for employee_id in range(1, NUM_EMPLOYEES + 1):

        department = random.choice(DEPARTMENTS)
        position = random.choice(POSITIONS[department])

        employees.append({
            "Employee_ID": employee_id,
            "Employee_Name": fake.name(),
            "Department": department,
            "Position": position,
            "Manager": fake.name(),
            "Hire_Date": fake.date_between(
                start_date=date.today() - timedelta(days=3650),  
                end_date=date.today()
            ),
            "Cost_Center_ID": random.randint(1,8)
        })

    df = pd.DataFrame(employees)

    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    output_path = os.path.join(
        OUTPUT_FOLDER,
        "employees.csv"
    )

    df.to_csv(
        output_path,
        index=False
    )

    print(f"{len(df)} employees generated.")
    print(f"Saved to {output_path}")


if __name__ == "__main__":
    generate_employees()