
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
from adt.Logo import logo
from adt.containers import *

from story import nextEvent
from story import Narrative

from fuzzywuzzy import process

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

    # for line in logo:
    #     disp.type(line,0.000001)

    # get_location returns a location object from the name of a location
    # In this case, we are starting at scotland yard, so we get the scotland yard location
    starting_location = locations.get_location("Scotland Yard")
    # And set the player current location here
    narrative.check()
    change_location(starting_location,False)
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
        # print_map()

        current_location = player.getLocation()
        # Updates the room display at the top of the screen with information about the current room
        update_room_display(current_location)

        # Ask the user for their command
        command_given = False
        command = ""
        while not command_given:
            command = input("> ")
            if not command == "":
                command_given = True

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
    elif command[0] == "make":
            execute_take_note()
    elif command[0] == "read":
            execute_read_notes()
    elif command[0] == "look":
        if len(command) > 1:
            execute_look(command[1])
        else:
            execute_look()
    else:
        print(Fore.RED + " Your command made no sense" + Style.RESET_ALL)

def execute_go(direction): #KYLE
    current_location = player.getLocation()
    possible_exits = current_location.exits

    best_guess = process.extract(direction, possible_exits.keys(), limit=1)
    certainty = best_guess[0][1]
    direction = ""
    if certainty > 80:
        direction = best_guess[0][0]
    else:
        print("What direction did you mean")


    if direction in possible_exits:
        location_name = possible_exits.get(direction)
        location = locations.get_location_fuzzy(location_name)
        change_location(location)
        time.advance_time(30)
    else:
        print("You can't travel in that direction")
        time.advance_time(5)

def execute_wait(hours): #KYLE

    minute_to_wait = int(hours) * 60
    time.advance_time(minute_to_wait)
    print("You wait {} hours.".format(hours))

def execute_talk(who): #KYLE

    location = player.getLocation()
    people_in_room = location.get_people()

    if people_in_room:
        person_to_talk_to = characters.get_character_fuzzy(who,people_in_room)
        if person_to_talk_to:
            dialogue = person_to_talk_to.next_dialogue()
            dialogue_count = person_to_talk_to.get_dialogue_count()
            total_dialogues = person_to_talk_to.get_dialogue_length()
            dialogue_counter = ( Fore.GREEN + " ("
                                + Fore.LIGHTGREEN_EX + str(dialogue_count)
                                + Fore.GREEN + "/"
                                + Fore.LIGHTGREEN_EX + str(total_dialogues)
                                + Fore.GREEN + ")" + Style.RESET_ALL
                                )
            print(Fore.GREEN + "[" + Fore.LIGHTGREEN_EX + person_to_talk_to.name + Fore.GREEN + "] "
                  + Fore.WHITE + dialogue
                  + dialogue_counter
                  + Style.RESET_ALL)
        else:
            print("Couldn't find who you meant to talk to")
    else:
        print("There is no one here to talk to")

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
def execute_look(target=False): # Nathan
    # Prints items in the room
    current_location = player.getLocation()
    print_description(current_location)
    print_exits(current_location)
    print_room_items(current_location)
    print_characters(current_location)
    pass

#
def execute_take_note(): #Jonny
    note = input("Write a Note for yourself:")
    player.setNotes(note)

#
def execute_read_notes(): #Jonny
    i = 1
    note = player.getNotes()
    for word in note:
        print("{}:{}".format(i,word))
        i = i + 1
#
def print_map(): # Nathan
    if player.getLocation() == "Bank":
        asciimap = asciimap.replace(218,"◈")
    if player.getLocation() == "Church":
        asciimap.replace(472,"◈")
    if player.getLocation() == "Hospital":
        asciimap.replace(218,"◈")
    if player.getLocation() == "Scotland":
        asciimap.replace(218,"◈")
    if player.getLocation() == "Thames":
        asciimap.replace(218,"◈")
    if player.getLocation() == "Factory":
        asciimap.replace(218,"◈")
    if player.getLocation() == "Kirills":
        asciimap.replace(218,"◈")
    if player.getLocation() == "Docks":
        asciimap.replace(218,"◈")
    if player.getLocation() == "Marketplace":
        asciimap.replace(218,"◈")
    if player.getLocation() == "Gamestore":
        asciimap.replace(218,"◈")
#
def print_time(): # Peter
    disp.update_top_bar(Fore.GREEN + "Ripper v1.0 " + Style.RESET_ALL + "Week "
                        + str(time.get_week()) + " "
                        + time.get_day_name() + ", the time is "
                        + time.get_time_string()
                        )



def print_exits(location):
    print(Fore.GREEN + "From here you can travel:" + Style.RESET_ALL)
    for exit in location.exits:
        print(Fore.LIGHTYELLOW_EX + exit.upper() + Fore.WHITE +
              " for " + Fore.LIGHTYELLOW_EX + location.exits[exit]
              + Style.RESET_ALL)

def print_description(location):
    print(Fore.GREEN + "[Description] " + Style.RESET_ALL + location.description)
    print()

def update_room_display(location): # Peter
    disp.update_room_display(location.name)

#
def print_room_items(location): # Peter
    item_list_string = ""
    if location.inventory:
        print(Fore.GREEN + "Items in room:" + Style.RESET_ALL)
        for item in location.inventory:
            item_list_string += (Fore.LIGHTYELLOW_EX + item.name)
        print(item_list_string)
    else:
        print(Fore.LIGHTBLACK_EX + "There are no items here" + Style.RESET_ALL)

def print_room_containers(location):
    print(Fore.GREEN + "Containers:" + Style.RESET_ALL)
    for container in location.containers:
        print(container.name)


def print_characters(location):
    current_location = location
    people_in_room = current_location.get_people()
    people_string = ""
    if people_in_room:
        print(Fore.GREEN + "People that were found here:" + Style.RESET_ALL)
        for people in people_in_room:
            if not people.alive:
                people_string += " " + (Fore.BLACK + people.name + Style.RESET_ALL + " ")
            elif people.gender == "male":
                people_string += " " + (Fore.BLUE + people.name + Style.RESET_ALL + " ")
            elif people.gender == "female":
                people_string += " " + (Fore.MAGENTA + people.name + Style.RESET_ALL + " ")
        print(people_string.center(20))
    else:
        print(Fore.LIGHTBLACK_EX + "There are no people here" + Style.RESET_ALL)

    

    

    



    # print(location.get_location(player.get_location()).get_people())

def print_locations(): # Kyle
     
    i = 1
    print("You can go to...\n")
    all_locations = locations.get_all_locations()
    
    for location in all_locations: 
        print("{} : {}".format(i, location.name))
        i += 1
    input("Press any key to continue")

def change_location(location,reset_display=True):
    player.setLocation(location)
    if reset_display:
        disp.reset_display()
    execute_look()


if __name__ == "__main__":
    main()
    

