from abc import ABC, abstractmethod


class InterestStrategy(ABC):
    
    @abstractmethod
    def calculate_interest(self, principal: float, rate: float, tenure: int) -> float:
        pass