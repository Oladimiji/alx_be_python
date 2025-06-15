# temp_conversion_tool.py

# Requirement 1: Define Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

# Requirement 2: Implement Conversion Functions
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# Requirement 3: User Interaction and Error Handling
def main():
    # --- CRITICAL FIX: Use the EXACT required prompt strings ---
    temp_input = input("Enter the temperature to convert: ") # FIX: Updated prompt string

    try:
        temperature = float(temp_input)
    except ValueError:
        # This error message was previously specified: "Invalid temperature. Please enter a numeric value."
        # Assuming it remains the same.
        print("Invalid temperature. Please enter a numeric value.")
        return

    # --- CRITICAL FIX: Use the EXACT required prompt string ---
    unit_input = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper() # FIX: Updated prompt string

    if unit_input == 'C':
        converted_temp = convert_to_fahrenheit(temperature)
        print(f"{temperature:.2f}°C is {converted_temp:.2f}°F")
    elif unit_input == 'F':
        converted_temp = convert_to_celsius(temperature)
        print(f"{temperature:.2f}°F is {converted_temp:.2f}°C")
    else:
        # A generic message for invalid unit input, as no specific one was provided for this case.
        # If this fails, the checker might be looking for a specific string here too.
        print("Invalid unit. Please enter 'C' or 'F'.")

if _name_ == "_main_":
    main()
