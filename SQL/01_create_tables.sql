/*
===========================================================
Project : Global Sales Intelligence Platform
Database: MySQL
Author  : Carine Kuimi
Purpose : ERP Database Schema
===========================================================
*/

DROP DATABASE IF EXISTS global_sales;

CREATE DATABASE global_sales;

USE global_sales;

-- =========================================================
-- TABLE: REGIONS
-- =========================================================

CREATE TABLE REGIONS (

    Region_ID INT PRIMARY KEY AUTO_INCREMENT,

    Country VARCHAR(50) NOT NULL,

    Region VARCHAR(50) NOT NULL,

    City VARCHAR(50) NOT NULL,

    Sales_Area VARCHAR(50) NOT NULL

);

-- =========================================================
-- TABLE: COST_CENTERS
-- =========================================================

CREATE TABLE COST_CENTERS (

    Cost_Center_ID INT PRIMARY KEY AUTO_INCREMENT,

    Cost_Center_Name VARCHAR(100) NOT NULL,

    Department VARCHAR(50) NOT NULL,

    Budget DECIMAL(12,2) NOT NULL

);

-- =========================================================
-- TABLE: PROFIT_CENTERS
-- =========================================================

CREATE TABLE PROFIT_CENTERS (

    Profit_Center_ID INT PRIMARY KEY AUTO_INCREMENT,

    Profit_Center_Name VARCHAR(100) NOT NULL,

    Business_Unit VARCHAR(50) NOT NULL

);

-- =========================================================
-- TABLE: CUSTOMERS
-- =========================================================

CREATE TABLE CUSTOMERS (

    Customer_ID INT PRIMARY KEY AUTO_INCREMENT,

    Customer_Name VARCHAR(100) NOT NULL,

    Customer_Type VARCHAR(20) NOT NULL,

    Industry VARCHAR(50),

    Segment VARCHAR(30) NOT NULL,

    Country VARCHAR(50) NOT NULL,

    City VARCHAR(50) NOT NULL,

    Postal_Code VARCHAR(15),

    Registration_Date DATE NOT NULL,

    Region_ID INT NOT NULL,

    FOREIGN KEY (Region_ID)
        REFERENCES REGIONS(Region_ID)

);

-- =========================================================
-- TABLE: PRODUCTS
-- =========================================================

CREATE TABLE PRODUCTS (

    Product_ID INT PRIMARY KEY AUTO_INCREMENT,

    Product_Name VARCHAR(100) NOT NULL,

    Category VARCHAR(50) NOT NULL,

    Subcategory VARCHAR(50) NOT NULL,

    Brand VARCHAR(50),

    Unit_Cost DECIMAL(10,2) NOT NULL,

    Standard_Price DECIMAL(10,2) NOT NULL,

    Supplier VARCHAR(100),

    Product_Status VARCHAR(20) NOT NULL,

    Profit_Center_ID INT NOT NULL,

    FOREIGN KEY (Profit_Center_ID)
        REFERENCES PROFIT_CENTERS(Profit_Center_ID)

);

-- =========================================================
-- TABLE: EMPLOYEES
-- =========================================================

CREATE TABLE EMPLOYEES (

    Employee_ID INT PRIMARY KEY AUTO_INCREMENT,

    Employee_Name VARCHAR(100) NOT NULL,

    Department VARCHAR(50) NOT NULL,

    Position VARCHAR(50) NOT NULL,

    Manager VARCHAR(100),

    Hire_Date DATE NOT NULL,

    Cost_Center_ID INT NOT NULL,

    FOREIGN KEY (Cost_Center_ID)
        REFERENCES COST_CENTERS(Cost_Center_ID)

);

-- =========================================================
-- TABLE: ORDERS
-- =========================================================

CREATE TABLE ORDERS (

    Order_ID INT PRIMARY KEY AUTO_INCREMENT,

    Customer_ID INT NOT NULL,

    Employee_ID INT NOT NULL,

    Order_Date DATE NOT NULL,

    Delivery_Date DATE,

    Order_Status VARCHAR(30) NOT NULL,

    Payment_Method VARCHAR(30) NOT NULL,

    FOREIGN KEY (Customer_ID)
        REFERENCES CUSTOMERS(Customer_ID),

    FOREIGN KEY (Employee_ID)
        REFERENCES EMPLOYEES(Employee_ID)

);

-- =========================================================
-- TABLE: ORDER_ITEMS
-- =========================================================

CREATE TABLE ORDER_ITEMS (

    Order_Item_ID INT PRIMARY KEY AUTO_INCREMENT,

    Order_ID INT NOT NULL,

    Product_ID INT NOT NULL,

    Quantity INT NOT NULL,

    Unit_Price DECIMAL(10,2) NOT NULL,

    Discount DECIMAL(5,2) DEFAULT 0,

    Revenue DECIMAL(12,2),

    Cost DECIMAL(12,2),

    Profit DECIMAL(12,2),

    FOREIGN KEY (Order_ID)
        REFERENCES ORDERS(Order_ID),

    FOREIGN KEY (Product_ID)
        REFERENCES PRODUCTS(Product_ID)

);
