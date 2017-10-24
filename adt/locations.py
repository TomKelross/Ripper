from adt.items import *
from adt.characters import *
from adt.containers import *

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
    
    "inventory": [],

    "container" : [drawers],

    "exits" : {"east" : "Hospital",
               "north" : "Bank of England",
               "west" : "Church",
               "south" : "Thames"
               }
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
    "name": "Gamestore",
    
    "description": "Welcome to the Gamestore! ",

    "people": [],
    
    "inventory": [],

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
location_list = [bank,church,hospital,scotland,thames,factory,kirills,docks,marketplace,gamestore]