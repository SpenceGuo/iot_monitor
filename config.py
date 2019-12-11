"""
database configuration
put your database information here
"""

# your host address
host = '127.0.0.1'

# the username you log into the database server
username = 'root'
# the password you log into the database server
password = ''

# database name
database = 'iot_monitor'

# user table name
tbname = 'users'

"""
CSRF:
Flask-WTF提供了对所有Form表单免受跨站请求伪造（Cross-Site Request Forgery，CSRF）攻击的技术支持
通过添加动态token令牌的方式,关于CSRF可以自行在网上搜索相关内容
"""
CSRF_ENABLED = True
SECRET_KEY = 'iot_monitor_secret_key'
