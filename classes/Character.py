class Character(object):

	def __init__(self,name="Joe Bloggs",occupation="Townsperson",gender="Male",check="None",dialogue=[]):
		self.name = name
		self.occupation = occupation
		self.gender = gender 
		self.check = check
		self.dialogue = dialogue

		self.location = "None"

		self.alive = True

	def __repr__(self):
		return "<Character {}>".format(self.name)

	def is_alive(self):
		return self.alive


class CharacterManager(object):

	def __init__(self,list_of_characters):
		self.characters = list_of_characters

	def get_character(self,name):
		for character in self.characters:
			if character.name == name:
				return character
		return False
