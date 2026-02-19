from BankAccount import *
from AccountWithTransferLimitClass import *
from savingsAccount import *

Marvin = MarvinBank("Marvin", 100000, 1000)
Marvin.deposit(100000)
Marvin.withdraw(200000)
Marvin.withdraw(100000)

Marvin.print_customer_info()

Lucy = MarvinBank("Lucy", 200000, 100)
Lucy.deposit(500000)
Lucy.withdraw(300000)
# Lucy.withdraw(300000)

Lucy.print_customer_info()

Samuel = AccountWithTransferLimit("Samuel", 100000, 100, 500)
Samuel.deposit(100000)
Samuel.withdraw(100000)

Samuel.print_customer_info()