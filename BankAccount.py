class MarvinBank:
    bankName = "Marvin's Bank"
    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance

        """Protected member (Account Number)"""
        self._account_number = account_number

        """Private member (Routing Number)"""
        self.__routing_number = routing_number

    def deposit(self, balance):
        self.current_balance += balance

    def withdraw(self, balance):
        if self.current_balance < self.minimum_balance:
            print("Your current balance is lower than the minimum balance.")
            return

        self.current_balance -= balance

    def print_customer_info(self):
        print("********"+ MarvinBank.bankName + "********")
        print("Customer Name: " + self.customer_name)
        print("Current Balance: " + str(self.current_balance))
        print("Minimum Balance: " + str(self.minimum_balance))
        print("**************************")


