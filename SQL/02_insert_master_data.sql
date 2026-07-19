/*
===========================================================
Project : Global Sales Intelligence Platform
Database: MySQL
Author  : Carine Kuimi
Purpose : Insert Master Data
===========================================================
*/

USE global_sales;

-- =========================================================
-- INSERT REGIONS
-- =========================================================

INSERT INTO REGIONS
(Country, Region, City, Sales_Area)
VALUES
('Germany','Bavaria','Munich','South'),
('Germany','Baden-Württemberg','Stuttgart','South'),
('Germany','Berlin','Berlin','East'),
('Germany','Hamburg','Hamburg','North'),
('Germany','North Rhine-Westphalia','Cologne','West'),

('France','Île-de-France','Paris','North'),
('France','Auvergne-Rhône-Alpes','Lyon','South'),
('France','Provence-Alpes-Côte d''Azur','Marseille','South'),

('Spain','Madrid','Madrid','Center'),
('Spain','Catalonia','Barcelona','East'),

('Italy','Lombardy','Milan','North'),
('Italy','Lazio','Rome','Center'),

('Netherlands','North Holland','Amsterdam','West'),
('Belgium','Brussels-Capital','Brussels','Center'),

('Austria','Vienna','Vienna','East'),

('Switzerland','Zurich','Zurich','North'),

('Poland','Mazovia','Warsaw','East'),

('Czech Republic','Prague','Prague','East'),

('Denmark','Capital Region','Copenhagen','North'),

('Sweden','Stockholm County','Stockholm','North');



-- =========================================================
-- INSERT COST CENTERS
-- =========================================================

INSERT INTO COST_CENTERS
(Cost_Center_Name, Department, Budget)
VALUES

('Sales Germany','Sales',300000),

('Sales Europe','Sales',450000),

('Marketing','Marketing',250000),

('Finance','Finance',180000),

('Human Resources','HR',150000),

('IT Services','IT',500000),

('Operations','Operations',600000),

('Research & Development','R&D',800000);



-- =========================================================
-- INSERT PROFIT CENTERS
-- =========================================================

INSERT INTO PROFIT_CENTERS
(Profit_Center_Name, Business_Unit)
VALUES

('Consumer Electronics','Electronics'),

('Office Solutions','Office'),

('Furniture Division','Furniture'),

('Software Solutions','Software'),

('Accessories','Retail'),

('Professional Services','Services');
