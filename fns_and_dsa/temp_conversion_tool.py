# Requirement 1: Define Global Conversion Factors
# These factors are accessible throughout the script.
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# Requirement 2: Implement Conversion Functions

def convert_to_celsius(fahrenheit):
    """
    Converts a temperature from Fahrenheit to Celsius using the global factor.

    Args:
        fahrenheit (float): The temperature in Fahrenheit.

    Returns:
        float: The temperature converted to Celsius.
    """
    # Use the global FAHRENHEIT_TO_CELSIUS_FACTOR
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Converts a temperature from Celsius to Fahrenheit using the global factor.

    Args:
        celsius (float): The temperature in Celsius.

    Returns:
        float: The temperature converted to Fahrenheit.
    """
    # Use the global CELSIUS_TO_FAHRENHEIT_FACTOR
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# Requirement 3: User Interaction and Error Handling
def main():
    """
    Handles user interaction, calls conversion functions, and displays results.
    Includes input validation for temperature and unit.
    """
    # Prompt for temperature input
    temp_input = input("Enter the temperature value: ")

    try:
        temperature = float(temp_input)
    except ValueError:
        # Exact error message as required
        print("Invalid temperature. Please enter a numeric value.")
        return # Exit the function if input is not a number

    # Prompt for unit input
    unit_input = input("Enter the unit (C for Celsius, F for Fahrenheit): ").strip().upper()

    if unit_input == 'C':
        # Convert Celsius to Fahrenheit
        converted_temp = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {converted_temp:.2f}°F")
    elif unit_input == 'F':
        # Convert Fahrenheit to Celsius
        converted_temp = convert_to_celsius(temperature)
        print(f"{temperature}°F is {converted_temp:.2f}°C")
    else:
        # Handle invalid unit input
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

if _name_ == "_main_":
    main()
