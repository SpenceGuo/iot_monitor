"""
check the form information
"""
import config
from flask import Flask, render_template, request
from controller.db_operation import Check, Select, Insert
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField, ValidationError, HiddenField, \
    BooleanField, PasswordField, DateField
from wtforms.validators import DataRequired, Email, Length, Optional, URL, Regexp, EqualTo


class ResisterForm(FlaskForm):
    # name = StringField(validators=[Length(max=17, min=6)])
    # password = StringField(validators=[Length(max=17, min=6, message='密码长度必须大于3并且小于10')])
    # repeat_pwd = StringField(validators=[Length(max=17, min=6, message='密码长度必须大于3并且小于10'), EqualTo("password")])
    username = StringField('username', validators=[DataRequired(), Length(5, 15), Regexp('^[A-Za-z][A-Za-z0-9]*$', 0, 'name is invaild')], render_kw={"placeholder": "please input your username"})
    password = PasswordField('password', validators=[DataRequired(), Length(5, 25)], render_kw={'placeholder': 'set your password'})
    repeat_pwd = PasswordField("repeat_pwd", validators=[DataRequired(), Length(5, 25)], render_kw={'placeholder:': 'set your password again'})


app = Flask(__name__)
app.config["SECRET_KEY"] = config.SECRET_KEY


@app.route('/')
def hello_world():
    return render_template('login/test.html')


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'GET':
        return render_template('templates/failed.html')
    else:
        form = ResisterForm(request.form)
        if form.validate_on_submit():
            return 'success!!!'
        else:
            print(form.errors)
            return 'fail...'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=9999, debug=True)
