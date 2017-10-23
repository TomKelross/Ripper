from adt.characters import char_list
from adt.locations import location_list
from .Character import Character
from .Location import Location
# print(char_list)



def create_character(char_dict):

	name = char_dict["name"]
	occupation = char_dict["occupation"]
	gender = char_dict["gender"] 
	check = char_dict["check"]
	dialogue = char_dict["dialogue"]

	char_object = Character(name,occupation,gender,check,dialogue)

	return char_object


def character_factory():
	list_of_chars = []
	for char_dict in char_list:
		char_o = create_character(char_dict)
		list_of_chars.append(char_o)

	return list_of_chars

def create_location(location_dict):

	name = location_dict["name"]
	description = location_dict["description"]
	people = location_dict["people"] 
	inventory = location_dict["inventory"]

	location_object = Location(name,description,people,inventory)

	return location_object


def location_factory():
	list_of_locations = []
	for location_dict in location_list:
		location_o = create_location(location_dict)
		list_of_locations.append(location_o)

	return list_of_locations