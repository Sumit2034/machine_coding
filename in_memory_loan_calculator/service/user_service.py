from model.user import User


class UserService:
    _instance = None
    _users = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(UserService, cls).__new__(cls)
        return cls._instance

    def create_user(self, username: str, is_admin: bool):
        if username not in self._users:
            self._users[username] = User(username, is_admin)
            print("User created successfully.")
            return self._users[username]
        else:
            print(f"User with username {username} already exists.")
            return
        

    def get_user(self, username: str):
        return self._users.get(username)
