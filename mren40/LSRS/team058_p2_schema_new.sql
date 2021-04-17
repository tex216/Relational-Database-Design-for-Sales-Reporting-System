-- CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'password';
CREATE USER IF NOT EXISTS gatechUser058@localhost IDENTIFIED BY 'gatech058';

DROP DATABASE IF EXISTS `cs6400_sp21_team058`; 
SET default_storage_engine=InnoDB;
SET NAMES utf8mb4 COLLATE utf8mb4_unicode_ci;

CREATE DATABASE IF NOT EXISTS cs6400_sp21_team058 
    DEFAULT CHARACTER SET utf8mb4 
    DEFAULT COLLATE utf8mb4_unicode_ci;
USE cs6400_sp21_team058;

GRANT SELECT, INSERT, UPDATE, DELETE, FILE ON *.* TO 'gatechUser058'@'localhost';
GRANT ALL PRIVILEGES ON `gatechuser`.* TO 'gatechUser058'@'localhost';
GRANT ALL PRIVILEGES ON `cs6400_sp21_team058`.* TO 'gatechUser058'@'localhost';
FLUSH PRIVILEGES;


-- CREATE TABLEs 
CREATE TABLE STORE (
  Store_Number varchar(50) NOT NULL,
  Phone_Number varchar(14),
  Street_Address varchar(200) NOT NULL,
  Has_Restaurant tinyint NOT NULL,
  Has_Snack_Bar tinyint NOT NULL,
  State_Location varchar(50) NOT NULL,
  City_Name varchar(50) NOT NULL,
  Time_Limit int NULL,
  PRIMARY KEY (Store_Number) 
);

CREATE TABLE CITY (
  State_Location varchar(50) NOT NULL,
  City_Name varchar(50) NOT NULL,
  Population int NOT NULL,
  PRIMARY KEY (State_Location, City_Name)
);

CREATE TABLE CHILDCARE (
  Time_Limit int NOT NULL,
  PRIMARY KEY (Time_Limit)
);

CREATE TABLE PRODUCT (
  PID varchar(50) NOT NULL,
  Product_Name varchar(50) NOT NULL,
  Retail_Price float NOT NULL,
  PRIMARY KEY (PID)
);

CREATE TABLE SELL (
  Store_Number varchar(50) NOT NULL,
  PID varchar(50) NOT NULL,
  PRIMARY KEY (Store_Number, PID),
  FOREIGN KEY (PID) REFERENCES PRODUCT (PID) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (Store_Number) REFERENCES STORE (Store_Number) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE `DAY` (
  `Date` date NOT NULL,
  PRIMARY KEY (`Date`)
);

CREATE TABLE SALE (
  `Date` date NOT NULL,
  Store_Number varchar(50) NOT NULL,
  PID varchar(50) NOT NULL,
  Quantity int NOT NULL,
  Total_Amount float NOT NULL,
  PRIMARY KEY (`Date`, Store_Number, PID),
  FOREIGN KEY (`Date`) REFERENCES `DAY` (`Date`) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (PID) REFERENCES PRODUCT (PID) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (Store_Number) REFERENCES STORE (Store_Number) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE CATEGORY (
  Category_Name varchar(50) NOT NULL,
  PRIMARY KEY (Category_Name)
);

CREATE TABLE ASSIGNED (
  PID varchar(50) NOT NULL,
  Category_Name varchar(50) NOT NULL,
  PRIMARY KEY (PID, Category_Name),
  FOREIGN KEY (Category_Name) REFERENCES CATEGORY (Category_Name) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (PID) REFERENCES PRODUCT (PID) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE HOLIDAY (
  `Date` date NOT NULL,
  `Name` varchar(50) NOT NULL,
  PRIMARY KEY (`Date`, `Name`),
  FOREIGN KEY (`Date`) REFERENCES `DAY` (`Date`) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE DISCOUNT (
  `Date` date NOT NULL,
  PID varchar(50) NOT NULL,
  Discount_Price float NOT NULL,
  PRIMARY KEY (`Date`, PID),
  FOREIGN KEY (`Date`) REFERENCES `DAY` (`Date`) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (PID) REFERENCES PRODUCT (PID) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE ADVERTISING_CAMPAIGN (
  `Description` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`Description`)
);

CREATE TABLE HOLD (
  `Date` date NOT NULL,
  `Description` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`Date`, `Description`),
  FOREIGN KEY (`Date`) REFERENCES `DAY` (`Date`) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (`Description`) REFERENCES ADVERTISING_CAMPAIGN (`Description`) ON DELETE CASCADE ON UPDATE CASCADE
);


-- Add more CONSTRAINT
ALTER TABLE STORE
ADD CONSTRAINT fk_STORE_StateLocation_CityName_CITY_StateLocation_CityName FOREIGN KEY (State_Location, City_Name) REFERENCES CITY (State_Location, City_Name);  
ALTER TABLE STORE
ADD CONSTRAINT fk_STORE_TimeLimit_CHILDCARE_TimeLimit FOREIGN KEY (Time_Limit) REFERENCES CHILDCARE (Time_Limit);