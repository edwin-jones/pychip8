from numpy import uint8 as byte

class DrawSprite:

    def execute(self, opcode, cpu):

        cpu.should_draw = True
        cpu.clear_arithmetic_flag()

        x = cpu.general_purpose_registers[opcode.x]
        y = cpu.general_purpose_registers[opcode.y]

        height = opcode.n

        for current_row_offset in range(height):

            row = y + current_row_offset
            new_pixels = cpu.ram[cpu.index_register + current_row_offset]

            for x_offset in range(8):

                mask = 128 >> x_offset

                column = x + x_offset

                # make sure x and y wrap around and don't go out of bounds!
                column %= 64
                row %= 32
                
                old_bit = cpu.frame_buffer[column][row]
                new_bit = bool(new_pixels & mask)
                bit_value = old_bit ^ new_bit
                cpu.frame_buffer[column][row] = True if bit_value else False

                if old_bit and new_bit:
                    cpu.set_arithmetic_flag()

