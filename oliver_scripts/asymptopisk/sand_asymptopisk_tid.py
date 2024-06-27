import math

def analyze_runtime(algorithm_code, n):
    # Setup the initial environment for the algorithm
    local_vars = {'n': n, 'iterations': 0}
    exec(algorithm_code, {}, local_vars)
    return local_vars['iterations']

def compute_asymptotic_runtime(iterations, n):
    log_n = math.log(n)
    log_n_squared = (math.log(n)) ** 2
    sqrt_n = math.sqrt(n)
    n_log_n = n * math.log(n)
    n_log_n_squared = n * (math.log(n)) ** 2
    n_squared = n ** 2
    n_cubed = n ** 3
    two_power_n = 2 ** n

    # Create a dictionary to store the complexity types
    complexity = {
        "Θ(1)": 1,
        "Θ(log n)": log_n,
        "Θ((log n)^2)": log_n_squared,
        "Θ(√n)": sqrt_n,
        "Θ(n)": n,
        "Θ(n log n)": n_log_n,
        "Θ(n(log n)^2)": n_log_n_squared,
        "Θ(n^2)": n_squared,
        "Θ(n^3)": n_cubed,
        "Θ(2^n)": two_power_n,
    }

    # Use the minimum absolute relative difference to determine the closest complexity class
    closest_complexity = min(complexity, key=lambda key: abs((iterations - complexity[key]) / iterations))

    return closest_complexity

# Example usage:
n = 1024
# algorithm_code = """
# iterations = 0
# i = n
# while i > 1:
#     j = i
#     while j < n:
#         j = j + 1
#         iterations += 1
#     i = i // 2
# """

# algorithm_code = """
# iterations = 0
# i = 1
# j = n
# while i < j:
#     i = i + 1
#     j = j - 1
#     iterations += 1
# """

algorithm_code = """
iterations = 0
i = 1
j = n
for i in range(1, n + 1):
        j = n - i
        while j < n:
            j += 1
            iterations += 1
"""

# algorithm_code = """
# iterations = 0
# i = n
# while i>1:
#     j = 1
#     while j < i:
#         j = 2 * j
#         iterations += 1
#     i = i - 1
# """

# algorithm_code = """
# iterations = 0
# i = 1
# while i<n:
#     j = i
#     while j > 1:
#         j = j / 2
#         iterations += 1
#     i = 2 * i
# """



"""
This code snippet demonstrates the correct way to use nested for loops and an if statement to perform a specific task.

for i in range(1, n+1):  
    for j in range(1, n+1):
        if i == j:
            for k in range(1, n+1):
                s += 1 
                iterations += 1  # Task: increment the iterations counter by 1

Explanation:
- The outer loop initializes and iterates the variable i from 1 to n. 
- The middle loop initializes and iterates the variable j from 1 to n for each iteration of i.
- The if statement checks if the current values of i and j are equal.
- If the condition i == j is true, the inner loop initializes and iterates the variable k from 1 to n.
- Inside the inner loop, the variable s is incremented by 1, and the iterations counter is also incremented by 1.
- This structure allows you to perform specific tasks whenever the condition i == j is met within the nested loops.
"""





iterations = analyze_runtime(algorithm_code, n)
asymptotic_runtime = compute_asymptotic_runtime(iterations, n)

print(f"For n = {n}, the algorithm runs {iterations} iterations.")
print(f"The asymptotic runtime is {asymptotic_runtime}.")