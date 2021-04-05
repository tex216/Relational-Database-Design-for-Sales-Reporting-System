import pymysql


class SqlHelper(object):

    def __init__(self):
        self.conn = pymysql.connect(host='127.0.0.1', port=3306, user='cs6400_sp21_team058', passwd='gatech058',  db='cs6400_sp21_team058')
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)






    def close(self):
        self.cursor.close()
        self.conn.close()
