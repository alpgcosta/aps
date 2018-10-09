class Facade:
    def login(email, password):
        return UserRepositoryInstance.get_user(email, password)

    def signup(email, password):
        signed_up = False
        user = User(email, password)
        if UserRepositoryInstance.verify_email(email):
            UserRepositoryInstance.add(user)
            signed_up = True
        return signed_up