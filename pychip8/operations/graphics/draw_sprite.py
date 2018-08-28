from numpy import uint8 as byte

class DrawSprite:

    def _check_collision_flag(self, cpu, mask, current_pixels):
        current_bit_value = mask & current_pixels
        if(current_bit_value):
            cpu.set_arithmetic_flag()

    def _get_framebuffer_byte(self, cpu, current_pixels, new_pixels):
        result = 0

        for shift in range(0, 8):
            mask = (1 << shift)
            bit_value = mask & new_pixels
        
            if bit_value:
                result |= mask
                self._check_collision_flag(cpu, mask, current_pixels)
                
        return result

    def execute(self, opcode, cpu):
        cpu.clear_arithmetic_flag()

        x = opcode.x
        y = opcode.y
        height = opcode.n

        for current_row_offset in range(height):
            y_line = y + current_row_offset

            current_pixels = cpu.frame_buffer[x + y_line]
            new_pixels = cpu.ram[cpu.index_register + current_row_offset]

            result = self._get_framebuffer_byte(cpu, current_pixels, new_pixels)
            cpu.frame_buffer[x + y_line] = result
