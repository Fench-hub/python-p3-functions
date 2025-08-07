 #!/usr/bin/env python3

def greet_programmer():
    """
    Outputs the string "Hello, programmer!" to the terminal.
    """
    print("Hello, programmer!")

def greet(name):
    """
    Outputs a personalized greeting to the terminal.

    Args:
        name (str): The name to be included in the greeting.
    """
    print(f"Hello, {name}!")

def greet_with_default(name="programmer"):
    """
    Outputs a greeting with a default name if no argument is provided.

    Args:
        name (str, optional): The name to be included in the greeting.
                               Defaults to "programmer".
    """
    print(f"Hello, {name}!")

def add(num1, num2):
    """
    Returns the sum of two numbers.

    Args:
        num1 (int or float): The first number.
        num2 (int or float): The second number.

    Returns:
        int or float: The sum of the two numbers.
    """
    return num1 + num2

def halve(number):
    """
    Returns half the value of a given number, or None if the input is not a number.

    Args:
        number (int or float): The number to be halved.

    Returns:
        float or None: Half of the input number, or None.
    """
    # Check if the number is an integer or a float
    if not isinstance(number, (int, float)):
        return None

    return number / 2
