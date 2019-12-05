"""
mySQL Helper

"""

import pymysql
import config


class MysqlHelper:

    # 构造函数
    # def __init__(self):

    # the first speak function, just for testing...
    def speak(self):
        sql = 'SELECT * FROM ' + config.tbname
        # 打开数据库连接
        db = pymysql.connect(config.host, config.username, config.password, config.database)
        cursor = db.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        return data
        db.close()

    # rewrite the speak function... this function need two parameters
    def speak(self, username, password):
        # get the sql...
        sql = 'SELECT * FROM ' + config.tbname + " WHERE username=\'" + username + "\' AND password=\'" + password + "\'"
        db = pymysql.connect(config.host, config.username, config.password, config.database)
        cursor = db.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        return data
        db.close()

    # process sql automatically, remains to be finished...
    # it will be finished later...
    # @staticmethod
    # def sql_process(self, sql):
    #     result = sql[0:6]
    #     return result



