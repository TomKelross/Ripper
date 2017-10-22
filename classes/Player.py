class Player:

    """
    Author: Kyle Davies
    """
    
    # Players name
    __name = ""
    
    # Players notes
    __notes = []

    # Players location
    __location = "Scotland"

    # Players inventory
    __inventory = []

    # Default Constructor
    def __init__(self, name):
        self.__name = name
    
    #  Gets the player's name
    def getName(self):   
        return self.__name

    # Sets the player's name
    def setName(self, name):
        self.__name = name
    
    # Sets the player's 
    def setNotes(self, text):
        self.__notes.append(text)

    def getNotes(self):
        return self.__notes
    
    def setLocation(self, location):
        self.__location = location
   
    def getLocation(self):
        return self.__location

    def addToInventory(self, item):
        self.__inventory.append(item)
    
    def removeToInvebtory(self, item):
        self.__inventory.remove(item)
    
    def returnInventory(self):
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
    
    