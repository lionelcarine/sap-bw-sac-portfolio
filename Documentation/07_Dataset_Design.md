# 06 – Dataset Design

---

# Project Information

| Item | Description |
|------|-------------|
| Project | Global Sales Intelligence Platform |
| Company | Global Retail Group (GRG) |
| Version | 1.0 |

---

# 1. Ziel

Für dieses Portfolio wird ein realistisches ERP-Datenset entwickelt.

Das Datenset dient als Grundlage für:

- SAP BW/4HANA
- SAP Datasphere
- SAP Analytics Cloud
- Python Machine Learning

---

# 2. Tabellenumfang

| Tabelle | Anzahl Datensätze |
|----------|------------------:|
| REGIONS | 20 |
| COST_CENTERS | 8 |
| PROFIT_CENTERS | 6 |
| EMPLOYEES | 80 |
| CUSTOMERS | 1.000 |
| PRODUCTS | 250 |
| ORDERS | 10.000 |
| ORDER_ITEMS | ca. 30.000 |

---

# 3. Länder

- Deutschland
- Frankreich
- Spanien
- Italien
- Niederlande
- Belgien
- Österreich
- Schweiz

---

# 4. Produktkategorien

- Electronics
- Furniture
- Office Supplies
- Accessories
- Software
- Services

---

# 5. Kundensegmente

- Consumer
- Corporate
- Small Business

---

# 6. Zahlungsmethoden

- Bank Transfer
- Credit Card
- PayPal

---

# 7. Auftragsstatus

- Open
- Processing
- Delivered
- Cancelled

---

# 8. Zeitraum

Die Daten decken den Zeitraum von Januar 2022 bis Dezember 2025 ab.

---

# 9. Business Rules

- Jeder Kunde besitzt mindestens eine Bestellung.
- Jeder Auftrag enthält mindestens eine Position.
- Ein Produkt kann in mehreren Aufträgen vorkommen.
- Rabatte liegen zwischen 0 % und 20 %.
- Negative Umsätze sind nicht zulässig.

---

# 10. Ziel

Das Datenset soll realistische Verkaufsdaten simulieren und als Grundlage für Reporting, Dashboarding und Predictive Analytics dienen.
