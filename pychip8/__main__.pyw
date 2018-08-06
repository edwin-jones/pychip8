"""This is the main entry point for the program"""

import settings
from renderer import Renderer
from keyboard_input_handler import KeyboardInputHandler
from chip8 import Chip8

from app import App
#from keyboard_input_handler import KeyboardInputHandler
#from player import Player
#from renderer import Renderer

if __name__ == "__main__":

    renderer = Renderer()
    input_handler = KeyboardInputHandler()
    chip8 = Chip8()


    app = App(renderer, input_handler)
    app.run()
