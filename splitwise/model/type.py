from enum import Enum

class Type(Enum):
    EXPENSE = "EXPENSE"
    SHOW = "SHOW"
    QUIT = "QUIT"

    def __str__(self):
        return self.value

    @staticmethod
    def of(name):
        try:
            return Type[name]
        except KeyError:
            return None
