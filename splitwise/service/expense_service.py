from typing import List

from model.expense.equal_expense import EqualExpense
from model.expense.exact_expense import ExactExpense
from model.expense.expense import Expense
from model.expense.expense_data import ExpenseData
from model.expense.percent_expense import PercentExpense
from model.expense_type import ExpenseType
from model.split.percent_split import PercentSplit
from model.split.split import Split
from model.user import User

class ExpenseService:

    @staticmethod
    def create_expense(expense_type: ExpenseType, amount: float, expense_paid_by: User, splits: List[Split], expense_data: ExpenseData) -> Expense:
        if expense_type == ExpenseType.EXACT:
            return ExactExpense(amount, expense_paid_by, splits, expense_data)
        
        elif expense_type == ExpenseType.PERCENT:
            for split in splits:
                if isinstance(split, PercentSplit):
                    percent_split = split
                    split.amount = (amount * percent_split.percent) / 100.0
            return PercentExpense(amount, expense_paid_by, splits, expense_data)
        
        elif expense_type == ExpenseType.EQUAL:
            total_splits = len(splits)
            split_amount = round(amount * 100 / total_splits) / 100.0
            for split in splits:
                split.amount = split_amount
            return EqualExpense(amount, expense_paid_by, splits, expense_data)
        
        return None

# Assuming the following classes are defined: Expense, User, ExpenseData, PercentSplit, Split, ExactExpense, PercentageExpense, EqualExpense
