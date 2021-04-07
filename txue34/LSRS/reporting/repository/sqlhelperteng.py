import pymysql


class SqlHelper(object):

    def __init__(self):
        self.conn = pymysql.connect(
            host='127.0.0.1', port=3306, user='root',
            passwd='xueteng1993!',  db='cs6400_sp21_team058'
        )
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    # report 1 Category:  get data set
    def get_report1(self):
        self.cursor.execute(
            "SELECT C.Category_Name AS Cate_Name, COUNT(P.PID) AS Cnt_Product, MIN(P.Retail_Price) AS Min_RtlPrc, "
            "AVG(P.Retail_Price) AS Avg_RtlPrc, MAX(P.Retail_Price) AS Max_RtlPrc "
            "FROM CATEGORY AS C "
            "LEFT JOIN ASSIGNED AS A ON C.Category_Name = A.Category_Name "
            "LEFT JOIN PRODUCT AS P ON A.PID = P.PID "
            "GROUP BY C.Category_Name "
            "ORDER BY C.Category_Name ASC; "
        )
        report1_res = self.cursor.fetchall()
        return report1_res

    # report 2 Actual versus Predicted Revenue for Couches and Sofas: get data set
    def get_report2(self):
        self.cursor.execute(
            "SELECT P.PID AS PID, P.Product_Name AS Name, P.Retail_Price AS Price, "
            "SUM(IFNULL(S.Quantity,0)) AS Tot_UnitSold, "
            "SUM(IF(D.Discount_Price IS NULL,0,1) * IFNULL(S.Quantity,0)) AS Tot_UnitSold_AtDsct, "
            "SUM(IF(D.Discount_Price IS NULL,1,0) * IFNULL(S.Quantity,0)) AS Tot_UnitSold_AtRtl, "
            "SUM(IFNULL(S.Total_Amount,0)) AS Act_Revenue, "
            "SUM(P.Retail_Price * IFNULL(S.Quantity,0) * IF(D.Discount_Price IS NULL, 1, 0.75)) AS Pred_Revenue, "
            "(SUM(IFNULL(S.Total_Amount,0)) - SUM(P.Retail_Price * IFNULL(S.Quantity,0) * "
            "IF(D.Discount_Price IS NULL, 1, 0.75))) AS Diff_Act_Pred_Revenue "
            "FROM CATEGORY AS C "
            "LEFT JOIN ASSIGNED AS A ON C.Category_Name = A.Category_Name "
            "LEFT JOIN PRODUCT AS P ON A.PID = P.PID "
            "LEFT JOIN SALE AS S ON P.PID = S.PID "
            "LEFT JOIN DISCOUNT AS D ON S.Date = D.Date AND S.PID = D.PID "
            "WHERE C.Category_Name = 'Couches and Sofas' "
            "GROUP BY P.PID "
            "HAVING Diff_Act_Pred_Revenue > 5000 OR Diff_Act_Pred_Revenue < -5000 "
            "ORDER BY Diff_Act_Pred_Revenue DESC; "
        )
        report2_res = self.cursor.fetchall()
        return report2_res

    # report 4 Outdoor Furniture Revenue: get data set
    def get_report4(self):
        self.cursor.execute(
            "SELECT YEAR(Date) AS Year, SUM(IFNULL(Quantity, 0)) AS Tot_Quantity, "
            "(SUM(IFNULL(Quantity, 0)) / 365) AS Avg_Quantity, "
            "SUM(IF(MONTH(Date)=2 AND DAY(Date)=2,1,0) * IFNULL(Quantity, 0)) AS GhDay_Quantity "
            "FROM CATEGORY AS C "
            "LEFT JOIN ASSIGNED AS A ON C.Category_Name = A.Category_Name "
            "LEFT JOIN PRODUCT AS P ON A.PID = P.PID "
            "LEFT JOIN SALE AS S ON P.PID = S.PID "
            "WHERE C.Category_Name = 'Outdoor Furniture' "
            "GROUP BY YEAR(Date) "
            "ORDER BY YEAR(Date) ASC; "
        )
        report4_res = self.cursor.fetchall()
        return report4_res

    def close(self):
        self.cursor.close()
        self.conn.close()
