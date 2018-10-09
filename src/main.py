from flask import Flask, render_template, redirect, request, flash, session
from signup import SignupController
from login import LoginController

app = Flask(__name__)
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'memcache'

@app.route("/signup/", methods = ["GET", "POST"])
def signup():
    if request.method == "GET":
        return render_template('signup.html')
    else:
        email = request.form['email']
        password = request.form['password']
        return SignupController.signup(email, password)

@app.route("/login/", methods = ["GET", "POST"])
def login():
    if request.method == "GET":
        if 'email' in session:
            return "Welcome, " + session['email']
        return render_template('login.html')
    else:
        email = request.form['email']
        password = request.form['password']
        return LoginController.login(email, password)

app.run(host='0.0.0.0', port=80)
