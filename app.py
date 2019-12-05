from flask import Flask, render_template, request
from controller.db_operation import Check


app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('login/sign_in.html')


@app.route('/sign_up')
def sign_up():
    return render_template('login/sign_up.html')


@app.route('/sign_in')
def index():
    return render_template('login/sign_in.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    username = ''
    password = ''
    check_info = False
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        check_info = Check().check_info(username, password)
    else:
        username = '0'
        password = '0'

    if check_info:
        return render_template('success.html')
    else:
        return render_template('failed.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=9999, debug=True)
