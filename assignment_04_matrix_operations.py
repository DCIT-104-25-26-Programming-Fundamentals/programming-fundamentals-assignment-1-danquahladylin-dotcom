# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================


def print_matrix(matrix):
    """Utility function to print a matrix in a neat grid format."""
    for row in matrix:
        for val in row:
            print(f"{val:>4}", end=" ")
        print()
    print()


def transpose_matrix(matrix):
    """Part A: Transposes an M x N matrix into an N x M matrix."""
    rows = len(matrix)
    cols = len(matrix[0])

    # Create an empty N x M matrix initialized with zeros
    transposed = [[0 for _ in range(rows)] for _ in range(cols)]

    # Swap rows and columns using nested loops
    for r in range(rows):
        for c in range(cols):
            transposed[c][r] = matrix[r][c]

    return transposed


def add_matrices(matrix_a, matrix_b):
    """Part B: Computes the element-wise sum of two M x N matrices."""
    rows = len(matrix_a)
    cols = len(matrix_a[0])

    result = [[0 for _ in range(cols)] for _ in range(rows)]

    for r in range(rows):
        for c in range(cols):
            result[r][c] = matrix_a[r][c] + matrix_b[r][c]

    return result


def multiply_matrices(matrix_a, matrix_b):
    """Part C: Multiplies Matrix A (M x N) by Matrix B (N x P) -> Result (M x P)."""
    m = len(matrix_a)
    n = len(matrix_a[0])  # Must equal len(matrix_b)
    p = len(matrix_b[0])

    # Result matrix will be M x P initialized to 0
    result = [[0 for _ in range(p)] for _ in range(m)]

    # Triple nested loop for matrix multiplication
    for i in range(m):
        for j in range(p):
            for k in range(n):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]

    return result


def read_matrix(rows, cols, name="Matrix"):
    """Helper function to read matrix rows from user input on a single line."""
    print(f"\nEnter values for {name} ({rows}x{cols}):")
    matrix = []
    for r in range(rows):
        while True:
            row_input = input(f"Enter row {r + 1}: ").strip().split()
            if len(row_input) == cols:
                try:
                    row = [float(x) if "." in x else int(x) for x in row_input]
                    matrix.append(row)
                    break
                except ValueError:
                    print("Error: All items must be valid numbers.")
            else:
                print(f"Error: Expected exactly {cols} values.")
    return matrix


def main():
    try:
        # --- PART A: Transpose ---
        print("=== PART A: Transpose a Matrix ===")
        m = int(input("Enter number of rows: "))
        n = int(input("Enter number of columns: "))
        if m <= 0 or n <= 0:
            print("Error: Dimensions must be positive integers.")
            return

        mat_a = read_matrix(m, n, "Original Matrix")

        print("\nOriginal Matrix:")
        print_matrix(mat_a)

        transposed = transpose_matrix(mat_a)
        print("Transposed Matrix:")
        print_matrix(transposed)

        # --- PART B: Addition ---
        print("=== PART B: Add Two Matrices (Same Dimensions) ===")
        print(f"Reading Matrix B of size {m}x{n}...")
        mat_b = read_matrix(m, n, "Matrix B")

        added = add_matrices(mat_a, mat_b)
        print("\nSum of Matrix A + Matrix B:")
        print_matrix(added)

        # --- PART C: Multiplication ---
        print("=== PART C: Multiply Two Matrices ===")
        p = int(input(f"For Matrix C (size {n} x P), enter number of columns P: "))
        if p <= 0:
            print("Error: Dimension must be a positive integer.")
            return

        mat_c = read_matrix(n, p, "Matrix C")

        print("\nMatrix A:")
        print_matrix(mat_a)

        print("Matrix C:")
        print_matrix(mat_c)

        product = multiply_matrices(mat_a, mat_c)
        print(f"Product Matrix A × C ({m}x{p}):")
        print_matrix(product)

    except ValueError:
        print("Error: Invalid numerical input.")


if __name__ == "__main__":
    main()

