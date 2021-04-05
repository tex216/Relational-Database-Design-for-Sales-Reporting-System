import pymysql


class SqlHelper(object):
    def __init__(self):
        self.conn = pymysql.connect(
            host="127.0.0.1", port=3306, user="root", passwd="spring2021_cs6400", db="cs6400_sp21_team058"
        )
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def get_report8(self):
        self.cursor.execute(
            "SELECT COLS.Category, COLS.`Store Type` AS StoreType, IFNULL(ACT.`Quantity Sold`, 0) AS QuantitySold "
            "FROM "
            "( ( SELECT C01.Category_Name AS Category, 'Restaurant' AS `Store Type` FROM CATEGORY AS C01) "
            "UNION "
            "( SELECT C02.Category_Name AS Category, 'Non-restaurant' AS `Store Type` FROM CATEGORY AS C02) ) "
            "AS COLS "
            "LEFT JOIN "
            "(SELECT C.Category_Name AS Category, "
            "IF(T.Has_Restaurant IS TRUE, 'Restaurant', 'Non-restaurant') AS `Store Type`, "
            "SUM(S.Quantity) AS `Quantity Sold` "
            "FROM CATEGORY AS C "
            "INNER JOIN ASSIGNED AS A ON C.Category_Name = A.Category_Name "
            "INNER JOIN PRODUCT AS P ON A.PID = P.PID "
            "INNER JOIN SALE AS S ON P.PID = S.PID "
            "INNER JOIN STORE AS T ON S.Store_Number = T.Store_Number "
            "GROUP BY Category, `Store Type` "
            ") AS ACT "
            "ON COLS.Category = ACT.Category AND COLS.`Store Type` = ACT.`Store Type` "
            "ORDER BY COLS.Category ASC, COLS.`Store Type` ASC; "
        )
        report8_res = self.cursor.fetchall()
        return report8_res

    def get_report9(self):
        self.cursor.execute(
            "SELECT `Product ID` AS ProductID, `Product Name` AS ProductName, `Sold During Campaign`, `Sold Outside Campaign`, Difference "
            "FROM( "
            "( "
            "SELECT P.PID AS `Product ID`, P.Product_Name AS `Product Name`, "
            "SUM(IF(A.`Description` IS NULL,0,1) * IFNULL(S.Quantity,0)) AS `Sold During Campaign`, "
            "SUM(IF(A.`Description` IS NULL,1,0) * IFNULL(S.Quantity,0)) AS `Sold Outside Campaign`, "
            "(SUM(IF(A.`Description` IS NULL,0,1) * IFNULL(S.Quantity,0)) - "
            "SUM(IF(A.`Description` IS NULL,1,0) * IFNULL(S.Quantity,0))) AS Difference "
            "FROM PRODUCT AS P "
            "INNER JOIN DISCOUNT AS I ON P.PID = I.PID "
            "LEFT JOIN SALE AS S ON I.`Date` = S.`Date` AND I.PID = S.PID "
            "LEFT JOIN DAY AS D ON S.`Date` = D.`Date` "
            "LEFT JOIN HOLD AS H ON D.`Date` = H.`Date` "
            "LEFT JOIN ADVERTISING_CAMPAIGN AS A ON H.`Description` = A.`Description` "
            "GROUP BY `Product ID` "
            "ORDER BY Difference DESC "
            "LIMIT 10 "
            ") "
            "UNION "
            "( "
            "SELECT P2.PID AS `Product ID`, P2.Product_Name AS `Product Name`, "
            "SUM(IF(A2.`Description` IS NULL,0,1) * IFNULL(S2.Quantity,0)) AS `Sold During Campaign`, "
            "SUM(IF(A2.`Description` IS NULL,1,0) * IFNULL(S2.Quantity,0)) AS `Sold Outside Campaign`, "
            "(SUM(IF(A2.`Description` IS NULL,0,1) * IFNULL(S2.Quantity,0)) - "
            "SUM(IF(A2.`Description` IS NULL,1,0) * IFNULL(S2.Quantity,0))) AS Difference "
            "FROM PRODUCT AS P2 "
            "INNER JOIN DISCOUNT AS I2 ON P2.PID = I2.PID "
            "LEFT JOIN SALE AS S2 ON I2.`Date` = S2.`Date` AND I2.PID = S2.PID "
            "LEFT JOIN DAY AS D2 ON S2.`Date` = D2.`Date` "
            "LEFT JOIN HOLD AS H2 ON D2.`Date` = H2.`Date` "
            "LEFT JOIN ADVERTISING_CAMPAIGN AS A2 ON H2.`Description` = A2.`Description` "
            "GROUP BY `Product ID` "
            "ORDER BY Difference ASC "
            "LIMIT 10 "
            ") "
            ") AS UN "
            "ORDER BY Difference DESC; "
        )
        report9_res = self.cursor.fetchall()
        return report9_res

    def close(self):
        self.cursor.close()
        self.conn.close()
