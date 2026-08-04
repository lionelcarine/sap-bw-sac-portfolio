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