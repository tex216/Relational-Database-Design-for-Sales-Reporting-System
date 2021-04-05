import pymysql


class SqlHelper(object):
    def __init__(self):
        self.conn = pymysql.connect(
            host="127.0.0.1", port=3306, user="root", passwd="spring2021_cs6400", db="cs6400_sp21_team058"
        )
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def get_report8(self):
        self.cursor.execute(
            "SELECT COLS.Category, COLS.`Store Type`, IFNULL(ACT.`Quantity Sold`, 0)"
            "FROM"
            "( ( SELECT C01.Category_Name AS Category, 'Restaurant' AS `Store Type` FROM CATEGORY AS C01)"
            "UNION"
            "( SELECT C02.Category_Name AS Category, 'Non-restaurant' AS `Store Type` FROM CATEGORY AS C02) ) AS COLS"
            "LEFT JOIN"
            "(SELECT C.Category_Name AS Category,"
            "IF(T.Has_Restaurant IS TRUE, 'Restaurant', 'Non-restaurant') AS `Store Type`, SUM(S.Quantity) AS `Quantity Sold`"
            "FROM CATEGORY AS C"
            "INNER JOIN ASSIGNED AS A ON C.Category_Name = A.Category_Name INNER JOIN PRODUCT AS P ON A.PID = P.PID"
            "INNER JOIN SALE AS S ON P.PID = S.PID"
            "INNER JOIN STORE AS T ON S.Store_Number = T.Store_Number GROUP BY Category, `Store Type`"
            ") AS ACT"
            "ON COLS.Category = ACT.Category AND COLS.`Store Type` = ACT.`Store Type`"
            "ORDER BY COLS.Category ASC, COLS.`Store Type` ASC;"
        )
        report8_res = self.cursor.fetchall()
        return report8_res

    def close(self):
        self.cursor.close()
        self.conn.close()
