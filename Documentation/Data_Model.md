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
