from numpy import uint8 as byte
from numpy import uint16

from opcode import Opcode


class Chip8:
    """This class represents the CHIP 8 cpu"""

    def __init__(self):

        self.should_draw = False

        self.PROGRAM_START_ADDRESS = 512 #game memory begins at address 0x200 / 512

        self.memory = [byte(0)] * 4096
        self.program_counter = uint16(self.PROGRAM_START_ADDRESS) 

        self.index_register = byte(0)
        self.main_registers = [byte(0)] * 16

        self.delay_timer = byte(0)
        self.sound_timer = byte(0)

        self.stack = [uint16(0)] * 16
        self.stack_pointer = uint16(0)

        self.keys = [byte(0)] * 16

        self.frame_buffer = [byte(0)] * (64 * 32)

    def load_rom(self, rom_bytes):

        for i, byte in enumerate(rom_bytes):
           self.memory[self.PROGRAM_START_ADDRESS + i] = byte 


    def emulate_cycle(self):
        word = self.fetch_word()
        opcode = Opcode(word)

        #Execute Opcode
        update_timers()
        pass

    def fetch_word(self):

        #load the next two bytes of memory into one 16 bit value - the current opcode.
        pc = int(self.program_counter) #indexes must be ints!
        word = uint16(self.memory[pc] << 8 | self.memory[pc + 1])

        return word   

    def draw_graphics(self):
        if(self.should_draw):
            pass

    def set_keys(self):
        pass

    def update_timers(self):
        if(self.delay_timer > 0) self.delay_timer--
        if(self.sound_timer > 0) self.sound_timer--