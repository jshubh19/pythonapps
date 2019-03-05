#method overriding
print("Welcome to City Bank")
class BankAccount:
    def __init__(self,accountname='BankAccount',balance=10000):
        self.accountname=accountname
        self.balance=balance

    def deposite(self,value):
        self.balance=self.balance+value
        print("your account balance is :", self.balance)

    def withdraw(self,value):
        self.balance=self.balance-value
        print("your account balance is :", self.balance)

class CurrentAccount(BankAccount):
    def __init__(self,accountname='currentaccount',balance=10000):
        self.accountname=accountname
        self.balance=balance

    def withdraw(self,value):
        if value>1000:
            print("you cant withdraw that much amount")
        else:
            self.balance=self.balance-value
            print("your current account balance is :",self.balance)

class SavingAccount(BankAccount):
    def __init__(self, accountname= 'savingaccount' ,balance=10000):
        self.accountname=accountname
        self.balance=balance

    def deposite(self,value):
        if value>100:
            self.balance=self.balance+value*0.3
            print("your saving account balance is :",self.balance)


oc=CurrentAccount()
os=SavingAccount()

while True:
    print("1.CurrentAccount")
    print("2.SavingAccount")
    main_menu=int(input("enter your choice of account: "))
    if main_menu==1:
        print("1.deposite")
        print("2.withdraw")
        sub_menu=int(input("enter your choice : "))
        if sub_menu==1:
            value=int(input("enter amount to deposite: "))
            oc.deposite(value)
        elif sub_menu==2:
            value=int(input("enter amount for withdraw: "))
            oc.withdraw(value)
        else:
            print("you chose invalid option")
    elif main_menu==2:
        print("1.deposite")
        print("2.withdraw")
        sub_menu=int(input("enter your choice: "))
        if sub_menu==1:
            value=int(input("enter amount to deposite: "))
            os.deposite(value)
        elif sub_menu==2:
            value=int(input("enter amount for withdraw: "))
            os.withdraw(value)
        else:
            print("you entered invalid option:")
    else:
        print("you choose acoount type is invalid")

    break
