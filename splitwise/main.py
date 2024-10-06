from model.expense.expense_data import ExpenseData
from model.expense_type import ExpenseType
from model.split.equal_split import EqualSplit
from model.split.exact_split import ExactSplit
from model.split.percent_split import PercentSplit
from model.type import Type
from model.user import User
from repository.expense_repository import ExpenseRepository
from service.splitwise_service import SplitWiseService
from service.user_service import UserService


def main():
    # Sample Users
    user1 = User(user_id=1, user_name="u1", email="u1@gmail.com", mobile_number="9890098900")
    user2 = User(user_id=2, user_name="u2", email="u2@gmail.com", mobile_number="9999999999")
    user3 = User(user_id=3, user_name="u3", email="u3@gmail.com", mobile_number="9898989899")
    user4 = User(user_id=4, user_name="u4", email="u4@gmail.com", mobile_number="8976478292")

    # Initialize services
    expense_repository = ExpenseRepository()
    user_service = UserService(expense_repository)
    user_service.add_user(user1)
    user_service.add_user(user2)
    user_service.add_user(user3)
    user_service.add_user(user4)
    service = SplitWiseService(expense_repository)

    while True:
        commands = input().split()
        command_type = Type[commands[0].upper()]
        if command_type == Type.EXPENSE:
            user_name = commands[1]
            amount_spent = float(commands[2])
            total_members = int(commands[3])
            splits = []
            expense_index = 4 + total_members
            expense_type = ExpenseType[commands[expense_index].upper()]
            if expense_type == ExpenseType.EQUAL:
                for i in range(total_members):
                    splits.append(EqualSplit(user=user_service.get_user(commands[4+i])))
                service.add_expense(expense_type, amount_spent, user_name, splits, ExpenseData(name="GoaFlight"))
            elif expense_type == ExpenseType.EXACT:
                for i in range(total_members):
                    splits.append(ExactSplit(user=user_service.get_user(commands[4+i]), amount=float(commands[expense_index+1+i])))
                service.add_expense(expense_type, amount_spent, user_name, splits, ExpenseData(name="CabTickets"))
            elif expense_type == ExpenseType.PERCENT:
                for i in range(total_members):
                    splits.append(PercentSplit(user=user_service.get_user(commands[4+i]), percent=float(commands[expense_index+1+i]), amount=0))
                service.add_expense(expense_type, amount_spent, user_name, splits, ExpenseData(name="Dinner"))
        elif command_type == Type.SHOW:
            if len(commands) == 1:
                service.show_balances()
            else:
                service.show_balance(commands[1])
        elif command_type == Type.QUIT:
            print("Quitting...")
            break
        else:
            print("No Expected Argument Found")

if __name__ == "__main__":
    main()