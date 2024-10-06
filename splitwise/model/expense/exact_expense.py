from typing import List

from model.expense.expense import Expense
from model.split.exact_split import ExactSplit

class ExactExpense(Expense):
    def __init__(self, amount, expense_paid_by, splits, expense_data):
        super().__init__(amount, expense_paid_by, splits, expense_data)

    def validate(self):
        total_amount = self.amount
        total_split_amount = 0.0
        for split in self.splits:
            if not isinstance(split, ExactSplit):
                return False
            total_split_amount += split.amount
        
        return total_amount == total_split_amount

