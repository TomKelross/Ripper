from classes.Player import Player
from classes.Time import Time
from modules.parser import *
from adt.locations import *
from adt.items import *
from adt.characters import *

from story import nextEvent

# Creates a Player Object
player = Player("Decetive Joe Smith")

# Creates a Timer Object
time = Time()

def main(): #KYLE

    while True:
         
        ############################################
        # DEBUGGING REMOVE ON COMPLETION           #
        #############################################
        print(player.getName())
        print("Location" + player.getLocation())
        
        
        print(getLocation[player.getLocation()]["name"])
        print(getLocation[player.getLocation()]["description"])
        print(getLocation[player.getLocation()]["people"])
        print(getLocation[player.getLocation()]["inventory"])
        print(str(player.returnInventory()))
        #############################################

        # Print the map
        print_map()
        
        # Prints the time 
        print_time()

        # Prints the room information 
        print_room()

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

    if goto in getLocation:
        player.setLocation(goto)
    else:
        print("not found")

def execute_wait(wait): #KYLE
        
    wait = int(wait) + 1

    for i in range(0, wait):         
        
        time.incTime()

    print("You wait {} hours.".format(i))

def execute_talk(who): #KYLE

    flag = False

    room = getLocation[player.getLocation()]

    for i in room["people"]:
        if i["name"] == who:
            flag = True
            print(i["diaglogue"])
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
    print("=" * 100)
    print("Time: " + str(time.getTime()) + str(":00"))
    print("Day: " + time.getDay())

#
def print_room(): # Peter
    pass

#
def print_room_items(): # Peter
    pass


def print_locations(): # Kyle
    
    i = 1;
    
    print("You can go to...\n")
    
    for location in getLocation:
        
        print("{} : {}".format(i, location))
        
        i = i + 1

if __name__ == "__main__":
    main()
    

