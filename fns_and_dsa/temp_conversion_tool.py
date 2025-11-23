# temp_conversion_tool.py

# Definition of global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5.0 / 9.0
CELSIUS_TO_FAHRENHEIT_FACTOR = 9.0 / 5.0


def convert_to_celsius(fahrenheit):
    """Convert a temperature from Fahrenheit to Celsius."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    """Convert a temperature from Celsius to Fahrenheit."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


def main():
    # User interaction
    temp_str = input("Enter the temperature to convert: ").strip()
    try:
        temp_value = float(temp_str)
    except ValueError:
        # Implementation of ValueError if user input is not a numeric value
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    unit = input(
        "Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
    if unit == 'F':
        resul
