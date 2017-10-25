import  math

def periods_passed(number,period):
    return math.floor(number / period)

class Time:

    __time = 0
    
    __day = "Monday"
    __day_names = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

    __month = "January"
    __month_names = ["January","February","March","April","May","June","July","August","September"]

    def __init__(self):
        self.day = 1  # It is the first day
        self.week = 1  # Of the first week
        self.time = 420 # The day starts at 7am, so 420 minutes into the day
        pass

    def set_date(self,time,day,week):
        # A date consists of a week number, the day of the week in that week, and the number of minutes into that day.
        # It is a particular moment in history
        self.time = time
        self.day = day
        self.week = day

    def set_time(self,time):
        self.time = time

    def set_day(self,day):
        self.day = day

    def set_week(self,week):
        self.week = week

    def get_week(self):
        return self.week

    def get_day(self):
        return self.day

    def get_time(self):
        return self.time

    def advance_time(self, time_to_add):
        current_time = self.time
        minutes_in_day = 24 * 60
        advanced_time = current_time + time_to_add

        if (advanced_time) > minutes_in_day: # If we go into a new day
            days_to_advance = periods_passed(advanced_time,minutes_in_day) # How many multiples of 1440 are there
            self.advance_day(days_to_advance) # Increment the day that many times
            # Then set the current time to the new time into the new day
            self.time = advanced_time - (minutes_in_day * days_to_advance)
        else:  # Otherwise lets just advance the time of the current day
            self.time = advanced_time

    def advance_day(self,days_to_add):
        current_day = self.day
        days_in_week = 7
        advanced_day = current_day + days_to_add

        if advanced_day > days_in_week:
            weeks_to_advance = periods_passed(advanced_day,days_in_week)
            self.advance_week(weeks_to_advance)
            self.day = advanced_day - (days_in_week * weeks_to_advance)
        else:
            self.day = advanced_day

    def advance_week(self,weeks_to_add):
        current_week = self.week
        advanced_week = current_week + weeks_to_add
        self.week = advanced_week

    def get_time_string(self):
        time = self.time
        hours = str(math.floor(time / 60)).zfill(2)
        minutes = str(time % 60).zfill(2)
        return "{}:{}".format(hours,minutes)

    def get_day_name(self):
        return self.__day_names[self.day - 1]



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

