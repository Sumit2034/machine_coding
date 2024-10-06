from typing import Optional

from model.user import User
from repository.expense_repository import ExpenseRepository

class UserService:
    def __init__(self, expense_repository: ExpenseRepository):
        self.expense_repository = expense_repository
    
    def add_user(self, user: User):
        self.expense_repository.add_user(user)
    
    def get_user(self, user_name: str) -> Optional[User]:
        return self.expense_repository.get_user(user_name)
