from fuzzywuzzy import process

class Item(object):
    def __init__(self, name="Trash", description="Some random trash", mass=1, value=0,droppable=True):
        self.name = name
        self.description = description
        self.mass = mass
        self.value = value
        self.droppable = droppable

    def __repr__(self):
        return "<Item {}>".format(self.name)

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

class ItemManager(object):
    def __init__(self, list_of_Items):
        self.items = list_of_Items

    def get_item(self, name):
        for Item in self.items:
            if Item.name == name:
                return Item
        return False

    def get_container_fuzzy(self,fuzzy_name):
        all_containers = self.containers
        names_of_all_containers = [ container.get_name() for container in all_containers]
        best_guess = process.extract(fuzzy_name, names_of_all_containers, limit=1)
        certainty = best_guess[0][1]
        if certainty > 50:
            return self.get_container(best_guess[0][0])
        else:
            return False


