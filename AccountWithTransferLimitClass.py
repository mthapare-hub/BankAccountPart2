from BankAccount import MarvinBank

class AccountWithTransferLimit(MarvinBank):
    bankName = "AccountWithTransferLimit"

    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number, transfer_limit):
        super().__init__(customer_name, current_balance, minimum_balance, account_number, routing_number)
        self.transfer_limit = transfer_limit
    def withdraw(self, balance):
        if balance > self.transfer_limit:
            print("The amount you're trying to withdraw is higher than the transfer limit. Your transfer limit is: " + str(self.transfer_limit))
            return

        super().withdraw(balance)