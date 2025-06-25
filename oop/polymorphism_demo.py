# polymorphism_demo.py

import math

class Shape:
    """
    Base class for geometric shapes.
    """
    def area(self):
        """
        Calculates the area of the shape. This method must be overridden by derived classes.
        """
        raise NotImplementedError("Subclasses must implement the 'area' method.")

class Rectangle(Shape):
    """
    Derived class representing a rectangle, inheriting from Shape.
    """
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """
        Overrides the area() method to calculate the rectangle's area.
        """
        return self.length * self.width

class Circle(Shape):
    """
    Derived class representing a circle, inheriting from Shape.
    """
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """
        Overrides the area() method to calculate the circle's area.
        """
        return math.pi * (self.radius ** 2)