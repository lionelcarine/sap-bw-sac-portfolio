"""
===========================================================
Project : Global Sales Intelligence Platform
Author  : Carine Kuimi
Purpose : Generate Region Master Data
===========================================================
"""

import os
import pandas as pd

from config import OUTPUT_FOLDER


def generate_regions():

    regions = [

        {"Region_ID": 1, "Country": "Germany", "Region": "Bavaria", "City": "Munich", "Sales_Area": "South Germany"},
        {"Region_ID": 2, "Country": "Germany", "Region": "Hesse", "City": "Frankfurt", "Sales_Area": "Central Germany"},
        {"Region_ID": 3, "Country": "Germany", "Region": "Berlin", "City": "Berlin", "Sales_Area": "East Germany"},
        {"Region_ID": 4, "Country": "Germany", "Region": "Hamburg", "City": "Hamburg", "Sales_Area": "North Germany"},

        {"Region_ID": 5, "Country": "France", "Region": "Île-de-France", "City": "Paris", "Sales_Area": "North France"},
        {"Region_ID": 6, "Country": "France", "Region": "Auvergne-Rhône-Alpes", "City": "Lyon", "Sales_Area": "South-East France"},

        {"Region_ID": 7, "Country": "Spain", "Region": "Madrid", "City": "Madrid", "Sales_Area": "Central Spain"},
        {"Region_ID": 8, "Country": "Spain", "Region": "Catalonia", "City": "Barcelona", "Sales_Area": "North-East Spain"},

        {"Region_ID": 9, "Country": "Italy", "Region": "Lombardy", "City": "Milan", "Sales_Area": "North Italy"},
        {"Region_ID": 10, "Country": "Italy", "Region": "Lazio", "City": "Rome", "Sales_Area": "Central Italy"},

        {"Region_ID": 11, "Country": "Netherlands", "Region": "North Holland", "City": "Amsterdam", "Sales_Area": "Netherlands"},

        {"Region_ID": 12, "Country": "Belgium", "Region": "Brussels", "City": "Brussels", "Sales_Area": "Belgium"},

        {"Region_ID": 13, "Country": "Austria", "Region": "Vienna", "City": "Vienna", "Sales_Area": "Austria"},

        {"Region_ID": 14, "Country": "Switzerland", "Region": "Zurich", "City": "Zurich", "Sales_Area": "North Switzerland"},
        {"Region_ID": 15, "Country": "Switzerland", "Region": "Geneva", "City": "Geneva", "Sales_Area": "West Switzerland"},

        {"Region_ID": 16, "Country": "Germany", "Region": "Saxony", "City": "Dresden", "Sales_Area": "East Germany"},
        {"Region_ID": 17, "Country": "France", "Region": "Provence", "City": "Marseille", "Sales_Area": "South France"},
        {"Region_ID": 18, "Country": "Italy", "Region": "Veneto", "City": "Venice", "Sales_Area": "North-East Italy"},
        {"Region_ID": 19, "Country": "Spain", "Region": "Valencia", "City": "Valencia", "Sales_Area": "East Spain"},
        {"Region_ID": 20, "Country": "Germany", "Region": "North Rhine-Westphalia", "City": "Cologne", "Sales_Area": "West Germany"}

    ]

    df = pd.DataFrame(regions)

    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    output_path = os.path.join(
        OUTPUT_FOLDER,
        "regions.csv"
    )

    df.to_csv(
        output_path,
        index=False,
        encoding="utf-8"
    )

    print(f"{len(df)} regions generated.")
    print(f"Saved to {output_path}")