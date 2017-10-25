from adt.items import *
from adt.characters import *
from adt.containers import *
from adt.investigatables import  *

# Bank of England
bank = {
    "name": "Bank of England",

    "description": "Bank of England",

    "people": [patrick , steven],
    
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

    "people": [vicar],

    "inventory": [],

    "exits": {"north": "Bank of England",
              "south": "Scotland Yard",
              }
}

# Hospital
hospital ={
    "name": "Hospital",
    
    "description": "Welcome to Hospital ",

    "people": [trisha , brian_ferguson , doctor],
    
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

    "people": [thomas],

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

    "people": [christine],
    
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

    "people": [clark , store_owner],
    
    "inventory": [scene_1_police_officer , clark],

    "exits": {
        "north": "MARKETPLACE",
    }
}

gamestore_murder = {
    "name": "XXX GAMESTORE (Murder Scene)",

    "description": "Littered around the room are adult films and broken shelves but the cash register is untouched. A bin also stands suspiciously upright in the corner)",

    "people": [scene_1_police_officer , gamestore_murder],

    "inventory": [],

    "containers" : [scene_1_bin],

    "investigatables" : [cash_register,shop_counter],

    "exits": {
        "north": "MARKETPLACE",
    }
}

docks_murder = {
    "name": "Docks",
    
    "description": "There has been another murder!",

    "people": [],

    "inventory" : [],

    "containers" : [boot , body_2 , seats , under_car],

    "investigatables" : [],

    "exits": {
        "west": "Kirills Tavern",
    }
}

marketplace_murder = {
    "name": "Marketplace",
    
    "description": "There has been another murder!",

    "people": [],
    
    "inventory": [],

    "investigatables": [card , cash],

    "exits": {
        "north": "Kirills Tavern",
        "south": "XXX GAMESTORE"
    }
}

hospital_murder ={
    "name": "Hospital",
    
    "description": "There has been another murder!",

    "people": [brian_ferguson , doctor],
    
    "inventory": [],

    "investigatables": [tissue],

    "exits": {"north": "Bank of England",
              "south": "Scotland Yard",
              }
}

factory_murder = {
    "name": "Factory",
    
    "description": "There has been another murder!",

    "people": [],

    "inventory": [],

    "investigatables": [axe , cloth , rod],

    "exits": {
        "east": "Kirills Tavern",
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