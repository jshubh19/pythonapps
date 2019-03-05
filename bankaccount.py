# bank account
class BankAccount:
    ''' this is Janta ka Bank'''
    def __init__(self,accountname='BankAccount',balance=20000): #for making class method we use __init__ const
        self.accountname=accountname
        self.balance=baalance
    def deposite (self,value):
        self.balance=self.balance+value
        print('your balance is ',self.balance)
    def withdraw (self,value):
        self.balance=self.balance-value
        print('your balance is ',self.balance)

class currentaccount(BankAccount):
    def __init__(self,accountname='currentaccount',balance=20000):
        self.accountname=accountname
        self.balance=balance
    def withdraw(self,value):
        if value>1000:
            print('you cant withdraw that amount')
        else:
            self.balance=self.balance-value
            print('your currentaccount balance is',self.balance)

class savingaccount(BankAccount):
    def __init__(self,accountname='savingaccount',balance=20000):
        self.accountname=accountname
        self.balance=balance
    def deposite (self,value):
        self.balance=self.balance+value*0.3
        print('your savingaccount balance is ',self.balance)

oc=currentaccount()
os=savingaccount()

while True:
    print('1.currentaccount')
    print('2.savingaccount')
    main_menu=int(input('please select your option '))
    if main_menu==1:
        print('1.deposite')
        print('2.withdraw')
        sub_menu=int(input('please choose your option '))
        if sub_menu==1:
            value=int(input('enter the amount to deposite '))
            oc.deposite(value)
        
        elif sub_menu==2:
            value=int(input('enter amount to withdraw '))
            oc.withdraw(value)
            
        else:
                print('you just choosed invalid option ')
    elif main_menu==2:
        print('1.deposite')
        print('2.withdraw')
        sub_menu=int(input('please choose your option  '))
        if sub_menu==1:
            value=int(input('enter your amount for deposite  '))
            os.deposite(value)
            
        elif sub_menu==2:
            value=int(input('enter amount to withdraw  '))
            os.withdraw(value)
            
        else:
            print('you just choosed invalid option ')
    else:
        print('you choose invalid account type ')
    break
        
            
                
            
            
