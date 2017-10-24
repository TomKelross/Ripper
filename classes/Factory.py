from adt.characters import char_list
from adt.locations import location_list
from adt.containers import container_list
from adt.items import item_list
from classes.Item import Item
from .Character import Character
from .Location import Location
from .Container import Container

# print(char_list)



def create_character(char_dict):
    name = char_dict["name"]
    occupation = char_dict["occupation"]
    gender = char_dict["gender"]
    check = char_dict["check"]
    dialogue = char_dict["dialogue"]

    char_object = Character(name, occupation, gender, check, dialogue)

    return char_object


def character_factory():
    list_of_chars = []
    for char_dict in char_list:
        char_o = create_character(char_dict)
        list_of_chars.append(char_o)

    return list_of_chars


def create_location(location_dict, characters, items,containers):
    name = location_dict["name"]
    description = location_dict["description"]
    inventory = location_dict["inventory"]
    exits = location_dict.get("exits",[])
    
    people = []
    for person_dict in location_dict["people"]:
        person_object = characters.get_character(person_dict["name"])
        people.append(person_object)

    inventory = []
    for item_dict in location_dict["inventory"]:
        item_object = items.get_item(item_dict["name"])
        inventory.append(item_object)

    containers = []
    for container_dict in location_dict.get("containers",[]):
        container = containers.get_container(container_dict["name"])
        containers.append(person_object)
        
        
    location_object = Location(name,description,exits,people,inventory,containers)

    return location_object


def location_factory(characters,items,containers):
    list_of_locations = []
    for location_dict in location_list:
        location_o = create_location(location_dict, characters,items,containers)
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