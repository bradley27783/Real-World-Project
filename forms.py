from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo

class LoginForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired()])
    submit = SubmitField('Login')

class Searchbar(FlaskForm):
    searchbar = StringField('Searchbar',validators=[DataRequired()])
    submit = SubmitField('Search')
