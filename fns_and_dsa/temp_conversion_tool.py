# temp_conversion_tool.py

# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5.0 / 9.0
CELSIUS_TO_FAHRENHEIT_FACTOR = 9.0 / 5.0


def convert_to_celsius(fahrenheit):
    """
    Convert a temperature from Fahrenheit to Celsius using global factor.
    Formula: (°F - 32) * (5/9)
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    """
    Convert a temperature from Celsius to Fahrenheit using global factor.
    Formula: (°C * (9/5)) + 32
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


def main():
    # User interaction
    temp_str = input("Enter the temperature to convert: ").strip()
    try:
        temp_value = float(temp_str)
    except ValueError:
        # Raise ValueError if the input cannot be converted to float
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    unit = input(
        "Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
    if unit == 'F':
        result = convert_to_celsius(temp_value)
        print(f"{temp_value}°F is {result}°C")
    elif unit == 'C':
        result = convert_to_fahrenheit(temp_value)
        print(f"{temp_value}°C is {result}°F")
    else:
        # Raise ValueError if the unit is not C or F
        raise ValueError(
            "Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")


if __name__ == "__main__":
    main()
