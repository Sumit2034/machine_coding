from typing import List, Dict
from collections import defaultdict

from service.expense_service import ExpenseService
from model.user import User

class ExpenseRepository:
    def __init__(self):
        self.expenses = []
        self.user_map = {}
        self.balance_sheet = defaultdict(lambda: defaultdict(float))

    def add_user(self, user: User):
        self.user_map[user.user_name] = user
        self.balance_sheet[user.user_name] = defaultdict(float)

    def get_user(self, user_name):
        return self.user_map.get(user_name)

    def add_expense(self, expense_type, amount, paid_by, splits, expense_data):
        expense = ExpenseService.create_expense(expense_type, amount, self.user_map.get(paid_by), splits, expense_data)
        if expense:
            self.expenses.append(expense)
            for split in expense.splits:
                paid_to = split.user.user_name

                self.balance_sheet[paid_by][paid_to] += split.amount
                self.balance_sheet[paid_to][paid_by] -= split.amount

    def get_balance(self, user_name):
        balances = []
        user_balances = self.balance_sheet.get(user_name, {})
        for other_user, balance in user_balances.items():
            if balance != 0:
                balances.append(self.check_sign(user_name, other_user, balance))
        return balances

    def get_balances(self):
        balances = []
        for user, user_balances in self.balance_sheet.items():
            for other_user, balance in user_balances.items():
                if balance > 0:
                    balances.append(self.check_sign(user, other_user, balance))
        return balances

    def check_sign(self, user1, user2, amount):
        user1_name = self.user_map[user1].user_name
        user2_name = self.user_map[user2].user_name
        if amount < 0:
            return f"{user1_name} owes {user2_name}: {abs(amount)}"
        elif amount > 0:
            return f"{user2_name} owes {user1_name}: {abs(amount)}"
        return ""

