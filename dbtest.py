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
from controller.db_operation import Select

# part 1
test = MysqlHelper()
data = test.speak('admin', 'admin')
for row in data:
    user_name = row[0]
    pass_word = row[1]
    permission = row[2]
    print(user_name, pass_word, permission, end='\n')

# part 2
str_test = 'SELECT * FROM users'
final_str = str_test[0:6]
print(final_str)

# part 3
list_op = Select()
result = []
result = list_op.select('admin', 'admin')
print(result[0], result[1])


