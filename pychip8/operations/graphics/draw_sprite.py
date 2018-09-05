from numpy import uint8 as byte

class DrawSprite:

    def execute(self, opcode, cpu):
        cpu.clear_arithmetic_flag()

        x = cpu.general_purpose_registers[opcode.x]
        y = cpu.general_purpose_registers[opcode.y]

        height = opcode.n

        for current_row_offset in range(height):

            y_line = y + current_row_offset
            new_pixels = cpu.ram[cpu.index_register + current_row_offset]

            for x_offset in range(8):

                mask = 128 >> x_offset

                new_x = x + x_offset
                new_x %= 63

                y_line %= 31
                
                old_bit = cpu.frame_buffer[new_x][y_line]
                new_bit = bool(new_pixels & mask)
                bit_value = old_bit ^ new_bit
                cpu.frame_buffer[new_x][y_line] = True if bit_value else False

                if old_bit and new_bit:
                    cpu.set_arithmetic_flag()

