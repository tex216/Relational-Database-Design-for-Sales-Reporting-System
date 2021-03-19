-- insert sample data
INSERT INTO CITY
VALUES 
('NY', 'New York', 8419000, 'Large');

INSERT INTO STORE
VALUES 
('Store_Number_1', '1234567890', 'Street_Address_1', 0, 0, 'NY', 'New York');

INSERT INTO PRODUCT
VALUES 
('PID_1', 'Product_Name_1', 10), 
('PID_2', 'Product_Name_2', 20),
('PID_3', 'Product_Name_3', 30);

INSERT INTO CATEGORY
VALUES 
('Couches and Sofas'), 
('Other Category');

INSERT INTO ASSIGNED
VALUES 
('PID_1', 'Couches and Sofas'), 
('PID_2', 'Couches and Sofas'), 
('PID_3', 'Other Category');

INSERT INTO `DAY`
VALUES 
('2012-5-1'), 
('2012-6-1'), 
('2012-6-2');

INSERT INTO SALE
VALUES 
('2012-5-1', 'Store_Number_1', 'PID_1', 50000,  500000), 
('2012-6-1', 'Store_Number_1', 'PID_1', 100000, 800000), 
('2012-6-2', 'Store_Number_1', 'PID_1', 50000,  350000),
('2012-6-2', 'Store_Number_1', 'PID_2', 50000,  1000000);

INSERT INTO DISCOUNT
VALUES  
('2012-6-1', 'PID_1', 8), 
('2012-6-2', 'PID_1', 7);


-- verify insertion results
/*
SELECT * FROM CITY;
SELECT * FROM STORE;
SELECT * FROM PRODUCT;
SELECT * FROM CATEGORY;
SELECT * FROM ASSIGNED;
SELECT * FROM `DAY`;
SELECT * FROM SALE;
SELECT * FROM DISCOUNT;
*/


-- verify SQL - Report 1
SELECT C.Category_Name, COUNT(P.PID) AS Cnt_Product, MIN(P.Retail_Price) AS Min_RtlPrc, AVG(P.Retail_Price) AS Avg_RtlPrc, MAX(P.Retail_Price) AS Max_RtlPrc
FROM CATEGORY AS C
LEFT JOIN ASSIGNED AS A ON C.Category_Name = A.Category_Name 
LEFT JOIN PRODUCT AS P ON A.PID = P.PID
GROUP BY C.Category_Name
ORDER BY C.Category_Name ASC;


-- verify SQL - Report 2
SELECT P.PID, P.Product_Name, P.Retail_Price, 
SUM(IFNULL(S.Quantity,0)) AS Tot_UnitSold, 
SUM(IF(D.Discount_Price IS NULL,0,1) * IFNULL(S.Quantity,0)) AS Tot_UnitSold_AtDsct,
SUM(IF(D.Discount_Price IS NULL,1,0) * IFNULL(S.Quantity,0)) AS Tot_UnitSold_AtRtl,
SUM(IFNULL(S.Total_Amount,0)) AS Act_Revenue,
SUM(P.Retail_Price * IFNULL(S.Quantity,0) * IF(D.Discount_Price IS NULL, 1, 0.75)) AS Pred_Revenue,
(SUM(IFNULL(S.Total_Amount,0)) - SUM(P.Retail_Price * IFNULL(S.Quantity,0) * IF(D.Discount_Price IS NULL, 1, 0.75))) AS Diff_Act_Pred_Revenue
FROM CATEGORY AS C
LEFT JOIN ASSIGNED AS A ON C.Category_Name = A.Category_Name 
LEFT JOIN PRODUCT AS P ON A.PID = P.PID
LEFT JOIN SALE AS S ON P.PID = S.PID
LEFT JOIN DISCOUNT AS D ON S.Date = D.Date AND S.PID = D.PID 
WHERE C.Category_Name = 'Couches and Sofas'
GROUP BY P.PID
HAVING Diff_Act_Pred_Revenue > 5000 OR Diff_Act_Pred_Revenue < - 5000
ORDER BY Diff_Act_Pred_Revenue DESC;

