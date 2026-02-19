from BankAccount import MarvinBank


class SavingsAccount(MarvinBank):
    interestRate = 5
    def __init__(self, customer_name, current_balance, minimum_balance):
        super().__init__(customer_name, current_balance, minimum_balance)

