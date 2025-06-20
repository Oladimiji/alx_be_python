def safe_divide(numerator, denominator):
    """
    Performs division, handling potential errors like division by zero and non-numeric input.

    Args:
        numerator (str or float): The numerator for the division.
        denominator (str or float): The denominator for the division.

    Returns:
        str: An error message if an error occurs, or the result of the division.
    """
    try:
        num = float(numerator)
        den = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."

    try:
        result = num / den
        return f"The result of the division is {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."