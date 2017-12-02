from flask import Flask, render_template, url_for, redirect, session
from flask_bootstrap import Bootstrap
from flask_mongoengine import MongoEngine 
from mongoengine import StringField, EmailField

from form import LoginForm
#from form import EntryForm

app = Flask(__name__)
app.config['DEBUG'] = True #every time you run an error, it will show an error message; without this line, the server will crash and you won't know why
app.config['SECRET_KEY'] = 'SOME_STRING_THATS_SECRET'

bootstrap = Bootstrap()
bootstrap.init_app(app)


db = MongoEngine()
db.init_app(app)

"""
app.config['MONGODB_SETTINGS'] = {
    'db': adi_academy,
    'host': ds125126.mlab.com,
    'port': 25126,
    'username': ayz2105,
    'password': #### !!!!!!!
}
"""
"""
class Entry(db.Document):
	author = StringField(required=True) #new Entry has to have author defined
	content = StringField()
"""

@app.route('/')
def home():
	return render_template('me.html', name='Alice', my_friends={'jonathan': 68, 'cesar': 62, 'nick': 100})

"""
@app.route('/diary', methods=['GET','POST'])
def diary():
	form = EntryForm() #create new instance
	if form.validate_on_submit():
		entry = Entry(author=form.author.data, concent=form.content.data)
		entry.save()

		redirect(url_for('diary'))
	return render_template('/diary.html', form=form)
"""

@app.route('/login', methods = ['GET', 'POST'])
def login(): #create decorator
	username = None
	form = LoginForm()
	if form.validate_on_submit():
		session['username'] = form.username.data
		session['name'] = form.name.data
		print session.get('username')
		return redirect(url_for('login'))
	return render_template('login.html', form=form, username=session.get('username'), name=session.get('name'))

if __name__ == "__main__": #main is magic variable
	app.run() 