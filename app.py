from flask import Flask 
from flask import render_template
import forms
from flask import request
import csv

app = Flask(__name__)

@app.route('/')
def index():
	
	form = forms.FormLogin()		
	return render_template('index.html', form=form)


@app.route('/login', methods=["POST"])
def login():

	valido = False
	
	form = forms.FormLogin(request.form)

	user = form.user.data		
	password = form.password.data

	with open("usuarios.csv") as usuarios_archivo:
		usuarios = csv.reader(usuarios_archivo)

		for usuario in usuarios:
			if usuario[0] == user and usuario[1] == password:
				valido = True

	return render_template('account.html', password=password, usuario=user, valido=valido)


@app.route('/create')
def create():
	
	form = forms.FormLogin()		
	return render_template('create.html', form=form)


@app.route('/add', methods=["POST"])
def add():
	
	form = forms.FormLogin(request.form)

	user = form.user.data		
	password = form.password.data

	with open("usuarios.csv", "a") as usuarios_archivo:
		usuarios_archivo.write(user + "," + password + "\n")
		
	return render_template('created.html')
	
		
if __name__ == ('__main__'):
	app.run(debug = True)	