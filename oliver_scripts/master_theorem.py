import sympy as sp

def master_theorem(a, b, f_n):
    n = sp.symbols('n')

    # Convert f(n) to a sympy expression
    f_n = sp.sympify(f_n)

    # Calculate log_b(a)
    log_b_a = sp.log(a, b)

    # Get the exponent c from the leading term of f(n)
    c = f_n.as_leading_term(n).as_coeff_exponent(n)[1]

    # Case 1: f(n) = O(n^c) where c < log_b(a)
    if c < log_b_a:
        result = sp.O(n ** log_b_a)
        case = "Case 1"

    # Case 2: f(n) = Theta(n^c) where c = log_b(a)
    elif c == log_b_a:
        result = sp.O(n ** log_b_a * sp.log(n))
        case = "Case 2"

    # Case 3: f(n) = Omega(n^c) where c > log_b_a
    else:
        # Check if af(n/b) <= kf(n) for some k < 1
        lhs = a * f_n.subs(n, n / b)
        rhs = f_n
        if sp.simplify(lhs / rhs).limit(n, sp.oo) < 1:
            result = sp.O(f_n)
            case = "Case 3"
        else:
            result = "Master Theorem does not apply"
            case = "None"

    return result, case

# Example usage
a = 2
b = 3
f_n = 'n*(log(n))'

result, case = master_theorem(a, b, f_n)
print(f"Result: {result}")
print(f"Case: {case}")
