from models.user import *
from flask import render_template, redirect, request, flash, session
from facade import Facade

class SignupController:
    def signup(email: str, password: str):
        if Facade.signup(email, password):
            return redirect('/login/')
        else:
            flash('failed')
            return redirect('/signup/')