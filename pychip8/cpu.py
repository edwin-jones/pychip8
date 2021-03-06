"this module defines the chip 8 cpu"

# see https://en.wikipedia.org/wiki/CHIP-8 for the chip 8 spec
from pychip8.opcode import Opcode
import pychip8.font as Font


class Cpu:
    """this class represents the CHIP 8 cpu"""

    PROGRAM_START_ADDRESS = 0x200 # game ram begins at address 0x200 / 512
    WORD_SIZE_IN_BYTES = 2 # the chip 8 works with 16 bit/2 byte opcodes
    ARITHMETIC_FLAG_REGISTER_ADDRESS = 0xF #V[15] is used as a carry/no borrow flag for certain ops
    FRAME_BUFFER_WIDTH = 64
    FRAME_BUFFER_HEIGHT = 32

    def __init__(self, operation_mapper):
        self.operation_mapper = operation_mapper

        self.ram = [0] * 4096 # 4k of RAM
        self.program_counter = self.PROGRAM_START_ADDRESS

        self.index_register = 0
        self.general_purpose_registers = [0] * 16

        self.delay_timer = 0
        self.sound_timer = 0

        self.stack = []
        self.stack_pointer = 0

        self.keys = set()

        self.frame_buffer = [[bool()] * 32 for i in range(64)]

        self._load_font()

        self._current_word = 0
        self._current_operation = None

    def key_down(self, key):
        "This method sets a key as pressed"
        if key not in self.keys:
            self.keys.add(key)

    def key_up(self, key):
        "This method sets a key as released"
        if key in self.keys:
            self.keys.remove(key)

    def move_to_next_instruction(self):
        "this method will move the program counter forward to the next instruction"
        self.program_counter += Cpu.WORD_SIZE_IN_BYTES

    def move_to_previous_instruction(self):
        "this method will move the program counter backward to the previous instruction"
        self.program_counter -= Cpu.WORD_SIZE_IN_BYTES

    def load_rom(self, rom_bytes):
        "this will load rom bytes intom main memory/RAM"
        for i, byte_value in enumerate(rom_bytes):
            self.ram[Cpu.PROGRAM_START_ADDRESS + i] = byte_value

    def set_arithmetic_flag(self):
        "this method will set the arithmetic flag to 1"
        self.general_purpose_registers[self.ARITHMETIC_FLAG_REGISTER_ADDRESS] = 1

    def clear_arithmetic_flag(self):
        "this method will set the arithmetic flag to 0"
        self.general_purpose_registers[self.ARITHMETIC_FLAG_REGISTER_ADDRESS] = 0

    def emulate_cycle(self):
        "this method will run one cpu cycle"
        self._current_word = self.fetch_word()

        opcode = Opcode(self._current_word)
        self._current_operation = self.operation_mapper.find_operation(self._current_word)

        self.move_to_next_instruction()
        self._current_operation.execute(opcode, self)

    def fetch_word(self):
        "this method will load the next two bytes of ram into one 16 bit value - the current opcode"
        word = self.ram[self.program_counter] << 8 | self.ram[self.program_counter + 1]

        return word

    def update_timers(self):
        "this method will decrement any timers that are above 0 by 1"
        if self.delay_timer > 0:
            self.delay_timer -= 1

        if self.sound_timer > 0:
            self.sound_timer -= 1

    def get_debug_strings(self):
        """
        this method will get a list of strings containing
        current register values and other debug info
        """
        debug_strings = []
        debug_strings.append(f"program counter: {self.program_counter:#06x}")
        debug_strings.append(f"index register: {self.index_register:#06x}")
        debug_strings.append(f"word: {self._current_word:#06x}")
        debug_strings.append(f"op: {self._current_operation.__class__.__name__}")
        debug_strings.append(f"sound timer: {self.sound_timer:#06x}")
        debug_strings.append(f"delay timer: {self.delay_timer:#06x}")

        for i in range(16):
            debug_strings.append(f"register V{i}: {self.general_purpose_registers[i]:#06x}")

        return debug_strings

    def _load_font(self):
        offset = 0x0
        for item in Font.DATA:
            self.ram[offset] = item
            offset += 1
