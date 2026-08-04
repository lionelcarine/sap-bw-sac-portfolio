"""
===========================================================
Project : Global Sales Intelligence Platform
Author  : Carine Kuimi
Purpose : Connect Python to the MySQL database
===========================================================
"""

import os
from pathlib import Path

import mysql.connector
from dotenv import load_dotenv
from mysql.connector import Error


# Racine du projet : sap-bw-sac-portfolio
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Charger les variables contenues dans .env
load_dotenv(PROJECT_ROOT / ".env")


def create_connection():
    """Create a connection to the global_sales database."""

    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT", "3306")),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
    )


def main():
    connection = None

    print("=" * 60)
    print("Testing MySQL connection")
    print("=" * 60)

    try:
        connection = create_connection()

        if connection.is_connected():
            cursor = connection.cursor()

            cursor.execute(
                "SELECT DATABASE(), CURRENT_USER(), VERSION();"
            )

            database, user, version = cursor.fetchone()

            print("MySQL connection successful.")
            print(f"Database : {database}")
            print(f"User     : {user}")
            print(f"Version  : {version}")

            cursor.close()

    except Error as error:
        print(f"MySQL connection failed: {error}")

    finally:
        if connection is not None and connection.is_connected():
            connection.close()
            print("MySQL connection closed.")


if __name__ == "__main__":
    main()