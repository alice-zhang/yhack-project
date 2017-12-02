from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

class LoginForm(FlaskForm):
	email = StringField('Email')
	name = StringField('Name')
	username = StringField('Username')
	password = PasswordField('Password')
	submit = SubmitField('Register')

"""
class EntryForm(FlaskForm):
	author = StringField()
	content = StringField()
	submit = SubmitField()
"""