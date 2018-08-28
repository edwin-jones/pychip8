"""This is the main entry point for the program"""

#from renderer import Renderer
#from keyboard_input_handler import KeyboardInputHandler
from pychip8.cpu import Cpu
from pychip8.rom_loader import RomLoader
from pychip8.operation_mapper import OperationMapper

#from app import App
#from keyboard_input_handler import KeyboardInputHandler
#from player import Player
#from renderer import Renderer

if __name__ == "__main__":

    #renderer = Renderer()
    mapper = OperationMapper
    cpu = Cpu(mapper)

    rom_loader = RomLoader()

    cpu.load_rom(rom_loader.get_rom())

    #app = App(renderer, input_handler)
    #app.run()
