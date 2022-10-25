# superclass
class Appointment:
    # every appointment has description
    def __init__(self, description):
        self._description = description

    # will be overridden in subclasses  
    def occursOn(self, day, month, year):
        return 

    # returns description 
    def getDescription(self):   
        return self._description

    # save description in the file 
    def save(self, outfile):
        # description will be inside the quotation marks
        outfile.write("'" + self._description + "'")        

class OneTime(Appointment):
    # Need all information: year, month and day 
    def __init__(self, description, day, month, year):
        # call constructor from the superclass
        super().__init__(description)
        self._year = year
        self._month = month
        self._day = day

    def occursOn(self, day, month, year):
        if self._year == year and self._month == month and self._day == day:
            return True
        else:
            return False

    def save(self, outfile):
        super().save(outfile)
        # for one time events add day, month and year in the file
        outfile.write(" " + str(self._day) + " " + str(self._month) + " " + str(self._year) + "\n")
        

class Daily(Appointment):
    def __init__(self, description):
        super().__init__(description)

    # occurs everyday, so just return True
    def occursOn(self, day, month, year):
        return True

    def save(self, outfile):
        super().save(outfile)
        # we don't need the data, since daily events occurs everyday 
        # just go to next line for following appointment 
        outfile.write("\n")

class Monthly(Appointment):
    def __init__(self, description, day):
        super().__init__(description)
        self._day = day
    # just compare days
    def occursOn(self, day, month, year):
        if self._day == day:
            return True
        else:
            return False

    def save(self, outfile):
        # save description 
        super().save(outfile)
        # and we need just day, month and year don't matter 
        outfile.write(" " + str(self._day) + "\n")

appointment = []

# appointment program 
done = False
while not done :
    # option menu for adding, printing, saving and loading
    action = input("A)dd appointment P)rint appointments S)ave appointments L)oad appointments Q)uit: ")
    action = action.upper()
    # Asks for date if its add or print
    if action == "A" or action == "P" :
        day = int(input("Enter a day: "))
        month = int(input("Enter a month: "))
        year = int(input("Enter a year: "))
        # asks for description of the appointment as well if its add, and which type of app it is
        if action == "A" :
            description = input("Enter a description: ")
            subclass = input("O)ne time M)onthly D)aily ? ")
            if subclass.upper() == "O":
                a = OneTime(description, day, month, year)
                appointment.append(a)   
            elif subclass.upper() == "M":
                a = Monthly(description, day)
                appointment.append(a)
            else:
                a = Daily(description)
                appointment.append(a)         
        else :
            for a in appointment:
                if a.occursOn(day, month, year):
                    print(a.getDescription())
    elif action == "Q" :
        done = True
    elif action == "L" or action == "S":
        # if user want to save the appointments 
        if action == "S":
            filename = input("Enter a filename: ")
            outfile = open(filename, "w")
            for a in appointment:
                # call function from correspond class
                a.save(outfile)
            outfile.close()
        # user want to load appointments from the file
        else:
            filename = input("Enter a filename: ")
            infile = open(filename, "r")
            
            line = infile.readline()
            while line != "":
                # find description (without quotation marks)
                endDes = line.find("'", 1, len(line))
                description = line[1:endDes]
                # characters after description
                line = line[endDes + 1:]
                # split it into a list
                line = line.split()
                num = len(line)
                # if length of the list is zero,
                # it must be daily appointment
                if num == 0:
                    a = Daily(description)
                    appointment.append(a)
                # if length of the list is 1, 
                # it must be monthly appointment
                # since for it we only need day 
                elif num == 1:
                    a = Monthly(description, int(line[0]))
                    appointment.append(a)
                # it's one time appointment
                # day = line[0], month = line[1], year = line[2]
                else: 
                    a = OneTime(description, int(line[0]), int(line[1]), int(line[2]))
                    appointment.append(a)
                # read the next line (appointment)
                line = infile.readline() 
            infile.close()
