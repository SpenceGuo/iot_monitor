from model.mysql_helper import MysqlHelper
import config


class Select:
    def select(self, tbname):
        db_option = MysqlHelper()
        data = db_option.speak(tbname)
        return data

    def select(self, username, password):
        result = []
        result.append(2)
        result.append(False)
        db_option = MysqlHelper()
        data = db_option.speak(username, password)
        for row in data:
            result[0] = row[2]
            if data.__len__() == 0:
                result[1] = False
            else:
                result[1] = True
        return result


class Insert:
    def insert(self, user_info=[]):
        username = user_info[0]
        password = user_info[1]
        user_permission = user_info[2]

        str_colon = '\''
        sql = 'INSERT INTO users(username,password,permission)VALUES(' + str_colon + username + str_colon +\
      ',' + str_colon + password + str_colon + ',' + str_colon + user_permission + str_colon + ')'
        db_option = MysqlHelper().speak(sql)
        return db_option


class Delete:
    def delete1(self, username):
        db_option = MysqlHelper()
        data = db_option.speak(username)
        return data


class Check:
    def check_info(self, username, password):
        db_option = MysqlHelper()
        data = db_option.speak(username, password)
        if data.__len__() == 0:
            return False
        else:
            return True
