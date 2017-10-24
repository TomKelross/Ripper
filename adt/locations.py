from adt.items import *
from adt.characters import *
from adt.containers import *

# Bank of England
bank = {
    "name": "Bank of England",

    "description": "Bank of England",

    "people": [],
    
    "inventory": [],

}

# Church
church = {
    "name": "Church",

    "description": "Welcome to Church ",

    "people": [],

    "inventory": [],
}

# Hospital
hospital ={
    "name": "Hospital",
    
    "description": "Welcome to Hospital ",

    "people": [],
    
    "inventory": [],
}

# Scotland Yard
scotland = {
    "name": "Scotland Yard",

    "description": "Welcome to New Scotland Yard!",

    "people": [police_man],
    
    "inventory": [],

    "container" : [drawers]
}

# Thames
thames = {
    "name": "Thames",

    "description": "Welcome to Thames Barrier!",

    "people": [],

    "inventory": [],
}

# Factory
factory = {
    "name": "Factory",
    
    "description": "Welcome to the Factory!",

    "people": [],

    "inventory": [],
}

# Kirills Tavern
kirills = {
    "name": "Kirills Tavern",
    
    "description": "Welcome to Kirills Tavern!",

    "people": [kirill, clark],
    
    "inventory": [beer, beer, beer],
}

# Docks
docks = {
    "name": "Docks",
    
    "description": "Welcome to the Docks!",

    "people": [],

    "inventory" : []
}

# Marketpalce
marketplace = {
    "name": "Marketplace",
    
    "description": "Welcome to the Market!",

    "people": [],
    
    "inventory": []
}

# Gamestore
gamestore = {
    "name": "Gamestore",
    
    "description": "Welcome to the Gamestore! ",

    "people": [],
    
    "inventory": []
}

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