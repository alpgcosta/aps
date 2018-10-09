import pymongo

class User:
    def __init__(self, email: str, password: str):
        self.email = email
        self.password = password

class UserRepository:
    def __init__(self):
        self.db = pymongo.MongoClient('mongodb://root:aps@mongo:27017').aps.users

    def add(self, user: User):
        assert(isinstance(user, User))
        assert(self.verify_email(user.email))
        self.db.insert_one({"email": user.email, "password": user.password})

    def verify_email(self, email: str) -> bool:
        assert(isinstance(email, str))
        user = self.db.find_one({"email": email})
        return user == None

    def get_user(self, email: str, password: str) -> User:
        ret = self.db.find_one({"email": email, "password": password})
        if ret == None:
            return ret
        return User(ret["email"], ret["password"])

UserRepositoryInstance = UserRepository()