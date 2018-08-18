class SetIndexRegister():
    def execute(self, opcode, cpu):
        cpu.index_register = opcode.nnn