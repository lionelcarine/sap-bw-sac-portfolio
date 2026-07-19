/*
===========================================================
Project : Global Sales Intelligence Platform
Purpose : Insert Master Data
===========================================================
*/

USE global_sales;

-- =========================================================
-- REGIONS
-- =========================================================

INSERT INTO REGIONS (Country, Region, City, Sales_Area)
VALUES
('Germany','Bavaria','Munich','South'),
('Germany','Berlin','Berlin','East'),
('Germany','Hamburg','Hamburg','North'),
('Germany','North Rhine-Westphalia','Cologne','West'),
('France','Île-de-France','Paris','North'),
('France','Auvergne-Rhône-Alpes','Lyon','South'),
('Spain','Madrid','Madrid','Center'),
('Spain','Catalonia','Barcelona','East'),
('Italy','Lombardy','Milan','North'),
('Italy','Lazio','Rome','Center'),
('Netherlands','North Holland','Amsterdam','West'),
('Belgium','Brussels','Brussels','Center'),
('Austria','Vienna','Vienna','East'),
('Switzerland','Zurich','Zurich','North');
