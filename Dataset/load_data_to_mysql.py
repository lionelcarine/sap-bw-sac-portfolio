"""
===========================================================
Project : Global Sales Intelligence Platform
Author  : Carine Kuimi
Purpose : Load CSV data into MySQL
===========================================================
"""

import csv
import os
from pathlib import Path

import mysql.connector
from dotenv import load_dotenv
from mysql.connector import Error


# ----------------------------------------------------------
# Project paths
# ----------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_FOLDER = PROJECT_ROOT / "Dataset" / "output"

load_dotenv(PROJECT_ROOT / ".env")


# ----------------------------------------------------------
# MySQL connection
# ----------------------------------------------------------

def create_connection():
    """Create a connection to the global_sales database."""

    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT", "3306")),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
    )


# ----------------------------------------------------------
# Regions import
# ----------------------------------------------------------

def load_regions(connection):
    """Load regions.csv into the REGIONS table."""

    csv_path = OUTPUT_FOLDER / "regions.csv"

    if not csv_path.exists():
        raise FileNotFoundError(f"CSV file not found: {csv_path}")

    with csv_path.open(
        mode="r",
        encoding="utf-8-sig",
        newline=""
    ) as csv_file:

        reader = csv.DictReader(csv_file)

        expected_columns = [
            "Region_ID",
            "Country",
            "Region",
            "City",
            "Sales_Area",
        ]

        if reader.fieldnames != expected_columns:
            raise ValueError(
                "Invalid regions.csv columns.\n"
                f"Expected: {expected_columns}\n"
                f"Found: {reader.fieldnames}"
            )

        rows = [
            (
                int(row["Region_ID"]),
                row["Country"],
                row["Region"],
                row["City"],
                row["Sales_Area"],
            )
            for row in reader
        ]

    insert_query = """
        INSERT INTO REGIONS (
            Region_ID,
            Country,
            Region,
            City,
            Sales_Area
        )
        VALUES (%s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
            Country = VALUES(Country),
            Region = VALUES(Region),
            City = VALUES(City),
            Sales_Area = VALUES(Sales_Area);
    """

    cursor = connection.cursor()

    try:
        cursor.executemany(insert_query, rows)

        cursor.execute("SELECT COUNT(*) FROM REGIONS;")
        database_count = cursor.fetchone()[0]

        print(f"{len(rows)} regions read from CSV.")
        print(f"{database_count} regions available in MySQL.")

    finally:
        cursor.close()


# ----------------------------------------------------------
# Cost centers import
# ----------------------------------------------------------

def load_cost_centers(connection):
    """Load cost_centers.csv into the COST_CENTERS table."""

    csv_path = OUTPUT_FOLDER / "cost_centers.csv"

    if not csv_path.exists():
        raise FileNotFoundError(f"CSV file not found: {csv_path}")

    with csv_path.open(
        mode="r",
        encoding="utf-8-sig",
        newline=""
    ) as csv_file:

        reader = csv.DictReader(csv_file)

        expected_columns = [
            "Cost_Center_ID",
            "Cost_Center_Name",
            "Department",
            "Budget",
        ]

        if reader.fieldnames != expected_columns:
            raise ValueError(
                "Invalid cost_centers.csv columns.\n"
                f"Expected: {expected_columns}\n"
                f"Found: {reader.fieldnames}"
            )

        rows = [
            (
                int(row["Cost_Center_ID"]),
                row["Cost_Center_Name"],
                row["Department"],
                row["Budget"],
            )
            for row in reader
        ]

    insert_query = """
        INSERT INTO COST_CENTERS (
            Cost_Center_ID,
            Cost_Center_Name,
            Department,
            Budget
        )
        VALUES (%s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
            Cost_Center_Name = VALUES(Cost_Center_Name),
            Department = VALUES(Department),
            Budget = VALUES(Budget);
    """

    cursor = connection.cursor()

    try:
        cursor.executemany(insert_query, rows)

        cursor.execute("SELECT COUNT(*) FROM COST_CENTERS;")
        database_count = cursor.fetchone()[0]

        print(f"{len(rows)} cost centers read from CSV.")
        print(f"{database_count} cost centers available in MySQL.")

    finally:
        cursor.close()


# ----------------------------------------------------------
# Profit centers import
# ----------------------------------------------------------

def load_profit_centers(connection):
    """Load profit_centers.csv into the PROFIT_CENTERS table."""

    csv_path = OUTPUT_FOLDER / "profit_centers.csv"

    if not csv_path.exists():
        raise FileNotFoundError(f"CSV file not found: {csv_path}")

    with csv_path.open(
        mode="r",
        encoding="utf-8-sig",
        newline=""
    ) as csv_file:

        reader = csv.DictReader(csv_file)

        expected_columns = [
            "Profit_Center_ID",
            "Profit_Center_Name",
            "Business_Unit",
        ]

        if reader.fieldnames != expected_columns:
            raise ValueError(
                "Invalid profit_centers.csv columns.\n"
                f"Expected: {expected_columns}\n"
                f"Found: {reader.fieldnames}"
            )

        rows = [
            (
                int(row["Profit_Center_ID"]),
                row["Profit_Center_Name"],
                row["Business_Unit"],
            )
            for row in reader
        ]

    insert_query = """
        INSERT INTO PROFIT_CENTERS (
            Profit_Center_ID,
            Profit_Center_Name,
            Business_Unit
        )
        VALUES (%s, %s, %s)
        ON DUPLICATE KEY UPDATE
            Profit_Center_Name = VALUES(Profit_Center_Name),
            Business_Unit = VALUES(Business_Unit);
    """

    cursor = connection.cursor()

    try:
        cursor.executemany(insert_query, rows)

        cursor.execute("SELECT COUNT(*) FROM PROFIT_CENTERS;")
        database_count = cursor.fetchone()[0]

        print(f"{len(rows)} profit centers read from CSV.")
        print(f"{database_count} profit centers available in MySQL.")

    finally:
        cursor.close()

# ----------------------------------------------------------
# Customers import
# ----------------------------------------------------------

def load_customers(connection):
    """Load customers.csv into the CUSTOMERS table."""

    csv_path = OUTPUT_FOLDER / "customers.csv"

    if not csv_path.exists():
        raise FileNotFoundError(f"CSV file not found: {csv_path}")

    with csv_path.open(
        mode="r",
        encoding="utf-8-sig",
        newline=""
    ) as csv_file:

        reader = csv.DictReader(csv_file)

        expected_columns = [
            "Customer_ID",
            "Customer_Name",
            "Customer_Type",
            "Industry",
            "Segment",
            "Country",
            "City",
            "Postal_Code",
            "Registration_Date",
            "Region_ID",
        ]

        if reader.fieldnames != expected_columns:
            raise ValueError(
                "Invalid customers.csv columns.\n"
                f"Expected: {expected_columns}\n"
                f"Found: {reader.fieldnames}"
            )

        rows = [
            (
                int(row["Customer_ID"]),
                row["Customer_Name"],
                row["Customer_Type"],
                row["Industry"] or None,
                row["Segment"],
                row["Country"],
                row["City"],
                row["Postal_Code"] or None,
                row["Registration_Date"],
                int(row["Region_ID"]),
            )
            for row in reader
        ]

    insert_query = """
        INSERT INTO CUSTOMERS (
            Customer_ID,
            Customer_Name,
            Customer_Type,
            Industry,
            Segment,
            Country,
            City,
            Postal_Code,
            Registration_Date,
            Region_ID
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
            Customer_Name = VALUES(Customer_Name),
            Customer_Type = VALUES(Customer_Type),
            Industry = VALUES(Industry),
            Segment = VALUES(Segment),
            Country = VALUES(Country),
            City = VALUES(City),
            Postal_Code = VALUES(Postal_Code),
            Registration_Date = VALUES(Registration_Date),
            Region_ID = VALUES(Region_ID);
    """

    cursor = connection.cursor()

    try:
        cursor.executemany(insert_query, rows)

        cursor.execute("SELECT COUNT(*) FROM CUSTOMERS;")
        database_count = cursor.fetchone()[0]

        print(f"{len(rows)} customers read from CSV.")
        print(f"{database_count} customers available in MySQL.")

    finally:
        cursor.close()

# ----------------------------------------------------------
# Employees import
# ----------------------------------------------------------

def load_employees(connection):
    """Load employees.csv into the EMPLOYEES table."""

    csv_path = OUTPUT_FOLDER / "employees.csv"

    if not csv_path.exists():
        raise FileNotFoundError(f"CSV file not found: {csv_path}")

    with csv_path.open(
        mode="r",
        encoding="utf-8-sig",
        newline=""
    ) as csv_file:

        reader = csv.DictReader(csv_file)

        expected_columns = [
            "Employee_ID",
            "Employee_Name",
            "Department",
            "Position",
            "Manager",
            "Hire_Date",
            "Cost_Center_ID",
        ]

        if reader.fieldnames != expected_columns:
            raise ValueError(
                "Invalid employees.csv columns.\n"
                f"Expected: {expected_columns}\n"
                f"Found: {reader.fieldnames}"
            )

        rows = [
            (
                int(row["Employee_ID"]),
                row["Employee_Name"],
                row["Department"],
                row["Position"],
                row["Manager"] or None,
                row["Hire_Date"],
                int(row["Cost_Center_ID"]),
            )
            for row in reader
        ]

    insert_query = """
        INSERT INTO EMPLOYEES (
            Employee_ID,
            Employee_Name,
            Department,
            Position,
            Manager,
            Hire_Date,
            Cost_Center_ID
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
            Employee_Name = VALUES(Employee_Name),
            Department = VALUES(Department),
            Position = VALUES(Position),
            Manager = VALUES(Manager),
            Hire_Date = VALUES(Hire_Date),
            Cost_Center_ID = VALUES(Cost_Center_ID);
    """

    cursor = connection.cursor()

    try:
        cursor.executemany(insert_query, rows)

        cursor.execute("SELECT COUNT(*) FROM EMPLOYEES;")
        database_count = cursor.fetchone()[0]

        print(f"{len(rows)} employees read from CSV.")
        print(f"{database_count} employees available in MySQL.")

    finally:
        cursor.close()


# ----------------------------------------------------------
# Products import
# ----------------------------------------------------------

def load_products(connection):
    """Load products.csv into the PRODUCTS table."""

    csv_path = OUTPUT_FOLDER / "products.csv"

    if not csv_path.exists():
        raise FileNotFoundError(f"CSV file not found: {csv_path}")

    with csv_path.open(
        mode="r",
        encoding="utf-8-sig",
        newline=""
    ) as csv_file:

        reader = csv.DictReader(csv_file)

        expected_columns = [
            "Product_ID",
            "Product_Name",
            "Category",
            "Subcategory",
            "Brand",
            "Unit_Cost",
            "Standard_Price",
            "Supplier",
            "Product_Status",
            "Profit_Center_ID",
        ]

        if reader.fieldnames != expected_columns:
            raise ValueError(
                "Invalid products.csv columns.\n"
                f"Expected: {expected_columns}\n"
                f"Found: {reader.fieldnames}"
            )

        rows = [
            (
                int(row["Product_ID"]),
                row["Product_Name"],
                row["Category"],
                row["Subcategory"],
                row["Brand"] or None,
                row["Unit_Cost"],
                row["Standard_Price"],
                row["Supplier"] or None,
                row["Product_Status"],
                int(row["Profit_Center_ID"]),
            )
            for row in reader
        ]

    insert_query = """
        INSERT INTO PRODUCTS (
            Product_ID,
            Product_Name,
            Category,
            Subcategory,
            Brand,
            Unit_Cost,
            Standard_Price,
            Supplier,
            Product_Status,
            Profit_Center_ID
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
            Product_Name = VALUES(Product_Name),
            Category = VALUES(Category),
            Subcategory = VALUES(Subcategory),
            Brand = VALUES(Brand),
            Unit_Cost = VALUES(Unit_Cost),
            Standard_Price = VALUES(Standard_Price),
            Supplier = VALUES(Supplier),
            Product_Status = VALUES(Product_Status),
            Profit_Center_ID = VALUES(Profit_Center_ID);
    """

    cursor = connection.cursor()

    try:
        cursor.executemany(insert_query, rows)

        cursor.execute("SELECT COUNT(*) FROM PRODUCTS;")
        database_count = cursor.fetchone()[0]

        print(f"{len(rows)} products read from CSV.")
        print(f"{database_count} products available in MySQL.")

    finally:
        cursor.close()

# ----------------------------------------------------------
# Orders import
# ----------------------------------------------------------

def load_orders(connection):
    """Load orders.csv into the ORDERS table."""

    csv_path = OUTPUT_FOLDER / "orders.csv"

    if not csv_path.exists():
        raise FileNotFoundError(f"CSV file not found: {csv_path}")

    with csv_path.open(
        mode="r",
        encoding="utf-8-sig",
        newline=""
    ) as csv_file:

        reader = csv.DictReader(csv_file)

        expected_columns = [
            "Order_ID",
            "Customer_ID",
            "Employee_ID",
            "Order_Date",
            "Order_Status",
            "Payment_Method",
        ]

        if reader.fieldnames != expected_columns:
            raise ValueError(
                "Invalid orders.csv columns.\n"
                f"Expected: {expected_columns}\n"
                f"Found: {reader.fieldnames}"
            )

        rows = [
            (
                int(row["Order_ID"]),
                int(row["Customer_ID"]),
                int(row["Employee_ID"]),
                row["Order_Date"],
                None,
                row["Order_Status"],
                row["Payment_Method"],
            )
            for row in reader
        ]

    insert_query = """
        INSERT INTO ORDERS (
            Order_ID,
            Customer_ID,
            Employee_ID,
            Order_Date,
            Delivery_Date,
            Order_Status,
            Payment_Method
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
            Customer_ID = VALUES(Customer_ID),
            Employee_ID = VALUES(Employee_ID),
            Order_Date = VALUES(Order_Date),
            Delivery_Date = VALUES(Delivery_Date),
            Order_Status = VALUES(Order_Status),
            Payment_Method = VALUES(Payment_Method);
    """

    cursor = connection.cursor()

    try:
        cursor.executemany(insert_query, rows)

        cursor.execute("SELECT COUNT(*) FROM ORDERS;")
        database_count = cursor.fetchone()[0]

        print(f"{len(rows)} orders read from CSV.")
        print(f"{database_count} orders available in MySQL.")

    finally:
        cursor.close()


# ----------------------------------------------------------
# Main program
# ----------------------------------------------------------

def main():
    connection = None

    print("=" * 60)
    print("Loading CSV Data into MySQL")
    print("=" * 60)

    try:
        connection = create_connection()

        print("MySQL connection successful.")

        load_regions(connection)
        load_cost_centers(connection)
        load_profit_centers(connection)
        load_customers(connection)
        load_employees(connection)
        load_products(connection)
        load_orders(connection)

        connection.commit()

        print("Organizational master data imported successfully.")

    except (Error, OSError, ValueError) as error:
        if connection is not None and connection.is_connected():
            connection.rollback()

        print(f"Import failed: {error}")
        raise SystemExit(1) from error

    finally:
        if connection is not None and connection.is_connected():
            connection.close()
            print("MySQL connection closed.")


if __name__ == "__main__":
    main()