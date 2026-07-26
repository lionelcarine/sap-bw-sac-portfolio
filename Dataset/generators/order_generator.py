import os
import random
import pandas as pd
from faker import Faker

from config import NUM_ORDERS, OUTPUT_FOLDER

fake = Faker()

ORDER_STATUS = ["Completed", "Completed", "Completed", "Cancelled", "In Progress"]
PAYMENT_METHODS = ["Credit Card", "Bank Transfer", "PayPal", "Invoice"]

def generate_orders():
    customers_path = os.path.join(OUTPUT_FOLDER, "customers.csv")
    employees_path = os.path.join(OUTPUT_FOLDER, "employees.csv")

    if not os.path.exists(customers_path) or not os.path.exists(employees_path):
        print("Erreur : Générez d'abord les clients et les employés !")
        return

    df_cust = pd.read_csv(customers_path)
    df_emp = pd.read_csv(employees_path)

    customer_ids = df_cust["Customer_ID"].tolist()
    sales_emp_ids = df_emp[df_emp["Department"] == "Sales"]["Employee_ID"].tolist()
    
    if not sales_emp_ids:
        sales_emp_ids = df_emp["Employee_ID"].tolist()

    orders = []

    for order_id in range(100001, 100001 + NUM_ORDERS):
        orders.append({
            "Order_ID": order_id,
            "Customer_ID": random.choice(customer_ids),
            "Employee_ID": random.choice(sales_emp_ids),
            "Order_Date": fake.date_between(start_date="-3y", end_date="today"),
            "Order_Status": random.choice(ORDER_STATUS),
            "Payment_Method": random.choice(PAYMENT_METHODS)
        })

    df_orders = pd.DataFrame(orders)
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    output_path = os.path.join(OUTPUT_FOLDER, "orders.csv")
    df_orders.to_csv(output_path, index=False, encoding="utf-8")

    print(f"{len(df_orders)} orders generated.")

