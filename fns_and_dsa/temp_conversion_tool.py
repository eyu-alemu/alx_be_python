# temp_conversion_tool.py

# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5.0 / 9.0
CELSIUS_TO_FAHRENHEIT_FACTOR = 9.0 / 5.0


def convert_to_celsius(fahrenheit):
    """
    Convert a temperature from Fahrenheit to Celsius.
    Uses the global FAHRENHEIT_TO_CELSIUS_FACTOR.
    """
    # formula: °C = (°F − 32) × 5/9 :contentReference[oaicite:0]{index=0}
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    """
    Convert a temperature from Celsius to Fahrenheit.
    Uses the global CELSIUS_TO_FAHRENHEIT_FACTOR.
    """
    # formula: °F = (°C × 9/5) + 32 :contentReference[oaicite:1]{index=1}
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


def main():
    try:
        temp_input = float(input("Enter the temperature to convert: ").strip())
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    unit = input(
        "Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
    if unit == 'F':
        result = convert_to_celsius(temp_input)
        print(f"{temp_input}°F is {result}°C")
    elif unit == 'C':
        result = convert_to_fahrenheit(temp_input)
        print(f"{temp_input}°C is {result}°F")
    else:
        raise ValueError(
            "Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")


if __name__ == "__main__":
    main()
