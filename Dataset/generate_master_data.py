from generators.employee_generator import generate_employees
from generators.customer_generator import generate_customers
from generators.product_generator import generate_products


def main():

    print("=" * 60)
    print("Generating Master Data")
    print("=" * 60)

    generate_employees()

    generate_customers()

    generate_products()

    print("\nMaster data generated successfully.")


if __name__ == "__main__":
    main()
