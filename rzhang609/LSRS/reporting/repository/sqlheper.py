from django.db import connection, transaction
import pymysql


class SqlHelper(object):

    def __init__(self):
        self.conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='GatechOmsCS2021',  db='cs6400')
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def get_holiday_list(self):
        self.cursor.execute("SELECT Name, Date FROM Holiday")
        holiday_list = self.cursor.fetchall()
        return holiday_list

    def close(self):
        self.cursor.close()
        self.conn.close()
