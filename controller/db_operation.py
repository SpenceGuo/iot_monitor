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
