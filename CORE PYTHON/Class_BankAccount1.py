class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    #instance method
    def transfer(self,receiver,amount):
        if BankAccount.validate_transfer_amount(amount):
            if self.balance>=amount:
                self.balance-=amount
                receiver.balance+=amount
                print("Transfer successful")
                print("Transferred:",amount)
            else:
                print("Insufficient balance")
        else:
            print("Invalid transfer amount")
    #static method
    @staticmethod
    def validate_transfer_amount(amount):
        return amount > 0

a1 = BankAccount("Shrishail", 5000)
a2 = BankAccount("Rahul", 3000)

print("Before transfer:")
print("Shrishail:", a1.balance)
print("Rahul:", a2.balance)

a1.transfer(a2, 1000)

print("After transfer:")
print("Shrishail:", a1.balance)
print("Rahul:", a2.balance)
