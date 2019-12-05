"""
codes in this file is for testing, they are not concerned with the main project.
......
part 1 is the basic database test. it is used for testing the selecting function
......
part 2 is a demo. it can get the first word of the sql sentence.
because the first word of the sql sentence only have six letters.
(just for: select insert delete update)
......
part 3 is list testing.
"""

from model.mysql_helper import MysqlHelper
from controller.db_operation import Select,Insert

# part 1
# test = MysqlHelper()
# data = test.speak('admin', 'admin')
# for row in data:
#     user_name = row[0]
#     pass_word = row[1]
#     permission = row[2]
#     print(user_name, pass_word, permission, end='\n')

# part 2
# str_test = 'SELECT * FROM users'
# final_str = str_test[0:6]
# print(final_str)

# part 3
# list_op = Select()
# result = []
# result = list_op.select('admin', 'admin')
# print(result[0], result[1])

# part 4
user_info = []
user_info.append('u2')
user_info.append('222222')
user_info.append('2')
register_result = Insert().insert(user_info)
print(register_result)

# part 5
username = 'u2'
password = '222222'
permission = '2'
str_colon = '\''
sql = 'INSERT INTO users(username,password,permission)VALUES(' + str_colon + username + str_colon +\
      ',' + str_colon + password + str_colon + ',' + str_colon + permission + str_colon + ')'
print(sql)