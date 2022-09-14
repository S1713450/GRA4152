# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 12:49:46 2022

@author: A2010377
"""

class Adress:
    
    # Can create instances where apt number is optional 
    def __init__(self,house, street, city, state, postal, apt = None):
        self._house = house 
        self._street = street 
        self._apt = apt 
        self._city = city 
        self._state = state 
        self._postal = postal 
    
    # prints adress street and an optional apt number if it exists on one line and
    # state, city and postal number on the next. 
    def print(self):
        if self._apt == None:
            print(self._street + " " + str(self._house))
            print(self._city + ", " + self._state + ", " + str(self._postal))
        
        else:
            print(self._street  + " " + str(self._house ) + 
                  ", Apt number " + str(self._apt) )
            print(self._city + ", " + self._state + ", " + str(self._postal))
            
    
    # Compares two postal numbers and returns True if the first one
    # comes before the other one 
    def comesBefore(self, compare):
        if self._postal <= compare._postal:
            return True 
        else:
            return False 
        
        

#%%

HouseAdress = Adress(5, "Object road", "Los Angeles","California", 1337)
ApartmentAdress = Adress(5, "Object road", "Los Angeles","California", 1338, 203)

HouseAdress.print()
ApartmentAdress.print()

print(HouseAdress.comesBefore(ApartmentAdress))

