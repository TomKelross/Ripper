from adt.items import *

drawers = {
    "name": "Chest of drawers",
    "description": "Full of stuff",
    "inventory": [beer, beer, beer]
}

# Scene 1
bin = {
    "name": "Bin in the XXX Video Store",
    "description": "While the rest of the store is trashed, this bin seems supiciously upright",
    "inventory": [knife]
}
#############

# Scene 4 things
s4_car_boot = {
    "name": "Car Boot",
    "description": "Car boot in which the body was found at the Docks",
    "inventory": [wrench]
}

s4_body_steven = {
    "name": "Body of Steven Cornwall",
    "description": "The Body of the late Steven Cornwall",
    "inventory": [phone]
}
# ######

container_list = [drawers, bin, s4_car_boot, s4_body_steven]
scene_1_bin = {
    "name": "Upright Bin",
    "description": "Suspiciously upright",
    "inventory": [knife]
}

container_list = [drawers, scene_1_bin]
