from typing import List

from model.expense.expense import Expense
from model.split.equal_split import EqualSplit

class EqualExpense(Expense):
    def __init__(self, amount, expense_paid_by, splits, expense_data):
        super().__init__(amount, expense_paid_by, splits, expense_data)

    def validate(self):
        return all(isinstance(split, EqualSplit) for split in self.splits)
