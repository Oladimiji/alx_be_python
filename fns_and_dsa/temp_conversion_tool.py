# Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    temp_input = input("Enter temperature: ")
    unit = input("Enter unit (C for Celsius, F for Fahrenheit): ").strip().upper()

    try:
        temperature = float(temp_input)
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")
        return

    if unit == 'C':
        result = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {result:.2f}°F")
    elif unit == 'F':
        result = convert_to_celsius(temperature)
        print(f"{temperature}°F is {result:.2f}°C")
    else:
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

if _name_ == "_main_":
    main()
