from classes import Factory
from classes.Character import Character
from classes.Character import CharacterManager
from classes.Location import LocationManager
from classes.Player import Player
from classes.Time import Time
from modules.parser import *
from modules.display import DisplayManager
from adt.locations import *
from adt.items import *
from adt.characters import *

from story import nextEvent

# Creates a Player Object

list_of_character_objects = Factory.character_factory()
list_of_location_objects = Factory.location_factory()

characters = CharacterManager(list_of_character_objects)
locations = LocationManager(list_of_location_objects)
player = Player("Decetive Joe Smith")

disp = DisplayManager()
print = disp.print
input = disp.get_input

# Creates a Timer Object
time = Time()

def main(): #KYLE

    #Put the player in scotland yard
    starting_location = locations.get_location("Scotland Yard")
    print(starting_location)
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

        # Print the map
        print_map()
        
        # Prints the time 
        print_time()

        # Prints the room information
        current_location = player.getLocation() 
        print_room(current_location)

        # Prints items in the room
        print_room_items() 

        # Ask the user for their command
        command = input("Please enter your command: ")

        #command = normialze_input(command) Kawthar
        
        # Converts the command to a list
        command = string_to_list(command)
        
        commands(command)

        # Increments the Time
        time.incTime()

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
            print("takinggggggg")
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
        print("Your command made no sense")

def execute_go(goto): #KYLE

    # Allows us to access player
    global player

    location = locations.get_location(goto)

    time.advance_time(30) #Travelling anywhere takes half an hour

    if location:
        player.setLocation(location)
    else:
        print("not found")

def execute_wait(hours): #KYLE

    minute_to_wait = int(hours) * 60
    time.advance_time(minute_to_wait)
    print("You wait {} hours.".format(hours))

def execute_talk(who): #KYLE

    flag = False

    room = getLocation[player.getLocation()]

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
    pass

#
def print_time(): # Peter
    disp.update_top_bar("Ripper v1.0 / Week "
                        + str(time.get_week()) + " "
                        + time.get_day_name() + ", the time is "
                        + time.get_time_string()
                        )


#
def print_room(location): # Peter
    disp.update_room_display(location.name)
    return True
    print(" "*40 + "╔" + "═"* len(location.name) + "╗") 
    print("═"*40 + "╣" + (location.name).upper() + "╠" + "═"*30)
    print(" "*40 + "╚" + "═"* len(location.name) + "╝")
    print(location.description)
    print(location.people)
    print(location.inventory)

#
def print_room_items(): # Peter
    pass


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
    

