import sympy as sp

def check_exists(statement, variable, domain):
    for value in domain:
        if statement.subs(variable, value):
            return True
    return False

def check_forall(statement, variable, domain):
    for value in domain:
        if not statement.subs(variable, value):
            return False
    return True

def evaluate_quantified_statement(statement, quantifier_type, variables, domain):
    if quantifier_type == "forall":
        result = check_forall(statement, variables[0], domain)
    elif quantifier_type == "exists":
        result = check_exists(statement, variables[0], domain)
    else:
        result = None
    return result

def main():
    # Define the domain
    domain = range(-100, 101)  # You can change this range as needed

    # User input for quantified statements
    print("Enter your quantified statement:")
    print("Example: ∀a ∈ ℤ: a < 2*a or ∃a ∈ ℤ: a**2 + 1 == 82")
    print("Use ~ for negation, e.g., ~∀a ∈ ℤ: a < 2*a")

    user_input = input("Statement: ")

    # Handle negation
    negated = False
    if user_input.startswith('~'):
        negated = True
        user_input = user_input[1:].strip()

    # Parse user input
    quantifier, statement = user_input.split(':', 1)
    quantifier = quantifier.strip()
    statement = statement.strip()

    if quantifier.startswith("∀"):
        quantifier_type = "forall"
        variable_name = quantifier.split()[0][1:]
    elif quantifier.startswith("∃"):
        quantifier_type = "exists"
        variable_name = quantifier.split()[0][1:]
    else:
        print("Invalid input format")
        return

    # Define the variable
    variable = sp.symbols(variable_name, integer=True)

    # Convert the statement to a sympy expression
    statement_expr = sp.sympify(statement)

    # Handle negation by flipping the quantifier and negating the statement
    if negated:
        if quantifier_type == "forall":
            quantifier_type = "exists"
        elif quantifier_type == "exists":
            quantifier_type = "forall"
        statement_expr = ~statement_expr

    # Evaluate the statement
    result = evaluate_quantified_statement(statement_expr, quantifier_type, [variable], domain)

    # Print the result
    print(f"The statement '{user_input}' is {'True' if result else 'False'}")

if __name__ == "__main__":
    main()
