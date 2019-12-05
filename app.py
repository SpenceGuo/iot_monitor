from flask import Flask, render_template, request
from controller.db_operation import Check, Select, Insert


app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('login/sign_in.html')


@app.route('/sign_up')
def sign_up():
    return render_template('login/sign_up.html')


@app.route('/register', methods=['POST'])
def register():
    username = ''
    password = ''
    user_info = []
    user_permission = '2'
    username = request.form.get('username')
    password = request.form.get('password')
    user_info.append(username)
    user_info.append(password)
    user_info.append(user_permission)

    register_result = Insert().insert(user_info)
    if register_result:
        return render_template('success.html')
    else:
        return render_template('failed.html')


@app.route('/sign_in')
def sign_in():
    return render_template('login/sign_in.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    username = ''
    password = ''

    """
    user information check result. (True or False)
    default setting is False
    """
    check_info = False
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user_info = Select().select(username, password)

        """
        user permission level.
        decide the web page information that the user can see. (0 1 2, up to low)
        """
        user_permission = user_info[0]

        check_info = user_info[1]

    # GET method remains to be completed...
    else:
        username = '0'
        password = '0'

    if check_info:
        return render_template('success.html')
    else:
        return render_template('failed.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=9999, debug=True)
