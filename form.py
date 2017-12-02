from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
#from wtforms_components import TimeField

class LoginForm(FlaskForm):
	name = StringField('Name')
	uni = StringField('UNI')
	password = PasswordField('Password')
	email = StringField('Email')
	#phone = PhoneNumberField('Phone')
	phone = StringField('Phone')
	submit = SubmitField('Login')

"""
class DoForm(FlaskForm):
	task = StringField('Task')
	descr = StringField('Descr')
	finish_time = TimeField('Finish Time')
	location = StringField('Location')
	reward = StringField('Reward')
"""

"""
class SignupForm(FlaskForm):
	name = StringField('Name')
	uni = StringField('UNI')
	password = PasswordField('Password')
	email = StringField('Email')
	#phone = PhoneNumberField('Phone')
	phone = StringField('Phone')
	submit = SubmitField('Sign Up')
"""


"""
class EntryForm(FlaskForm):
	author = StringField()
	content = StringField()
	submit = SubmitField()
"""