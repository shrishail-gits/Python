class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposited:", amount)
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
                print("Withdrawn:", amount)
            else:
                print("Insufficient balance")
        else:
            print("Invalid withdrawal amount")

    def get_balance(self):
        return self.__balance


# Creating object
account = BankAccount(10000)

# Deposit
account.deposit(5000)

# Withdraw
account.withdraw(3000)

# Display balance
print("Current Balance:", account.get_balance())