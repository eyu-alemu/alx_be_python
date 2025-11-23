# Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5


def convert_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius using the global conversion factor.
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit using the global conversion factor.
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


def main():
    try:
        # Prompt user for temperature input
        temp_input = input("Enter the temperature to convert: ")

        # Validate numeric input
        if not temp_input.replace('.', '', 1).isdigit():
            raise ValueError(
                "Invalid temperature. Please enter a numeric value.")

        temperature = float(temp_input)

        # Prompt user for unit
        unit = input(
            "Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == "F":
            converted = convert_to_celsius(temperature)
            print(f"{temperature:.1f}°F is {converted:.6f}°C")
        elif unit == "C":
            converted = convert_to_fahrenheit(temperature)
            print(f"{temperature:.1f}°C is {converted:.1f}°F")
        else:
            raise ValueError(
                "Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    except ValueError as e:
        print(e)


# Run the program
if __name__ == "__main__":
    main()
