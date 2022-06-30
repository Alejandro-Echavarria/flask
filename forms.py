from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired, InputRequired, Email, Length

class LoginForm(FlaskForm):

    username = StringField("username", validators[InputRequired(), Length(min=4, max=25)])