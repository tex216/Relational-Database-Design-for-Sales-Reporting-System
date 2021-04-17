import pymysql


class SqlHelper(object):
    def __init__(self):
        self.conn = pymysql.connect(
            host='127.0.0.1', port=3306, user='root',
            passwd='GatechOmsCS2021', db='cs6400_sp21_team058'
        )
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    # dashboard the count of stores
    def get_count_of_store(self):
        self.cursor.execute("SELECT COUNT(Store_Number) AS Count FROM STORE;")
        count_of_store = self.cursor.fetchall()
        return count_of_store

    # dashboard the count of stores offering food
    def get_count_stores_offering_food(self):
        self.cursor.execute("SELECT COUNT(Store_Number) AS Count "
                            "FROM STORE "
                            "WHERE Has_Restaurant IS TRUE OR Has_Snack_Bar IS TRUE;")
        count_stores_offering_food = self.cursor.fetchall()
        return count_stores_offering_food

    # dashboard the count of stores offering childcare
    def get_count_stores_offering_childcare(self):
        self.cursor.execute("SELECT COUNT(Store_Number) AS Count "
                            "FROM STORE "
                            "WHERE Time_Limit IS NOT NULL;")
        count_stores_offering_childcare = self.cursor.fetchall()
        return count_stores_offering_childcare

    # dashboard the count of products
    def get_count_products(self):
        self.cursor.execute("SELECT COUNT(PID) AS Count FROM PRODUCT;")
        count_products = self.cursor.fetchall()
        return count_products

    # dashboard the count of distinct advertising campaigns
    def get_count_distinct_advertising_campaigns(self):
        self.cursor.execute("SELECT COUNT(Description) AS Count FROM ADVERTISING_CAMPAIGN;")
        count_distinct_advertising_campaigns = self.cursor.fetchall()
        return count_distinct_advertising_campaigns

    # population maintenance: get the state list
    def get_state_list(self):
        self.cursor.execute("SELECT DISTINCT State_Location FROM CITY ORDER BY State_Location ASC;")
        state_list = self.cursor.fetchall()
        return state_list

    # population maintenance: get the city list of selected state
    def get_city_list(self, state_location):
        self.cursor.execute("SELECT city_name FROM CITY "
                            "WHERE State_Location = %s ORDER BY city_name ASC;",
                            [state_location])
        city_list = self.cursor.fetchall()
        return city_list

    # population maintenance: get the city population of the selected state and city
    def get_city_population(self, state_location, city_name):
        self.cursor.execute("SELECT Population FROM CITY WHERE State_Location = %s AND city_name = %s;",
                            [state_location, city_name])
        city_population = self.cursor.fetchall()
        return city_population

    # population maintenance: update the city population of the selected state and city
    def update_city_population(self, state_location, city_name, city_population):
        self.cursor.execute("UPDATE CITY "
                            "SET Population = %s "
                            "WHERE State_Location = %s AND City_Name = %s AND Population <> %s;",
                            [city_population, state_location, city_name, city_population])
        self.conn.commit()

    # holiday maintenance: get the holiday list
    def get_holiday_list(self):
        self.cursor.execute("SELECT Date, GROUP_CONCAT(Name SEPARATOR ', ') AS Name "
                            "FROM Holiday "
                            "GROUP BY Date "
                            "ORDER BY DATE DESC;")
        holiday_list = self.cursor.fetchall()
        return holiday_list

    # holiday maintenance: check if holiday existed or not
    def check_if_holiday_existed(self, holiday_name, holiday_date):
        self.cursor.execute("SELECT * FROM holiday "
                            "WHERE DATE = %s AND NAME = %s;", [holiday_date, holiday_name])
        return self.cursor.rowcount

    # holiday maintenance: add holiday
    def add_holiday(self, holiday_name, holiday_date):
        self.cursor.execute("INSERT INTO `DAY` (`Date`) SELECT %s FROM `DAY` "
                            "WHERE NOT EXISTS (SELECT 1 FROM `DAY` WHERE `Date` = %s) LIMIT 1;",
                            [holiday_date, holiday_date])
        self.cursor.execute("INSERT INTO HOLIDAY (`Date`, `Name`) "
                            "SELECT %s, %s "
                            "FROM HOLIDAY WHERE NOT EXISTS ("
                            "SELECT 1 FROM HOLIDAY WHERE `Date` = %s AND `Name` = %s)"
                            "LIMIT 1;", [holiday_date, holiday_name, holiday_date, holiday_name])
        self.conn.commit()

    # report 1 Category:  get data set
    def get_report1(self):
        self.cursor.execute(
            "SELECT C.Category_Name AS Cate_Name"
            ", COUNT(P.PID) AS Cnt_Product"
            ", FORMAT(IFNULL(MIN(P.Retail_Price), 0.000), 2) AS Min_RtlPrc"
            ", FORMAT(IFNULL(AVG(P.Retail_Price), 0.000), 2) AS Avg_RtlPrc"
            ", FORMAT(IFNULL(MAX(P.Retail_Price), 0.000), 2) AS Max_RtlPrc "
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
            "SELECT P.PID AS PID"
            ", P.Product_Name AS Name"
            ", P.Retail_Price AS Price"
            ", ROUND(SUM(IFNULL(S.Quantity,0)), 2) AS Tot_UnitSold"
            ", SUM(IF(D.Discount_Price IS NULL,0,1) * IFNULL(S.Quantity,0)) AS Tot_UnitSold_AtDsct"
            ", SUM(IF(D.Discount_Price IS NULL,1,0) * IFNULL(S.Quantity,0)) AS Tot_UnitSold_AtRtl"
            ", ROUND(SUM(IFNULL(S.Total_Amount,0)), 2) AS Act_Revenue"
            ", ROUND(SUM(P.Retail_Price * IFNULL(S.Quantity,0) * "
            "   IF(D.Discount_Price IS NULL, 1, 0.75)), 2) AS Pred_Revenue"
            ", ROUND((SUM(IFNULL(S.Total_Amount,0)) - SUM(P.Retail_Price * IFNULL(S.Quantity,0) * "
            "   IF(D.Discount_Price IS NULL, 1, 0.75))), 2) AS Diff_Act_Pred_Revenue "
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

    # Report 3_Store Revenue by Year by State: Get Available State List
    def get_state_list(self):
        self.cursor.execute("SELECT DISTINCT State_Location FROM CITY ORDER BY State_Location ASC;")
        state_list = self.cursor.fetchall()
        return state_list

    # Report 3_Store Revenue by Year by State
    def report3_store_revenue_by_year_by_state(self, state_location):
        self.cursor.execute("SELECT STORE.Store_Number AS Store_ID"
                            ", Street_Address"
                            ", City_Name"
                            ", YEAR(Date) AS Year"
                            ", ROUND(SUM(IFNULL(Total_Amount, 0)), 2) AS Revenue "
                            "FROM STORE "
                            "LEFT JOIN SALE ON STORE.Store_Number = SALE.Store_Number "
                            "WHERE STORE.State_Location = %s"
                            "GROUP BY STORE.Store_Number, YEAR(Date)"
                            "ORDER BY YEAR(Date) ASC, Revenue DESC;", [state_location])
        report3_res = self.cursor.fetchall()
        return report3_res

    # report 4 Outdoor Furniture Revenue: get data set
    def get_report4(self):
        self.cursor.execute(
            "SELECT YEAR(Date) AS Year"
            ", SUM(IFNULL(Quantity, 0)) AS Tot_Quantity"
            ", (SUM(IFNULL(Quantity, 0)) / 365) AS Avg_Quantity"
            ", SUM(IF(MONTH(Date)=2 AND DAY(Date)=2,1,0) * IFNULL(Quantity, 0)) AS GhDay_Quantity "
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

    # report 5 Get Year List
    def get_year_list(self):
        self.cursor.execute("SELECT DISTINCT YEAR(`Date`) AS `Year` FROM `Day` ORDER BY `Year` DESC;")
        year_list = self.cursor.fetchall()
        return year_list

    # report 5 Get Month list
    def get_month_list(self, selected_year):
        self.cursor.execute("SELECT DISTINCT MONTH(`Date`) AS `Month` "
                            "FROM `Day` WHERE YEAR(`Date`) = %s "
                            "ORDER BY `Month` DESC;",
                            [selected_year])
        month_list = self.cursor.fetchall()
        return month_list

    # report 5 State with Highest Volume: get data set
    def get_report5(self, selected_year, selected_month):
        self.cursor.execute(
            "SELECT C.Category_Name, T.State_Location, SUM(IFNULL(S.Quantity,0)) AS Tot_UnitSold "
            "FROM CATEGORY AS C "
            "LEFT JOIN ASSIGNED AS A ON C.Category_Name = A.Category_Name "
            "LEFT JOIN PRODUCT AS P ON A.PID = P.PID "
            "LEFT JOIN SALE AS S ON P.PID = S.PID AND YEAR(S.`Date`) = %s AND MONTH(S.`Date`) = %s "
            "LEFT JOIN STORE AS T ON S.Store_Number = T.Store_Number "
            "GROUP BY C.Category_Name, T.State_Location "
            "HAVING Tot_UnitSold >= ALL ( "
            "SELECT SUM(IFNULL(S2.Quantity,0)) "
            "FROM CATEGORY AS C2 "
            "LEFT JOIN ASSIGNED AS A2 ON C2.Category_Name = A2.Category_Name "
            "LEFT JOIN PRODUCT AS P2 ON A2.PID = P2.PID "
            "LEFT JOIN SALE AS S2 ON P2.PID = S2.PID AND YEAR(S2.`Date`) = %s AND MONTH(S2.`Date`) = %s "
            "LEFT JOIN STORE AS T2 ON S2.Store_Number = T2.Store_Number "
            "WHERE C2.Category_Name = C.Category_Name "
            "GROUP BY C2.Category_Name, T2.State_Location "
            ") ORDER BY C.Category_Name ASC;", ([selected_year], [selected_month], [selected_year], [selected_month]))
        report5_res = self.cursor.fetchall()
        return report5_res

    # Report 6_Revenue by population
    def report6_revenue_by_population(self):
        self.cursor.execute(
            "SELECT YEAR(SRC.`Date`) AS Years"
            ", ROUND(SUM(IF(Population < 3700000, Total_Amount, 0)), 2) AS SmallCity"
            ", ROUND(SUM(IF(Population >= 3700000 AND Population < 6700000, Total_Amount, 0)), 2) AS MediumCity"
            ", ROUND(SUM(IF(Population >= 6700000 AND Population < 9000000, Total_Amount, 0)), 2) AS LargeCity"
            ", ROUND(SUM(IF(Population >= 9000000, Total_Amount, 0)), 2) AS ExtraLargeCity "
            "FROM ("
            "SELECT SALE.`Date`, SALE.Total_Amount, CITY.Population "
            "FROM CITY "
            "INNER JOIN STORE ON CITY.State_Location = STORE.State_Location AND CITY.City_Name = STORE.City_Name "
            "INNER JOIN SALE ON STORE.Store_Number = SALE.Store_Number) AS SRC "
            "GROUP BY YEAR(SRC.`Date`) "
            "ORDER BY YEAR(SRC.`Date`) ASC;"
        )
        report6_res = self.cursor.fetchall()
        return report6_res

    # report 7 Childcare Sales Volume:  get data set
    def get_report7(self):
        self.cursor.execute("SET @Sql = ''; ")
        self.cursor.execute(
            "SELECT @Sql:=CONCAT(@Sql, 'SUM(IF(Childcare_Category=\"',Childcare_Category,'\"',',Total_Amount,0)) AS \"', "
            "Childcare_Category,'\",') "
            "FROM ( "
            "SELECT DISTINCT "
            "IF(STORE.Time_Limit IS NOT NULL, CAST(STORE.Time_Limit AS CHAR(10)), 'No childcare') AS Childcare_Category "
            "FROM STORE "
            ") AS TL; "
        )
        self.cursor.execute(
            "SET @Sql = CONCAT('SELECT DATE_FORMAT(REV.`Date`, \"%Y-%m\") AS Sale_Year_Month,',LEFT(@Sql, LENGTH(@Sql)-1),' FROM ( "
            "SELECT SALE.`Date`, ROUND(SALE.Total_Amount, 2) AS Total_Amount, "
            "IF( STORE.Time_Limit IS NOT NULL, CAST(STORE.Time_Limit AS CHAR(10)), \"No childcare\") AS Childcare_Category "
            "FROM STORE INNER JOIN SALE ON STORE.Store_Number = SALE.Store_Number "
            ") AS REV "
            "GROUP BY Sale_Year_Month "
            "HAVING Sale_Year_Month >= "
            "(SELECT DATE_FORMAT(DATE_ADD( LAST_DAY(DATE_SUB(MAX(SALE.`Date`), INTERVAL 12 MONTH) ), INTERVAL 1 DAY), \"%Y-%m\") "
            "FROM SALE) "
            "ORDER BY Sale_Year_Month ASC'); "
        )
        self.cursor.execute(
            "PREPARE stmt FROM @Sql; "
        )
        self.cursor.execute("EXECUTE stmt; ")
        self.conn.commit()
        report7_res = self.cursor.fetchall()
        return report7_res

    # report 8 Restaurant Impact on Category Sales:  get data set
    def get_report8(self):
        self.cursor.execute(
            "SELECT COLS.Category, COLS.`Store Type` AS StoreType, IFNULL(ACT.`Quantity Sold`, 0) AS QuantitySold "
            "FROM "
            "( ( SELECT C01.Category_Name AS Category, 'Restaurant' AS `Store Type` "
            "FROM CATEGORY INNER JOIN ASSIGNED AS C01) "
            "UNION "
            "( SELECT C02.Category_Name AS Category, 'Non-restaurant' AS `Store Type` "
            "FROM CATEGORY INNER JOIN ASSIGNED AS C02) ) "
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

    # report 9 Advertising Campaign Analysis: get data set
    def get_report9(self):
        self.cursor.execute(
            "SELECT `Product ID` AS ProductID"
            ", `Product Name` AS ProductName"
            ", `Sold During Campaign` AS SoldDuringCampaign"
            ", `Sold Outside Campaign` AS SoldOutsideCampaign"
            ", Difference "
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
            "SELECT P2.PID AS `Product ID`"
            ", P2.Product_Name AS `Product Name`"
            ", SUM(IF(A2.`Description` IS NULL,0,1) * IFNULL(S2.Quantity,0)) AS `Sold During Campaign`"
            ", SUM(IF(A2.`Description` IS NULL,1,0) * IFNULL(S2.Quantity,0)) AS `Sold Outside Campaign`"
            ", (SUM(IF(A2.`Description` IS NULL,0,1) * IFNULL(S2.Quantity,0)) - "
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
