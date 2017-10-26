from fuzzywuzzy import process
from colorama import Fore,Back,Style

class Character(object):
    def __init__(self, name="Joe Bloggs", occupation="Townsperson", gender="Male", check="None", dialogue=[],inventory=[]):
        self.name = name
        self.occupation = occupation
        self.gender = gender
        self.check = check
        self.dialogue = dialogue
        self._dialogue_counter = 0
        self.location = None
        self.inventory = []

        self.alive = True

    def __repr__(self):
        return "<Character {}>".format(self.name)

    def is_alive(self):
        return self.alive

    def move_to(self,location):
        self.location = location

    def get_name(self):
        return self.name

    def investigate(self):
        investigation_to_print = []
        investigation_to_print.append(Fore.GREEN + "[" + Fore.LIGHTGREEN_EX + self.name + Fore.GREEN + "]")
        # investigation_to_print.append(Fore.GREEN+"  "+"Occupation " + Fore.BLUE + Style.RESET_ALL)
        investigation_to_print.append(Fore.GREEN+"  "+"Gender " + Fore.BLUE + self.gender)
        if self.check != "None" and self.check!= "none":
            investigation_to_print.append(Fore.GREEN+"  "+"["+Fore.LIGHTBLUE_EX+"Check"+Fore.GREEN+"]" + Style.RESET_ALL)
            investigation_to_print.append(Fore.WHITE+"     " + self.check)
        investigation_to_print.append(" " + Style.RESET_ALL)
        return investigation_to_print

    def next_dialogue_text(self):
        dialogue = self.dialogue
        if dialogue:
            if self._dialogue_counter < len(dialogue):
                self._dialogue_counter += 1
                return dialogue[self._dialogue_counter - 1]
            else:
                self._dialogue_counter = 0
                return dialogue[0]

    def next_dialogue(self):
        dialogue = self.next_dialogue_text()
        dialogue_count = self.get_dialogue_count()
        total_dialogues = self.get_dialogue_length()
        dialogue_counter = (Fore.GREEN + " ("
                            + Fore.LIGHTGREEN_EX + str(dialogue_count)
                            + Fore.GREEN + "/"
                            + Fore.LIGHTGREEN_EX + str(total_dialogues)
                            + Fore.GREEN + ")" + Style.RESET_ALL
                            )

        return (Fore.GREEN + "[" + Fore.LIGHTGREEN_EX + self.name + Fore.GREEN + "] "
        + Fore.WHITE + dialogue
        + dialogue_counter
        + Style.RESET_ALL)

    def get_dialogue_count(self):
        return self._dialogue_counter

    def get_dialogue_length(self):
        return len(self.dialogue)

    def get_items(self):
        return self.inventory

    def add_item(self, item):
        self.inventory.append(item)

    def remove_item(self, item):
        return self.inventory.remove(item)





class CharacterManager(object):
    def __init__(self, list_of_characters):
        self.characters = list_of_characters

    def get_character(self, name):
        for character in self.characters:
            if character.name == name:
                return character
        return False
    
    def get_character_fuzzy(self,fuzzy_name,search_space=False):
        if search_space:
            characters_to_match = search_space
        else:
            characters_to_match = self.characters

        names_of_characters = [ character.get_name() for character in characters_to_match]
        best_guess = process.extract(fuzzy_name, names_of_characters, limit=1)
        certainty = best_guess[0][1]
        if certainty > 50:
            return self.get_character(best_guess[0][0])
        else:
            return False
