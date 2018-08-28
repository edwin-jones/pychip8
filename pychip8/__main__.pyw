"""This is the main entry point for the program"""

from pychip8.rom_loader import RomLoader
from pychip8.operation_mapper import OperationMapper
from pychip8.cpu import Cpu
from pychip8.app import App

if __name__ == "__main__":

    rom_loader = RomLoader()
    operation_mapper = OperationMapper()
    cpu = Cpu(operation_mapper)
    app = App(cpu, rom_loader)
    
    app.run()
