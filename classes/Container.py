from fuzzywuzzy import process

class Container(object):
    def __init__(self, name="Broken Box", description="A old broken box", inventory=[], locked=False):
        self.name = name
        self.description = description
        self.inventory = inventory
        self.locked = False

    def __repr__(self):
        return "<Container {}>".format(self.name)

    def get_items(self):
        return self.inventory

    def add_item(self,item):
        self.inventory.append(item)

    def get_name(self):
        return self.name

    def remove_item(self,item):
        return self.inventory.remove(item)

    def get_description(self):
        return self.description


class ContainerManager(object):
    def __init__(self, list_of_Containers):
        self.containers = list_of_Containers

    def get_container(self, name):
        for Container in self.containers:
            if Container.name == name:
                return Container
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
