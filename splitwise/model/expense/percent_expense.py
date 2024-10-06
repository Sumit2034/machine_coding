from typing import List

from model.expense.expense import Expense
from model.split.percent_split import PercentSplit

class PercentExpense(Expense):
    def __init__(self, amount, expense_paid_by, splits, expense_data):
        super().__init__(amount, expense_paid_by, splits, expense_data)

    def validate(self):
        total_split_percent = 0.0
        for split in self.splits:
            if not isinstance(split, PercentSplit):
                return False
            total_split_percent += split.percent
        
        return total_split_percent == 100
