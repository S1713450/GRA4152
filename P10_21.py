## A bank account has a balance and a mechanism for
# the end of the month.
#
class BankAccount :
    ## Constructs a bank account with zero balance.
    #
    def __init__(self) :
        self._balance = 0.0
   
    ## Makes a deposit into this account.
    # @param amount the amount of the deposit
    #
    def deposit(self, amount) :
        self._balance = self._balance + amount
    
    ## Makes a withdrawal from this account, or charges
    # sufficient funds are not available.
    # @param amount the amount of the withdrawal
    #
    def withdraw(self, amount) :
        self._balance = self._balance - amount
    
    ## Carries out the end
    # for this account.
    #
    def monthEnd(self) :
        return
    
    ## Gets the current balance of this
    # @return the current balance
    #
    def getBalance(self) :
        return self._balance


# A savings account earns interest on the minimum balance.
#
class SavingsAccount(BankAccount) :
    ## Constructs a savings account with a zero balance.
    #
    def __init__(self, rate) :
        super().__init__()
        self._minBalance = 0
        self._rate = rate 

    ## Sets the interest rate for this account.
    # @param rate the monthly interest rate
    #
    def setInterestRate(self, rate) :
        self._rate = rate

    # These methods override superclass
    def withdraw(self, amount) :
        super().withdraw(amount)
        balance = self.getBalance()
        if balance < self._minBalance :
            self._minBalance = balance
    

    def monthEnd(self) :
        interest = self._minBalance * self._rate / 100
        self.deposit(interest)
        self._minBalance = self.getBalance()

## A checking account has a limited number of free deposits
#
class CheckingAccount(BankAccount) :
    ## Constructs a checking account with a zero balance.
    #
    def __init__(self) :
        super().__init__()
        self._withdrawals = 0 
        # overrides superclass
    def deposit(self, amount):
        super().deposit(amount)
        self.computeFee()
    
        # overrides superclass
    def withdraw(self, amount) :
        super().withdraw(amount)
        self.computeFee()
    
    # counts transactions and adds fee if it is above 3 in a month
    def computeFee(self):
        FREE_WITHDRAWS = 3
        WITHDRAWAL_FEE = 1

        self._withdrawals += 1
        if self._withdrawals > FREE_WITHDRAWS :
            super().withdraw(WITHDRAWAL_FEE)
            
    # resets transaction count at month end 
    def monthEnd(self) :
        self._withdrawals = 0 

# testing
a = CheckingAccount()

a.deposit(100) # 100 expected
print(a.getBalance())
a.withdraw(1) # 99 expected 
print(a.getBalance())
a.withdraw(1) # 98 expected 
print(a.getBalance())
a.withdraw(1) # 96 expected since this is the fourth transaction in one month
print(a.getBalance())
a.monthEnd() # new month
a.withdraw(1) # 95 expected 
print(a.getBalance())
a.withdraw(1) # 94 expected 
print(a.getBalance())
a.withdraw(1) # 93 expected
print(a.getBalance())
a.withdraw(1) # 91 expected since its the fourth transaction
print(a.getBalance())
a.withdraw(1) # 89 expected because fee 
print(a.getBalance())


# more accounts to use testing program from book

a1 = SavingsAccount(10)
a2 = CheckingAccount()
a3 = SavingsAccount(5)
a4 = CheckingAccount()
accounts = [a1, a2, a3, a4]


#%% Testing program from book
done = False
while not done :
    action = input("D)eposit W)ithdraw M)onth end Q)uit: ")
    action = action.upper()
    if action == "D" or action == "W" :
        # Deposit or withdrawal.
        num = int(input("Enter account number: "))
        amount = float(input("Enter amount: "))
        if action == "D" :
            accounts[num].deposit(amount)
        else :
            accounts[num].withdraw(amount)

        print("Balance:", accounts[num].getBalance())
    
    elif action == "M" :
        # Month end processing.
        for n in range(len(accounts)) :
            accounts[n].monthEnd()
            print(n, accounts[n].getBalance())
    elif action == "Q" :
        done = True
            
        