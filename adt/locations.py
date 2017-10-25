from adt.items import *
from adt.characters import *
from adt.containers import *
from adt.investigatables import  *

# Bank of England
bank = {
    "name": "Bank of England",

    "description": "Bank of England",

    "people": [],
    
    "inventory": [],

    "exits" : {"east" : "Hospital",
               "south" : "Scotland Yard",
               "west" : "Church",
               }
}

# Church
church = {
    "name": "Church",

    "description": "Welcome to Church ",

    "people": [],

    "inventory": [],

    "exits": {"north": "Bank of England",
              "south": "Scotland Yard",
              }
}

# Hospital
hospital ={
    "name": "Hospital",
    
    "description": "Welcome to Hospital ",

    "people": [],
    
    "inventory": [],

    "exits": {"north": "Bank of England",
              "south": "Scotland Yard",
              }
}

# Scotland Yard
scotland = {
    "name": "Scotland Yard",

    "description": "Welcome to New Scotland Yard!",

    "people": [police_man],
    
    "inventory": [police_badge],

    "containers" : [drawers],

    "exits" : {"east" : "Hospital",
               "north" : "Bank of England",
               "west" : "Church",
               "south" : "Thames"
               },

    "investigatables" : [ wanted_poster ]
}

# Thames
thames = {
    "name": "Thames",

    "description": "Welcome to Thames Barrier!",

    "people": [],

    "inventory": [],

    "exits": {
              "north": "Scotland Yard",
              "south": "Kirills Tavern"
              }
}

# Factory
factory = {
    "name": "Factory",
    
    "description": "Welcome to the Factory!",

    "people": [],

    "inventory": [],

    "exits": {
        "east": "Kirills Tavern",
    }
}

# Kirills Tavern
kirills = {
    "name": "Kirills Tavern",
    
    "description": "Welcome to Kirills Tavern!",

    "people": [kirill, clark],
    
    "inventory": [beer, beer, beer],

    "exits": {
        "north": "Thames",
        "east": "Docks",
        "south" : "Marketplace",
        "west" : "Factory"
    }
}

# Docks
docks = {
    "name": "Docks",
    
    "description": "Welcome to the Docks!",

    "people": [],

    "inventory" : [],

    "exits": {
        "west": "Kirills Tavern",
    }
}

# Marketpalce
marketplace = {
    "name": "Marketplace",
    
    "description": "Welcome to the Market!",

    "people": [],
    
    "inventory": [],

    "exits": {
        "north": "Kirills Tavern",
        "south": "XXX GAMESTORE"
    }
}

# Gamestore
gamestore = {
    "name": "XXX GAMESTORE",
    
    "description": "Welcome to the Gamestore! ",

    "people": [],
    
    "inventory": [],

    "exits": {
        "north": "MARKETPLACE",
    }
}

gamestore_murder = {
    "name": "XXX GAMESTORE (Murder Scene)",

    "description": "There has been a murder",

    "people": [scene_1_police_officer],

    "inventory": [],

    "containers" : [scene_1_bin],

    "investigatables" : [cash_register,shop_counter],

    "exits": {
        "north": "MARKETPLACE",
    }
}


# northern_courtyard = {
#     "name" : 'Northern Courtyard'
#     "description" {}
# }

getLocation = {
    "Bank": bank,
    "Church": church,
    "Hospital" : hospital,
    "Scotland": scotland,
    "Thames": thames,
    "Factory": factory,
    "Kirills": kirills,
    "Docks": docks,
    "Marketplace": marketplace,
    "Gamestore": gamestore,
}
location_list = [bank,church,hospital,scotland,thames,factory,kirills,docks,marketplace,gamestore,gamestore_murder]