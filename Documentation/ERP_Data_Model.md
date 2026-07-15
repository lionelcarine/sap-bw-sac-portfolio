# 02 – ERP Data Model

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
