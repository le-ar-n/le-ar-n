
import random
import math

# Base class
class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # Base class function
    def get_area(self):
        return self.length * self.width

# Square class based on the Rectangle class
class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length=length, width=length)

# Creating an instance of the Square class
sqr = Square(length=2.43)
# Class method from the base class can be accessed
print("Rectangle area:", sqr.get_area())
