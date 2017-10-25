from adt.characters import *
from adt.items import *
from adt.locations import *

from classes.Player import *
from classes.Time import *

from modules.parser import *

# from .game import characters,locations,player
# This module controls the story....

def nextEvent(time, day):

    if time == 17 and day == "Wednesday":
        krills["people"].remove(krill)
        print("Krill has been killed by a higher power, maybe someone with a keyboard??")
        clark["dialogue"].pop()
        clark["dialogue"].append("I didn't see nuttin!!!!")

    if time == 17 and day == "Friday":
        krills["people"].append(krill)
        print("Krill has been brought back to life!")

    if time == 17 and day == "Saturday":
        krills["inventory"].append(beer)
        print("Krill the new lord and saviour has restocked his beer")

class Narrative(object):
    #This class makes sure events happen at the right time in the story

    def __init__(self,time,display_manager,locations):
        self.time_manager = time
        self.display_manager = display_manager
        self.events = []
        self.locations = locations

    def check(self):
        pass #Given an instance of the time_manager, check if there are any events due to run and run them
        current_week = self.time_manager.get_week()
        current_day = self.time_manager.get_day()
        current_time = self.time_manager.get_time()

        for event in self.events:
            if current_week > event["week"]: #If it is a week past when the event was due
                self.call_event(event) # It definetly needs to be called
            elif (current_week == event["week"]) and current_day > event["day"]: # If it is later in the week
                self.call_event(event) # The event is late and needs to be called
            # Else if it is the same week and day as the event, but the time for it has passed, call the event
            elif (current_week == event["week"] and current_day == event["day"] and current_time > event["time"]):
                self.call_event(event)
            else:
                pass

    def add_event(self,week,day,time,callback):
        event = {
            "week": week,
            "day": day,
            "time": time,
            "callback" : callback,
            "finished": False
        }
        self.events.append(event)

    def call_event(self,event):
        #remove the event from the list of events, as it has now been called
        self.events.remove(event)
        callback = event["callback"]
        context = {
            "display" : self.display_manager,
            "time" : self.time_manager,
            "locations" : self.locations
        }
        callback(context)

