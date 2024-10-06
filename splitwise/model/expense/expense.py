from abc import ABC, abstractmethod
from typing import List
import uuid

class Expense(ABC):
    def __init__(self, amount, expense_paid_by, splits, expense_data):
        self._id = str(uuid.uuid4())
        self._amount = amount
        self._expense_paid_by = expense_paid_by
        self._splits = splits
        self._expense_data = expense_data

    @property
    def id(self):
        return self._id

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        self._amount = amount

    @property
    def expense_paid_by(self):
        return self._expense_paid_by

    @expense_paid_by.setter
    def expense_paid_by(self, expense_paid_by):
        self._expense_paid_by = expense_paid_by

    @property
    def splits(self):
        return self._splits

    @splits.setter
    def splits(self, splits):
        self._splits = splits

    @property
    def expense_data(self):
        return self._expense_data

    @expense_data.setter
    def expense_data(self, expense_data):
        self._expense_data = expense_data

    @abstractmethod
    def validate(self):
        pass
