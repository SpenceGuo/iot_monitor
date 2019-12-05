"""
mySQL Helper

"""

import pymysql
import config


class MysqlHelper:

    # 构造函数
    # def __init__(self):

    # rewrite the speak function... this function need two parameters
    def speak(self, username, password):
        # get the sql...
        sql = 'SELECT * FROM ' + config.tbname + " WHERE username=\'" + username + "\' AND password=\'" + password + "\'"
        db = pymysql.connect(config.host, config.username, config.password, config.database)
        cursor = db.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        db.close()
        return data

    def speak(self, sql):
        db = pymysql.connect(config.host, config.username, config.password, config.database)
        cursor = db.cursor()
        try:
            cursor.execute(sql)
            db.commit()
            db.close()
            return True
        except:
            db.close()
            return False


    # process sql automatically, remains to be finished...
    # it will be finished later...
    # @staticmethod
    # def sql_process(self, sql):
    #     result = sql[0:6]
    #     return result



