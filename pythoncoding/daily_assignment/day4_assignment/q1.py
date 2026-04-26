class BankAccount:

#constructor
    def __init__(self,acc_no,name,balance):
       self.__account_number=acc_no
       self.__account_holder=name
       self.__balance=balance

#getters
    def get_account_number(self):
        return self.__account_number
    def get_account_holder(self):
        return self.__account_holder
    def get_balance(self):
        return self.__balance
#setters
    def set_account_holder(self,name):
       self.__account_holder=name
    def set_balance(self,amount):
       if amount>=0:
        self.__balance=amount
       else:
        print("invalid balance amount")
    def deposit(self,amount):
       if amount>0:
        self.__balance+=amount
        print("deposited:",amount)
       else:
        print("invalid deposit amount")
    def withdraw(self,amount):
       if amount<=0:
        print("invalid withdrawal amount")
       elif amount>self.__balance:
        print("insufficient balance")
       else:
        self.__balance-=amount
        print("withdrawn:",amount)
    def display(self):
        print("account no:",self.__account_number)
        print("account holder:",self.__account_holder)
        print("balance:",self.__balance)