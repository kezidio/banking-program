# savingsaccount.py
"""SavingsAccount class definition."""
from account import Account
from decimal import Decimal

class SavingsAccount(Account):
    """SavingsAccount class."""
    
    def __init__(self, name, balance, interest_rate):
        """Initialize an SavingsAccount object."""
        
        # if interest_rate is out of range, raise an exception
        if interest_rate < Decimal('0.00') or interest_rate > Decimal('1.00'):
            raise ValueError('Interest rate must be in the range 0.0-1.0.')
            
        super().__init__(name, balance)
        self._interest_rate = interest_rate
        
    @property
    def interest_rate(self):
        return self._interest_rate
        
    def calculate_interest(self):
        return round(self.interest_rate * self.balance, 2)
    # Override Account class string method to include interest rate
    def __str__(self):
        return f"Name: {self.name}, Balance: {self.balance}, Interest Rate: {self.interest_rate}"



