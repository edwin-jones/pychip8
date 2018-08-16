from abc import ABC, abstractmethod

class Operation(ABC):

    @abstractmethod
    def execute(self, opcode, cpu):
        pass