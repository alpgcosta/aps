from models.user import *

class SignupController:
    def signup(email: str, password: str):
        user = User(email, password)
        if not UserRepositoryInstance.verify_email(email):
            return False
        UserRepositoryInstance.add(user)
        return not UserRepositoryInstance.verify_email(email)