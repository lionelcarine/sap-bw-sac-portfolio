/*
===========================================================
Project : Global Sales Intelligence Platform
Purpose : Business Analysis
===========================================================
*/

USE global_sales;

------------------------------------------------------------
-- Total Revenue
------------------------------------------------------------

SELECT

SUM(Revenue) AS Total_Revenue

FROM ORDER_ITEMS;



------------------------------------------------------------
-- Revenue by Product
------------------------------------------------------------

SELECT

p.Product_Name,

SUM(oi.Revenue) AS Revenue

FROM PRODUCTS p

JOIN ORDER_ITEMS oi

ON p.Product_ID = oi.Product_ID

GROUP BY p.Product_Name

ORDER BY Revenue DESC;
