"""
===========================================================
Project : Global Sales Intelligence Platform
Author  : Carine Kuimi
Purpose : Generate All Master Data
===========================================================
"""

from generators.region_generator import generate_regions
from generators.cost_center_generator import generate_cost_centers
from generators.profit_center_generator import generate_profit_centers
from generators.customer_generator import generate_customers
from generators.employee_generator import generate_employees
from generators.product_generator import generate_products


def main():
    print("=" * 60)
    print("Generating Master Data")
    print("=" * 60)

    # Organizational master data
    generate_regions()
    generate_cost_centers()
    generate_profit_centers()

    # Business master data
    generate_customers()
    generate_employees()
    generate_products()

    print("\nMaster data successfully generated.")


if __name__ == "__main__":
    main()