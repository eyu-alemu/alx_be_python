# arithmetic_operations.py

def perform_operation(num1, num2, operation):
    """
    Perform a basic arithmetic operation on two numbers.

    Args:
        num1 (float): first number
        num2 (float): second number
        operation (str): one of "add", "subtract", "multiply", "divide"

    Returns:
        float or str: result of the operation, or an error message for divide-by-zero or invalid operation
    """
    op = operation.strip().lower()

    if op == "add":
        return num1 + num2
    elif op == "subtract":
        return num1 - num2
    elif op == "multiply":
        return num1 * num2
    elif op == "divide":
        # divide-by-zero handling
        if num2 == 0:
            return "Error: Cannot divide by zero"
        return num1 / num2
    else:
        return "Error: Invalid operation"
