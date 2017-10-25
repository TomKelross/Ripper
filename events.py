# from .game import print
from colorama import init,Fore,Back,Style
from adt.locations import *
from adt.characters import *

# def murder_one(context):
#     context['display'].print('Someone was murdered in the night')

def start_of_game_cinematic(context):
    display = context["display"]
    display.set_screen("story")
    type = display.type
    type(Style.BRIGHT + Fore.MAGENTA + "London 2017",0.08)
    type(Style.RESET_ALL + Fore.WHITE + "You walk into Scotland Yard a fresh faced Police Detective with full training",0.01)
    type("but only a week's experience to your name. The voice coming from the phone in your hand",0.009)
    type("is telling you about the homicide case - your first homicide case - that has just been discovered in",0.007)
    type("the more squalid side of town",0.005)
    type(Fore.MAGENTA + "You should go there now" + Style.RESET_ALL,0.005)
    context["display"].print()
    type("Use" + Fore.YELLOW + " GO "
         + Fore.WHITE + "to get around. You can "
         + Style.BRIGHT + Fore.YELLOW + " talk "
         + Style.NORMAL + Fore.WHITE + " to people,"
         + Fore.YELLOW + " investigate "
         + Fore.WHITE + "them or other things in the room and"
         + Fore.YELLOW + " open "
         + Fore.WHITE + "containers for items which you can then"
         + Fore.YELLOW + " take "
         + Style.RESET_ALL, 0.005)
    type("Use " + Fore.YELLOW + "HELP"
         + Fore.WHITE + "to display useful commands if you get confused")
    context["display"].print()
    display.wait_for_input(False)
    display.set_screen("default")
    display.set_cinematic_mode(False)

    #todo - swap out exit for game stor for game store (murder scene)

def murder_one(context):
    locations = context["locations"]
    marketplace_object = locations.get_location(marketplace["name"])
    gamestore_murder_location = locations.get_location(gamestore_murder["name"])
    marketplace_object.exits["south"] = gamestore_murder_location.get_name()

def tavern_first_time(context):
    context['display'].delay_print('Kirill Eyes You With Suspicion')

def badge_pickup(context):
    context['display'].delay_print("You hope that wearing this badge won't have conseqeunces")

def badge_drop(context):
    context['display'].delay_print("You may be able to get into places more easily now")

def murder_two(context):
    #murder at the docks in the evening of the first day
    #todo: turn into a murder scene
    type = context["display"].type


def scene_1_first_arrival(context):
    display = context["display"]
    display.delay_print("You arrive at the scene and your first responders are giving you details of the murder")
    display.delay_print("A young man was found dead in an XXX video store, he is suspected to have been murdered")



def scene_1_found_murder_weapon(context):
    locations = context["locations"]
    charachters = context["characters"]
    display = context["display"]

    display.delay_print("You found the murder weapon, now take it back to the police station for DNA analysis")
    scotland_yard = locations.get_location(scotland["name"])
    lab_technician = charachters.get_character(scene_2_police_officer["name"])
    scotland_yard.add_person(lab_technician)

def scene_2_analyse_knife(context):
    locations = context["locations"]
    charachters = context["characters"]
    display = context["display"]
    type = display.type

    display.set_screen("story")

    display.type("The dead man was identified as Mr Clark Davidson",0.01)
    display.type("33-year-old with no criminal background or conviction.")
    display.type("However, he is on the Police database as having being a witness to a murder that happened six years ago")
    display.type("There are three suspects, who have motives to want him dead")
    display.type("Mrs Clark - Recently Filed For Divorce - Blood Type O")
    display.type("Mr James Robin - His buisness partner - Blood Type AB")
    display.type("Miss Diane B - His Mistress - Blood Type AB")
    display.print()
    display.type("The lab results on the knife show the killers blood type is AB")
    display.wait_for_input(False)
    display.set_screen("default")




def add_events(narrative):
    # narrative.add_time_event(1, 1, 0, start_of_game_cinematic)
    # narrative.add_time_event(1, 1, 1, murder_one)
    # narrative.add_location_event(kirills,tavern_first_time,sticky=True)

    #Scene 1 events
    narrative.add_location_event(gamestore_murder,scene_1_first_arrival)
    narrative.add_item_take_event(police_badge, badge_pickup)
    narrative.add_item_drop_event(police_badge, badge_drop)

    narrative.add_item_take_event(knife,scene_1_found_murder_weapon)


    # narrative.add_event(1,1,1260,murder_two)

