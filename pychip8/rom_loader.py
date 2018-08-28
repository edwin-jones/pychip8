
import os

class RomLoader():

    def get_rom(self):
        """A simple way to load the first rom in the roms folder"""

        folder = os.path.dirname(os.path.realpath(__file__))
        rom_folder = os.path.join(folder, "rom")
        rom_file = os.listdir(rom_folder)[0]
        rom_file_path = os.path.join(rom_folder, rom_file)
        file_bytes = []
        with open(rom_file_path, "rb") as file:
            file_bytes = file.read()
            return file_bytes
