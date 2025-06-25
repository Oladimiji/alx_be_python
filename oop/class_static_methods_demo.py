# class_static_methods_demo.py

class Calculator:
    """
    A class demonstrating the use of static and class methods.
    """
    # Class Attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Static Method: Returns the sum of two numbers.
        It does not require access to the class or instance.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Class Method: Returns the product of two numbers.
        It has access to class attributes via the 'cls' parameter.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
