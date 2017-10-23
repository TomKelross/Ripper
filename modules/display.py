import os
import sys
import time

class DisplayManager():

	_line_nums = 20
	_print_func = print
	_input_func = input

	def __init__(self):
		#Fill the display with empty lines
		self.lines = ['' for x in range(self._line_nums)]
		self.top_bar = "Ripper v1.0"

	def print(self,message):
		#Add 
		self.lines.pop(0)
		self.lines.append(message) 
		self.update_display()

	#https://stackoverflow.com/questions/4099422/printing-slowly-simulate-typing
	def type(self,message,speed=0.03):
		self.lines.pop(0)
		self.lines.append('') 
		for char in message:
		    self.lines[-1] = self.lines[-1] + char
		    time.sleep(speed)
		    self.update_display()

	def update_top_bar(self,message):
		self.top_bar = message

	def clear_display(self):
		#https://stackoverflow.com/questions/2084508/clear-terminal-in-python
		os.system('cls' if os.name == 'nt' else 'clear')

	def show_display(self):
		self._print_func(self.top_bar)
		for line in self.lines:
			self._print_func(line)

	def update_display(self):
		self.clear_display()
		self.show_display()

	def get_input(self,message):
		self.update_display()
		return self._input_func(message)


disp = DisplayManager()
print = disp.print
input = disp.get_input


while True:
	disp.type("Welcome to Ripper")
	disp.type("Can you solve the mystery",0.08)
	print(input(">"))
	

