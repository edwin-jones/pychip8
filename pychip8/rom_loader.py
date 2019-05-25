"This module defines a Rom Loader class for loading roms"

import os

class RomLoader():
    "This class handles loading roms"

    def __init__(self, rom_name):
        self.rom_name = rom_name

    def get_rom_bytes(self):
        """This method loads the bytes from a rom from the roms folder"""
        folder = os.path.dirname(os.path.realpath(__file__))
        rom_folder = os.path.join(folder, "roms")
        rom_file_path = os.path.join(rom_folder, self.rom_name)

        with open(rom_file_path, "rb") as file:
            file_bytes = file.read()
            return file_bytes
