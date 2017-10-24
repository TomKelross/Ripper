class Item(object):
    def __init__(self, name="Trash", description="Some random trash", mass=1, value=0,droppable=True):
        self.name = name
        self.description = description
        self.mass = mass
        self.value = value
        self.droppable = droppable

    def __repr__(self):
        return "<Item {}>".format(self.name)

    def is_alive(self):
        return self.alive


class ItemManager(object):
    def __init__(self, list_of_Items):
        self.Items = list_of_Items

    def get_Item(self, name):
        for Item in self.Items:
            if Item.name == name:
                return Item
        return False
