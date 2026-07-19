/*
===========================================================
Project : Global Sales Intelligence Platform
Purpose : Analytical Views
===========================================================
*/

USE global_sales;

------------------------------------------------------------
-- Sales Summary
------------------------------------------------------------

CREATE VIEW vw_sales_summary AS

SELECT

o.Order_ID,

o.Order_Date,

c.Customer_Name,

p.Product_Name,

oi.Quantity,

oi.Revenue,

oi.Profit

FROM ORDER_ITEMS oi

JOIN ORDERS o

ON oi.Order_ID = o.Order_ID

JOIN CUSTOMERS c

ON o.Customer_ID = c.Customer_ID

JOIN PRODUCTS p

ON oi.Product_ID = p.Product_ID;
