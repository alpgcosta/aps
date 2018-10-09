from models.user import *
from flask import render_template, redirect, request, flash, session
import sys

class LoginController:
    def login(email: str, password: str):
        user = UserRepositoryInstance.get_user(email, password)
        if user == None:
            return redirect('/login/')
        session['email'] = user.email
        return redirect('/login/')
        