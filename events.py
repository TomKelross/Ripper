# from .game import print
def murder_one(context):
    context['display'].print('Someone was murdered in the night')

def start_of_game(context):
    context["display"].type("Welcome to Ripper. You are detective John S",0.01)
    context["display"].type("Report to the police sargeant",0.05)


def add_events(narrative):
    narrative.add_event(1,2,0,murder_one)
    # narrative.add_event(1,1,0,start_of_game)

