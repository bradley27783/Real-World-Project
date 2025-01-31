from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, EqualTo

class LoginForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired()])
    submit = SubmitField('Login')

class Searchbar(FlaskForm):
    searchbar = StringField('Searchbar',validators=[DataRequired()])
    submit = SubmitField('Search')


class AccountForm(FlaskForm):
    fname = StringField('Firstname',validators=[DataRequired()])
    lname = StringField('Lastname',validators=[DataRequired()])
    course = SelectField('Course',choices=[('comsci', 'Computer Science'), ('eh', 'Ethical Hacking'), ('history', 'History')])
    submit = SubmitField('Setup')


class DeleteForm(FlaskForm):
    password = PasswordField('Password',validators=[DataRequired()])
    submit = SubmitField('Delete Current Account')
