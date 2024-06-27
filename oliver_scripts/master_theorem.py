import sympy as sp

def master_theorem(a, b, f_n):
    n = sp.symbols('n')

    # Convert f(n) to a sympy expression
    f_n = sp.sympify(f_n)

    # Calculate log_b(a)
    log_b_a = sp.log(a, b)

    # Extract the leading term of f(n)
    leading_term = f_n.as_leading_term(n)

    # Get the exponent c from the leading term
    if leading_term.is_polynomial(n):
        c = leading_term.as_coeff_exponent(n)[1]
    elif leading_term.is_Mul or leading_term.is_Pow:
        poly_part = 1
        log_part = 1
        for term in leading_term.args:
            if term.is_polynomial(n):
                poly_part *= term
            elif term.has(sp.log(n)):
                log_part *= term
        if poly_part != 1:
            c = poly_part.as_coeff_exponent(n)[1]
        else:
            c = None
    else:
        c = None

    # Case 1: f(n) = O(n^c) where c < log_b_a
    if c is not None and c < log_b_a:
        result = sp.O(n ** log_b_a)
        case = "Case 1"

    # Case 2: f(n) = Theta(n^c) where c = log_b_a
    elif c is not None and c == log_b_a:
        if f_n.has(sp.log(n)):
            log_factor = f_n / (n ** c)
            log_exponent = 0
            if log_factor.is_Mul:
                for term in log_factor.args:
                    if term.has(sp.log(n)):
                        log_exponent += term.as_coeff_exponent(sp.log(n))[1]
            elif log_factor.has(sp.log(n)):
                log_exponent += log_factor.as_coeff_exponent(sp.log(n))[1]

            if log_exponent == 1:
                result = sp.O(n ** log_b_a * sp.log(n))
                case = "Case 2"
            else:
                result = sp.O(n ** log_b_a)
                case = "Case 2"
        else:
            result = sp.O(n ** log_b_a * sp.log(n))
            case = "Case 2"

    # Case 3: f(n) = Omega(n^c) where c > log_b_a
    elif c is not None and c > log_b_a:
        # Check if af(n/b) <= kf(n) for some k < 1
        lhs = a * f_n.subs(n, n / b)
        rhs = f_n
        if sp.simplify(lhs / rhs).limit(n, sp.oo) < 1:
            result = sp.O(f_n)
            case = "Case 3"
        else:
            result = "Master Theorem does not apply"
            case = "None"
    else:
        # For logarithmic or other non-polynomial functions
        if f_n.has(sp.log(n)):
            if log_b_a == 0:
                result = sp.O(sp.log(n))
                case = "Special Case: log(n)"
            else:
                result = "Master Theorem does not apply"
                case = "None"
        else:
            result = "Master Theorem does not apply"
            case = "None"

    return result, case

# Example usage
a = 4
b = 3
f_n = 'n*log(n)'

result, case = master_theorem(a, b, f_n)
print(f"Result: {result}")
print(f"Case: {case}")
