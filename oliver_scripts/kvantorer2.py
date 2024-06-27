from sympy import symbols, S, simplify
from sympy.logic.boolalg import And, Or, Not
from sympy.logic.inference import satisfiable
from sympy.core.relational import Relational
from sympy.abc import x


def parse_input(logic_input):
    # Parse quantifier type and logical expression
    if logic_input.startswith("∀"):
        quantifier = "universal"
    elif logic_input.startswith("¬∃"):
        quantifier = "negated_existential"
    else:
        raise ValueError("Unknown quantifier type.")

    # Extract the logical expression
    expression = logic_input.split(":")[1].strip()
    return quantifier, expression


def evaluate_expression(quantifier, expression):
    x = symbols('x', integer=True)
    expr = simplify(eval(expression.replace("^", "**")))

    if quantifier == "universal":
        # Evaluate universal quantifier
        condition = ForAll(x, expr)
    elif quantifier == "negated_existential":
        # Evaluate negated existential quantifier
        condition = Not(Exists(x, expr))

    return condition


def main():
    print("Enter your logical statement (e.g., ∀x ∈ ℤ: x^2 > 2x or ¬∃x ∈ ℤ: x^2 > 2x):")
    logic_input = input().strip()

    quantifier, expression = parse_input(logic_input)
    result = evaluate_expression(quantifier, expression)

    if satisfiable(Not(result)):
        print(f"The statement '{logic_input}' is False.")
    else:
        print(f"The statement '{logic_input}' is True.")


if __name__ == "__main__":
    main()
