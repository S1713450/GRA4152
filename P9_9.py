# -*- coding: utf-8 -*-

class ComboLock:
    # constructor 
    def __init__(self, secret1, secret2, secret3):
        self._secret1 = secret1
        self._secret2 = secret2
        self._secret3 = secret3 
        # dial contains the number at which dial points to
        self._dial = 0
        # values and direction are list of previous pointed numbers/directions
        self._values = []
        self._direction = []

    def reset(self):
        self._dial = 0
        # emptying lists as well
        self._values = []
        self._direction = []

    def turnLeft(self, ticks):
        # the % operator returns the remaining number when something is divided
        # which is perfect for our lock with 40 different numbers
        self._dial = (self._dial - ticks) % 40
        self._values.append(self._dial)
        self._direction.append("L")

    def turnRight(self, ticks):
        self._dial = (self._dial + ticks) % 40
        self._values.append(self._dial)
        self._direction.append("R")

    # if last three numbers are equal to secret1, secret2, secret3
    # and if last three directions are R, L and R 
    # method open() returns True
    # otherwise, returns False
    def open(self):
        #First test if the lock has been turned at least 3 times, which is necessary to open it 
        if len(self._values) >= 3:
            if self._values[len(self._values) - 3 :] == [self._secret1, self._secret2, self._secret3] \
                and self._direction[len(self._direction) -3 :] == ["R", "L", "R"]:
                return True
            else:
                return False
        else:
            return False
        
# testing the lock

print( "Correct combination, true is expected")
lock = ComboLock(1, 2, 3)
lock.turnRight(1)
lock.turnLeft(39)
lock.turnRight(1)
print(lock.open()) # prints True


print("Turn right twice, False is expected")
lock.reset()
lock.turnRight(1)
lock.turnRight(1)
lock.turnLeft(39)
print(lock.open()) # prints False

print("Wrong number of ticks but right directions, false is expected ")
lock.reset()
lock.turnRight(1)
lock.turnLeft(39)
lock.turnRight(6)
print(lock.open()) # prints false

print("Only two turns, false is expected ")
lock.reset()
lock.turnRight(1)
lock.turnLeft(39)
print(lock.open()) # prints false

print("More than 3 turns, but last 3 are correct, true is expected ")
lock.reset()
lock.turnRight(40)
lock.turnRight(1)
lock.turnLeft(39)
lock.turnRight(1)
print(lock.open()) # prints True
