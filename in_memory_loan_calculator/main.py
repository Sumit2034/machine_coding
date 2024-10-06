from model.user import User
from service.loan_service import LoanService
from service.user_service import UserService
from strategies.simple_interest_strategy import SimpleInterestStrategy

def main():
    # Instantiate services
    user_service = UserService()
    loan_service = LoanService()

    # Create users
    admin = user_service.create_user("admin1", True)
    customer1 = user_service.create_user("customer1", False)
    customer2 = user_service.create_user("customer2", False)

    # Create loans by admin
    loan_service.create_loan(admin.get_username(), customer1.get_username(), 10000, 5.0, 2, SimpleInterestStrategy())
    loan_service.create_loan(admin.get_username(), customer1.get_username(), 5000, 4.0, 1, SimpleInterestStrategy())

    # Customer makes EMI payment
    loan_service.make_emi_payment(customer1.get_username(), 500)

    # Fetch loan info for customer
    loan_service.fetch_loan_info(customer1.get_username(), customer1.get_username())

    # Admin fetches all loans
    loan_service.fetch_all_loans("admin1")

    loan_service.create_loan("admin1", customer2.get_username(), 1000, 2, 3, SimpleInterestStrategy())

    loan_service.make_emi_payment(customer2.get_username(), 500)

    loan_service.fetch_loan_info(customer2.get_username(), customer2.get_username())

if __name__ == "__main__":
    main()
