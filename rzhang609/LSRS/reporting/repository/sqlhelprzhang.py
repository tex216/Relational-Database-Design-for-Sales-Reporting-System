from django.db import connection, transaction
import pymysql


class SqlHelper(object):

    def __init__(self):
        self.conn = pymysql.connect(host='127.0.0.1', port=3306, user='root',
                                    passwd='GatechOmsCS2021',  db='cs6400_sp21_team058')
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def get_holiday_list(self):
        self.cursor.execute("SELECT Name, Date FROM Holiday")
        holiday_list = self.cursor.fetchall()
        return holiday_list

    def get_state_list(self):
        self.cursor.execute("SELECT DISTINCT State_Location FROM CITY ORDER BY State_Location ASC")
        state_list = self.cursor.fetchall()
        return state_list

    def get_city_list(self, state_location):
        self.cursor.execute("SELECT city_name FROM CITY WHERE State_Location = %s ORDER BY city_name ASC;",
                            [state_location])
        city_list = self.cursor.fetchall()
        return city_list

    def get_city_population(self, state_location, city_name):
        self.cursor.execute("SELECT Population FROM CITY WHERE State_Location = %s AND city_name = %s;",
                            [state_location, city_name])
        city_population = self.cursor.fetchall()
        return city_population

    def update_city_population(self, state_location, city_name, city_population):
        self.cursor.execute("UPDATE CITY "
                            "SET Population = %s "
                            "WHERE State_Location = %s AND City_Name = %s AND Population <> %s;",
                            [city_population, state_location, city_name, city_population])
        self.conn.commit()

    def close(self):
        self.cursor.close()
        self.conn.close()
