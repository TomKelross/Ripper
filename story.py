from adt.characters import *
from adt.items import *
from adt.locations import *

from classes.Player import *
from classes.Time import *

from modules.parser import *

# This module controls the story....

def nextEvent(time, day):
    print(time, day)

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