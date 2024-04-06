from flask import Flask, request, render_template, url_for, redirect
from validator import value
import mysql.connector

app = Flask(__name__)

conn = mysql.connector.connect(host="127.0.0.1", user="root", password="", database= "pro")
cursor = conn.cursor()

@app.route("/main")
def home():
    return render_template("login.html")

@app.route("/SignUp")
def SignUp():
	return render_template("SignupForm.html")

@app.route("/Login",methods=['POST'])
def Login():
	email = request.form.get('email')
	password = request.form.get('password')
	cursor.execute(""" SELECT * FROM `users` WHERE `email` LIKE '{}' AND `password` LIKE '{}'""".format(email, password))
	users = cursor.fetchall()
	if len(users)>0:
		return render_template('index.html')
	else:
		return render_template('login.html')
#	return render_template("SignupForm.html")

@app.route("/addUser",methods=['POST'])
def addUser():
	name = request.form.get('name')
	email = request.form.get('email')
	password = request.form.get('password')
	
	cursor.execute("""INSERT INTO `users` (`name`, `email`, `password`) VALUES ('{}', '{}', '{}')""".format(name, email, password))
	conn.commit()
	
	return "Registered successfully"

@app.route("/",methods=["POST"])
def output():
    form_data = request.form
    status = value(form_data)
    return render_template("response.html",status=status)

if __name__ == "__main__":
    app.run(debug=True)

