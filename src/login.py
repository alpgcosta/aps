from models.user import *
from flask import render_template, redirect, request, flash, session
import sys
from facade import Facade

class LoginController:
    def login(email: str, password: str):
        user = Facade.login(email, password)
        if user == None:
            return redirect('/login/')
        session['email'] = user.email
        return redirect('/login/')
        