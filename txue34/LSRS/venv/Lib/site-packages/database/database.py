#!/usr/bin/python

# MIT License
# Author : Kwon Hong Kyun

"""
MIT License

    Copyright (c) 2018 

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
"""

import time
import sqlite3,os
from collections import OrderedDict
from abc import *

# Create only one instance for a (handler) class
class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


# You don't have to directly call this class instance on the outside.
# I'd recommend that create a handler class for the database query.
# SELECT column-list FROM table_name WHERE [conditions] GROUP BY column1, column2 .... columnN ORDER BY column1, column2 .... columnN

class DataBaseHandlerConst(object):
    QUERYBYrow_id       = 1
    QUERYBYCOND     = 2
    MODIFYEACH      = 1
    MODIFYCOLUMNS   = 2
    ADDCOLUMN       = 1
    DROPCOLUMN      = 2

class DataBaseQuery:
    def __init__(self,dbname,primary):
        self.TBL     = dbname
        self.primary = primary
        self.conn    = 0
        self.cursor  = 0
    
    def __del__(self):
        return self.close()
    
    def __query(self,sql):
        try:
            self.cursor.execute(sql)
            self.conn.commit()
            return True
        except:return None
    
    def __query_lazy(self,sql):
        try:
            self.cursor.execute(sql)
            return True
        except:return None
    
    def __fetch(self,sql):
        try:
            self.cursor.execute(sql)
            for row in self.cursor:
                return row
        except:return None
    
    def __fetchAll(self,sql):
        #try:
        self.cursor.execute(sql)
        return self.cursor.fetchall()
        #except:return None
    
    # Database Initialization Method Family
    def connect(self,path):
        self.conn = sqlite3.connect(path)
        self.cursor = self.conn.cursor()
    def close(self):
        self.conn.close()
    def build(self,tables):
        self.conn.execute("""DROP TABLE IF EXISTS {0}""".format(self.TBL))
        self.conn.execute("""CREATE TABLE {0} ( {1} )""".format(self.TBL,tables))
        self.conn.commit()
    def build_in(self,table,tables):
        self.conn.execute("""DROP TABLE IF EXISTS {0}""".format(table))
        self.conn.execute("""CREATE TABLE {0} ( {1} )""".format(table,tables))
        self.conn.commit()
    
    # Data Operation Method Family
    def query(self,statement):
        return self.__query(str(statement))
    def fetch(self,statement,mode=0):
        if(mode==0):return self.__fetch(str(statement))
        else:return self.__fetchAll(str(statement))
    def commit(self):
        self.conn.commit()

    def drop(self):
        self.conn.execute("""DROP TABLE IF EXISTS {0}""".format(self.TBL))
        self.conn.commit()
    def drop_in(self,table):
        self.conn.execute("""DROP TABLE IF EXISTS {0}""".format(table))
        self.conn.commit()
    def delete(self,row_id):
        sql = "DELETE FROM {0} WHERE {1}='{2}'".format(self.TBL,self.primary,row_id)
        return self.__query(sql)
    def delete_in(self,table,row_id):
        sql = "DELETE FROM {0} WHERE {1}='{2}'".format(table,self.primary,row_id)
        return self.__query(sql)
    def drop_duplicate(self,table,column):
        sql = "DELETE FROM {0} WHERE rowid NOT IN (SELECT min(rowid) FROM {0} GROUP BY {1})".format(table,column)
        return self.__query(sql)
    def insert(self,row,lazy=False):
        cols = ', '.join('"{}"'.format(col) for col in row.keys())
        vals = ', '.join(':{}'.format(col)  for col in row.keys())
        sql  = 'INSERT INTO "{0}" ({1}) VALUES ({2})'.format(self.TBL,cols,vals)
        self.cursor.execute(sql,row)
        if(lazy==False):self.conn.commit()
    def insert_in(self,table,row,lazy=False):
        cols = ', '.join('"{}"'.format(col) for col in row.keys())
        vals = ', '.join(':{}'.format(col)  for col in row.keys())
        sql  = 'INSERT INTO "{0}" ({1}) VALUES ({2})'.format(table,cols,vals)
        self.cursor.execute(sql,row)
        if(lazy==False):self.conn.commit()
    def insert_many(self,column,values):
        cols = ', '.join('"{}"'.format(col) for col in column)
        vals = '?, '* (len(column)-1) + "?"
        sql  = 'INSERT INTO "{0}" ({1}) VALUES ({2})'.format(self.TBL,cols,vals)
        return self.cursor.executemany(sql,values)
    def insert_many_in(self,table,column,values):
        cols = ', '.join('"{}"'.format(col) for col in column)
        vals = '?, '* (len(column)-1) + "?"
        sql  = 'INSERT INTO "{0}" ({1}) VALUES ({2})'.format(table,cols,vals)
        return self.cursor.executemany(sql,values)
    
    # Read Method Family
    # get a row with primary id in the database
    def read(self,table,row_id,PRIMARY_ORDER=""):
        sql  = "SELECT * FROM {0} WHERE {1}='{2}' ORDER BY {3} DESC".format(table,self.primary,row_id,PRIMARY_ORDER)
        return self.__fetch(sql)
    # get a row matched primary id with the specific column in the database
    def read_column(self,table,row_id,col,PRIMARY_ORDER=""):
        sql  = "SELECT {0} FROM {1} WHERE {2}='{3}' ORDER BY {4} DESC".format(col,table,self.primary,row_id,PRIMARY_ORDER)
        return self.__fetch(sql)
    # get a row with the given condition statement in the database
    def read_condition(self,table,cond,PRIMARY_ORDER=""):
        sql  = "SELECT * FROM {0} WHERE {1} ORDER BY {2} DESC".format(table,cond,PRIMARY_ORDER)
        return self.__fetch(sql)
    # get a row with the given condition statement and specific column in the database
    def read_column_condition(self,table,col,cond,PRIMARY_ORDER=""):
        sql  = "SELECT {0} FROM {1} WHERE {2} ORDER BY {3} DESC".format(col,table,cond,PRIMARY_ORDER)
        return self.__fetch(sql)
    # get all rows with the given condition statement and specific column in the database
    def read_column_condition_all(self,table,col,cond,PRIMARY_ORDER=""):
        sql  = "SELECT {0} FROM {1} WHERE {2} ORDER BY {3} DESC".format(col,table,cond,PRIMARY_ORDER)
        return self.__fetchAll(sql)
    def read_column_all(self,table,col,PRIMARY_ORDER=""):
        sql  = "SELECT {0} FROM {1} ORDER BY {2} DESC".format(col,table,PRIMARY_ORDER)
        return self.__fetchAll(sql)
    def read_all(self,table,PRIMARY_ORDER=""):
        sql  = "SELECT * FROM {0} ORDER BY {1} DESC".format(table,PRIMARY_ORDER)
        return self.__fetchAll(sql)
    # get rows with the given condition statement in the database
    def filter(self,table,cond,PRIMARY_ORDER=""):
        sql  = "SELECT * FROM {0} WHERE {1} ORDER BY {2} DESC".format(table,cond,PRIMARY_ORDER)
        return self.__fetchAll(sql)
    # Modify Method Family
    def modify(self,table,row_id,col,data,lazy=False):
        sql  = "UPDATE {0} SET {1}='{2}' WHERE {3}='{4}'".format(table,col,data,self.primary,row_id)
        if(lazy==False):
            return self.__query(sql)
        return self.__query_lazy(sql)
    def modifies(self,table,row_id,col,data,lazy=False):
        var = list()
        for (i,j) in zip(col,data):var.append("{0} = '{1}'".format(i,j))
        var = ', '.join(var)
        sql  = "UPDATE {0} SET {1} WHERE {2}='{3}'".format(table,var,self.primary,row_id)
        if(lazy==False):
            return self.__query(sql)
        return self.__query_lazy(sql)

    def get_drop_duplicate(self,table,order,column):
        colist = ""
        for i in column:colist+="{0},".format(i)
        if(order==None):
            sql = "SELECT DISTINCT {1} FROM {0} ".format(table,colist[:-1])
        else:
            sql = "SELECT DISTINCT {1} FROM {0} ORDER BY {3} ".format(table,colist[:-1],order)
        return self.__fetchAll(sql)

    def get_drop_duplicate_by_cond(self,table,order,cond,column):
        colist = ""
        for i in column:colist+="{0},".format(i)
        if(order==None):
            sql = "SELECT DISTINCT {1} FROM {0} WHERE {2} ".format(table,colist[:-1],cond)
        else:
            sql = "SELECT DISTINCT {1} FROM {0} WHERE {2} ORDER BY {3}".format(table,colist[:-1],cond,order) 
        return self.__fetchAll(sql)

    def getTop(self,table):
        sql  = "SELECT * FROM {0} LIMIT 1".format(table)
        return self.__fetch(sql)

    def group(self,table,cond,groups,PRIMARY_ORDER=""):
        sql  = "SELECT * FROM {0} WHERE {1} GROUP BY {2} ORDER BY {3} DESC".format(table,cond,groups,PRIMARY_ORDER)
        return self.__fetch(sql)

    def create_view(self,view,col,cond=""):
        if(cond==""):return self.__query("CREATE VIEW {0} AS SELECT {1} FROM {2}".format(view,col,self.TBL))
        else:return self.__query("CREATE VIEW {0} AS SELECT {1} FROM {2} WHERE {3}".format(view,col,self.TBL,cond))
    def destroy_view(self,view):
        return self.__query("DROP VIEW {0}".format(view))
    def alterColumn(self,table,cmd,add,type):
        if(cmd==DataBaseHandlerConst.ADDCOLUMN):
            return self.__query("ALTER TABLE {0} ADD {1} {2}".format(table,add,type))
        elif(cmd==DataBaseHandlerConst.DROPCOLUMN):
            return self.__query("ALTER TABLE {0} DROP {1} {2}".format(table,add))
        else:return None
        
    def get_min(self,table,col,cond=""):
        if(cond==""):
            return self.__fetchAll("SELECT {2}, MIN({0}) FROM {1}".format(col,table,self.primary))
        else:
            return self.__fetchAll("SELECT {3}, MIN({0}) FROM {1} WHERE {2}".format(col,table,cond,self.primary))
    def get_max(self,table,col,cond=""):
        if(cond==""):
            return self.__fetchAll("SELECT {2}, MAX({0}) FROM {1}".format(col,table,self.primary))
        else:
            return self.__fetchAll("SELECT {3}, MAX({0}) FROM {1} WHERE {2}".format(col,table,cond,self.primary)) 

# This class is a parent class for the inheritance
class DataBaseHandler(metaclass=ABCMeta):
    def __init__(self,Table):
        self.db      = DataBaseQuery(Table.TBL_NAME,Table.PRIMARY_ORDER)
        self.sep     = os.sep
        self.table   = Table
        self.__count = 0
        self.page    = 0
        self.contain = list()
        self.onCreate()
    def __del__(self):
        return self.end()
    # Create a database according to defined table class.
    def create(self):
        self.db.build(self.table.COLUMNS)
    def create_in(self,table):
        self.db.build_in(table.TBL_NAME,table.COLUMNS)
    
    # Connect to the database
    def begin(self,path=None):
        if(path==None):
            path = "{0}{1}{2}".format(self.table.PATH,self.sep,self.table.DEFAULT_NAME)
        ret = os.path.exists(path)
        self.db.connect(path)
        if(ret==False):
            self.create()
            return (True,1)
        return (True,0)

    # Close the current connection.
    def end(self):
        self.db.close()
        self.onDestory()
    # Commit to the database.
    def commit(self):
        try:
            self.db.commit()
            self.contain = list()
            self.__count=0
            return (True,0)
        except sqlite3.Error as e:
            return (None,e)
    # Add a row in the database.
    def add(self,value,lazy=False):
        if(type(value)!=list and len(value)!=self.table.LENGTH):
            return (False,0)
        try:
            self.db.insert(OrderedDict(zip(self.table.COLUMNSLIST,value)),lazy)
            return (True,0)
        except sqlite3.Error as e:
            return (None,e)
    def add_in(self,table,value,lazy=False):
        if(type(value)!=list and len(value)!=LENGTH):
            return (False,0)
        try:
            self.db.insert_in(table.TBL_NAME,OrderedDict(zip(table.COLUMNSLIST,value)),lazy)
            return (True,0)
        except sqlite3.Error as e:
            return (None,e)
    # Add records in the database (Lazy)
    def add_count(self,value):
        if(type(value)!=list and len(value)!=self.table.LENGTH):
            return (False,0)
        try:
            self.__count+=1
            self.contain.append(tuple(value))
            if(self.__count>=self.page):
                ret = self.db.insert_many(self.table.COLUMNSLIST,tuple(self.contain))
                self.commit()
            return (True,0)
        except sqlite3.Error as e:
            self.contain = list()
            return (None,e)
    def add_count_in(self,table,value):
        if(type(value)!=list and len(value)!=table.LENGTH):
            return (False,0)
        try:
            self.__count+=1
            self.contain.append(tuple(value))
            if(self.__count>=self.page):
                ret = self.db.insert_many_in(table.TBL_NAME,table.COLUMNSLIST,tuple(self.contain))
                self.commit()
            return (True,0)
        except sqlite3.Error as e:
            self.contain = list()
            return (None,e)
    def insert_rest(self):
        try:
            self.db.insert_many(self.table.COLUMNSLIST,tuple(self.contain))
            self.commit()
            return (True,0)
        except sqlite3.Error as e:
            self.contain = list()
            return (None,e)
    def insert_rest_in(self,table):
        try:
            self.db.insert_many_in(table.TBL_NAME,table.COLUMNSLIST,tuple(self.contain))
            self.commit()
            return (True,0)
        except sqlite3.Error as e:
            self.contain = list()
            return (None,e)
    # Remove a row from the database.
    def delete(self,key):
        try:return (True,self.db.delete(key))
        except sqlite3.Error as e:return (None,e)
    # Pop a row in the database.
    def pop(self):
        ret = self.db.getTop()
        if(ret==None or ret==False):
            return (None,0)
        try:
            self.db.delete(ret[0])
            return (True,ret)
        except sqlite3.Error as e:
            return (None,e)
        return (None,0)

    # Get a row from the database.
    def get(self,table,key,primary):
        try:return (True,self.db.read(table,key,primary))
        except sqlite3.Error as e:return (None,e)
    def get_by_col(self,table,key,col,primary):
        try:return (True,self.db.read_column(table,key,col,primary))
        except sqlite3.Error as e:return (None,e)
    def get_by_cond(self,table,cond,primary):
        try:return (True,self.db.read_condition(table,cond,primary))
        except sqlite3.Error as e:return (None,e)
    def get_by_col_cond(self,table,col,cond,primary):
        try:return (True,self.db.read_column_condition(table,col,cond,primary))
        except sqlite3.Error as e:return (None,e)
    def get_all(self,table,primary):
        try:return (True,self.db.read_all(table,primary))
        except sqlite3.Error as e:return (None,e)
    def filter(self,table,cond,primary):
        try:return (True,self.db.read_condition(table,cond,primary))
        except sqlite3.Error as e:return (None,e)
    def filter_all(self,table,cond,primary):
        try:return (True,self.db.filter(table,cond,primary))
        except sqlite3.Error as e:return (None,e)
    # Modify the value in database by the specific column.
    def set(self,table,key,col,value,lazy=False):
        try:return (True,self.db.modify(table,key,col,value,lazy))
        except sqlite3.Error as e:return (None,e)
    def set_by_cols(self,table,key,col,data,lazy=False):
        if(len(col)!=len(data)):return (False,0)
        try:return (True,self.db.modifies(table,key,col,data,lazy))
        except sqlite3.Error as e:return (None,e)
        
    def group(self,table,cond,grp):
        if(len(grp)>len(cond)):return (False,0)
        try:return (True,self.db.group(table,col,cond))
        except sqlite3.Error as e:return (None,e)
    def create_view(self,view,col,cond=""):
        try:return (True,self.db.create_view(view,col,cond))
        except sqlite3.Error as e:return (None,e)
    def destroy_view(self,view):
        try:return (True,self.db.destroy_view(view))
        except sqlite3.Error as e:return (None,e)
    def alter_column(self,table,cmd,add,type):
        return self.db.alterColumn(table,cmd,add,type)
    def get_min(self,table,col,cond=""):
        try:return (True,self.db.get_min(table,col,cond))
        except sqlite3.Error as e:return (None,e)
    def get_min(self,table,col,cond=""):
        try:return (True,self.db.get_max(table,col,cond))
        except sqlite3.Error as e:return (None,e)

    # Interfaces.
    @abstractmethod
    def onCreate(self):
        pass
    @abstractmethod
    def onDestory(self):
        pass

class __DataBaseTableStruct(object):
    TBL_NAME      = "Configuration_Table"
    DEFAULT_NAME  = "conf.db"
    COLUMN        = (("id","text primary key not NULL"),("value","int"),("desc","varchar[128]"))
    COLUMNS       = """
                    key    text primary key not NULL,
                    value  int,
                    desc   varchar[128]
                    """
    COLUMNSLIST   = ["key","value","desc"]
    PRIMARY_ORDER = "key"
    LENGTH        = len(COLUMNSLIST)
    PATH          = "."

class DataBaseTable(__DataBaseTableStruct):
    def __init__(self):
        super().__init__()
    def setTableName(self,name):
        self.TBL_NAME = name
    def setDefaultName(self,name):
        self.DEFAULT_NAME = name
    def setColumns(self,col,colist,primary=None):
        self.COLUMNS     = col
        self.COLUMNSLIST = colist
        self.LENGTH      = len(self.COLUMNSLIST)
        if(primary==None):
            self.PRIMARY_ORDER = colist[0]
        else:self.PRIMARY_ORDER = primary
    def setPath(self,path):
        self.PATH   = path
    def setTable(self,name,col,colist,primary=None):
        self.setTableName(name)
        self.setColumns(col,colist,primary)
    def showColumns(self):
        print(self.COLUMNSLIST)
    def showName(self):
        print(self.TBL_NAME)
    def create_table_text(self):
        __str = ""
        if(type(self.COLUMN[0])!=tuple):
            return "{0} {1}".format(self.COLUMN[0],self.COLUMN[1])
        for i in self.COLUMN:
            if(len(i)!=2):return ""
            __str += "{0} {1}, ".format(i[0],i[1])
        return __str[:-2]
    def create_column_list(self):
        __str = list()
        if(type(self.COLUMN[0])!=tuple):
            __str.append(self.COLUMN[0])
            return __str
        for i in self.COLUMN:
            __str.append(i[0])
        return __str

class DataBaseTableHandler(DataBaseHandler):
    # The type must be DataBaseTable.
    # tableStruct = DataBaseTable()
    # ... setup TableStruct ...
    # handler = DataBaseTableHandler(talbeStruct)
    def __init__(self,DataBaseTableStruct):
        super().__init__(DataBaseTableStruct)
    def onCreate(self):
        pass
    def onDestory(self):
        pass
