INSERT INTO CITY
VALUES 
('CA', 'Los Angeles', 3792621),
('CA', 'San Diego', 1423851),
('IL', 'Chicago', 2695598);

INSERT INTO `DAY`
VALUES 
('2013-5-1'), 
('2014-6-1'), 
('2015-6-2'),
('2016-6-2'), 
('2017-6-2'), 
('2018-6-2');


INSERT INTO STORE
VALUES 
('Store_Number_3', '1234567893', 'Street_Address_3', 1, 1, 'NY', 'New York', 30),
('Store_Number_4', '1234567894', 'Street_Address_4', 0, 0, 'NY', 'New York', 30),
('Store_Number_5', '1234567895', 'Street_Address_5', 1, 1, 'IL', 'Chicago', 30),
('Store_Number_6', '1234567896', 'Street_Address_6', 0, 0, 'IL', 'Chicago', 60),
('Store_Number_7', '1234567897', 'Street_Address_7', 1, 1, 'CA', 'Los Angeles', 60),
('Store_Number_8', '1234567898', 'Street_Address_8', 0, 0, 'CA', 'Los Angeles', 60),
('Store_Number_9', '1234567899', 'Street_Address_9', 1, 1, 'CA', 'San Diego', 60),
('Store_Number_10', '1234567809', 'Street_Address_10', 0, 0, 'CA', 'San Diego', 30);


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
('2018-6-2', 'Store_Number_8', 'PID_2', 5,  100);

