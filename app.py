from flask import Flask, render_template, url_for, redirect, session
from flask_bootstrap import Bootstrap
from flask_mongoengine import MongoEngine 
from mongoengine import StringField, EmailField

from form import LoginForm

app = Flask(__name__)
app.config['DEBUG'] = True #every time you run an error, it will show an error message; without this line, the server will crash and you won't know why
app.config['SECRET_KEY'] = 'SOME_STRING_THATS_SECRET'

bootstrap = Bootstrap()
bootstrap.init_app(app)

app.config['MONGODB_SETTINGS'] = {
    'db': 'yhack-db',
    'host': 'ds125906.mlab.com',
    'port': 25906,
    'username': 'admin',
    'password': 'gocolumbia2021'
}

db = MongoEngine()
db.init_app(app)

class User(db.Document):
	name = StringField(required=True)
	uni = StringField(required=True)
	password = StringField(required=True)
	email = EmailField(required=True)
	phone = StringField(required=True)

class Task(db.Document):
	task = StringField(required=True)
	descr = StringField(required=True)
	reward = StringField(required=True)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/login', methods=['GET','POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		user = User(name=form.name.data, uni=form.uni.data, password=form.password.data, email=form.email.data, phone=form.phone.data)
		user.save()

		session['name'] = user.name
		session['uni'] = uni.name
		session['password'] = user.password
		session['email'] = user.email
		session['phone'] = user.phone

		redirect(url_for('login')) 
	return render_template('login.html', form=form, name=session.get('name'), )

@app.route('/asks', methods=['GET','POST'])
def asks():
	return render_template('asks.html')

@app.route('/do', methods=['GET','POST'])
	form = DoForm()
	if form.validate_on_submit():
		session['task'] = form.task.data
		session['descr'] = form.descr.data
		session['reward'] = form.reward.data

		redirect(url_for('do'))
	return render_template('do.html', form=form, task=session.get('task'), descr=session.get('descr'), reward=session.get('reward'))

@app.route('/me', methods=['GET','POST'])
def me():
	return render_template('me.html')

if __name__ == "__main__": #main is magic variable
	app.run() 
