
from classes import Factory
from classes.Character import Character
from classes.Character import CharacterManager
from classes.Location import LocationManager
from classes.Container import ContainerManager
from classes.Item import ItemManager
from classes.Player import Player
from classes.Time import Time
from modules.parser import *
from modules.display import DisplayManager
from adt.locations import *
from adt.items import *
from adt.characters import *
from adt.ascimap import asciimap
from adt.containers import *

from story import nextEvent
from story import Narrative

from colorama import init, Fore, Back, Style
init()

# Creates a Player Object
disp = DisplayManager()
print = disp.print
input = disp.get_input


list_of_item_objects = Factory.item_factory()
items = ItemManager(list_of_item_objects)

list_of_container_objects = Factory.container_factory(items)
containers = ContainerManager(list_of_container_objects)

list_of_character_objects = Factory.character_factory()
characters = CharacterManager(list_of_character_objects)

list_of_location_objects = Factory.location_factory(characters,items,containers)
locations = LocationManager(list_of_location_objects)


time = Time()
narrative = Narrative(time,disp)
from events import add_events
add_events(narrative)
player = Player("Detective Joe Smith")


# Creates a Timer Object


def main(): #KYLE

    # get_location returns a location object from the name of a location
    # In this case, we are starting at scotland yard, so we get the scotland yard location
    starting_location = locations.get_location("Scotland Yard")
    # And set the player current location here
    player.setLocation(starting_location)

    while True:
         
        ############################################
        # DEBUGGING REMOVE ON COMPLETION           #
        #############################################
        # disp.reset_display()
        # location = player.getLocation()
        # print(location)
        # print("Location" + location.name)
        # print(location.people)
        # print(location.description)
        # print(location.inventory)
        # print(str(player.returnInventory()))
        #############################################

        # Updates the top of the screen with the current time information
        print_time()

        # Check and run and scheduled events that should have happened by now
        narrative.check()

        # Print the map
        print_map()

        current_location = player.getLocation()
        # Updates the room display at the top of the screen with information about the current room
        print_room(current_location)
        # Prints items in the room
        print_room_items(current_location)
        print_characters(locations)

        # Ask the user for their command
        command = input("> ")

        # Make sure the input is properly sanitised
        command = normalize_input(command)
        
        # Execute the command    
        commands(command)

        # Increments the Time
        # time.incTime()

        # Excute the next event
        nextEvent(time.getTime(), time.getDay())

def commands(command): #KYLE
   
    """
    Author: Kyle Davies
    """

    if command[0] == "go":
        if len(command) > 1:
            execute_go(command[1])
        else:
            print_locations()
    elif command[0] == "talk":
        if len(command) > 1:
            execute_talk(command[1])
        else:
            print("Talk to who?")
    elif command[0] == "take":
        if len(command) > 1:
            execute_take(command[1])
        else:
            print("Take what?")
    elif command[0] == "arrest":
        if len(command) > 1:
            pass
        else:
            print("Arrest who?")    
    elif command[0] == "wait":
        if len(command) > 1:
            execute_wait(command[1])
        else:
            print("Wait how long?")    
    else:
        print(Fore.RED + "✘ Your command made no sense" + Style.RESET_ALL)

def execute_go(goto): #KYLE
    print(goto)
    # Allows us to access player
    global player
    print(locations) 
    location = locations.get_location(goto)
    print(location)

    if location:
        player.setLocation(location)
        time.advance_time(30)  # Travelling anywhere takes half an hour
    else:
        time.advance_time(5)  # Loose five minutes for faffing around
        print("Couldn't find that location")

def execute_wait(hours): #KYLE

    minute_to_wait = int(hours) * 60
    time.advance_time(minute_to_wait)
    print("You wait {} hours.".format(hours))

def execute_talk(who): #KYLE

    flag = False

    location = player.getLocation()

    for i in room["people"]:
        if i["name"] == who:
            flag = True
            print(i["dialogue"])
            break

    if flag == False:
        print("That person doesn't seem to be here.")

def execute_take(item_to_take): #KYLE

    flag = False

    room = getLocation[player.getLocation()]

    for item in room["inventory"]:
        if item["name"] == item_to_take:
            flag = True
            
            player.addToInventory(item)
            
            room["inventory"].remove(item)

            print("You take {}.".format(item_to_take))

            break
    if flag == False:
        print("That item doesn't seem to be here.")

#
def execute_investigate(who): #Judith 
    pass

#
def execute_look(): # Nathan
    pass    

#
def execute_take_note(note): #Johnny
    pass

#
def execute_read_notes(): # Johhny
    pass

#
def print_map(): # Nathan
    if player.getLocation() == "Bank":
        asciimap.replace(218,"◈")
        print(asciimap)



#
def print_time(): # Peter
    disp.update_top_bar(Fore.GREEN + "Ripper v1.0 " + Style.RESET_ALL + "Week "
                        + str(time.get_week()) + " "
                        + time.get_day_name() + ", the time is "
                        + time.get_time_string()
                        )


#
def print_room(location): # Peter
    disp.update_room_display(location.name)
    print(location.description)
    if location.people == []:
        print("")



#
def print_room_items(location): # Peter
    pass
def print_characters(location):

    current_location = player.getLocation()
    people_in_room = current_location.get_people()
    print(people_in_room)
    # print(location.get_location(player.get_location()).get_people())

def print_locations(): # Kyle
     
    i = 1
    print("You can go to...\n")
    all_locations = locations.get_all_locations()
    
    for location in all_locations: 
        print("{} : {}".format(i, location.name))
        i += 1
    input("Press any key to continue")
       

if __name__ == "__main__":
    main()
    

