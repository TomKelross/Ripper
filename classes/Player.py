

class Player:

    """
    Author: Kyle Davies
    """
    
    # Players name
    __name = ""
    
    # Players notes
    __notes = []

    # Players location
    __location = False

    # Players inventory
    __inventory = []

    # Default Constructor
    def __init__(self, name):
        self.__name = name

    def __repr__(self):
        return "<Player {}>".format(self.__name)
    
    #  Gets the player's name
    def get_name(self):
        return self.__name

    # Sets the player's name
    def set_name(self, name):
        self.__name = name
    
    # Sets the player's 
    def set_notes(self, text):
        self.__notes.append(text)

    def get_notes(self):
        return self.__notes
    
    def set_location(self, location):
        self.__location = location

   
    def get_location(self):
        return self.__location

    def add_to_inventory(self, item):
        self.__inventory.append(item)
    
    def remove_from_inventory(self, item):
        self.__inventory.remove(item)
    
    def get_inventory(self):
        return self.__inventory

    def inventoryToString(self): #BROKE
        
        list = []

        csv = " "
        
        list = self.__inventory

        for item in list:
            csv = csv + item + ", "
        
        # Removes " ," from the end of the string
        csv = csv[:-2]

        return csv
    
    