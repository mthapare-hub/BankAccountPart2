from savingsAccount import SavingsAccount

class MarvinBank:
    bankName = "Marvin's Bank"
    def __init__(self, customer_name, current_balance, minimum_balance):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance

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


# Marvin =  MarvinBank("Marvin", 100000, 1000)
# Marvin.deposit(100000)
# Marvin.withdraw(200000)
# Marvin.withdraw(100000)
#
# Marvin.print_customer_info()
#
# Lucy = MarvinBank("Lucy", 200000, 100)
# Lucy.deposit(500000)
# Lucy.withdraw(300000)
# #Lucy.withdraw(300000)
#
# Lucy.print_customer_info()
