# 02 – ERP Data ModelERP Data Model

---

# Project Information

| Item | Description |
|------|-------------|
| Project | Global Sales Intelligence Platform |
| Company | Global Retail Group (GRG) |
| Industry | Retail & Consumer Goods |
| Author | Carine Kuimi |
| Version | 1.0 |
| Status | In Progress |

---

# 1. Überblick

Das Quellsystem der **Global Sales Intelligence Platform** ist ein simuliertes SAP S/4HANA ERP-System.

Das ERP-System speichert sämtliche operativen Geschäftsprozesse des Unternehmens. Es enthält sowohl **Stammdaten (Master Data)** als auch **Bewegungsdaten (Transactional Data)**.

Diese Daten dienen als Ausgangspunkt für den späteren ETL-Prozess und werden anschließend in das Data Warehouse (SAP BW/4HANA) sowie in SAP Datasphere und SAP Analytics Cloud übertragen.

---

# 2. Geschäftsprozess

Der Geschäftsprozess des Unternehmens lässt sich wie folgt darstellen:

```text
Kunde

↓

Bestellung

↓

Auftragspositionen

↓

Lieferung

↓

Rechnung

↓

Umsatz
```

Jede Bestellung wird einem Kunden zugeordnet und kann mehrere Produkte enthalten.

Die Verkaufsdaten werden später für Reporting, KPI-Berechnungen und Predictive Analytics verwendet.

---

# 3. ERP-Datenmodell

Das ERP-System besteht aus zwei Arten von Daten.

## Stammdaten (Master Data)

Diese Tabellen enthalten Informationen, die sich nur selten ändern.

- Customers
- Products
- Employees
- Regions
- Cost_Centers
- Profit_Centers

## Bewegungsdaten (Transactional Data)

Diese Tabellen enthalten die täglichen Geschäftsprozesse.

- Orders
- Order_Items

---

# 4. ERP-Tabellen

| Tabelle | Beschreibung |
|----------|--------------|
| Customers | Kundendaten |
| Products | Produktstammdaten |
| Employees | Vertriebsmitarbeiter |
| Regions | Vertriebsregionen |
| Cost_Centers | Kostenstellen |
| Profit_Centers | Profit Center |
| Orders | Verkaufsaufträge |
| Order_Items | Positionen eines Verkaufsauftrags |

---

# 5. Entity Relationship Overview

```text
                    CUSTOMERS
                         │
                         │
                   ┌─────┴─────┐
                   │  ORDERS   │
                   └─────┬─────┘
                         │
                    ORDER_ITEMS
                  ┌──────┼──────┐
                  │      │      │
             PRODUCTS EMPLOYEES REGIONS

          COST_CENTERS

          PROFIT_CENTERS
```

---

# 6. Ziel des ERP-Datenmodells

Das ERP-Datenmodell bildet die operative Grundlage der Global Sales Intelligence Platform.

Im nächsten Projektschritt werden die Daten in ein analytisches Star Schema transformiert, welches anschließend in SAP BW/4HANA implementiert wird.



---

# 7. Tabellenbeschreibung

## 7.1 CUSTOMERS

### Beschreibung

Die Tabelle **CUSTOMERS** enthält alle Stammdaten der Kunden.

Jeder Kunde besitzt eine eindeutige Customer_ID und kann mehrere Bestellungen aufgeben.

---

### Primärschlüssel

- Customer_ID

---

### Attribute

| Feld | Datentyp | Beschreibung |
|------|----------|--------------|
| Customer_ID | INTEGER | Eindeutige Kundennummer |
| Customer_Name | VARCHAR(100) | Kundenname |
| Customer_Type | VARCHAR(20) | B2B oder B2C |
| Industry | VARCHAR(50) | Branche |
| Segment | VARCHAR(30) | Kundensegment |
| Country | VARCHAR(50) | Land |
| City | VARCHAR(50) | Stadt |
| Postal_Code | VARCHAR(15) | Postleitzahl |
| Registration_Date | DATE | Registrierungsdatum |

---

### Beziehungen

Eine Customer_ID kann mehreren Bestellungen zugeordnet werden.

Relationship:

CUSTOMERS (1) -------- (n) ORDERS

---

### Business Rules

- Jeder Kunde besitzt genau eine Customer_ID.
- Ein Kunde kann mehrere Bestellungen aufgeben.
- Ein Kunde gehört genau einem Land.
- Jeder Kunde besitzt genau ein Kundensegment.



---

## 7.2 PRODUCTS

### Beschreibung

Die Tabelle **PRODUCTS** enthält alle Stammdaten der im Unternehmen angebotenen Produkte.

Jedes Produkt besitzt eine eindeutige Produktnummer und gehört genau einer Kategorie sowie einer Unterkategorie an.

---

### Primärschlüssel

- Product_ID

---

### Attribute

| Feld | Datentyp | Beschreibung |
|------|----------|--------------|
| Product_ID | INTEGER | Eindeutige Produktnummer |
| Product_Name | VARCHAR(100) | Produktname |
| Category | VARCHAR(50) | Produktkategorie |
| Subcategory | VARCHAR(50) | Unterkategorie |
| Brand | VARCHAR(50) | Marke |
| Unit_Cost | DECIMAL(10,2) | Einkaufspreis |
| Standard_Price | DECIMAL(10,2) | Standardverkaufspreis |
| Supplier | VARCHAR(100) | Lieferant |
| Product_Status | VARCHAR(20) | Aktiv oder Inaktiv |

---

### Beziehungen

Ein Produkt kann in mehreren Bestellungen vorkommen.

Relationship:

PRODUCTS (1) -------- (n) ORDER_ITEMS

---

### Business Rules

- Jedes Produkt besitzt genau eine Product_ID.
- Ein Produkt gehört genau einer Kategorie an.
- Ein Produkt besitzt genau einen Standardpreis.
- Inaktive Produkte können nicht neu verkauft werden.



---

## 7.3 EMPLOYEES

### Beschreibung

Die Tabelle **EMPLOYEES** enthält die Stammdaten aller Vertriebsmitarbeiter.

Jeder Verkaufsauftrag wird genau einem Mitarbeiter zugeordnet.

---

### Primärschlüssel

- Employee_ID

---

### Attribute

| Feld | Datentyp | Beschreibung |
|------|----------|--------------|
| Employee_ID | INTEGER | Mitarbeiter-ID |
| Employee_Name | VARCHAR(100) | Name |
| Department | VARCHAR(50) | Abteilung |
| Position | VARCHAR(50) | Position |
| Manager | VARCHAR(100) | Vorgesetzter |
| Hire_Date | DATE | Eintrittsdatum |

---

### Beziehungen

EMPLOYEES (1) -------- (n) ORDERS

---

### Business Rules

- Jeder Mitarbeiter besitzt eine eindeutige Employee_ID.
- Jeder Auftrag wird genau einem Mitarbeiter zugeordnet.



---

## 7.4 REGIONS

### Beschreibung

Die Tabelle **REGIONS** enthält geografische Informationen über die Vertriebsgebiete.

---

### Primärschlüssel

- Region_ID

---

### Attribute

| Feld | Datentyp | Beschreibung |
|------|----------|--------------|
| Region_ID | INTEGER | Regions-ID |
| Country | VARCHAR(50) | Land |
| Region | VARCHAR(50) | Bundesland / Region |
| City | VARCHAR(50) | Stadt |
| Sales_Area | VARCHAR(50) | Vertriebsgebiet |

---

### Beziehungen

REGIONS (1) -------- (n) CUSTOMERS

---

### Business Rules

- Jede Region besitzt eine eindeutige Region_ID.
- Jeder Kunde gehört genau einer Region an.



---

## 7.5 COST_CENTERS

### Beschreibung

Die Tabelle **COST_CENTERS** enthält Informationen über die Kostenstellen des Unternehmens.

---

### Primärschlüssel

- Cost_Center_ID

---

### Attribute

| Feld | Datentyp | Beschreibung |
|------|----------|--------------|
| Cost_Center_ID | INTEGER | Kostenstellen-ID |
| Cost_Center_Name | VARCHAR(100) | Name |
| Department | VARCHAR(50) | Abteilung |
| Budget | DECIMAL(12,2) | Jahresbudget |

---

### Beziehungen

COST_CENTERS (1) -------- (n) EMPLOYEES

---

### Business Rules

- Jede Kostenstelle besitzt eine eindeutige ID.
- Jeder Mitarbeiter gehört genau einer Kostenstelle an.



---

## 7.6 PROFIT_CENTERS

### Beschreibung

Die Tabelle **PROFIT_CENTERS** enthält die organisatorischen Profit Center des Unternehmens.

---

### Primärschlüssel

- Profit_Center_ID

---

### Attribute

| Feld | Datentyp | Beschreibung |
|------|----------|--------------|
| Profit_Center_ID | INTEGER | Profit Center-ID |
| Profit_Center_Name | VARCHAR(100) | Bezeichnung |
| Business_Unit | VARCHAR(50) | Geschäftsbereich |

---

### Beziehungen

PROFIT_CENTERS (1) -------- (n) PRODUCTS

---

### Business Rules

- Jedes Produkt ist genau einem Profit Center zugeordnet.
- Ein Profit Center kann mehrere Produkte enthalten.



---

## 7.7 ORDERS

### Beschreibung

Die Tabelle **ORDERS** enthält alle Verkaufsaufträge.

Ein Auftrag wird von einem Kunden erstellt und durch einen Vertriebsmitarbeiter bearbeitet.

---

### Primärschlüssel

- Order_ID

---

### Fremdschlüssel

- Customer_ID
- Employee_ID

---

### Attribute

| Feld | Datentyp | Beschreibung |
|------|----------|--------------|
| Order_ID | INTEGER | Auftragsnummer |
| Customer_ID | INTEGER | Kunde |
| Employee_ID | INTEGER | Vertriebsmitarbeiter |
| Order_Date | DATE | Bestelldatum |
| Delivery_Date | DATE | Lieferdatum |
| Order_Status | VARCHAR(30) | Status |
| Payment_Method | VARCHAR(30) | Zahlungsmethode |

---

### Beziehungen

CUSTOMERS (1) -------- (n) ORDERS

EMPLOYEES (1) -------- (n) ORDERS

ORDERS (1) -------- (n) ORDER_ITEMS

---

### Business Rules

- Jeder Auftrag gehört genau einem Kunden.
- Jeder Auftrag besitzt mindestens eine Auftragsposition.
- Jeder Auftrag wird genau einem Mitarbeiter zugeordnet.



---

## 7.8 ORDER_ITEMS

### Beschreibung

Die Tabelle **ORDER_ITEMS** enthält die einzelnen Positionen eines Verkaufsauftrags.

Jede Position beschreibt genau ein verkauftes Produkt.

---

### Primärschlüssel

- Order_Item_ID

---

### Fremdschlüssel

- Order_ID
- Product_ID

---

### Attribute

| Feld | Datentyp | Beschreibung |
|------|----------|--------------|
| Order_Item_ID | INTEGER | Positionsnummer |
| Order_ID | INTEGER | Auftrag |
| Product_ID | INTEGER | Produkt |
| Quantity | INTEGER | Verkaufsmenge |
| Unit_Price | DECIMAL(10,2) | Verkaufspreis |
| Discount | DECIMAL(5,2) | Rabatt in % |
| Revenue | DECIMAL(12,2) | Umsatz |
| Cost | DECIMAL(12,2) | Kosten |
| Profit | DECIMAL(12,2) | Gewinn |

---

### Beziehungen

ORDERS (1) -------- (n) ORDER_ITEMS

PRODUCTS (1) -------- (n) ORDER_ITEMS

---

### Business Rules

- Jede Position gehört genau einem Auftrag.
- Jede Position beschreibt genau ein Produkt.
- Revenue = Quantity × Unit_Price × (1 − Discount).
- Profit = Revenue − Cost.
