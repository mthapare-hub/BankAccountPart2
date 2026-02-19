from BankAccount import MarvinBank

class AccountWithTransferLimit(MarvinBank):
    bankName = "AccountWithTransferLimit"

    def __init__(self, customer_name, current_balance, minimum_balance, transfer_limit):
        super().__init__(customer_name, current_balance, minimum_balance)
        self.transfer_limit = transfer_limit

    def withdraw(self, balance):
        if self.current_balance < self.minimum_balance:
            print("Your current balance is lower than the minimum balance.")
            return
        elif balance > self.transfer_limit:
            print("The amount you're trying to withdraw is higher than the transfer limit. Your transfer limit is: " + str(self.transfer_limit))

        self.current_balance -= balance