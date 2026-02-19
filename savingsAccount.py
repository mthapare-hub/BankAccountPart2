from BankAccount import MarvinBank

class SavingsAccount(MarvinBank):
    interestRate = .05
    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number):
        super().__init__(customer_name, current_balance, minimum_balance, account_number, routing_number)

    def apply_interest(self):
        interest = self.current_balance * (1 + SavingsAccount.interestRate)
        print(f"{self.customer_name} balance after interest would be:  ${interest}")

    def deposit(self, amount):
        print(f"You deposited ${amount} for a total of ${amount + self.current_balance}")
        self.current_balance = (self.current_balance + amount) * (1 + SavingsAccount.interestRate)
        print(f"Your new balance after interest would be:  ${self.current_balance}")