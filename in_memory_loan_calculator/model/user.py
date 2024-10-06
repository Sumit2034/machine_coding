class User:

    def __init__(self, username, is_admin) -> None:
        self.username = username
        self.is_admin = is_admin

    def get_username(self):
        return self.username

    def is_user_admin(self):
        return self.is_admin