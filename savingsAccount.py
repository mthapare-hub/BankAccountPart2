from BankAccount import MarvinBank

class SavingsAccount(MarvinBank):
    interestRate = .05
    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number):
        super().__init__(customer_name, current_balance, minimum_balance, account_number, routing_number)

    def apply_interest(self):
        interest = self.current_balance * (1 + SavingsAccount.interestRate)
        print(f"{self.customer_name} balance after interest would be:  ${interest}")