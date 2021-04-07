from django.db import connection, transaction
import pymysql


class SqlHelper(object):

    def __init__(self):
        self.conn = pymysql.connect(host='127.0.0.1', port=3306, user='gatechUser058', passwd='password',  db='cs6400_sp21_team058')
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    # Report 3_Store Revenue by Year by State: Get Available State List
    def get_state_list(self):
        self.cursor.execute("SELECT DISTINCT State_Location FROM CITY ORDER BY State_Location ASC")
        state_list = self.cursor.fetchall()
        return state_list

    # Report 3_Store Revenue by Year by State
    def report3_store_revenue_by_year_by_state(self, state_location):
        self.cursor.execute(
            "SELECT STORE.Store_Number, Street_Address, City_Name, YEAR(Date), SUM(IFNULL("
            "Total_Amount, 0)) AS Revenue "
            "FROM STORE"
            "LEFT JOIN SALE ON STORE.Store_Number = SALE.Store_Number"
            "WHERE State_Location = %s "
            "GROUP BY STORE.Store_Number, YEAR(Date)"
            "ORDER BY YEAR(Date) ASC, Revenue DESC;",
            [state_location])

        report3_res = self.cursor.fetchall()
        return report3_res

    # Report 6_Revenue by population
    def report6_revenue_by_population(self):
        self.cursor.execute(
            "SELECT YEAR(SRC.`Date`) AS Years, SUM(IF(Population < 3700000, Total_Amount, 0)) AS SmallCity, "
            "SUM(IF(Population >= 3700000 AND Population < 6700000, Total_Amount, 0)) AS MediumCity, "
            "SUM(IF(Population >= 6700000 AND Population < 9000000, Total_Amount, 0)) AS LargeCity, SUM(IF(Population "
            ">= 9000000, Total_Amount, 0)) AS ExtraLargeCity "
            "FROM (SELECT SALE.`Date`, SALE.Total_Amount, CITY.Population FROM CITY INNER JOIN STORE ON "
            "CITY.State_Location = STORE.State_Location AND CITY.City_Name = STORE.City_Name INNER JOIN SALE ON "
            "STORE.Store_Number = SALE.Store_Number) AS SRC "
            "GROUP BY YEAR(SRC.`Date`) ORDER BY YEAR(SRC.`Date`) ASC;"
        )
        report6_res = self.cursor.fetchall()
        return report6_res

    def close(self):
        self.cursor.close()
        self.conn.close()
