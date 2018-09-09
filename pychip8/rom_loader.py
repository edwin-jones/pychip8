"This module defines a Rom Loader class for loading roms"

import os

class RomLoader():
    "This class handles loading roms"

    @staticmethod
    def get_rom_bytes(rom_name):
        """This method loads the bytes from a rom from the roms folder"""
        folder = os.path.dirname(os.path.realpath(__file__))
        rom_folder = os.path.join(folder, "roms")
        rom_file_path = os.path.join(rom_folder, rom_name)

        with open(rom_file_path, "rb") as file:
            file_bytes = file.read()
            return file_bytes
