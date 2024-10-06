from enum import Enum

class ExpenseType(Enum):
    EQUAL = "EQUAL"
    EXACT = "EXACT"
    PERCENT = "PERCENT"

    def __str__(self):
        return self.value

    @staticmethod
    def of(name):
        return ExpenseType._value2member_map_.get(name, None)

