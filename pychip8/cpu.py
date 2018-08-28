# see https://en.wikipedia.org/wiki/CHIP-8 for the chip 8 spec

from numpy import uint8 as byte
from numpy import uint16
import numpy

from pychip8.opcode import Opcode
import pychip8.font as Font

class Cpu:
    """This class represents the CHIP 8 cpu"""
    PROGRAM_START_ADDRESS = 512 # game ram begins at address 0x200 / 512
    WORD_SIZE_IN_BYTES = 2 # the chip 8 works with 16 bit/2 byte opcodes
    ARITHMETIC_FLAG_REGISTER_ADDRESS = 0xF #V[15] is used as a carry/no borrow flag for certain ops

    def __init__(self, operation_mapper):

        self.operation_mapper = operation_mapper

        self.should_draw = False
        self.ram = [byte(0)] * 4096 # 4k of RAM
        self.program_counter = uint16(self.PROGRAM_START_ADDRESS)

        self.index_register = uint16(self.PROGRAM_START_ADDRESS)
        self.general_purpose_registers = [byte(0)] * 16

        self.delay_timer = byte(0)
        self.sound_timer = byte(0)

        self.stack = []
        self.stack_pointer = uint16(0)

        self.keys = set()

        self.frame_buffer = [byte(0)] * (64 * 32)

        self._load_font()

    def key_down(self, key):
        self.keys.add(key)
    
    def key_up(self, key):
        self.keys.remove(key)

    def move_to_next_instruction(self):
        self.program_counter += Cpu.WORD_SIZE_IN_BYTES

    def move_to_previous_instruction(self):
        self.program_counter -= Cpu.WORD_SIZE_IN_BYTES

    def load_rom(self, rom_bytes):
        for i, byte_value in enumerate(rom_bytes):
           self.ram[Cpu.PROGRAM_START_ADDRESS + i] = byte_value

    def set_arithmetic_flag(self):
        self.general_purpose_registers[self.ARITHMETIC_FLAG_REGISTER_ADDRESS] = 1

    def clear_arithmetic_flag(self):
        self.general_purpose_registers[self.ARITHMETIC_FLAG_REGISTER_ADDRESS] = 0

    def emulate_cycle(self):
        word = self.fetch_word()
        opcode = Opcode(word)
        operation = self.operation_mapper.find_operation(word)

        operation.execute(opcode, self)
        self.update_timers()
        
    def fetch_word(self):

        # load the next two bytes of ram into one 16 bit value - the current opcode.
        pc = int(self.program_counter) #indexes must be ints!
        word = uint16(self.ram[pc] << 8 | self.ram[pc + 1])

        return word   

    def draw_graphics(self):
        if(self.should_draw):
            pass

    def set_keys(self):
        pass

    def update_timers(self):
        if(self.delay_timer > 0):
            self.delay_timer -= 1

        if(self.sound_timer > 0):
            self.sound_timer -= 1

    def _load_font(self):
        offset = 0x0
        for item in Font.DATA:
             self.ram[offset] = byte(item)
             offset += 1
