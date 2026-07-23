"""
===========================================================
Project : Global Sales Intelligence Platform
Author  : Carine Kuimi
Purpose : Generate Master Data
===========================================================
"""

from Generators.employee_generator import generate_employees
from Generators.customer_generator import generate_customers
from Generators.product_generator import generate_products


def main():

    print("=" * 60)
    print("Generating Master Data")
    print("=" * 60)

    generate_employees()
    generate_customers()
    generate_products()

    print("\nMaster Data successfully generated.")


if __name__ == "__main__":
    main()
