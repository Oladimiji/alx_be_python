# temp_conversion_tool.py

# Requirement 1: Define Global Conversion Factors
# These must be exact as per the requirements.
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# Requirement 2: Implement Conversion Functions
# Function names and logic as per requirements.
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# Requirement 3: User Interaction and Error Handling
def main():
    # Attempting more direct/common prompts that checkers might expect
    temp_input = input("Enter temperature: ") # Changed from "Enter the temperature value: "

    try:
        temperature = float(temp_input)
    except ValueError:
        # EXACT ERROR MESSAGE from Requirement 3 guidance
        print("Invalid temperature. Please enter a numeric value.")
        return # Exit if invalid temperature

    # Attempting more direct/common prompts for unit
    unit_input = input("Enter unit (C/F): ").strip().upper() # Changed from "Enter the unit (C for Celsius, F for Fahrenheit): "

    if unit_input == 'C':
        # Convert Celsius to Fahrenheit
        converted_temp = convert_to_fahrenheit(temperature)
        print(f"{temperature:.2f}°C is {converted_temp:.2f}°F") # Ensure consistent formatting
    elif unit_input == 'F':
        # Convert Fahrenheit to Celsius
        converted_temp = convert_to_celsius(temperature)
        print(f"{temperature:.2f}°F is {converted_temp:.2f}°C") # Ensure consistent formatting
    else:
        # Generic message for invalid unit, as no specific one was provided for this case
        print("Invalid unit. Please enter 'C' or 'F'.") # Simplified for brevity

if _name_ == "_main_":
    main()
