from typing import List

from strategies.interest_strategy import InterestStrategy


class Loan:
    def __init__(self, admin_username: str, customer_username: str, principal_amount: float, interest_rate: float, loan_tenure: int, interest_strategy: InterestStrategy):
        self.admin_username = admin_username
        self.customer_username = customer_username
        self.principal_amount = principal_amount
        self.interest_rate = interest_rate
        self.loan_tenure = loan_tenure
        self.emi_payments: List[float] = []
        self.remaining_principal = 0.0
        self.calculate_emi_payments(interest_strategy)

    def calculate_emi_payments(self, interest_strategy: InterestStrategy):
        interest = interest_strategy.calculate_interest(self.principal_amount, self.interest_rate, self.loan_tenure)
        total_amount = self.principal_amount + interest
        emi = total_amount / (self.loan_tenure * 12)
        self.emi_payments = [emi] * (self.loan_tenure * 12)
        self.remaining_principal = total_amount

    def make_emi_payment(self, amount: float):
        if self.remaining_principal > 0 and self.emi_payments:
            self.emi_payments.pop(0)
            self.remaining_principal -= amount
    
    def fetch_loan_info(self):
        print("Loan Details:")
        print(f"Admin Username: {self.admin_username}")
        print(f"Customer Username: {self.customer_username}")
        print(f"Principal Amount: {self.principal_amount}")
        print(f"Interest Rate: {self.interest_rate}")
        print(f"Loan Tenure: {self.loan_tenure}")
        print(f"EMI Payments Done: {self.loan_tenure * 12 - len(self.emi_payments)}")
        print(f"Remaining Principal: {self.remaining_principal}")
        print(f"Remaining EMIs: {len(self.emi_payments)}")

    def get_customer_username(self) -> str:
        return self.customer_username
