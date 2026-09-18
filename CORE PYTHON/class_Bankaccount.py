class BankAccount:
    bank_name="HDFC Bank"
    def __init__(self,account_no,holder_name,balance):
        self.account_no=account_no
        self.holder_name=holder_name
        self.balance=balance
    def deposit(self,amount):
       self.balance+=amount

    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
        else:
            print("Insufficient balance")
    def display(self):
        print("Account no:",self.account_no)
        print("Holder:",self.holder_name)
        print("Balance:",self.balance)
        print("Bank:",BankAccount.bank_name)

    @classmethod
    def change_bank(cls,new_bank):
        cls.bank_name=new_bank

    @staticmethod
    def validate_amount(amount):
        if amount>0:
            return True
        else:
            return False
a1=BankAccount(101,"Shrishail",5000)
a1.deposit(2000)
a1.withdraw(1000)
a1.display()
print("valid:",BankAccount.validate_amount(500))
BankAccount.change_bank("Axis Bank")
a1.display()


