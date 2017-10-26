# from .game import print
from colorama import init,Fore,Back,Style
from adt.locations import *
from adt.characters import *
from adt.Logo import logo
from time import sleep
# def scene_1_murder_one(context):
#     context['display'].print('Someone was murdered in the night')

def start_of_game_cinematic(context):
    display = context["display"]
    display.set_screen("story")
    screen = display.get_screen('story')
    print = screen.print
    type = screen.type
    for line in logo: 
        type(Style.BRIGHT+ Fore.RED + line + Style.RESET_ALL,0.005)
    print("")
    print("")
    
    type(Style.BRIGHT + Fore.MAGENTA + "London 2017",0.08)
    sleep(1)
    print(Style.RESET_ALL + Fore.WHITE + "You walk into Scotland Yard a fresh faced Police Detective with full training",True)
    sleep(0.7)
    print("but only a week's experience to your name. The voice coming from the phone ",True)
    sleep(0.7)
    print("in your hand is telling you about the homicide case - your first homicide case",True)
    sleep(0.7)
    print("that has just been discovered in the more squalid side of town",True)
    sleep(1.2)
    type(Fore.MAGENTA + "You should go to the" + Fore.YELLOW +  " Adult Gamestore " + Fore.MAGENTA + "now!" + Style.RESET_ALL)
    context["display"].print()
    type("Use" + Style.BRIGHT + Fore.YELLOW + " GO "
         + Style.NORMAL + Fore.WHITE + "to get around. You can"
         + Style.BRIGHT + Fore.YELLOW + " talk "
         + Style.NORMAL + Fore.WHITE + "to people,"
         + Style.BRIGHT + Fore.YELLOW + " investigate "
         + Style.NORMAL + Fore.WHITE + "them or other things in the room and"
          )
    sleep(0.1)
    type(Style.BRIGHT + Fore.YELLOW + "Look "
         + Style.NORMAL + Fore.WHITE + "in containers to find items which you can then"
         + Style.BRIGHT + Fore.YELLOW + " take"
         + Style.NORMAL + Fore.WHITE + "."
         + Style.RESET_ALL
          )
    sleep(0.1)
    # print("Use" + Fore.YELLOW + " HELP "
    #      + Fore.WHITE + "to display useful commands if you get confused")
    print("",True)
    display.wait_for_input(False)
    display.set_screen("default")
    display.set_cinematic_mode(False)

    #todo - swap out exit for game stor for game store (murder scene)

def scene_1_murder_one(context):
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

    screen = display.get_screen('story')
    display.delay_print("You found the murder weapon, now take it back to the police station for DNA analysis")
    scotland_yard = locations.get_location(scotland["name"])
    lab_technician = charachters.get_character(scene_2_police_officer["name"])
    scotland_yard.add_person(lab_technician)

def scene_2_analyse_knife(context):
    locations = context["locations"]
    charachters = context["characters"]
    display = context["display"]
    type = display.type

    screen = display.get_screen('story')

    screen.print("The dead man was identified as Mr Clark Davidson")
    screen.print("33-year-old with no criminal background or conviction.")
    screen.print("However, he is on the Police database as having being a witness to a murder that happened six years ago")
    screen.print("There are three suspects, who have motives to want him dead")
    screen.print("Mrs Clark - Recently Filed For Divorce - Blood Type O")
    screen.print("Mr James Robin - His buisness partner - Blood Type AB")
    screen.print("Miss Diane B - His Mistress - Blood Type AB")
    screen.print('')
    screen.print("The lab results on the knife show the killers blood print is AB")
    screen.print('')
    screen.print(Fore.MAGENTA + "You should look around the city for more " + Fore.YELLOW + " clues " + Fore.MAGENTA + "now" + Style.RESET_ALL)
    screen.print('')

    screen.update_display()
    display.wait_for_input(update=False)
    display.set_screen('default')
    display.update_display()

def drop_beer(context):
    chars = context['characters']
    kirill_obj = chars.get_character(kirill["name"])
    kirill_obj.dialogue.append('Why would you waste good beer like that, get out of my sight!')

def scene_3_murder_two(context):
    locations = context["locations"]
    display = context["display"]

    tavern_object = locations.get_location(kirills["name"])
    docks_murder_location = locations.get_location(docks_murder["name"])
    tavern_object.exits["east"] = docks_murder_location.get_name()

    screen = display.get_screen('story')
    screen.print("It's been less than a day since the first murder, the blood has barely dried at the scene,")
    screen.print("and yet another body has been found at the Docks. ")
    screen.print("Could they be linked? You must get there right away!")
    screen.print( Fore.MAGENTA + "Go to the" + Fore.YELLOW + " docks " + Fore.MAGENTA + "now!" + Style.RESET_ALL)
    screen.update_display()
    display.wait_for_input(update=False)
    display.set_screen('default')
    display.update_display()


def add_events(narrative):
    narrative.add_time_event(1, 1, 0, start_of_game_cinematic)
    narrative.add_time_event(1, 1, 1, scene_1_murder_one)

    narrative.add_location_event(kirills,tavern_first_time,sticky=True)

    #Scene 1 events
    narrative.add_location_event(gamestore_murder,scene_1_first_arrival)
    narrative.add_item_take_event(police_badge, badge_pickup)
    # narrative.add_item_drop_event(police_badge, badge_drop)
    narrative.add_item_take_event(knife,scene_1_found_murder_weapon)
    
    narrative.add_item_drop_event(police_badge,scene_2_analyse_knife)
    narrative.add_item_drop_event(knife,scene_2_analyse_knife)

    narrative.add_time_event(1,1,1380,scene_3_murder_two)

    narrative.add_item_drop_event(beer,drop_beer)

    # narrative.add_event(1,1,1260,murder_two)

