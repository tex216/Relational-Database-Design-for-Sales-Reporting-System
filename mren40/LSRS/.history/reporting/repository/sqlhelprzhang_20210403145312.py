from django.db import connection, transaction
import pymysql


class SqlHelper(object):
    def __init__(self):
        self.conn = pymysql.connect(
            host="127.0.0.1", port=3306, user="root", passwd="spring2021_cs6400", db="cs6400_sp21_team058"
        )
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    # dashboard the count of stores
    def get_count_of_store(self):
        self.cursor.execute("SELECT COUNT(Store_Number) AS Count FROM STORE")
        count_of_store = self.cursor.fetchall()
        return count_of_store

    # dashboard the count of stores offering food
    def get_count_stores_offering_food(self):
        self.cursor.execute(
            "SELECT COUNT(Store_Number) AS Count FROM STORE " "WHERE Has_Restaurant IS TRUE OR Has_Snack_Bar IS TRUE;"
        )
        count_stores_offering_food = self.cursor.fetchall()
        return count_stores_offering_food

    # dashboard the count of stores offering childcare
    def get_count_stores_offering_childcare(self):
        self.cursor.execute("SELECT COUNT(Store_Number) AS Count FROM STORE WHERE Time_Limit IS NOT NULL;")
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
        self.cursor.execute("SELECT DISTINCT State_Location FROM CITY ORDER BY State_Location ASC")
        state_list = self.cursor.fetchall()
        return state_list

    # population maintenance: get the city list of selected state
    def get_city_list(self, state_location):
        self.cursor.execute(
            "SELECT city_name FROM CITY WHERE State_Location = %s ORDER BY city_name ASC;", [state_location]
        )
        city_list = self.cursor.fetchall()
        return city_list

    # population maintenance: get the city population of the selected state and city
    def get_city_population(self, state_location, city_name):
        self.cursor.execute(
            "SELECT Population FROM CITY WHERE State_Location = %s AND city_name = %s;", [state_location, city_name]
        )
        city_population = self.cursor.fetchall()
        return city_population

    # population maintenance: update the city population of the selected state and city
    def update_city_population(self, state_location, city_name, city_population):
        self.cursor.execute(
            "UPDATE CITY " "SET Population = %s " "WHERE State_Location = %s AND City_Name = %s AND Population <> %s;",
            [city_population, state_location, city_name, city_population],
        )
        self.conn.commit()

    # holiday maintenance: get the holiday list
    def get_holiday_list(self):
        self.cursor.execute("SELECT Name, Date FROM Holiday")
        holiday_list = self.cursor.fetchall()
        return holiday_list

    # holiday maintenance: check if holiday existed or not
    def check_if_holiday_existed(self, holiday_name, holiday_date):
        self.cursor.execute("SELECT * FROM holiday " "WHERE DATE = %s AND NAME = %s;", [holiday_date, holiday_name])
        return self.cursor.rowcount

    # holiday maintenance: add holiday
    def add_holiday(self, holiday_name, holiday_date):
        self.cursor.execute(
            "INSERT INTO `DAY` (`Date`) SELECT %s FROM `DAY` "
            "WHERE NOT EXISTS (SELECT 1 FROM `DAY` WHERE `Date` = %s) LIMIT 1;",
            [holiday_date, holiday_date],
        )
        self.cursor.execute(
            "INSERT INTO HOLIDAY (`Date`, `Name`) "
            "SELECT %s, %s "
            "FROM HOLIDAY WHERE NOT EXISTS ("
            "SELECT 1 FROM HOLIDAY WHERE `Date` = %s AND `Name` = %s)"
            "LIMIT 1;",
            [holiday_date, holiday_name, holiday_date, holiday_name],
        )
        self.conn.commit()

    def close(self):
        self.cursor.close()
        self.conn.close()
