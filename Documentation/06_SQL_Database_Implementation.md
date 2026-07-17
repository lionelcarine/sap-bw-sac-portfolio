# 05 – SQL Database Implementation

---

# Project Information

| Item | Description |
|------|-------------|
| Project | Global Sales Intelligence Platform |
| Database | MySQL |
| Version | 1.0 |

---

# 1. Overview

Die relationale Datenbank simuliert das operative ERP-System der Global Sales Intelligence Platform.

Sie dient als Datenquelle für das spätere Data Warehouse.

Die Implementierung erfolgt in MySQL.

---

# 2. Database Architecture

Die Datenbank besteht aus folgenden Tabellen:

- CUSTOMERS
- PRODUCTS
- EMPLOYEES
- REGIONS
- COST_CENTERS
- PROFIT_CENTERS
- ORDERS
- ORDER_ITEMS

---

# 3. Datenmodell

Das relationale Datenmodell basiert auf folgenden Beziehungen:

CUSTOMERS (1) ----- (n) ORDERS

EMPLOYEES (1) ----- (n) ORDERS

ORDERS (1) ----- (n) ORDER_ITEMS

PRODUCTS (1) ----- (n) ORDER_ITEMS

REGIONS (1) ----- (n) CUSTOMERS

COST_CENTERS (1) ----- (n) EMPLOYEES

PROFIT_CENTERS (1) ----- (n) PRODUCTS

---

# 4. SQL Scripts

Die Implementierung erfolgt über folgende SQL-Dateien.

| Datei | Beschreibung |
|--------|--------------|
| create_tables.sql | Erstellt alle Tabellen |
| insert_data.sql | Fügt Testdaten ein |
| create_views.sql | Erstellt Analyse-Views |
| analytical_queries.sql | Enthält SQL-Analysen |

---

# 5. Database Constraints

Zur Sicherstellung der Datenqualität werden folgende Constraints verwendet.

- Primary Keys
- Foreign Keys
- NOT NULL
- UNIQUE
- CHECK Constraints

---

# 6. Indexing Strategy

Folgende Felder werden indiziert:

- Customer_ID
- Product_ID
- Order_ID
- Date
- Region_ID

Dies verbessert die Performance analytischer Abfragen.

---

# 7. Views

Zur Vereinfachung der Analyse werden SQL-Views erstellt.

Beispiele:

- vw_sales_summary
- vw_customer_sales
- vw_product_performance
- vw_regional_sales

---

# 8. Analytical Queries

Die Datenbank unterstützt unter anderem folgende Analysen.

- Umsatz nach Monat
- Umsatz nach Produkt
- Umsatz nach Region
- Top 10 Kunden
- Top Produkte
- Gewinnentwicklung
- Umsatzwachstum

---

# 9. Data Flow

ERP Tables

↓

SQL Database

↓

SAP BW/4HANA

↓

SAP Datasphere

↓

SAP Analytics Cloud

↓

Python Machine Learning

---

# Conclusion

Die relationale Datenbank bildet die Grundlage der gesamten Analytics-Plattform und stellt konsistente Daten für Reporting, Business Intelligence und Machine Learning bereit.
