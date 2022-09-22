# -*- coding: utf-8 -*-

class BankAccount:
    # back account class which is used in Portfolio
    def __init__(self, initialBalance = 0.0):
        self._balance = initialBalance
    

    def addInterest(self, rate) :
        self._balance = self._balance + self._balance * rate / 100.0
    
    def deposit(self, amount) :
        self._balance = self._balance + amount

    def withdraw(self, amount) :
        PENALTY = 10.0
        if amount > self._balance :
            self._balance = self._balance - PENALTY
        else :
            self._balance = self._balance - amount

    def getBalance(self):
        return self._balance

class Portfolio:
    # class contains two instances of class BankAccount
    # methods from class BankAccount can be used within Portfolio class
    def __init__(self):
        self._checking = BankAccount()
        self._savings = BankAccount()
        
    # Since there is only checking and savings, only need a simple
    # if statement to decide which account amount is deposited into
    # here method deposit from BankAccount class is used 
    def deposit(self, amount, account):
        if account == "C":
            self._checking.deposit(amount)
        else:
            self._savings.deposit(amount)

    # for the withdraw method, same procedure as deposit is used
    # here withdraw from BankAccount class is used 

    def withdraw(self, amount, account):
        if account == "C":
            self._checking.withdraw(amount)
        else:
            self._savings.withdraw(amount)

    # in addition to the if statement to decide account
    # it is also needed to use getBalance method to check 
    # if there is enough funds in the account for the amount which 
    # should be transferred 
    
    def transfer(self, amount, account):
        if account == "C":
            if self._checking.getBalance() >= amount: 
                self._checking.withdraw(amount)
                self._savings.deposit(amount)
            else:
                print("You don't have enough funds in your checking\
 account for this transfer.")
        else:
            if self._savings.getBalance() >= amount: 
                self._savings.withdraw(amount)
                self._checking.deposit(amount)
            else:
                print("You don't have enough funds in your savings account\
 for this transfer.")
 
 #Returns balance, only need a if statement to determine account,
 #then uses getBalance from BankAccount
    def getBalance(self, account):
        if account == "C":
            return self._checking.getBalance()
        else:
            return self._savings.getBalance()

# testing

accounts = Portfolio()
accounts.deposit(2000, "C")
accounts.deposit(5000, "S")
print(accounts.getBalance("C")) # prints 2000
print(accounts.getBalance("S")) # prints 5000
accounts.transfer(4000,"S")
print(accounts.getBalance("C")) # prints 6000
print(accounts.getBalance("S")) # prints 1000
accounts.transfer(8000, "C") # prints "You don't have enough funds in your checking account for this transfer."
accounts.withdraw(6000, "C")
print(accounts.getBalance("C")) # prints 0