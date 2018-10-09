from models.user import *
import sys

class LoginController:
    def login(email: str, password: str):
        user = UserRepositoryInstance.get_user(email, password)
        return user
        