from typing import List
from abc import ABC, abstractmethod

# Define an abstract base class for figures
class Figure(ABC):
    # Abstract method for calculating area
    @abstractmethod
    def calculate_area(self)->float:
        pass

# Rectangle class, a subtype of Figure
class Rectangle(Figure):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Concrete implementation of area calculation for rectangles
    def calculate_area(self):
        return self.width * self.height

# Square class, another subtype of Figure
class Square(Figure):
    def __init__(self, side):
        self.side = side

    # Concrete implementation of area calculation for squares
    def calculate_area(self):
        return self.side * self.side

# Function to calculate the total area of multiple figures
def calculate_total_area(figures:List[Figure]):
    total_area = 0
    for obj in figures:
        total_area += obj.calculate_area()
    return total_area

# Example usage
figures = [Rectangle(5,6),Square(10)]
print (calculate_total_area(figures))