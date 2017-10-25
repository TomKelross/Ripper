# from .game import print
from colorama import init,Fore,Back,Style
def murder_one(context):
    context['display'].print('Someone was murdered in the night')

def start_of_game(context):
    type = context["display"].type
    type(Style.BRIGHT + Fore.MAGENTA + "London 2017",0.08)
    type(Style.RESET_ALL + Fore.WHITE + "You walk into Scotland Yard a fresh faced Police Detective with full training",0.01)
    type("but only a week's experience to your name. The voice coming from the phone in your hand",0.009)
    type("is telling you about the homicide case - your first homicide case - that has just been discovered in",0.007)
    type("the more squalid side of town. You should go there now" + Style.RESET_ALL,0.005)
    context["display"].print()
    print("Use help to display useful commands, make sure to investigate and talk to as many people as you can")

    #todo - swap out exit for game stor for game store (murder scene)

def murder_two(context):
    #murder at the docks in the evening of the first day
    #todo: turn into a murder scene
    type = context["display"].type



def add_events(narrative):
    narrative.add_event(1,2,0,murder_one)
    narrative.add_event(1,1,0,start_of_game)
    # narrative.add_event(1,1,1260,murder_two)

