# 03 – Data Warehouse Model

---

# Project Information

| Item | Description |
|------|-------------|
| Project | Global Sales Intelligence Platform |
| Company | Global Retail Group (GRG) |
| Technology | SAP BW/4HANA |
| Data Model | Star Schema |
| Author | Carine Kuimi |
| Version | 1.0 |

---

## 1. Overview

Das Data Warehouse dient als analytische Datenbasis der Global Sales Intelligence Platform.

Im Gegensatz zum ERP-System, das operative Geschäftsprozesse unterstützt, ist das Data Warehouse für Reporting, Business Intelligence und Predictive Analytics optimiert.

Die Daten werden aus dem ERP-System extrahiert, transformiert und in ein Star Schema überführt.

---

## 2. Architektur

```text
                SAP S/4HANA ERP
                       │
                       ▼
                 ETL-Prozess
                       │
                       ▼
                 SAP BW/4HANA
                       │
        ┌──────────────┼──────────────┐
        │              │              │
        ▼              ▼              ▼
   Faktentabelle   Dimensionen    BW Queries
                       │
                       ▼
            SAP Analytics Cloud
                       │
                       ▼
            Executive Dashboards
```

---

## 3. Star Schema

Das analytische Datenmodell basiert auf einem Star Schema.

Eine zentrale Faktentabelle enthält alle Kennzahlen.

Die Dimensionstabellen liefern den fachlichen Kontext.

---

## 4. Star Schema

```text
                    DIM_DATE
                        │
                        │
DIM_CUSTOMER ---- FACT_SALES ---- DIM_PRODUCT
                        │
                        │
                  DIM_EMPLOYEE
                        │
                        │
                   DIM_REGION
                        │
                        │
               DIM_COST_CENTER
                        │
                        │
              DIM_PROFIT_CENTER
```

---

## 5. Mapping ERP → Data Warehouse

| ERP-Tabelle | Data Warehouse |
|--------------|----------------|
| CUSTOMERS | DIM_CUSTOMER |
| PRODUCTS | DIM_PRODUCT |
| EMPLOYEES | DIM_EMPLOYEE |
| REGIONS | DIM_REGION |
| COST_CENTERS | DIM_COST_CENTER |
| PROFIT_CENTERS | DIM_PROFIT_CENTER |
| ORDERS + ORDER_ITEMS | FACT_SALES |

Der ETL-Prozess transformiert die operativen Daten in ein analytisches Datenmodell.

Dadurch werden Berichte und Analysen deutlich performanter.

---

## 6. FACT_SALES

### Beschreibung

Die Faktentabelle enthält sämtliche Verkaufskennzahlen.

Jeder Datensatz beschreibt eine verkaufte Produktposition.

---

### Kennzahlen

| Kennzahl | Beschreibung |
|-----------|--------------|
| Quantity | Verkaufsmenge |
| Revenue | Umsatz |
| Cost | Kosten |
| Profit | Gewinn |
| Discount | Rabatt |

---

### Fremdschlüssel

- Customer_ID
- Product_ID
- Employee_ID
- Region_ID
- Cost_Center_ID
- Profit_Center_ID
- Date_ID

---

## 7. Dimensionstabellen 
### 7.1 DIM_CUSTOMER

#### Beschreibung

Die Dimension **DIM_CUSTOMER** enthält alle kundenbezogenen Stammdaten.

Sie ermöglicht Analysen nach Kundensegment, Kundentyp und geografischen Merkmalen.

---

#### Attribute

| Attribut | Beschreibung |
|----------|--------------|
| Customer_ID | Eindeutige Kundennummer |
| Customer_Name | Kundenname |
| Customer_Type | B2B oder B2C |
| Industry | Branche |
| Segment | Kundensegment |
| Country | Land |
| City | Stadt |
| Postal_Code | Postleitzahl |

---

#### Herkunft

Quelle: **CUSTOMERS**

---

#### Verwendung

Diese Dimension unterstützt Analysen wie:

- Umsatz nach Kundensegment
- Umsatz nach Land
- Top-Kunden
- Neukundenanalyse

---

### 7.2 DIM_PRODUCT

#### Beschreibung

Die Dimension **DIM_PRODUCT** enthält sämtliche Produktstammdaten.

Sie dient der Analyse von Umsatz, Gewinn und Verkaufszahlen auf Produktebene.

---

#### Attribute

| Attribut | Beschreibung |
|----------|--------------|
| Product_ID | Produktnummer |
| Product_Name | Produktname |
| Category | Produktkategorie |
| Subcategory | Unterkategorie |
| Brand | Marke |
| Supplier | Lieferant |
| Product_Status | Aktiv oder Inaktiv |

---

#### Herkunft

Quelle: **PRODUCTS**

---

#### Verwendung

Diese Dimension unterstützt Analysen wie:

- Umsatz nach Produkt
- Umsatz nach Kategorie
- Umsatz nach Marke
- Top-Produkte

---

### 7.3 DIM_DATE

#### Beschreibung

Die Zeitdimension ermöglicht zeitbezogene Analysen.

Sie wird von nahezu allen Reports verwendet.

---

#### Attribute

| Attribut | Beschreibung |
|----------|--------------|
| Date_ID | Datumsschlüssel |
| Date | Kalenderdatum |
| Day | Tag |
| Month | Monat |
| Month_Name | Monatsname |
| Quarter | Quartal |
| Year | Jahr |
| Week | Kalenderwoche |
| Weekday | Wochentag |

---

#### Herkunft

Quelle: **ORDERS.Order_Date**

---

#### Verwendung

- Monatsreporting
- Quartalsanalysen
- Jahresvergleiche
- Trendanalysen

---

### 7.4 DIM_EMPLOYEE

#### Beschreibung

Die Dimension enthält Informationen über alle Vertriebsmitarbeiter.

---

#### Attribute

| Attribut | Beschreibung |
|----------|--------------|
| Employee_ID | Mitarbeiter-ID |
| Employee_Name | Name |
| Department | Abteilung |
| Position | Position |
| Manager | Vorgesetzter |

---

#### Herkunft

Quelle: **EMPLOYEES**

---

#### Verwendung

- Umsatz pro Mitarbeiter
- Verkaufsleistung
- Teamvergleich

---

### 7.5 DIM_REGION

#### Beschreibung

Diese Dimension beschreibt die geografische Struktur des Unternehmens.

---

#### Attribute

| Attribut | Beschreibung |
|----------|--------------|
| Region_ID | Regions-ID |
| Country | Land |
| Region | Region |
| City | Stadt |
| Sales_Area | Vertriebsgebiet |

---

#### Herkunft

Quelle: **REGIONS**

---

#### Verwendung

- Umsatz nach Land
- Umsatz nach Region
- Geografische Analysen

---

### 7.6 DIM_COST_CENTER

#### Beschreibung

Die Dimension enthält alle Kostenstellen.

Sie dient der Analyse von Kosten und Budgetabweichungen.

---

#### Attribute

| Attribut | Beschreibung |
|----------|--------------|
| Cost_Center_ID | Kostenstellen-ID |
| Cost_Center_Name | Kostenstelle |
| Department | Abteilung |
| Budget | Budget |

---

#### Herkunft

Quelle: **COST_CENTERS**

---

#### Verwendung

- Budgetkontrolle
- Kostenanalysen
- Kostenstellenvergleich

---

### 7.7 DIM_PROFIT_CENTER

#### Beschreibung

Die Profit-Center-Dimension ermöglicht die Analyse der Profitabilität verschiedener Geschäftsbereiche.

---

#### Attribute

| Attribut | Beschreibung |
|----------|--------------|
| Profit_Center_ID | Profit-Center-ID |
| Profit_Center_Name | Profit Center |
| Business_Unit | Geschäftsbereich |

---

#### Herkunft

Quelle: **PROFIT_CENTERS**

---

#### Verwendung

- Gewinn nach Business Unit
- Profitabilitätsanalyse

---

## 8. Schlüsseldefinitionen

Zur Sicherstellung der Datenintegrität verwendet das Data Warehouse Primär- und Fremdschlüssel.

### Primärschlüssel

| Tabelle | Primärschlüssel |
|----------|-----------------|
| FACT_SALES | Sales_ID |
| DIM_CUSTOMER | Customer_ID |
| DIM_PRODUCT | Product_ID |
| DIM_DATE | Date_ID |
| DIM_EMPLOYEE | Employee_ID |
| DIM_REGION | Region_ID |
| DIM_COST_CENTER | Cost_Center_ID |
| DIM_PROFIT_CENTER | Profit_Center_ID |

---

### Fremdschlüssel der Faktentabelle

Die Faktentabelle referenziert alle Dimensionstabellen.

| Fremdschlüssel | Referenz |
|----------------|-----------|
| Customer_ID | DIM_CUSTOMER |
| Product_ID | DIM_PRODUCT |
| Employee_ID | DIM_EMPLOYEE |
| Region_ID | DIM_REGION |
| Cost_Center_ID | DIM_COST_CENTER |
| Profit_Center_ID | DIM_PROFIT_CENTER |
| Date_ID | DIM_DATE |

Dadurch entsteht das Star Schema des Data Warehouse.
- Executive Reporting

---

## 9. Granularität der Faktentabelle

Die Granularität beschreibt die kleinste Informationseinheit innerhalb der Faktentabelle.

Für dieses Projekt wurde folgende Granularität definiert:

> Eine Zeile entspricht genau einer Position eines Verkaufsauftrags.

Beispiel:

| Sales_ID | Order_ID | Product | Quantity |
|-----------|----------|----------|----------|
| 100001 | SO-1001 | Laptop | 2 |
| 100002 | SO-1001 | Monitor | 1 |

Ein Auftrag mit mehreren Produkten erzeugt mehrere Datensätze in der Faktentabelle.

Diese Granularität ermöglicht detaillierte Analysen auf Produktebene.

---

## 10. Slowly Changing Dimensions (SCD)

Dimensionstabellen ändern sich im Laufe der Zeit.

Für dieses Projekt werden folgende SCD-Strategien verwendet.

| Dimension | SCD-Typ |
|------------|----------|
| DIM_CUSTOMER | Type 2 |
| DIM_PRODUCT | Type 2 |
| DIM_EMPLOYEE | Type 2 |
| DIM_REGION | Type 1 |
| DIM_COST_CENTER | Type 1 |
| DIM_PROFIT_CENTER | Type 1 |

---

### Erläuterung

#### Type 1

Der alte Wert wird überschrieben.

Beispiel:

Land = Deutschland

↓

Land = Österreich

Der alte Wert geht verloren.

---

#### Type 2

Historische Änderungen bleiben erhalten.

Beispiel:

Customer Segment

2023 → Standard

2024 → Premium

Beide Versionen bleiben im Data Warehouse gespeichert.

Dadurch können historische Reports korrekt erstellt werden.

---

## 11. ETL-Regeln

Während des ETL-Prozesses werden die operativen ERP-Daten in analytische Daten transformiert.

Folgende Regeln werden angewendet.

### Extraktion

Daten werden aus folgenden ERP-Tabellen extrahiert.

- CUSTOMERS
- PRODUCTS
- EMPLOYEES
- REGIONS
- ORDERS
- ORDER_ITEMS

---

### Transformation

Folgende Transformationen werden durchgeführt.

- Berechnung von Revenue
- Berechnung von Profit
- Berechnung von Profit Margin
- Erstellung der Date Dimension
- Bereinigung fehlender Werte
- Standardisierung von Produktkategorien
- Dublettenprüfung

---

### Laden

Die transformierten Daten werden in SAP BW/4HANA geladen.

Anschließend werden BW Queries erstellt und für SAP Analytics Cloud bereitgestellt.

---

## 12. KPI-Definitionen

Folgende Kennzahlen werden im Projekt verwendet.

| KPI | Formel |
|------|---------|
| Revenue | Quantity × Unit_Price × (1 − Discount) |
| Cost | Quantity × Unit_Cost |
| Profit | Revenue − Cost |
| Profit Margin | Profit / Revenue × 100 |
| Average Order Value | Revenue / Anzahl Bestellungen |
| Revenue Growth | (Revenue aktuelles Jahr − Revenue Vorjahr) / Revenue Vorjahr |

---

Diese KPIs bilden die Grundlage aller Dashboards in SAP Analytics Cloud.

---

## 13. Reporting Layer

Die Daten werden nach erfolgreicher Modellierung in SAP Analytics Cloud visualisiert.

Geplante Dashboards:

- Executive Dashboard
- Sales Dashboard
- Customer Dashboard
- Product Dashboard
- Regional Dashboard
- Profitability Dashboard
- Forecast Dashboard


