# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 9
# =============================================================================
#
# TASK: Console-Based Simple Calculator
#
# Build a calculator program that runs in the console and performs basic
# arithmetic operations based on the user's input.
#
# -----------------------------------------------------------------------------
# OPERATIONS YOUR CALCULATOR MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Addition          ( + )    e.g.  10 + 3  =  13
#   2. Subtraction       ( - )    e.g.  10 - 3  =  7
#   3. Multiplication    ( * )    e.g.  10 * 3  =  30
#   4. Division          ( / )    e.g.  10 / 3  =  3.33
#   5. Modulus           ( % )    e.g.  10 % 3  =  1  (remainder)
#   6. Exponentiation    ( ** )   e.g.  2 ** 8  =  256
#   7. Quit
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ============================
#        SIMPLE CALCULATOR
#   ============================
#   1. Addition
#   2. Subtraction
#   3. Multiplication
#   4. Division
#   5. Modulus
#   6. Exponentiation
#   7. Quit
#   Select an operation (1-7):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Select an operation (1-7): 4
#   Enter first number : 10
#   Enter second number: 3
#   Result: 10 / 3 = 3.33
#
#   Select an operation (1-7): 4
#   Enter first number : 5
#   Enter second number: 0
#   Error: Cannot divide by zero.
#
#   Select an operation (1-7): 7
#   Goodbye!
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Each arithmetic operation MUST be written as its own function.
# - Use a loop so the calculator keeps running until the user selects Quit.
# - Division by zero must be caught and handled with a clear error message
#   (do NOT let the program crash).
# - Division results should be rounded to 2 decimal places.
# - Handle invalid menu choices gracefully.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 9
# =============================================================================


def show_menu():
    """Displays the calculator menu options."""
    print("\n============================")
    print("        SIMPLE CALCULATOR")
    print("============================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Quit")


def add(a, b):
    """Returns the sum of two numbers."""
    return a + b


def subtract(a, b):
    """Returns the difference of two numbers."""
    return a - b


def multiply(a, b):
    """Returns the product of two numbers."""
    return a * b


def divide(a, b):
    """Returns the quotient of two numbers rounded to 2 decimal places, or None on division by zero."""
    if b == 0:
        return None
    return round(a / b, 2)


def modulus(a, b):
    """Returns the remainder of division, or None on division by zero."""
    if b == 0:
        return None
    return a % b


def power(a, b):
    """Returns a raised to the power of b."""
    return a ** b


def get_two_numbers():
    """Helper function to prompt user for two numeric inputs."""
    num1 = float(input("Enter first number : "))
    num2 = float(input("Enter second number: "))
    return num1, num2


def format_num(val):
    """Helper to display integers cleanly without trailing .0 if whole."""
    return int(val) if val.is_integer() else val


def main():
    while True:
        show_menu()
        choice = input("Select an operation (1-7): ").strip()

        if choice == "7":
            print("Goodbye!")
            break

        if choice not in ("1", "2", "3", "4", "5", "6"):
            print("Error: Invalid choice. Please enter a number between 1 and 7.")
            continue

        try:
            a, b = get_two_numbers()
            disp_a, disp_b = format_num(a), format_num(b)

            if choice == "1":
                res = add(a, b)
                print(f"Result: {disp_a} + {disp_b} = {format_num(res)}")

            elif choice == "2":
                res = subtract(a, b)
                print(f"Result: {disp_a} - {disp_b} = {format_num(res)}")

            elif choice == "3":
                res = multiply(a, b)
                print(f"Result: {disp_a} * {disp_b} = {format_num(res)}")

            elif choice == "4":
                res = divide(a, b)
                if res is None:
                    print("Error: Cannot divide by zero.")
                else:
                    print(f"Result: {disp_a} / {disp_b} = {res}")

            elif choice == "5":
                res = modulus(a, b)
                if res is None:
                    print("Error: Cannot calculate modulus with zero.")
                else:
                    print(f"Result: {disp_a} % {disp_b} = {format_num(res)}")

            elif choice == "6":
                res = power(a, b)
                print(f"Result: {disp_a} ** {disp_b} = {format_num(res)}")

        except ValueError:
            print("Error: Please enter valid numerical values.")


if __name__ == "__main__":
    main()
