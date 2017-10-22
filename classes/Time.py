class Time:

    __time = 0
    
    __day = "Monday"

    __month = "January"

    def __init__(self):
        pass
    
    # Sets Time
    def setTime(self, time):
        self.__time == time
    
    # Gets Time
    def getTime(self):
        return self.__time

    # Gets Day
    def getDay(self):
        return self.__day
    
    # Increments Time
    def incTime(self):
        
        time = self.__time

        if time == 23:
            self.nextDay()
            time = 0
        else:
            time = time + 1
        
        self.__time = time
    
    # Decrements Time
    def decTime(self):
        
        time = self.__time

        if time == 23:
            time = 0
        else:
            time = time - 1

        self.__time = time

    def nextDay(self):
        
        day = self.__day

        if day == "Monday":
            day = "Tuesday"
        
        elif day == "Tuesday":
            day = "Wednesday"
        
        elif day == "Wednesday":
            day = "Thursday"
        
        elif day == "Thursday":
            day = "Friday"
        
        elif day == "Friday":
            day = "Saturday"
        
        elif day == "Saturday":
            day = "Sunday"

        elif day == "Sunday":
            day = "Monday"

        self.__day = day

