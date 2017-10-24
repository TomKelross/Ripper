class Character(object):
    def __init__(self, name="Joe Bloggs", occupation="Townsperson", gender="Male", check="None", dialogue=[]):
        self.name = name
        self.occupation = occupation
        self.gender = gender
        self.check = check
        self.dialogue = dialogue
        self._dialogue_counter = 0
        self.location = None

        self.alive = True

    def __repr__(self):
        return "<Character {}>".format(self.name)

    def is_alive(self):
        return self.alive

    def move_to(self,location):
        self.location = location

    def talk(self):
        counter = self._dialogue_counter
        dialogue = self.dialogue

        if counter < len(dialogue):
            counter += 1
            return dialogue[counter - 1]
        else:
            counter = 0
            return dialogue[0]


class CharacterManager(object):
    def __init__(self, list_of_characters):
        self.characters = list_of_characters

    def get_character(self, name):
        for character in self.characters:
            if character.name == name:
                return character
        return False
