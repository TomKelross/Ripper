
from classes import Factory
from classes.Character import Character
from classes.Character import CharacterManager
from classes.Location import LocationManager
from classes.Container import ContainerManager
from classes.Item import ItemManager
from classes.Investigatable import InvestigatableManager
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

import itertools

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

list_of_investigatable_objects = Factory.investigatable_factory()
investigatables = InvestigatableManager(list_of_investigatable_objects)

list_of_character_objects = Factory.character_factory()
characters = CharacterManager(list_of_character_objects)

list_of_location_objects = Factory.location_factory(characters,items,containers,investigatables)
locations = LocationManager(list_of_location_objects)

player = Player("Detective Joe Smith")

time = Time()
narrative = Narrative(time,disp,locations,player,items,characters)
from events import add_events
add_events(narrative)

def main(): #KYLE

    # for line in logo:
    #     disp.type(line,0.000001)

    # get_location returns a location object from the name of a location
    # In this case, we are starting at scotland yard, so we get the scotland yard location
    starting_location = locations.get_location("Scotland Yard")
    # And set the player current location here
    narrative.check_time_event()
    change_location(starting_location,False)
    while True:
         
        ############################################
        # DEBUGGING REMOVE ON COMPLETION           #
        #############################################
        # disp.reset_screen()
        # location = player.get_location()
        # print(location)
        # print("Location" + location.name)
        # print(location.people)
        # print(location.description)
        # print(location.inventory)
        # print(str(player.get_inventory()))
        #############################################

        # Updates the top of the screen with the current time information
        print_time()

        # Check and run and scheduled time_events that should have happened by now
        narrative.check_time_event()

        # Print the map
        # print_map()

        current_location = player.get_location()
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
        # nextEvent(time.getTime(), time.getDay())

def commands(command): #KYLE
   
    """
    Author: Kyle Davies
    """

    if command[0] == "go":
        if len(command) > 1:
            execute_go(command[1])
        else:
             print(Style.BRIGHT + Fore.RED + "Please specify where?" + Style.RESET_ALL)
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
    elif command[0] == "drop":
        if len(command) > 1:
            execute_drop(command[1])
        else:
            print("Drop what?")
    elif command[0] == "examine":
        if len(command) > 1:
            execute_examine(command[1])
        else:
            print("Examine what?")
    elif command[0] == "investigate":
        if len(command) > 1:
            execute_investigate(command[1])
        else:
            print("Investigate who or what?")
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
    elif command[0] == "story":
            execute_story()
    elif command[0] == "look":
        if len(command) > 1:
            execute_look(command[1])
        else:
            display_information()
    else:
        print(Style.BRIGHT + Fore.RED + " Your command made no sense" + Style.RESET_ALL)

def execute_go(direction): #KYLE
    current_location = player.get_location()

    exits_dict = current_location.exits
    cardinal_directions = exits_dict.keys()
    place_names = exits_dict.values()
    all_possible_correct_choices = list(cardinal_directions) + list(place_names)
    best_guess = process.extract(direction, all_possible_correct_choices, limit=1)
    certainty = best_guess[0][1]
    direction = ""
    location = False
    if certainty > 80:
        direction = best_guess[0][0]
        if direction in cardinal_directions:
            location_name = exits_dict.get(direction)
            location = locations.get_location_fuzzy(location_name)
        elif direction in place_names:
            location = locations.get_location_fuzzy(direction)
        else:
            print("Couldn't tell where you wan't to go")
            time.advance_time(5)
    else:
        print("Couldn't work out where you want to go")
    if location:
        change_location(location)
        time.advance_time(30)

def execute_wait(hours): #KYLE

    minute_to_wait = int(hours) * 60
    time.advance_time(minute_to_wait)
    print("You wait {} hours.".format(hours))

def execute_talk(who): #KYLE

    location = player.get_location()
    people_in_room = location.get_people()

    if people_in_room:
        person_to_talk_to = characters.get_character_fuzzy(who,people_in_room)
        if person_to_talk_to:
            if person_to_talk_to.get_dialogue_length():
                print(person_to_talk_to.next_dialogue())
            else:
                print("They don't look like they have very much to say")
        else:
            print("Couldn't find who you meant to talk to")
    else:
        print("There is no one here to talk to")

def execute_take(name_to_take): #KYLE

    current_location = player.get_location()
    items_in_room = current_location.get_items()
    item_names_in_room = [item.get_name() for item in items_in_room]
    containers_in_room = current_location.get_containers()

    # https: // stackoverflow.com / questions / 14807689 / python - list - comprehension - to - join - list - of - lists
    items_in_containers = list(itertools.chain.from_iterable([cont.get_items() for cont in containers_in_room]))

    container_item_names = [item.get_name() for item in items_in_containers]

    all_possible_item_names = item_names_in_room + container_item_names

    if all_possible_item_names:
        best_guess = process.extract(name_to_take, all_possible_item_names, limit=1)
        certainty = best_guess[0][1]
        guess_name = best_guess[0][0]
        if certainty > 80:
            item = items.get_item(guess_name)
            player.add_to_inventory(item)

            if item in items_in_containers:
                for container in containers_in_room:
                    if container.remove_item(item):
                        break
            if item in items_in_room:
                current_location.remove_item(item)
            narrative.check_item_take_event(item)
            display_information()
        else:
            print("Not sure what you were trying to take")

def execute_drop(name_to_drop,container=False):
    current_location = player.get_location()
    player_items = player.get_inventory()
    if player_items:
        player_item_names = [item.get_name() for item in player_items]
        best_guess = process.extract(name_to_drop,player_item_names,limit=1)
        certainty = best_guess[0][1]
        guess_name = best_guess[0][0]
        if certainty > 80:
            item = items.get_item(guess_name)
            player.remove_from_inventory(item)
            current_location.add_item(item)
            narrative.check_item_drop_event(item)
            display_information()
        else:
            print('Not sure what you were trying to drop')
    else:
        print("You have nothing to drop")


def execute_examine(item_to_examine):
    current_location = player.get_location()
    player_items = player.get_inventory()
    if player_items:
        player_item_names = [item.get_name() for item in player_items]
        best_guess = process.extract(item_to_examine, player_item_names, limit=1)
        certainty = best_guess[0][1]
        guess_name = best_guess[0][0]
        if certainty > 80:
            item = items.get_item(guess_name)
            name = item.get_name()
            description = item.get_description()
            print(Fore.GREEN + "[" + Fore.LIGHTYELLOW_EX + name + Fore.GREEN + "] ")
            print(Fore.WHITE + description + Style.RESET_ALL)
        else:
            print('Not sure what you were trying to examine')
    else:
        print("You have nothing to drop")


def execute_investigate(target): #Judith
    current_location = player.get_location()

    investigatables_in_room = current_location.get_investigatables()
    investigatables_names_in_room = [investigatable.get_name() for investigatable in investigatables_in_room]
    players_in_room = current_location.get_people()

    people_in_room = current_location.get_people()
    people_names_in_room = [person.get_name() for person in people_in_room]

    # https: // stackoverflow.com / questions / 14807689 / python - list - comprehension - to - join - list - of - lists


    all_possible_investigation_names = investigatables_names_in_room + people_names_in_room

    if all_possible_investigation_names:
        best_guess = process.extract(target, all_possible_investigation_names, limit=1)
        certainty = best_guess[0][1]
        guess_name = best_guess[0][0]
        if certainty > 80:
            if guess_name in investigatables_names_in_room:
                thing_to_investigate = investigatables.get_investigatable_fuzzy(target, investigatables_in_room)
                if thing_to_investigate:
                    print(thing_to_investigate.investigate())
            elif guess_name in people_names_in_room:
                person_to_investigate = characters.get_character_fuzzy(target, people_in_room)
                if person_to_investigate:
                   investigation = person_to_investigate.investigate()
                   for line in investigation:
                       print(line)
        else:
            print("Not sure what you were trying to investigate")
    pass

#
def execute_look(target): # Nathan
    if target == 'around':
        display_information()
    else:
        current_location = player.get_location()
        location_containers = current_location.get_containers()
        if location_containers:
            container_names = [container.get_name() for container in location_containers]
            best_guess = process.extract(target, container_names, limit=1)
            certainty = best_guess[0][1]
            guess_name = best_guess[0][0]
            if certainty > 80:
                container = containers.get_container(guess_name)
                name = container.get_name()
                description = container.get_description()
                print(Fore.GREEN + "[" + Fore.YELLOW + name + Fore.GREEN + "] ")
                print("    " + Fore.WHITE + description + Style.RESET_ALL)
                items = container.get_items()
                if items:
                    print(Fore.GREEN + "  Contains: " + Style.RESET_ALL)
                    for item in items:
                        print("    " + Fore.LIGHTYELLOW_EX + item.name)
                        print("       " + Fore.WHITE + item.description)

            else:
                print('Not sure what you were trying to examine')
        else:
            print("There are no containers to look in here")


def display_information():
    disp.reset_screen()
    current_location = player.get_location()
    print_exits(current_location)
    print()
    print_inventory()
    print_room_items(current_location)
    print_room_containers(current_location)
    print_room_investigatables(current_location)
    print()
    print_characters(current_location)
    print()
    print_description(current_location)
    disp.print_delayed()


#
def execute_take_note(): #Jonny
    note = input("Write a Note for yourself:")
    player.set_notes(note)

#
def execute_read_notes(): #Jonny
    i = 1
    note = player.get_notes()
    for word in note:
        print("{}:{}".format(i,word))
        i = i + 1


def execute_story(): #Jonny
    screen = disp.get_screen('story')
    screen.update_display()
    disp.wait_for_input(update=False)
    disp.set_screen('default')
    disp.update_display()


def print_map(): # Nathan
    if player.get_location() == "Bank":
        asciimap = asciimap.replace(218,"◈")
    if player.get_location() == "Church":
        asciimap.replace(472,"◈")
    if player.get_location() == "Hospital":
        asciimap.replace(218,"◈")
    if player.get_location() == "Scotland":
        asciimap.replace(218,"◈")
    if player.get_location() == "Thames":
        asciimap.replace(218,"◈")
    if player.get_location() == "Factory":
        asciimap.replace(218,"◈")
    if player.get_location() == "Kirills":
        asciimap.replace(218,"◈")
    if player.get_location() == "Docks":
        asciimap.replace(218,"◈")
    if player.get_location() == "Marketplace":
        asciimap.replace(218,"◈")
    if player.get_location() == "Gamestore":
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

def print_inventory():
    if player.get_inventory():
        item_list_string = Fore.GREEN + "Items in inventory: " + Style.RESET_ALL
        for item in player.get_inventory():
            item_list_string += (Fore.LIGHTYELLOW_EX + item.name + " ")
        print(item_list_string)
    else:
        print(Fore.LIGHTBLACK_EX + "You hold no items" + Style.RESET_ALL)

def print_room_items(location): # Peter

    if location.inventory:
        item_list_string = Fore.GREEN + "Items in room: " + Style.RESET_ALL
        for item in location.inventory:
            item_list_string += (Fore.LIGHTYELLOW_EX + item.name)
        print(item_list_string)
    else:
        print(Fore.LIGHTBLACK_EX + "There are no items here" + Style.RESET_ALL)


def print_room_containers(location):
    if location.containers:
        container_string = ""
        for container in location.containers:
            if container.locked:
                container_string += container.name + "(Locked)"
            else:
                container_string += container.name
        print(Fore.GREEN + "Containers: " + Fore.LIGHTYELLOW_EX + container_string)
    else:
        print(Fore.LIGHTBLACK_EX + "There are no containers here" + Style.RESET_ALL)

def print_room_investigatables(location):
    if location.investigatables:
        print(Fore.GREEN + "Investigatables:" + Style.RESET_ALL)
        for investigatable in location.investigatables:
            print(investigatable.name)
    else:
        print(Fore.LIGHTBLACK_EX + "There is nothing to investigate here" + Style.RESET_ALL)


def print_characters(location):
    current_location = location
    people_in_room = current_location.get_people()
    if people_in_room:
        if len(people_in_room) == 1:
            person = people_in_room[0]
            if not person.alive:
                print(Fore.GREEN + "Person in this room: " + Fore.BLACK + person.name +" (DEAD)" + Style.RESET_ALL)
            elif person.gender == "male":
                print(Fore.GREEN + "Person in this room: " + (Fore.CYAN + person.name + Style.RESET_ALL))
            elif person.gender == "female":
                print(Fore.GREEN + "Person in this room: " + " " + (Fore.MAGENTA + person.name + Style.RESET_ALL + " "))
        else:
            print(Fore.GREEN + "People in this room: ")
            for people in people_in_room:
                if not people.alive:
                    print("    " + Fore.BLACK + people.name + " (DEAD)"  + Style.RESET_ALL)
                elif people.gender == "male":
                    print("    " + Fore.CYAN + people.name + Style.RESET_ALL + " ")
                elif people.gender == "female":
                    print("    " + Fore.MAGENTA + people.name + Style.RESET_ALL + " ")
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
    player.set_location(location)
    if reset_display:
        disp.reset_screen()
    narrative.check_location_event()
    display_information()


if __name__ == "__main__":
    main()
    

