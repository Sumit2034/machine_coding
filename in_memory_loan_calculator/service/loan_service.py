from collections import defaultdict

from model.loan import Loan
from service.user_service import UserService


class LoanService:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(LoanService, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self.loans = defaultdict(list)
        self.user_service = UserService()

    def create_loan(self, admin_username, customer_username, principal_amount, interest_rate, loan_tenure, interest_strategy):
        admin = self.user_service.get_user(admin_username)
        if admin and admin.is_user_admin():
            new_loan = Loan(admin_username, customer_username, principal_amount, interest_rate, loan_tenure, interest_strategy)
            self.loans[customer_username].append(new_loan)
            print("Loan created successfully.")
        else:
            print(f"Admin with username {admin_username} not found or unauthorized.")

    def make_emi_payment(self, customer_username, amount):
        customer_loans = self.loans.get(customer_username)
        if customer_loans:
            for loan in customer_loans:
                loan.make_emi_payment(amount)
            print("EMI payment successful.")
        else:
            print(f"No active loan found for customer {customer_username}")

    def fetch_loan_info(self, customer_username, requesting_username):
        if customer_username != requesting_username:
            print("Access denied. You are not authorized to fetch loan info for this user.")
            return

        customer_loans = self.loans.get(customer_username)
        if customer_loans:
            for loan in customer_loans:
                loan.fetch_loan_info()
                print("--------------------------")
        else:
            print(f"No active loan found for customer {customer_username}")

    def fetch_all_loans(self, admin_username):
        admin = self.user_service.get_user(admin_username)
        if admin and admin.is_admin:
            for customer_loans in self.loans.values():
                for loan in customer_loans:
                    loan.fetch_loan_info()
                    print("--------------------------")
        else:
            print(f"Admin with username {admin_username} not found or unauthorized.")

