INSERT INTO CITY
VALUES
('NY', 'New York', 8419000);

INSERT INTO CHILDCARE
VALUES
(30);

INSERT INTO `DAY`
VALUES
('2012-02-02'),
('2012-06-02'),
('2013-09-02');

INSERT INTO STORE
VALUES
('Store_Number_1', '1234567890', 'Street_Address_1', 0, 0, 'NY', 'New York', 30);

INSERT INTO PRODUCT
VALUES
('PID_1', 'Product_Name_1', 10),
('PID_2', 'Product_Name_2', 20),
('PID_3', 'Product_Name_3', 7);

INSERT INTO CATEGORY
VALUES
('Couches and Sofas'),
('Outdoor Furniture'),
('NO product category');


INSERT INTO ASSIGNED
VALUES
('PID_1', 'Couches and Sofas'),
('PID_2', 'Outdoor Furniture'),
('PID_3', 'Outdoor Furniture');


INSERT INTO SALE
VALUES
('2012-02-02', 'Store_Number_1', 'PID_2', 10, 80),
('2012-06-02', 'Store_Number_1', 'PID_1', 5,  100),
('2013-09-02', 'Store_Number_1', 'PID_3', 100, 20);

INSERT INTO DISCOUNT
VALUES
('2012-02-02', 'PID_2', 8),
('2013-09-02', 'PID_3', 7);












