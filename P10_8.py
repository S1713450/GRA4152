# -*- coding: utf-8 -*-
# superclass
class Person:
    # constructor
    # Testing that arguments are correct type
    def __init__(self, name, year):
        if type(name) == str and type(year) == int:
            self._name = name
            self._year = year
        else:
            print("Name must be a string, and year must be an integer")
    # returns persons name
    def getName(self):
        return self._name
     
    # returns persons year of birth 
    def getYear(self):
        return self._year

    # prints information of the class instance
    def __repr__(self):
        return "[Person: " + self._name + " " + self._year + "]"

# subclass of Person
class Student(Person):
    # constructor
    # tests that major argument is correct data type
    def __init__(self, name, year, major):
        # call constructor from class Person
        super().__init__(name, year)
        # student has a major
        if type(major) == str:
            self._major = major
        else:
            print("Major must be a string")
    # return students major 
    def getMajor(self):
        return self._major

    # return information about student instance
    def __repr__(self):
        return "[Student: " + self._name + " " + str(self._year) + " " + str(self._major) + "]"

# another subclass of Person
class Instructor(Person):
    # constructor
    def __init__(self, name, year, salary, currency = None):
        # call constructor from the Person class
        # Added option to specify currency of salary, because why not
        super().__init__(name, year)
        # instructor has a salary
        if type(salary) == int:
            self._salary = salary
            self._currency = currency
        else:
            print("Salary must be an integer")
    # return instructors salary
    def getSalary(self):
        if type(self._currency) == str:
            return str(self._salary) + self._currency
        else:
            return self._salary

    # returns information about instructor instance
    def __repr__(self):
        # Checks if currency is added and if it is correct data type
        if type(self._currency) == str:
            return "[Instructor: " + self._name + " " + str(self._year) + " " + str(self._salary) + str(self._currency) + "]"
        else:
            return "[Instructor: " + self._name + " " + str(self._year) + " " + str(self._salary) + "]"
# testing

s = Student("Ola Nordmann", 1996, "History")

print(s.getName()) # prints Name
print(s.getYear()) # prints 1996
print(s.getMajor()) # prints Major
print(s.__repr__()) # prints [Student: Name Year Major]

i = Instructor("Lorenzo", 1977, 68561)

print(i.getSalary()) # prints salary
print(i.__repr__()) # prints [Instructor: Print Name Year Salary]

i = Instructor("Lorenzo", 1977, 68561, "USD")
print(i.getSalary())
print(i.__repr__()) # prints [Instructor: Print Name Year Salary Currency]

WrongInputType = Student(123, 1997, "History") #Prints that inputs are wrong type
WrongInputType2 = Student("Ola Normann", 1996, 413) #prints that major must be string
