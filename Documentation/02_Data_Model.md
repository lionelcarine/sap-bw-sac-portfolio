# Datenmodell

## Übersicht

Die Global Sales Intelligence Platform basiert auf einem **Star Schema**.

Das Datenmodell besteht aus einer Faktentabelle und mehreren Dimensionstabellen.

Dieses Modell ermöglicht eine performante Datenanalyse in:

- SAP BW/4HANA
- SAP Datasphere
- SAP Analytics Cloud

---

# Datenmodell

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

# Faktentabelle

## FACT_SALES

Die Faktentabelle enthält alle Verkaufsinformationen.

| Feld | Beschreibung |
|------|--------------|
| Sales_ID | Primärschlüssel |
| Order_ID | Verkaufsauftrag |
| Customer_ID | Kunde |
| Product_ID | Produkt |
| Employee_ID | Vertriebsmitarbeiter |
| Region_ID | Region |
| Cost_Center_ID | Kostenstelle |
| Profit_Center_ID | Profit Center |
| Date_ID | Datum |
| Quantity | Verkaufsmenge |
| Unit_Price | Stückpreis |
| Discount | Rabatt |
| Revenue | Umsatz |
| Cost | Kosten |
| Profit | Gewinn |

---

# Dimensionstabellen

## DIM_CUSTOMER

Die Dimension **DIM_CUSTOMER** enthält alle relevanten Stammdaten der Kunden.

| Feld | Beschreibung |
|------|--------------|
| Customer_ID | Primärschlüssel |
| Customer_Name | Kundenname |
| Customer_Type | Privatkunde oder Geschäftskunde |
| Industry | Branche |
| Segment | Kundensegment |
| City | Stadt |
| Country | Land |
| Postal_Code | Postleitzahl |
| Registration_Date | Registrierungsdatum |

### Zweck

Diese Dimension ermöglicht Analysen nach:

- Kundensegment
- Branche
- Land
- Stadt
- Kundentyp

Beispiel:

- Welches Kundensegment erzielt den höchsten Umsatz?
- Welche Branche generiert den größten Gewinn?
- Aus welchem Land stammen die umsatzstärksten Kunden?

---

## DIM_PRODUCT

Die Dimension **DIM_PRODUCT** enthält die Stammdaten aller Produkte.

| Feld | Beschreibung |
|------|--------------|
| Product_ID | Primärschlüssel |
| Product_Name | Produktname |
| Category | Produktkategorie |
| Subcategory | Unterkategorie |
| Brand | Marke |
| Unit_Cost | Einkaufspreis |
| Standard_Price | Standardverkaufspreis |
| Supplier | Lieferant |
| Product_Status | Aktiv / Inaktiv |

### Zweck

Diese Dimension ermöglicht Analysen nach:

- Produkt
- Kategorie
- Unterkategorie
- Marke

Beispiel:

- Welche Produkte erzielen den höchsten Umsatz?
- Welche Kategorien sind am profitabelsten?
- Welche Marken verkaufen sich am besten?

---

## DIM_DATE

Die Dimension **DIM_DATE** enthält alle Kalenderinformationen.

| Feld | Beschreibung |
|------|--------------|
| Date_ID | Primärschlüssel |
| Date | Kalenderdatum |
| Day | Tag |
| Month | Monat |
| Month_Name | Monatsname |
| Quarter | Quartal |
| Year | Jahr |
| Week | Kalenderwoche |
| Weekday | Wochentag |

### Zweck

Diese Dimension ermöglicht Zeitanalysen wie:

- Umsatz pro Monat
- Umsatz pro Quartal
- Umsatz pro Jahr
- Saisonale Trends

---

## DIM_REGION

Die Dimension **DIM_REGION** beschreibt die geografischen Informationen.

| Feld | Beschreibung |
|------|--------------|
| Region_ID | Primärschlüssel |
| Country | Land |
| Region | Region |
| City | Stadt |
| Sales_Area | Vertriebsgebiet |

### Zweck

Ermöglicht Analysen nach Regionen und Ländern.

---

## DIM_EMPLOYEE

Die Dimension **DIM_EMPLOYEE** enthält die Stammdaten der Vertriebsmitarbeiter.

| Feld | Beschreibung |
|------|--------------|
| Employee_ID | Primärschlüssel |
| Employee_Name | Name |
| Department | Abteilung |
| Position | Position |
| Manager | Vorgesetzter |
| Hire_Date | Eintrittsdatum |

### Zweck

Ermöglicht Analysen der Vertriebsleistung.

---

## DIM_COST_CENTER

Die Dimension **DIM_COST_CENTER** enthält Informationen zu Kostenstellen.

| Feld | Beschreibung |
|------|--------------|
| Cost_Center_ID | Primärschlüssel |
| Cost_Center_Name | Kostenstelle |
| Department | Abteilung |
| Budget | Budget |

### Zweck

Vergleich von Budget und tatsächlichen Kosten.

---

## DIM_PROFIT_CENTER

Die Dimension **DIM_PROFIT_CENTER** enthält Informationen zu Profit Centern.

| Feld | Beschreibung |
|------|--------------|
| Profit_Center_ID | Primärschlüssel |
| Profit_Center_Name | Profit Center |
| Business_Unit | Geschäftsbereich |

### Zweck

Analyse der Profitabilität nach Geschäftsbereichen.
