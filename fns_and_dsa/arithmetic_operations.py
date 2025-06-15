def perform_operation(num1, num2, operation):
    """
    Performs the specified arithmetic operation on num1 and num2.

    Args:
        num1 (float): The first number.
        num2 (float): The second number.
        operation (str): The operation to perform: "add", "subtract", "multiply", or "divide".

    Returns:
        float: The result of the arithmetic operation.

    Raises:
        ValueError: If an invalid operation is specified or division by zero occurs.
    """
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            raise ValueError("Cannot divide by zero.")
        return num1 / num2
    else:
        raise ValueError(f"Unsupported operation: {operation}")