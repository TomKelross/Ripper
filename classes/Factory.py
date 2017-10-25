from adt.characters import char_list
from adt.locations import location_list
from adt.containers import container_list
from adt.items import item_list
from adt.investigatables import investigatable_list
from classes.Item import Item
from classes.Investigatable import Investigatable
from .Character import Character
from .Location import Location
from .Container import Container

# print(char_list)



def create_character(char_dict):
    name = char_dict.get("name","Joe Bloggs")
    occupation = char_dict.get("occupation","NA")
    gender = char_dict.get("gender","male")
    check = char_dict.get("check","NA")
    dialogue = char_dict.get("dialogue",[])
    inventory = char_dict.get("inventory",[])

    char_object = Character(name, occupation, gender, check, dialogue,inventory)

    return char_object


def character_factory():
    list_of_chars = []
    for char_dict in char_list:
        char_o = create_character(char_dict)
        list_of_chars.append(char_o)

    return list_of_chars


def create_location(location_dict, characters, items,containers,investigatables):
    name = location_dict["name"]
    description = location_dict["description"]
    inventory = location_dict.get("inventory",[])
    exits = location_dict.get("exits",[])
    
    people = []
    for person_dict in location_dict["people"]:
        person_object = characters.get_character(person_dict["name"])
        people.append(person_object)

    item_list = []
    for item_dict in inventory:
        item_object = items.get_item(item_dict["name"])
        item_list.append(item_object)

    room_containers = []
    for container_dict in location_dict.get("containers",[]):
        container = containers.get_container(container_dict["name"])
        room_containers.append(container)

    room_investigatables = []
    for investigatable_dict in location_dict.get("investigatables", []):
        investigatable = investigatables.get_investigatable(investigatable_dict["name"])
        room_investigatables.append(investigatable)

    location_object = Location(name,description,exits,people,item_list,room_containers,room_investigatables)

    return location_object


def location_factory(characters,items,containers,investigatables):
    list_of_locations = []
    for location_dict in location_list:
        location_o = create_location(location_dict, characters,items,containers,investigatables)
        list_of_locations.append(location_o)

    return list_of_locations

def create_item(item_dict):
    name = item_dict["name"]
    description = item_dict["description"]
    mass = item_dict.get("mass",1)
    value = item_dict.get("value",0)
    droppable = item_dict.get("droppable",False)

    item_object = Item(name, description, mass, value, droppable)

    return item_object


def item_factory():
    list_of_items = []
    for item_dict in item_list:
        item_o = create_item(item_dict)
        list_of_items.append(item_o)

    return list_of_items

def create_container(container_dict,items):
    name = container_dict["name"]
    description = container_dict["description"]
    
    inventory = [] 
    for item_dict in container_dict.get("inventory",[]):
        item_object = items.get_item(item_dict.get("name"))
        inventory.append(item_object)

    locked = container_dict.get("locked",False)

    container_object = Container(name,description,inventory,locked)

    return container_object


def container_factory(items):
    list_of_containers = []
    for container_dict in container_list:
        container_o = create_container(container_dict,items)
        list_of_containers.append(container_o)

    return list_of_containers


def create_investigatable(investigatable_dict):
    name = investigatable_dict["name"]
    description = investigatable_dict["description"]
    
    investigatable_object = Investigatable(name, description)

    return investigatable_object


def investigatable_factory():
    list_of_investigatables = []
    for investigatable_dict in investigatable_list:
        investigatable_o = create_investigatable(investigatable_dict)
        list_of_investigatables.append(investigatable_o)

    return list_of_investigatables