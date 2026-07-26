"""
===========================================================
Project : Global Sales Intelligence Platform
Author  : Carine Kuimi
Purpose : Generate Master Data
===========================================================
"""

from generators.employee_generator import generate_employees
from generators.customer_generator import generate_customers
from generators.product_generator import generate_products
from generators.region_generator import generate_regions


def main():

    print("=" * 60)
    print("Generating Master Data")
    print("=" * 60)

    generate_employees()
    generate_customers()
    generate_products()
    generate_regions()

    print("\nMaster Data successfully generated.")
    


if __name__ == "__main__":
    main()
