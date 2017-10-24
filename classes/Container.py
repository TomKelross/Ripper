class Container(object):
    def __init__(self, name="Broken Box", description="A old broken box", inventory=[], locked=False):
        self.name = name
        self.description = description
        self.inventory = inventory
        self.locked = False

    def __repr__(self):
        return "<Container {}>".format(self.name)


class ContainerManager(object):
    def __init__(self, list_of_Containers):
        self.Containers = list_of_Containers

    def get_Container(self, name):
        for Container in self.Containers:
            if Container.name == name:
                return Container
        return False
