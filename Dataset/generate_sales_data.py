from generators.order_generator import generate_orders
from generators.order_item_generator import generate_order_items


def main():

    print("=" * 60)
    print("Generating Transaction Data")
    print("=" * 60)

    generate_orders()

    generate_order_items()

    print("\nTransaction data generated successfully.")


if __name__ == "__main__":
    main()
