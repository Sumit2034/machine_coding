from abc import ABC, abstractmethod

class Split(ABC):
    def __init__(self, user, amount=0.0):
        self._user = user
        self._amount = amount

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, user):
        self._user = user

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        self._amount = amount

