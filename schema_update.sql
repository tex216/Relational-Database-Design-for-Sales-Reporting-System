-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               8.0.23 - MySQL Community Server - GPL
-- Server OS:                    Win64
-- HeidiSQL Version:             11.2.0.6213
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Dumping database structure for lsrs
CREATE DATABASE IF NOT EXISTS `lsrs` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `lsrs`;

-- Dumping structure for table lsrs.advertising_campaign
CREATE TABLE IF NOT EXISTS `advertising_campaign` (
  `Description` varchar(50) NOT NULL,
  PRIMARY KEY (`Description`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table lsrs.advertising_campaign: ~0 rows (approximately)
/*!40000 ALTER TABLE `advertising_campaign` DISABLE KEYS */;
/*!40000 ALTER TABLE `advertising_campaign` ENABLE KEYS */;

-- Dumping structure for table lsrs.assigned
CREATE TABLE IF NOT EXISTS `assigned` (
  `PID` varchar(50) NOT NULL,
  `Category_Name` varchar(50) NOT NULL,
  KEY `FK__product_assigned` (`PID`),
  KEY `FK__assigned_category` (`Category_Name`),
  CONSTRAINT `FK__assigned_category` FOREIGN KEY (`Category_Name`) REFERENCES `category` (`Category_Name`),
  CONSTRAINT `FK__product_assigned` FOREIGN KEY (`PID`) REFERENCES `product` (`PID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table lsrs.assigned: ~0 rows (approximately)
/*!40000 ALTER TABLE `assigned` DISABLE KEYS */;
/*!40000 ALTER TABLE `assigned` ENABLE KEYS */;

-- Dumping structure for table lsrs.category
CREATE TABLE IF NOT EXISTS `category` (
  `Category_Name` varchar(50) NOT NULL,
  PRIMARY KEY (`Category_Name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table lsrs.category: ~0 rows (approximately)
/*!40000 ALTER TABLE `category` DISABLE KEYS */;
/*!40000 ALTER TABLE `category` ENABLE KEYS */;

-- Dumping structure for table lsrs.childcare
CREATE TABLE IF NOT EXISTS `childcare` (
  `Limit` int unsigned NOT NULL DEFAULT '30',
  `Store_Number` varchar(50) NOT NULL,
  KEY `FK__childcare_store` (`Store_Number`) USING BTREE,
  CONSTRAINT `FK__store` FOREIGN KEY (`Store_Number`) REFERENCES `store` (`Stroe_Number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table lsrs.childcare: ~0 rows (approximately)
/*!40000 ALTER TABLE `childcare` DISABLE KEYS */;
/*!40000 ALTER TABLE `childcare` ENABLE KEYS */;

-- Dumping structure for table lsrs.city
CREATE TABLE IF NOT EXISTS `city` (
  `State_Location` varchar(50) NOT NULL,
  `City_Name` varchar(50) NOT NULL,
  `Population` int NOT NULL,
  `Population_Size_Category` varchar(50) NOT NULL,
  PRIMARY KEY (`State_Location`,`City_Name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table lsrs.city: ~0 rows (approximately)
/*!40000 ALTER TABLE `city` DISABLE KEYS */;
/*!40000 ALTER TABLE `city` ENABLE KEYS */;

-- Dumping structure for table lsrs.day
CREATE TABLE IF NOT EXISTS `day` (
  `Date` date NOT NULL,
  PRIMARY KEY (`Date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table lsrs.day: ~0 rows (approximately)
/*!40000 ALTER TABLE `day` DISABLE KEYS */;
/*!40000 ALTER TABLE `day` ENABLE KEYS */;

-- Dumping structure for table lsrs.discount
CREATE TABLE IF NOT EXISTS `discount` (
  `Discount_Price` float NOT NULL,
  `PID` varchar(50) NOT NULL,
  `Date` date NOT NULL,
  KEY `FK_discount_product` (`PID`),
  KEY `FK_discount_day` (`Date`),
  CONSTRAINT `FK_discount_day` FOREIGN KEY (`Date`) REFERENCES `day` (`Date`),
  CONSTRAINT `FK_discount_product` FOREIGN KEY (`PID`) REFERENCES `product` (`PID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table lsrs.discount: ~0 rows (approximately)
/*!40000 ALTER TABLE `discount` DISABLE KEYS */;
/*!40000 ALTER TABLE `discount` ENABLE KEYS */;

-- Dumping structure for table lsrs.hold
CREATE TABLE IF NOT EXISTS `hold` (
  `Description` varchar(50) NOT NULL,
  `Date` date NOT NULL,
  KEY `FK__day_hold` (`Date`),
  KEY `FK_hold_advertising_campaign` (`Description`),
  CONSTRAINT `FK__day_hold` FOREIGN KEY (`Date`) REFERENCES `day` (`Date`) ON UPDATE RESTRICT,
  CONSTRAINT `FK_hold_advertising_campaign` FOREIGN KEY (`Description`) REFERENCES `advertising_campaign` (`Description`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table lsrs.hold: ~0 rows (approximately)
/*!40000 ALTER TABLE `hold` DISABLE KEYS */;
/*!40000 ALTER TABLE `hold` ENABLE KEYS */;

-- Dumping structure for table lsrs.holiday
CREATE TABLE IF NOT EXISTS `holiday` (
  `Name` varchar(50) NOT NULL,
  `Date` date NOT NULL,
  KEY `FK_holiday_day` (`Date`),
  CONSTRAINT `FK_holiday_day` FOREIGN KEY (`Date`) REFERENCES `day` (`Date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table lsrs.holiday: ~0 rows (approximately)
/*!40000 ALTER TABLE `holiday` DISABLE KEYS */;
/*!40000 ALTER TABLE `holiday` ENABLE KEYS */;

-- Dumping structure for table lsrs.product
CREATE TABLE IF NOT EXISTS `product` (
  `PID` varchar(50) NOT NULL,
  `Product_Name` varchar(50) NOT NULL,
  `Retail_Price` float NOT NULL,
  PRIMARY KEY (`PID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table lsrs.product: ~0 rows (approximately)
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
/*!40000 ALTER TABLE `product` ENABLE KEYS */;

-- Dumping structure for table lsrs.sale
CREATE TABLE IF NOT EXISTS `sale` (
  `Quantity` int NOT NULL,
  `Total_Amount` float NOT NULL,
  `PID` varchar(50) NOT NULL,
  `Store_Number` varchar(50) NOT NULL,
  `Date` date NOT NULL,
  KEY `FK__sale_store` (`Store_Number`),
  KEY `FK__sale_day` (`Date`),
  KEY `FK__sale_product` (`PID`),
  CONSTRAINT `FK__sale_day` FOREIGN KEY (`Date`) REFERENCES `day` (`Date`) ON UPDATE RESTRICT,
  CONSTRAINT `FK__sale_product` FOREIGN KEY (`PID`) REFERENCES `product` (`PID`) ON UPDATE RESTRICT,
  CONSTRAINT `FK__sale_store` FOREIGN KEY (`Store_Number`) REFERENCES `store` (`Stroe_Number`) ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table lsrs.sale: ~0 rows (approximately)
/*!40000 ALTER TABLE `sale` DISABLE KEYS */;
/*!40000 ALTER TABLE `sale` ENABLE KEYS */;

-- Dumping structure for table lsrs.sell
CREATE TABLE IF NOT EXISTS `sell` (
  `Store_Number` varchar(50) NOT NULL,
  `PID` varchar(50) NOT NULL,
  KEY `FK__sell_product` (`PID`),
  KEY `FK__store_sell` (`Store_Number`),
  CONSTRAINT `FK__sell_product` FOREIGN KEY (`PID`) REFERENCES `product` (`PID`),
  CONSTRAINT `FK__store_sell` FOREIGN KEY (`Store_Number`) REFERENCES `store` (`Stroe_Number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table lsrs.sell: ~0 rows (approximately)
/*!40000 ALTER TABLE `sell` DISABLE KEYS */;
/*!40000 ALTER TABLE `sell` ENABLE KEYS */;

-- Dumping structure for table lsrs.store
CREATE TABLE IF NOT EXISTS `store` (
  `Stroe_Number` varchar(50) NOT NULL,
  `Phone_Number` varchar(50) NOT NULL,
  `Street_Address` varchar(50) NOT NULL,
  `Has_Restaurant` tinyint NOT NULL DEFAULT '1',
  `Has_Snack_Bar` tinyint NOT NULL DEFAULT '1',
  `State_Location` varchar(50) NOT NULL,
  `City_Name` varchar(50) NOT NULL,
  PRIMARY KEY (`Stroe_Number`),
  KEY `Foreign Keys` (`State_Location`,`City_Name`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table lsrs.store: ~0 rows (approximately)
/*!40000 ALTER TABLE `store` DISABLE KEYS */;
/*!40000 ALTER TABLE `store` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
