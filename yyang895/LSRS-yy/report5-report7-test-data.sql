
INSERT INTO `ADVERTISING_CAMPAIGN` 
VALUES ('New Year Ad Campaign'),('Thanksgiving Ad Campaign');

INSERT INTO `ASSIGNED` 
VALUES ('1','Bedroom'),('2','Bedroom'),('3','Bedroom'),('5','Dining Room'),('4','Living Room');

INSERT INTO `CATEGORY` 
VALUES ('Bedroom'),('Dining Room'),('Living Room');

INSERT INTO `CHILDCARE` 
VALUES (30),(60),(120);

INSERT INTO `CITY` 
VALUES ('NC','Raleign',300000),('NY','Buffalo',350001),('NY','New York',670001),('WA','Seattle',3700000);

INSERT INTO `DAY` 
VALUES ('2020-11-26'),('2020-12-25'),('2021-01-01'),('2021-01-02'),('2021-01-03'),('2021-02-01'),('2021-03-01'),('2021-03-02');

INSERT INTO `HOLD` 
VALUES ('2021-01-01','New Year Ad Campaign'),('2021-01-02','New Year Ad Campaign'),('2021-01-03','New Year Ad Campaign'),('2020-11-26','Thanksgiving Ad Campaign');

INSERT INTO `HOLIDAY` 
VALUES ('2020-12-25','Christmas'),('2021-01-01','New Year');

INSERT INTO `PRODUCT` 
VALUES ('1','Chair',125),('2','Desk',160),('3','Mattress',500),('4','Sofa',4200),('5','Dining table',1900);

INSERT INTO `SALE` 
VALUES ('2020-11-26','Store_Number_3','3',20,10000),('2021-01-01','Store_Number_2','3',10,5000),
('2021-01-02','Store_Number_1','1',20,2500),('2021-01-03','Store_Number_3','2',10,1600),('2021-02-01','Store_Number_2','4',10,42000),
('2021-03-01','Store_Number_1','5',10,19000),('2021-03-02','Store_Number_3','1',20,2500),('2021-03-02','Store_Number_3','5',10,2500),
('2021-03-02','Store_Number_5','1',20,2500);

INSERT INTO `STORE` 
VALUES ('Store_Number_1','1234567890','Street_Address_1',0,0,'NY','New York',60),
('Store_Number_2','9175624545','Street_Address_2',1,0,'NY','Buffalo',30),
('Store_Number_3','6519192954','Street_Address_3',1,1,'WA','Seattle',120),
('Store_Number_4','4587965145','Street_Address_4',1,0,'NY','Buffalo',NULL),
('Store_Number_5','4568521549','Street_Address_5',1,1,'NC','Raleign',NULL);

