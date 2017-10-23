# from .game import print
def murder_one(context):
    context['display'].print('Someone was murdered in the night')


def add_events(narrative):
    narrative.add_event(1,2,0,murder_one)

