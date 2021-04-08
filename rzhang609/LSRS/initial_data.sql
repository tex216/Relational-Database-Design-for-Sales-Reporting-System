
INSERT INTO CITY(state_location, city_name, population)
VALUES 
('NY', 'New York', 670000), 
('NY', 'Buffalo', 350000), 
('WA', 'Seattle', 3700000), 
('CA', 'Los Angeles', 3792621),
('CA', 'San Diego', 1423851),
('IL', 'Chicago', 2695598);


INSERT INTO Day
VALUES 
('2013-5-1'), 
('2014-6-1'), 
('2015-6-2'),
('2016-6-2'), 
('2017-6-2'), 
('2018-6-2'),
('2021-1-1'),
('2012-5-1'), 
('2012-6-1'), 
('2012-6-2'),
('2020-11-26'),
('2012-2-2'),
('2012-6-3'),
('2013-4-28'),
('2013-4-29'),
('2013-9-02');


INSERT INTO Holiday(DATE, Name)
VALUES('2021-01-01', 'New Year');

INSERT INTO CHILDCARE
VALUES 
(30),
(60);




INSERT INTO STORE
VALUES 
('Store_Number_1', '1234567891', 'Street_Address_1', 1, 0, 'NY', 'New York', 30),
('Store_Number_2', '1234567892', 'Street_Address_2', 0, 0, 'NY', 'New York', 60),
('Store_Number_3', '1234567893', 'Street_Address_3', 1, 1, 'NY', 'New York', 30),
('Store_Number_4', '1234567894', 'Street_Address_4', 0, 0, 'NY', 'New York', 30),
('Store_Number_5', '1234567895', 'Street_Address_5', 1, 1, 'IL', 'Chicago', 30),
('Store_Number_6', '1234567896', 'Street_Address_6', 0, 0, 'IL', 'Chicago', 60),
('Store_Number_7', '1234567897', 'Street_Address_7', 1, 1, 'CA', 'Los Angeles', 60),
('Store_Number_8', '1234567898', 'Street_Address_8', 0, 0, 'CA', 'Los Angeles', 60),
('Store_Number_9', '1234567899', 'Street_Address_9', 1, 1, 'CA', 'San Diego', 60),
('Store_Number_10', '1234567809', 'Street_Address_10', 0, 0, 'CA', 'San Diego', 30);



INSERT INTO ADVERTISING_CAMPAIGN
VALUES ('New Year Ad Campaign'), ('Thanksgiving Ad Campaign'), ('June-1 Ad');





INSERT INTO PRODUCT
VALUES 
('PID_1', 'Product_Name_1', 10), 
('PID_2', 'Product_Name_2', 20),
('PID_3', 'Product_Name_3', 30),
('PID_4', 'Product_Name_4', 400);

INSERT INTO CATEGORY
VALUES 
('Couches'), 
('Pots and Pans'),
('Couches and Sofas'),
('Outdoor Furniture'),
('NO product category');

INSERT INTO ASSIGNED
VALUES 
('PID_1', 'Couches'), 
('PID_2', 'Pots and Pans'), 
('PID_3', 'Pots and Pans'),
('PID_1', 'Couches and Sofas'),
('PID_2', 'Outdoor Furniture'),
('PID_3', 'Outdoor Furniture'),
('PID_4', 'Couches and Sofas');

INSERT INTO DISCOUNT
VALUES  
('2012-6-1', 'PID_1', 8), 
('2012-02-02', 'PID_2', 8),
('2012-06-02', 'PID_1', 20),
('2013-09-02', 'PID_3', 7),
('2013-04-28', 'PID_4', 15);

INSERT INTO SALE
VALUES 
('2013-5-1', 'Store_Number_3', 'PID_1', 5,  50), 
('2014-6-1', 'Store_Number_4', 'PID_1', 10, 80), 
('2015-6-2', 'Store_Number_5', 'PID_1', 5,  35),
('2016-6-2', 'Store_Number_6', 'PID_2', 5,  100),
('2017-6-2', 'Store_Number_7', 'PID_3', 5,  150),
('2018-6-2', 'Store_Number_8', 'PID_3', 5,  150),
('2017-6-2', 'Store_Number_9', 'PID_3', 20,  150),
('2018-6-2', 'Store_Number_10', 'PID_3', 15,  150),
('2017-6-2', 'Store_Number_7', 'PID_1', 5,  250),
('2018-6-2', 'Store_Number_8', 'PID_2', 5,  100),
('2012-5-1', 'Store_Number_1', 'PID_1', 5,  50), 
('2012-6-1', 'Store_Number_1', 'PID_1', 10, 80), 
('2012-6-2', 'Store_Number_1', 'PID_2', 5,  100),
('2012-6-2', 'Store_Number_2', 'PID_3', 5,  150),
('2012-02-02', 'Store_Number_1', 'PID_2', 10, 80),
('2012-06-02', 'Store_Number_1', 'PID_1', 50000, 800000),
('2012-06-03', 'Store_Number_1', 'PID_1', 5000, 80000),
('2013-04-28', 'Store_Number_1', 'PID_4', 10000, 350000),
('2013-04-29', 'Store_Number_1', 'PID_4', 1000, 35000),
('2013-09-02', 'Store_Number_1', 'PID_3', 100, 20);





