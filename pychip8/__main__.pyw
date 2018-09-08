"""This is the main entry point for the program"""

from pychip8.rom_loader import RomLoader
from pychip8.operation_mapper import OperationMapper
from pychip8.cpu import Cpu
from pychip8.app import App
from pychip8.renderer import Renderer
from pychip8.keyboard_input_handler import KeyboardInputHandler
from pychip8.beeper import Beeper

if __name__ == "__main__":

    rom_loader = RomLoader()
    operation_mapper = OperationMapper()
    cpu = Cpu(operation_mapper)
    renderer = Renderer()
    input_handler = KeyboardInputHandler()
    beeper = Beeper()

    app = App(cpu, rom_loader, renderer, input_handler, beeper)

    app.run()
