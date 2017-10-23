from adt.items import *
from adt.characters import *

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

    "people": [],
    
    "inventory": [],
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

# Krills Tavern
krills = {
    "name": "Krills Tavern",
    
    "description": "Welcome to Krills Tavern!",

    "people": [krill, clark],
    
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
    "Krills": krills,
    "Docks": docks,
    "Marketplace": marketplace,
    "Gamestore": gamestore,
}
location_list = [bank,church,hospital,scotland,thames,factory,krills,docks,marketplace,gamestore]