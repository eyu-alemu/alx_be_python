def safe_divide(numerator, denominator):
    """
    Safely divide two values, handling:
    - Non-numeric inputs
    - Division by zero
    """

    # Attempt numeric conversion
    try:
        num = float(numerator)
        den = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."

    # Attempt division
    try:
        result = num / den
        return f"The result of the division is {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."


#!/usr/bin/env python3
import sys
from robust_division_calculator import safe_divide

def main():
    # Expect exactly 2 arguments: numerator and denominator
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)

    numerator = sys.argv[1]
    denominator = sys.argv[2]

    # Call the safe division function
    result = safe_divide(numerator, denominator)
    print(result)

if __name__ == "__main__":
    main()
