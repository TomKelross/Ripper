from adt.items import *

drawers = {
    "name": "Chest of drawers",
    "description": "Full of stuff",
    "inventory": [beer, beer, beer]
}

bin = {
    "name": "Bin in the XXX Video Store",
    "description": "While the rest of the store is trashed, this bin seems supiciously upright",
    "inventory": [knife]
}

boot = {
    "name": "Car Boot",
    "description": "Car boot in which the body was found at the Docks",
    "inventory": [wrench]
}

body_2 = {
    "name": "Body of Steven Cornwall",
    "description": "The Body of the late Steven Cornwall",
    "inventory": [phone]
}

container_list = [drawers, bin, boot, body_2]
scene_1_bin = {
    "name": "Upright Bin",
    "description": "Suspiciously upright",
    "inventory": [murder_knife]
}

container_list = [drawers, scene_1_bin]
