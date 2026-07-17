# 04 – Data Dictionary

---

# Project Information

| Item | Description |
|------|-------------|
| Project | Global Sales Intelligence Platform |
| Company | Global Retail Group (GRG) |
| Author | Carine Kuimi |
| Technology | SAP BW/4HANA |
| Version | 1.0 |

---

# 1. Purpose

Dieses Dokument beschreibt sämtliche Tabellen und Attribute der Global Sales Intelligence Platform.

Das Data Dictionary dient als zentrale Referenz für:

- Data Engineers
- SAP BW Consultants
- SAP Datasphere Consultants
- SAP Analytics Cloud Entwickler
- Business Analysten

Es dokumentiert Datentypen, Geschäftsdefinitionen und Validierungsregeln aller Tabellen.

---

# 2. ERP Tables

## 2.1 CUSTOMERS

| Feld | Datentyp | Pflichtfeld | Beschreibung |
|------|----------|-------------|--------------|
| Customer_ID | INTEGER | Ja | Eindeutige Kundennummer |
| Customer_Name | VARCHAR(100) | Ja | Kundenname |
| Customer_Type | VARCHAR(20) | Ja | B2B oder B2C |
| Industry | VARCHAR(50) | Nein | Branche |
| Segment | VARCHAR(30) | Ja | Kundensegment |
| Country | VARCHAR(50) | Ja | Land |
| City | VARCHAR(50) | Ja | Stadt |
| Postal_Code | VARCHAR(15) | Nein | Postleitzahl |
| Registration_Date | DATE | Ja | Registrierungsdatum |

---

## 2.2 PRODUCTS

| Feld | Datentyp | Pflichtfeld | Beschreibung |
|------|----------|-------------|--------------|
| Product_ID | INTEGER | Ja | Produktnummer |
| Product_Name | VARCHAR(100) | Ja | Produktname |
| Category | VARCHAR(50) | Ja | Produktkategorie |
| Subcategory | VARCHAR(50) | Ja | Unterkategorie |
| Brand | VARCHAR(50) | Nein | Marke |
| Unit_Cost | DECIMAL(10,2) | Ja | Einkaufspreis |
| Standard_Price | DECIMAL(10,2) | Ja | Verkaufspreis |
| Supplier | VARCHAR(100) | Nein | Lieferant |
| Product_Status | VARCHAR(20) | Ja | Aktiv oder Inaktiv |

---

## 2.3 EMPLOYEES

| Feld | Datentyp | Pflichtfeld | Beschreibung |
|------|----------|-------------|--------------|
| Employee_ID | INTEGER | Ja | Mitarbeiter-ID |
| Employee_Name | VARCHAR(100) | Ja | Name |
| Department | VARCHAR(50) | Ja | Abteilung |
| Position | VARCHAR(50) | Ja | Position |
| Manager | VARCHAR(100) | Nein | Vorgesetzter |
| Hire_Date | DATE | Ja | Eintrittsdatum |

---

## 2.4 REGIONS

| Feld | Datentyp | Pflichtfeld | Beschreibung |
|------|----------|-------------|--------------|
| Region_ID | INTEGER | Ja | Regions-ID |
| Country | VARCHAR(50) | Ja | Land |
| Region | VARCHAR(50) | Ja | Region |
| City | VARCHAR(50) | Ja | Stadt |
| Sales_Area | VARCHAR(50) | Ja | Vertriebsgebiet |

---

## 2.5 COST_CENTERS

| Feld | Datentyp | Pflichtfeld | Beschreibung |
|------|----------|-------------|--------------|
| Cost_Center_ID | INTEGER | Ja | Kostenstellen-ID |
| Cost_Center_Name | VARCHAR(100) | Ja | Kostenstelle |
| Department | VARCHAR(50) | Ja | Abteilung |
| Budget | DECIMAL(12,2) | Ja | Jahresbudget |

---

## 2.6 PROFIT_CENTERS

| Feld | Datentyp | Pflichtfeld | Beschreibung |
|------|----------|-------------|--------------|
| Profit_Center_ID | INTEGER | Ja | Profit-Center-ID |
| Profit_Center_Name | VARCHAR(100) | Ja | Profit Center |
| Business_Unit | VARCHAR(50) | Ja | Geschäftsbereich |

---

## 2.7 ORDERS

| Feld | Datentyp | Pflichtfeld | Beschreibung |
|------|----------|-------------|--------------|
| Order_ID | INTEGER | Ja | Auftragsnummer |
| Customer_ID | INTEGER | Ja | Kunde |
| Employee_ID | INTEGER | Ja | Vertriebsmitarbeiter |
| Order_Date | DATE | Ja | Bestelldatum |
| Delivery_Date | DATE | Nein | Lieferdatum |
| Order_Status | VARCHAR(30) | Ja | Status |
| Payment_Method | VARCHAR(30) | Ja | Zahlungsmethode |

---

## 2.8 ORDER_ITEMS

| Feld | Datentyp | Pflichtfeld | Beschreibung |
|------|----------|-------------|--------------|
| Order_Item_ID | INTEGER | Ja | Positionsnummer |
| Order_ID | INTEGER | Ja | Auftrag |
| Product_ID | INTEGER | Ja | Produkt |
| Quantity | INTEGER | Ja | Verkaufsmenge |
| Unit_Price | DECIMAL(10,2) | Ja | Verkaufspreis |
| Discount | DECIMAL(5,2) | Nein | Rabatt in % |
| Revenue | DECIMAL(12,2) | Ja | Umsatz |
| Cost | DECIMAL(12,2) | Ja | Kosten |
| Profit | DECIMAL(12,2) | Ja | Gewinn |

---

# 3. Data Warehouse Tables

## 3.1 FACT_SALES

| Feld | Datentyp | Beschreibung |
|------|----------|--------------|
| Sales_ID | INTEGER | Eindeutiger Verkaufsschlüssel |
| Date_ID | INTEGER | Zeitdimension |
| Customer_ID | INTEGER | Kunde |
| Product_ID | INTEGER | Produkt |
| Employee_ID | INTEGER | Mitarbeiter |
| Region_ID | INTEGER | Region |
| Cost_Center_ID | INTEGER | Kostenstelle |
| Profit_Center_ID | INTEGER | Profit Center |
| Quantity | INTEGER | Verkaufsmenge |
| Revenue | DECIMAL(12,2) | Umsatz |
| Cost | DECIMAL(12,2) | Kosten |
| Profit | DECIMAL(12,2) | Gewinn |
| Discount | DECIMAL(5,2) | Rabatt |

---

## 3.2 DIM_CUSTOMER

Customer_ID, Customer_Name, Customer_Type, Industry, Segment, Country, City, Postal_Code

---

## 3.3 DIM_PRODUCT

Product_ID, Product_Name, Category, Subcategory, Brand, Supplier, Product_Status

---

## 3.4 DIM_DATE

Date_ID, Date, Day, Month, Month_Name, Quarter, Year, Week, Weekday

---

## 3.5 DIM_EMPLOYEE

Employee_ID, Employee_Name, Department, Position, Manager

---

## 3.6 DIM_REGION

Region_ID, Country, Region, City, Sales_Area

---

## 3.7 DIM_COST_CENTER

Cost_Center_ID, Cost_Center_Name, Department, Budget

---

## 3.8 DIM_PROFIT_CENTER

Profit_Center_ID, Profit_Center_Name, Business_Unit

---

# 4. Business KPIs

| KPI | Formel |
|------|---------|
| Revenue | Quantity × Unit_Price × (1 − Discount) |
| Cost | Quantity × Unit_Cost |
| Profit | Revenue − Cost |
| Profit Margin | Profit / Revenue × 100 |
| Average Order Value | Revenue / Anzahl Bestellungen |
| Revenue Growth | (Revenue aktuelles Jahr − Revenue Vorjahr) / Revenue Vorjahr |

---

# 5. Naming Conventions

Folgende Namenskonventionen werden im gesamten Projekt verwendet:

- Tabellen: Großbuchstaben (CUSTOMERS, PRODUCTS)
- Dimensionstabellen: Präfix **DIM_**
- Faktentabellen: Präfix **FACT_**
- Primärschlüssel: *_ID
- Fremdschlüssel: gleicher Name wie Primärschlüssel der referenzierten Tabelle

---

# 6. Data Quality Rules

Zur Sicherstellung einer hohen Datenqualität gelten folgende Regeln:

- Alle Primärschlüssel müssen eindeutig sein.
- Pflichtfelder dürfen keine NULL-Werte enthalten.
- Revenue muss größer oder gleich 0 sein.
- Cost muss größer oder gleich 0 sein.
- Profit wird automatisch berechnet.
- Quantity muss größer als 0 sein.
- Discount muss zwischen 0 % und 100 % liegen.
- Jeder Auftrag muss mindestens eine Auftragsposition besitzen.

---

# 7. Conclusion

Dieses Data Dictionary dient als zentrale Dokumentation der Datenstruktur und unterstützt die Implementierung in SAP BW/4HANA, SAP Datasphere und SAP Analytics Cloud.

Es gewährleistet eine einheitliche Definition aller Datenobjekte innerhalb der Global Sales Intelligence Platform.
