# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 6
# Topic: Loops and Functions
# =============================================================================
#
# TASK: Multiplication Table Generator
#
# Write a Python program that generates multiplication tables using loops
# and functions.
#
# -----------------------------------------------------------------------------
# PART A — Single Table
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Print the multiplication table for that number from 1 to 12.
#
# Expected output (if user enters 5):
#
#   Multiplication Table for 5:
#   5  x  1  =  5
#   5  x  2  =  10
#   5  x  3  =  15
#   ...
#   5  x  12 =  60
#
# -----------------------------------------------------------------------------
# PART B — Bonus: Tables from 1 to N
# -----------------------------------------------------------------------------
# - Ask the user to enter a number N.
# - Print the full multiplication table for every number from 1 to N.
# - Add a separator line (e.g. "---") between each table.
#
# Expected output (if user enters 3):
#
#   Multiplication Table for 1:
#   1  x  1  =  1
#   ...
#   1  x  12 =  12
#   ---------------------------
#   Multiplication Table for 2:
#   2  x  1  =  2
#   ...
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - N must be a positive integer. If the user enters an invalid value,
#   print an error message and stop.
# - Each part must be in its own function (see scaffold below).
# - Complete Part A before attempting Part B.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 6
# Topic: Loops and Functions
# =============================================================================


def print_table(number):
    """Part A: Prints the multiplication table for a given number from 1 to 12."""
    print(f"\nMultiplication Table for {number}:")
    for i in range(1, 13):
        # Format aligned outputs nicely (e.g. 5  x  2 = 10)
        print(f"{number:<2} x {i:>2} = {number * i:>3}")


def print_all_tables(n):
    """Part B: Prints multiplication tables for every number from 1 to N."""
    for num in range(1, n + 1):
        print_table(num)
        if num < n:
            print("-" * 27)


def main():
    try:
        # --- PART A: Single Table ---
        print("=== PART A: Single Multiplication Table ===")
        num = int(input("Enter a number: "))

        if num <= 0:
            print("Error: Please enter a positive integer greater than 0.")
            return

        print_table(num)

        print("\n" + "=" * 40 + "\n")

        # --- PART B: Bonus (1 to N) ---
        print("=== PART B: Tables from 1 to N ===")
        n = int(input("Enter N (to print tables 1 through N): "))

        if n <= 0:
            print("Error: Please enter a positive integer greater than 0.")
            return

        print_all_tables(n)

    except ValueError:
        print("Error: Please enter a valid integer.")


if __name__ == "__main__":
    main()

