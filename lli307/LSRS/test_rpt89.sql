/*
INSERT INTO CITY
VALUES ('NY', 'New York', 8419000);
INSERT INTO CITY
VALUES ('NJ', 'New Jersey', 8882000);

INSERT INTO `DAY`
VALUES ('2021-4-1');
INSERT INTO `DAY`
VALUES ('2021-1-1');
INSERT INTO HOLIDAY
VALUES ('2021-4-1', 'Fools');
*/

-- insert sample data
INSERT INTO CITY
VALUES 
('NY', 'New York', 8419000);

INSERT INTO CHILDCARE
VALUES 
(30);
#(60);

INSERT INTO STORE
VALUES 
#('Store_Number_1', '1234567891', 'Street_Address_1', 1, 0, 'NY', 'New York', 30),
('Store_Number_2', '1234567892', 'Street_Address_2', 0, 0, 'NY', 'New York', 60);

INSERT INTO PRODUCT
VALUES 
('PID_1', 'Product_Name_1', 10), 
('PID_2', 'Product_Name_2', 20),
('PID_3', 'Product_Name_3', 30);

INSERT INTO CATEGORY
VALUES 
('Couches'), 
('Pots and Pans');

INSERT INTO ASSIGNED
VALUES 
('PID_1', 'Couches'), 
('PID_2', 'Pots and Pans'), 
('PID_3', 'Pots and Pans');

INSERT INTO `DAY`
VALUES 
('2012-5-1'), 
('2012-6-1'), 
('2012-6-2');

INSERT INTO SALE
VALUES 
('2012-5-1', 'Store_Number_1', 'PID_1', 5,  50), 
('2012-6-1', 'Store_Number_1', 'PID_1', 10, 80), 
('2012-6-2', 'Store_Number_1', 'PID_1', 5,  35),
('2012-6-2', 'Store_Number_1', 'PID_2', 5,  100),
('2012-6-2', 'Store_Number_2', 'PID_3', 5,  150);

INSERT INTO DISCOUNT
VALUES  
('2012-6-1', 'PID_1', 8), 
('2012-6-2', 'PID_1', 7);

INSERT INTO ADVERTISING_CAMPAIGN
VALUES ('June-1 Ad');

INSERT INTO HOLD
VALUES ('2012-6-1', 'June-1 Ad');


-- verify insertion results
/*
SELECT * FROM CITY;
SELECT * FROM CHILDCARE;
SELECT * FROM STORE;
SELECT * FROM PRODUCT;
SELECT * FROM CATEGORY;
SELECT * FROM ASSIGNED;
SELECT * FROM `DAY`;
SELECT * FROM SALE;
SELECT * FROM DISCOUNT;
SELECT * FROM ADVERTISING_CAMPAIGN;
SELECT * FROM HOLD;
*/


-- verify SQL - Report 8
SELECT COLS.Category, COLS.`Store Type`, IFNULL(ACT.`Quantity Sold`, 0) AS `Quantity Sold`
FROM
( ( SELECT C01.Category_Name AS Category, 'Restaurant' AS `Store Type` FROM CATEGORY AS C01)
UNION
( SELECT C02.Category_Name AS Category, 'Non-restaurant' AS `Store Type` FROM CATEGORY AS C02) ) 
AS COLS
LEFT JOIN 
(
	SELECT
	C.Category_Name AS Category,
	IF(T.Has_Restaurant IS TRUE, 'Restaurant', 'Non-restaurant') AS `Store Type`, 
	SUM(S.Quantity) AS `Quantity Sold`
	FROM CATEGORY AS C
	INNER JOIN ASSIGNED AS A ON C.Category_Name = A.Category_Name 
	INNER JOIN PRODUCT AS P ON A.PID = P.PID
	INNER JOIN SALE AS S ON P.PID = S.PID
	INNER JOIN STORE AS T ON S.Store_Number = T.Store_Number 
	GROUP BY Category, `Store Type`
) AS ACT
ON COLS.Category = ACT.Category AND COLS.`Store Type` = ACT.`Store Type` 
ORDER BY COLS.Category ASC, COLS.`Store Type` ASC;


-- verify SQL - Report 9
SELECT `Product ID`, `Product Name`, `Sold During Campaign`, `Sold Outside Campaign`, Difference 
FROM(
	(
		SELECT P.PID AS `Product ID`, P.Product_Name AS `Product Name`, 
		SUM(IF(A.`Description` IS NULL,0,1) * IFNULL(S.Quantity,0)) AS `Sold During Campaign`, 
		SUM(IF(A.`Description` IS NULL,1,0) * IFNULL(S.Quantity,0)) AS `Sold Outside Campaign`, 
		(SUM(IF(A.`Description` IS NULL,0,1) * IFNULL(S.Quantity,0)) -
		SUM(IF(A.`Description` IS NULL,1,0) * IFNULL(S.Quantity,0))) AS Difference 
		FROM PRODUCT AS P
		INNER JOIN DISCOUNT AS I ON P.PID = I.PID
		LEFT JOIN SALE AS S ON I.`Date` = S.`Date` AND I.PID = S.PID
		LEFT JOIN DAY AS D ON S.`Date` = D.`Date`
		LEFT JOIN HOLD AS H ON D.`Date` = H.`Date`
		LEFT JOIN ADVERTISING_CAMPAIGN AS A ON H.`Description` = A.`Description`
		GROUP BY `Product ID`
		ORDER BY Difference DESC
		LIMIT 10
	)
	UNION
	(
		SELECT P2.PID AS `Product ID`, P2.Product_Name AS `Product Name`, 
		SUM(IF(A2.`Description` IS NULL,0,1) * IFNULL(S2.Quantity,0)) AS `Sold During Campaign`, 
		SUM(IF(A2.`Description` IS NULL,1,0) * IFNULL(S2.Quantity,0)) AS `Sold Outside Campaign`, 
		(SUM(IF(A2.`Description` IS NULL,0,1) * IFNULL(S2.Quantity,0)) -
		SUM(IF(A2.`Description` IS NULL,1,0) * IFNULL(S2.Quantity,0))) AS Difference 
		FROM PRODUCT AS P2
		INNER JOIN DISCOUNT AS I2 ON P2.PID = I2.PID
		LEFT JOIN SALE AS S2 ON I2.`Date` = S2.`Date` AND I2.PID = S2.PID
		LEFT JOIN DAY AS D2 ON S2.`Date` = D2.`Date`
		LEFT JOIN HOLD AS H2 ON D2.`Date` = H2.`Date`
		LEFT JOIN ADVERTISING_CAMPAIGN AS A2 ON H2.`Description` = A2.`Description` 
		GROUP BY `Product ID`
		ORDER BY Difference ASC
		LIMIT 10
	)
	) AS UN
ORDER BY Difference DESC;


