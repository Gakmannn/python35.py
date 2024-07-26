import io
import os
from abc import ABC, abstractmethod

# Abstract base class for outputs
class Output(ABC):
    def __init__(self, data):
        self.data = data

    # Declare an abstract display method
    @abstractmethod
    def display(self):
        pass

# Console output implementation
class ConsoleOutput(Output):
    def display(self):
        print(f"{self.data}")

# File output implementation
class FileOutput(Output):
    def display(self):
        with open('output.txt', 'w') as f:
            f.write(self.data)

# Create a ConsoleOutput object and display
obj = ConsoleOutput("some string")
obj.display()

# Create a FileOutput object and display
obj2 = FileOutput("another string")
obj2.display()