# Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        temperature_input = input("Enter the temperature value: ")
        temperature = float(temperature_input)  # Validate numeric input

        unit = input("Is this in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == "F":
            converted = convert_to_celsius(temperature)
            print(f"{temperature}°F is equal to {converted:.2f}°C")
        elif unit == "C":
            converted = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is equal to {converted:.2f}°F")
        else:
            raise ValueError("Invalid temperature unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    except ValueError as e:
        print("Invalid temperature. Please enter a numeric value.")

if _name_ == "_main_":
    main()