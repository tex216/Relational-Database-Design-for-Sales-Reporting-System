
CREATE TABLE STORE (
  Store_Number varchar(50) NOT NULL,
  Phone_Number char(10) NOT NULL,
  Street_Address varchar(200) NOT NULL,
  Has_Restaurant tinyint NOT NULL,
  Has_Snack_Bar tinyint NOT NULL,
  State_Location varchar(50) NOT NULL,
  City_Name varchar(50) NOT NULL,
  PRIMARY KEY (Store_Number) 
);

CREATE TABLE CITY (
  State_Location varchar(50) NOT NULL,
  City_Name varchar(50) NOT NULL,
  Population int NOT NULL,
  Population_Size_Category ENUM('Small', 'Medium', 'Large', 'Extra Large') NOT NULL,
  PRIMARY KEY (State_Location, City_Name)
);

CREATE TABLE CHILDCARE (
  Store_Number varchar(50) NOT NULL,
  `Limit` int NOT NULL,
  PRIMARY KEY (Store_Number),
  FOREIGN KEY (Store_Number) REFERENCES STORE (Store_Number) ON DELETE CASCADE ON UPDATE CASCADE
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
  `Description` varchar(50) NOT NULL,
  PRIMARY KEY (`Description`)
);

CREATE TABLE HOLD (
  `Date` date NOT NULL,
  `Description` varchar(50) NOT NULL,
  PRIMARY KEY (`Date`, `Description`),
  FOREIGN KEY (`Date`) REFERENCES `DAY` (`Date`) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (`Description`) REFERENCES ADVERTISING_CAMPAIGN (`Description`) ON DELETE CASCADE ON UPDATE CASCADE
);

ALTER TABLE STORE
ADD CONSTRAINT fk_STORE_State_Location_CITY_State_Location FOREIGN KEY (State_Location) REFERENCES CITY (State_Location),
ADD CONSTRAINT fk_STORE_City_Name_CITY_City_Name FOREIGN KEY (City_Name) REFERENCES CITY (City_Name);




