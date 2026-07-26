"""
===========================================================
Project : Global Sales Intelligence Platform
Author  : Carine Kuimi
Purpose : Generate Master Data
===========================================================
"""

from generators.order_generator import generate_orders
from generators.order_item_generator import generate_order_items


def main():

    print("=" * 60)
    print("Generating Transaction Data")
    print("=" * 60)

    print("\n[Step 1/2] Generating Order Headers...")
    generate_orders()

    print("\n[Step 2/2] Generating Order Items...")
    generate_order_items()

    print("\n" + "=" * 60)
    print("\nTransaction data generated successfully.")
    print("=" * 60)


if __name__ == "__main__":
    main()
