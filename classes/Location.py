from fuzzywuzzy import fuzz
from fuzzywuzzy import process


class Location(object):
    def __init__(self, name, description, people=[], inventory=[],containers=[]):
        self.name = name
        self.description = description
        self.people = people
        self.inventory = inventory
        self.containers = containers

    def __repr__(self):
        return "< Location {} with {} people>".format(self.name, len(self.people))

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description = description

    def get_people(self):
        return self.people

    def remove_person(self, person):
        self.people.remove(person)

    def add_person(self, person):
        self.people.append(person)

    def set_people(self, people):
        self.people = people


class LocationManager(object):
    def __init__(self, list_of_locations):
        self.locations = list_of_locations

    def get_location(self, name):
        for location in self.locations:
            if location.name == name:
                return location
        return False

    def get_all_locations(self):
        return self.locations

    def get_location_fuzzy(self,fuzzy_name):
        all_locations = self.locations
        names_of_all_locations = [ location.get_name() for location in all_locations]
        best_guess = process.extract(fuzzy_name, names_of_all_locations, limit=1)
        certainty = best_guess[0][1]
        if certainty > 50:
            return self.get_location(best_guess[0][0])
        else:
            return False


