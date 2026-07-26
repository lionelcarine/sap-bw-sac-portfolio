import os
import random
import pandas as pd

from config import OUTPUT_FOLDER

def generate_order_items():
    orders_path = os.path.join(OUTPUT_FOLDER, "orders.csv")
    products_path = os.path.join(OUTPUT_FOLDER, "products.csv")

    if not os.path.exists(orders_path) or not os.path.exists(products_path):
        print("Erreur : Veuillez générer d'abord les commandes et les produits !")
        return

    df_orders = pd.read_csv(orders_path)
    df_products = pd.read_csv(products_path)

    order_ids = df_orders["Order_ID"].tolist()
    products_pool = df_products.to_dict(orient="records")

    order_items = []
    item_id_counter = 1

    for order_id in order_ids:
        num_items = random.randint(1, 5)
        selected_products = random.sample(products_pool, min(num_items, len(products_pool)))

        for position_id, product in enumerate(selected_products, start=1):
            quantity = random.randint(1, 10)
            unit_cost = product["Unit_Cost"]
            standard_price = product["Standard_Price"]
            
            total_cost = round(unit_cost * quantity, 2)
            total_revenue = round(standard_price * quantity, 2)
            margin = round(total_revenue - total_cost, 2)

            order_items.append({
                "Order_Item_ID": item_id_counter,
                "Order_ID": order_id,
                "Line_Number": position_id,
                "Product_ID": product["Product_ID"],
                "Quantity": quantity,
                "Unit_Cost": unit_cost,
                "Unit_Price": standard_price,
                "Total_Cost": total_cost,
                "Total_Revenue": total_revenue,
                "Gross_Margin": margin
            })
            item_id_counter += 1

    df_items = pd.DataFrame(order_items)
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    output_path = os.path.join(OUTPUT_FOLDER, "order_items.csv")
    df_items.to_csv(output_path, index=False, encoding="utf-8")

    print(f"{len(df_items)} sales items generated successfully.")

