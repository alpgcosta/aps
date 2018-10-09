from models.user import *
from flask import render_template, redirect, request, flash, session

class SignupController:
    def signup(email: str, password: str):
        signed_up = False
        user = User(email, password)
        if UserRepositoryInstance.verify_email(email):
            UserRepositoryInstance.add(user)
            return not UserRepositoryInstance.verify_email(email)
        if signed_up:
            return redirect('/login/')
        else:
            flash('failed')
            return redirect('/signup/')