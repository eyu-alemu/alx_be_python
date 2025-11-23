# arithmetic_operations.py

def perform_operation(num1: float, num2: float, operation: str):
    
    op = operation.strip().lower()

    if op == 'add':
        return num1 + num2
    elif op == 'subtract':
        return num1 - num2
    elif op == 'multiply':
        return num1 * num2
    elif op == 'divide':
        # Handle division by zero
        if num2 == 0:
            return "Error: Cannot divide by zero"
        return num1 / num2
    else:
        return f"Error: Invalid operation '{operation}'"
