from schema import User
from utils import verify_password


class UserService:
    def __init__(self, users: list[User]):
        self.users = users

    def find_user_by_email(self, email: str):
        for user in self.users:
            if user.email == email:
                return user

        return None

    def find_user_by_id(self, id: str):
        for user in self.users:
            if user.id == id:
                return user

        return None

    def check_password(self, email: str, password: str):
        user = self.find_user_by_email(email)
        if not user:
            return False

        return verify_password(password, user.password)
