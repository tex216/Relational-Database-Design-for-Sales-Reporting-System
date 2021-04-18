USE cs6400_sp21_team058;


-- 0. delete existing data
delete from SALE;
delete from DISCOUNT;
delete from STORE;
delete from CITY;
delete from CHILDCARE;
delete from PRODUCT;
delete from SELL;
delete from CATEGORY;
delete from ASSIGNED;
delete from HOLIDAY;
delete from ADVERTISING_CAMPAIGN;
delete from HOLD;
delete from `DAY`;



-- 1. load data
-- CITY
LOAD DATA INFILE 'population.tsv'
INTO TABLE CITY
FIELDS TERMINATED BY '\t'
LINES TERMINATED BY '\n'
IGNORE 1 Lines
(@col1, @col2, @col3) 
SET State_Location=@col2, City_Name=@col1, Population=@col3;

-- CHILDCARE
-- IGNORE: ignore duplicates
LOAD DATA INFILE 'stores.tsv'
IGNORE
INTO TABLE CHILDCARE
FIELDS TERMINATED BY '\t'
LINES TERMINATED BY '\n'
IGNORE 1 Lines
(@col1, @col2, @col3, @col4, @col5, @col6, @col7, @col8) 
SET Time_Limit=@col8;
-- remove 0 which doesn't exist in the original Demo Data
DELETE FROM CHILDCARE
WHERE Time_Limit = 0;

-- STORE
-- NULLIF() sets Time_Limit to NULL if @col8 contains an empty string
-- The NULLIF() function compares two expressions and returns NULL if they are equal. Otherwise, the first expression is returned.
LOAD DATA INFILE 'stores.tsv'
INTO TABLE STORE
FIELDS TERMINATED BY '\t'
LINES TERMINATED BY '\n'
IGNORE 1 Lines
(@col1, @col2, @col3, @col4, @col5, @col6, @col7, @col8) 
SET Store_Number=@col1, Phone_Number=@col2, Street_Address=@col3, City_Name=@col4, State_Location=@col5, Has_Restaurant=@col6, Has_Snack_Bar=@col7, Time_Limit=NULLIF(@col8,'');
-- For Phone_Number="", set to NULL
--UPDATE STORE
--SET Phone_Number = NULL
--WHERE Phone_Number = '""';

-- PRODUCT
LOAD DATA INFILE 'products.tsv'
INTO TABLE PRODUCT
FIELDS TERMINATED BY '\t'
LINES TERMINATED BY '\n'
IGNORE 1 Lines;

-- SELL
-- takes relatively long time to run
-- IGNORE: ignore duplicates
LOAD DATA INFILE 'sales.tsv'
IGNORE
INTO TABLE SELL
FIELDS TERMINATED BY '\t'
LINES TERMINATED BY '\n'
IGNORE 1 Lines
(@col1, @col2, @col3, @col4) 
SET Store_Number=@col2, PID=@col1;

-- `DAY`
LOAD DATA INFILE 'date.tsv'
INTO TABLE `DAY`
LINES TERMINATED BY '\n'
IGNORE 1 Lines;

-- SALE
-- takes relatively long time to run
-- compute Total_Amount later
LOAD DATA INFILE 'sales.tsv'
INTO TABLE SALE
FIELDS TERMINATED BY '\t'
LINES TERMINATED BY '\n'
IGNORE 1 Lines
(@col1, @col2, @col3, @col4) 
SET PID=@col1, Store_Number=@col2, `Date`=@col3, Quantity=@col4, Total_Amount=0.00;

-- CATEGORY
LOAD DATA INFILE 'categories.tsv'
INTO TABLE CATEGORY
LINES TERMINATED BY '\n'
IGNORE 1 Lines;

-- ASSIGNED
LOAD DATA INFILE 'productcategories.tsv'
INTO TABLE ASSIGNED
FIELDS TERMINATED BY '\t'
LINES TERMINATED BY '\n'
IGNORE 1 Lines;

-- HOLIDAY
LOAD DATA INFILE 'holidays.tsv'
INTO TABLE HOLIDAY
FIELDS TERMINATED BY '\t'
LINES TERMINATED BY '\n'
IGNORE 1 Lines;

-- DISCOUNT
LOAD DATA INFILE 'discounts.tsv'
INTO TABLE DISCOUNT
FIELDS TERMINATED BY '\t'
LINES TERMINATED BY '\n'
IGNORE 1 Lines
(@col1, @col2, @col3) 
SET `Date`=@col2, PID=@col1, Discount_Price=@col3;

-- ADVERTISING_CAMPAIGN
-- IGNORE: ignore duplicates
LOAD DATA INFILE 'ad_campaigns.tsv'
IGNORE
INTO TABLE ADVERTISING_CAMPAIGN
FIELDS TERMINATED BY '\t'
LINES TERMINATED BY '\n'
IGNORE 1 Lines
(@col1, @col2) 
SET `Description`=@col2;

-- HOLD
LOAD DATA INFILE 'ad_campaigns.tsv'
INTO TABLE HOLD
FIELDS TERMINATED BY '\t'
LINES TERMINATED BY '\n'
IGNORE 1 Lines;

-- SALE: compute Total_Amount
-- takes relatively long time to run
-- if not ROUND, 258.36 * 1 = 258.3599853515625
UPDATE SALE S
LEFT JOIN PRODUCT P ON S.PID = P.PID
LEFT JOIN DISCOUNT D ON S.`Date` = D.`Date` AND S.PID = D.PID
SET S.Total_Amount = ROUND((IFNULL(D.Discount_Price, P.Retail_Price) * S.Quantity), 2);



-- 2. verify results
select * from CITY order by City_Name, State_Location limit 5;
select count(*) from CITY; -- 250

select * from CHILDCARE limit 5;

select * from STORE limit 5;
select count(*) from STORE; -- 1000
select * from STORE where Phone_Number is NULL;
select * from STORE where Phone_Number = '""';

select * from PRODUCT limit 5;
select count(*) from PRODUCT; -- 25300

select * from SELL order by PID, Store_Number limit 5;

select * from `DAY` limit 5;
select count(*) from `DAY`; -- 4566

select * from SALE order by PID, Store_Number limit 5;
select count(*) from SALE; -- 500000

select * from CATEGORY limit 5;
select count(*) from CATEGORY; -- 30

select * from ASSIGNED order by PID limit 5;
select count(*) from ASSIGNED; -- 49410

select * from HOLIDAY limit 5;
select count(*) from HOLIDAY; -- 16

select * from DISCOUNT order by PID limit 5;
select count(*) from DISCOUNT; -- 57505

select * from ADVERTISING_CAMPAIGN limit 5;
select count(*) from ADVERTISING_CAMPAIGN; -- 39

select * from HOLD limit 5;
select count(*) from HOLD; -- 18456


SELECT S.`Date`, S.Store_Number, S.PID, P.Retail_Price, D.Discount_Price, S.Quantity, S.Total_Amount, ROUND((IFNULL(D.Discount_Price, P.Retail_Price) * S.Quantity), 2) AS Total_Amount_Cal
FROM SALE S
LEFT JOIN PRODUCT P ON S.PID = P.PID
LEFT JOIN DISCOUNT D ON S.`Date` = D.`Date` AND S.PID = D.PID
ORDER BY S.PID, S.Store_Number
LIMIT 5;

SELECT S.`Date`, S.Store_Number, S.PID, P.Retail_Price, D.Discount_Price, S.Quantity, S.Total_Amount, ROUND((IFNULL(D.Discount_Price, P.Retail_Price) * S.Quantity), 2) AS Total_Amount_Cal
FROM SALE S
LEFT JOIN PRODUCT P ON S.PID = P.PID
LEFT JOIN DISCOUNT D ON S.`Date` = D.`Date` AND S.PID = D.PID
WHERE D.Discount_Price IS NOT NULL
ORDER BY S.PID, S.Store_Number
LIMIT 5;