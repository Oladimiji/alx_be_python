# main.py

from polymorphism_demo import Shape, Rectangle, Circle
import math # Although math is imported in polymorphism_demo, it's good practice to import it here if used directly.

def main():
    shapes = [
        Rectangle(10, 5),
        Circle(7)
    ]

    for shape in shapes:
        print(f"The area of the {shape.__class.name__} is: {shape.area()}")

if __name__ == "__main__":
    main()