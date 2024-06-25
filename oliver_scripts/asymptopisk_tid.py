import sympy as sp


def analyze_algorithm():
    n = sp.symbols('n', integer=True)
    i, j = 1, 1
    operations = 0

    while i <= n:
        operations += 1  # Count the outer loop operation
        i += 5
        while j < i:
            operations += 1  # Count the inner loop operation
            j += 1

    print(f"Total operations: {operations}")

    # Define symbolic variables
    n = sp.symbols('n', integer=True)

    # Compute the upper bound (Big O)
    big_o = sp.O(operations, n)
    print(f"Big O: {big_o}")

    # Compute the lower bound (Omega)
    omega = sp.Omega(operations, n)
    print(f"Omega: {omega}")

    # Compute the tight bound (Theta)
    theta = sp.Order(operations, n)
    print(f"Theta: {theta}")


# Example usage
analyze_algorithm()
