from strategies.interest_strategy import InterestStrategy


class SimpleInterestStrategy(InterestStrategy):
    
    def calculate_interest(self, principal: float, rate: float, tenure: int) -> float:
        return (principal * rate * tenure) / 100