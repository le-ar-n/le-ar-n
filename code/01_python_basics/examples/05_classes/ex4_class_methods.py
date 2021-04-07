import random
import math

# Rectangle class
class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # Classmethod, creates a class from a class function
    @classmethod
    def as_square(cls, length):
        return cls(length, length)

    def get_area(self):
        return self.length * self.width

# Creating an instance of the Rectangle class from the classmethod
sqr = Rectangle.as_square(length=2.43)
print("Rectangle area:", sqr.get_area())
