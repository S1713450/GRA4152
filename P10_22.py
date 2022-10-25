# superclass
class Appointment:
    # every appointment has description
    def __init__(self, description):
        self._description = description

    # will be overridden in subclasses  
    def occursOn(self, year, month, day):
        return 

    # returns description 
    def getDescription(self):   
        return self._description

class OneTime(Appointment):
    # Need all information: year, month and day 
    def __init__(self, description, year, month, day):
        # call constructor from the superclass
        super().__init__(description)
        self._year = year
        self._month = month
        self._day = day

    #Checks if it is the correct date 
    def occursOn(self, year, month, day):
        if self._year == year and self._month == month and self._day == day:
            return True
        else:
            return False
        
class Monthly(Appointment):
    def __init__(self, description, day):
        super().__init__(description)
        self._day = day
    
    # same logic as before, but just compare days
    def occursOn(self, year, month, day):
        if self._day == day:
            return True
        else:
            return False

class Daily(Appointment):
    def __init__(self, description):
        super().__init__(description)

    # occurs everyday, so just returns True
    def occursOn(self, year, month, day):
        return True



a1 = OneTime("Job Interview", 2022, 2, 2)
a2 = Daily("Gym")
a3 = Monthly("lunch with Dad", 2)

appointment = [a1, a2, a3]

day = int(input("Enter a day: "))
month = int(input("Enter a month: "))
year = int(input("Enter a year: "))

for a in appointment:
    if a.occursOn(year, month, day):
        print(a.getDescription())

# for example for 2.2.2022. -> Job Interview, gym, lunch 
# for 8.8.2022. -> gym
# for 2.9.2019. -> gym, lunch