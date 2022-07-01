from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired, InputRequired, Email, Length

class LoginForm(FlaskForm):

    username = StringField("Usuario", validators = [InputRequired(), Length(min=4, max=25)])
    password = PasswordField("Contraseña", validators = [InputRequired(), Length(min=8, max=25)])
    remember = BooleanField("remember me")


class SingupForm(FlaskForm):
    email = StringField("Correo", validators = [InputRequired(), Email("Escribe un email válido"), Length(max=60)])
    username = StringField("Usuario", validators = [InputRequired(), Length(min=4, max=25)])
    password = PasswordField("Contraseña", validators = [InputRequired(), Length(min=8, max=25)])