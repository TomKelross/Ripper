import os
import sys
import time
from colorama import Fore, Style


class DisplayManager():
    _line_nums = 20
    _print_func = print
    _input_func = input

    def __init__(self):
        # Fill the display with empty lines
        _print_func = print
        _input_func = input

        self.screens = {
            "default": DefaultScreen('default', _print_func, _input_func),
            "story": Screen('story', _print_func, _input_func),
        }
        self.current_screen = "default"
        # self.lines = [{'content' : "", 'chunk' : 'default', 'tag' : '' } for x in range(self._line_nums)]

        self.cinematic_mode = False
        self.chunk_order = ['default']
        self.current_chunk = ['default']

    def get_current_screen(self):
        return self.screens[self.current_screen]

    def get_screen(self, name):
        return self.screens.get(name)

    def set_screen(self, screen_name):
        if screen_name in ['default', 'story']:
            self.current_screen = screen_name
        else:
            Exception()

    def print(self, message="", update=False, tag=''):
        # Add
        screen = self.get_current_screen()
        screen.print(message, update, tag)

    def delay_print(self, message=""):
        screen = self.get_current_screen()
        screen.delayed_print(message)

    def print_delayed(self):
        screen = self.get_current_screen()
        screen.print_delayed()

    # https://stackoverflow.com/questions/4099422/printing-slowly-simulate-typing
    def type(self, message, speed=0.03):
        screen = self.get_current_screen()
        screen.type(message, speed)

    def update_top_bar(self, message):
        default_screen = self.get_screen('default')
        default_screen.top_bar = message

    def update_room_display(self, room_name, murder_scene=False):
        default_screen = self.get_screen('default')
        default_screen.update_room_display(room_name, murder_scene)

    def clear_display(self):
        # https://stackoverflow.com/questions/2084508/clear-terminal-in-python
        os.system('cls' if os.name == 'nt' else 'clear')

    def reset_screen(self):
        screen = self.get_current_screen()
        screen.reset_screen()

    def print_screen(self, screen_name='default'):
        screen = self.get_screen(screen_name)
        screen.print_screen()

    def set_cinematic_mode(self, bool):
        self.cinematic_mode = bool

    def update_display(self):
        self.clear_display()
        self.print_screen()

    def get_input(self, message, update=True):
        if update:
            self.update_display()
        return self._input_func(message)

    def wait_for_input(self, update=True):
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

class Screen(object):
    def __init__(self, name, print_func, input_func, number_of_lines=25):
        self._print_func = print_func
        self._input_func = input_func
        self.name = name
        self.number_of_lines = number_of_lines
        self.lines = [{'content': "", 'chunk': 'default', 'tag': ''} for x in range(self.number_of_lines)]

        self.delayed_lines = []
        self.cinematic_mode = False
        self.chunk_order = ['default']
        self.current_chunk = ['default']

    def print(self, message, update=False, flag='', tag=''):
        self.lines.pop(0)
        current_chunk = self.current_chunk
        self.lines.append({'content': message, 'chunk': current_chunk, 'tag': tag})
        if update:
            self.update_display()

    def delayed_print(self, message):
        self.delayed_lines.append(message)

    def print_delayed(self):
        while self.delayed_lines:
            self.print(self.delayed_lines.pop(0))

    # https://stackoverflow.com/questions/4099422/printing-slowly-simulate-typing
    def type(self, message, speed=0.03,chunk='default',tag=''):
        self.lines.pop(0)
        self.lines.append({'content': '', 'chunk': chunk, 'tag': tag})
        for char in message:
            new_content = self.lines[-1]['content'] + char
            self.lines[-1] = {'content': new_content, 'chunk': chunk, 'tag': tag}
            time.sleep(speed)
            self.update_display()

    def clear_display(self):
        # https://stackoverflow.com/questions/2084508/clear-terminal-in-python
        os.system('cls' if os.name == 'nt' else 'clear')

    def reset_screen(self):
        self.lines = [{'content': "", 'chunk': 'default', 'tag': ''} for x in range(self.number_of_lines)]

    def update_display(self):
        self.clear_display()
        self.print_screen()

    def print_screen(self):
        for line in self.lines:
            content = line.get("content", "")
            self._print_func(content)


class DefaultScreen(Screen):
    def __init__(self, name, print_func, input_func, number_of_lines=25):
        super().__init__(name, print_func, input_func, number_of_lines=25)
        self.name = "Default"
        self.top_bar = ""
        self.room_lines = [{'content': "", 'chunk': 'room', 'tag': ''},
                           {'content': "", 'chunk': 'room', 'tag': ''},
                           {'content': "", 'chunk': 'room', 'tag': ''}]
        self.delayed_lines = []

    def print_screen(self):
        self._print_func(self.top_bar)
        self._print_func(self.room_lines[0]["content"])
        self._print_func(self.room_lines[1]["content"])
        self._print_func(self.room_lines[2]["content"])
        for line in self.lines:
            content = line.get("content", "")
            self._print_func(content)

    def update_room_display(self, room_name, murder_scene=False):
        if murder_scene:
            room_name = Fore.RED + room_name.upper() + Style.RESET_ALL
        else:
            room_name = room_name.upper()

        self.room_lines[0] = {'content': (" " * 40 + "╔" + "═" * len(room_name) + "╗")
            , 'chunk': 'room', 'tag': ''}
        self.room_lines[1] = {'content': ("═" * 40 + "╣" + room_name.upper() + "╠" + "═" * 30)
            , 'chunk': 'room', 'tag': ''}
        self.room_lines[2] = {'content': (" " * 40 + "╚" + "═" * len(room_name) + "╝")
            , 'chunk': 'room', 'tag': ''}
        pass

    def update_top_bar(self, message):
        self.top_bar = message
