# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 15:01:34 2022

@author: A2010377
"""

class Customer:
    # intialiazion 
    def __init__(self):
        self._saved = 0 
    
    # returning amount saved for next discount 
    def amountSaved(self):
        return self._saved
    # gives a 10$ discount if it is reached, if it is not reached
    # then it saves up for next discount 
    def makePurchase(self, amount):
        if not self.discountReached():
            self._saved = self._saved + amount
        else: 
            amount = amount -10
            self._saved = amount
    # Checks if discount is reached     
    def discountReached(self):
        if self._saved < 100:
            return False
        else:
            print("You got a 10$ discount on your purchase")
            return True 
        
customer = Customer()

customer.makePurchase(101) 
print(customer.amountSaved()) # prints 101
customer.makePurchase(107) # you earned discount, since you have accumulation 101
# so now you have to pay $97 instead of$107
# and the new accumulation value is 97
print(customer.amountSaved()) # prints 97
customer.makePurchase(20)
customer.makePurchase(10) # you earned discount      