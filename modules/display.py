import os
import sys
import time
from colorama import Fore, Style


class DisplayManager():
    _line_nums = 40
    _print_func = print
    _input_func = input

    def __init__(self):
        # Fill the display with empty lines
        self.lines = [{'content' : "", 'chunk' : 'default', 'tag' : '' } for x in range(self._line_nums)]
        self.top_bar = ""
        self.room_lines = [{'content' : "", 'chunk' : 'room', 'tag' : '' },
                           {'content' : "", 'chunk' : 'room', 'tag' : '' },
                           {'content' : "", 'chunk' : 'room', 'tag' : '' }]
        self.delayed_lines = []
        self.cinematic_mode = False
        self.chunk_order = ['default']
        self.current_chunk = ['default']

    def print(self, message="",update=True,tag=''):
        # Add
        self.lines.pop(0)
        current_chunk = self.current_chunk
        self.lines.append({'content' : message , 'chunk' : current_chunk, 'tag' : tag })
        if update:
            self.update_display()

    def delay_print(self,message=""):
        self.delayed_lines.append(message)

    def print_delayed(self):
        while self.delayed_lines:
            self.print(self.delayed_lines.pop(0))

    # https://stackoverflow.com/questions/4099422/printing-slowly-simulate-typing
    def type(self, message, speed=0.03):
        self.lines.pop(0)
        self.lines.append('')
        for char in message:
            self.lines[-1] = self.lines[-1] + char
            time.sleep(speed)
            self.update_display()

    def update_top_bar(self, message):
        self.top_bar = message

    def update_room_display(self,room_name,murder_scene = False):
        if murder_scene:
            room_name = Fore.RED + room_name.upper() + Style.RESET_ALL
        else:
            room_name = room_name.upper()

        self.room_lines[0] = {'content' : (" " * 40 + "╔" + "═" * len(room_name) + "╗")
            , 'chunk' : 'room', 'tag' : '' }
        self.room_lines[1] = {'content' : ("═" * 40 + "╣" + room_name.upper() + "╠" + "═" * 30)
            , 'chunk' : 'room', 'tag' : '' }
        self.room_lines[2] = {'content' : (" " * 40 + "╚" + "═" * len(room_name) + "╝")
            , 'chunk' : 'room', 'tag' : '' }
        pass

    def clear_display(self):
        # https://stackoverflow.com/questions/2084508/clear-terminal-in-python
        os.system('cls' if os.name == 'nt' else 'clear')

    def reset_display(self):
        self.lines = [{'content' : "", 'chunk' : 'default', 'tag' : '' } for x in range(self._line_nums)]

    def show_display(self):
        if not self.cinematic_mode:
            self._print_func(self.top_bar)
            self._print_func(self.room_lines[0]["content"])
            self._print_func(self.room_lines[1]["content"])
            self._print_func(self.room_lines[2]["content"])
        for line in self.lines:
            content = line.get("content","")
            self._print_func(content)


    def set_cinematic_mode(self,bool):
        self.cinematic_mode = bool

    def update_display(self):
        self.clear_display()
        self.show_display()

    def get_input(self, message,update=True):
        if update:
            self.update_display()
        return self._input_func(message)

    def wait_for_input(self,update=True):
        if update:
            self.update_display()
        return self._input_func("Press Enter To Continue")

# disp = DisplayManager()
# print = disp.print
# input = disp.get_input


# while True:
# 	disp.type("Welcome to Ripper")
# 	disp.type("Can you solve the mystery",0.08)
# 	print(input(">"))
