def worst_case_time_complexity(algorithm, n):
    complexities = {
        "Selection Sort": lambda n: f"O({n}^2)",
        "Bubble Sort": lambda n: f"O({n}^2)",
        "Insertion Sort": lambda n: f"O({n}^2)",
        "Heap Sort": lambda n: f"O({n} log({n}))",
        "Quick Sort": lambda n: f"O({n}^2)",
        "Merge Sort": lambda n: f"O({n} log({n}))",
        "Bucket Sort": lambda n: f"O({n}^2)",  # Assuming bucket count is proportional to n
        "Radix Sort": lambda n: f"O(3 * ({n} + 10))",  # 3 digits in the range [0, n^3)
        "Count Sort": lambda n: f"O({n} + {n}^3)",  # k = n^3
        "Shell Sort": lambda n: f"O({n}^(3/2))",
        "Tim Sort": lambda n: f"O({n} log({n}))",
        "Tree Sort": lambda n: f"O({n}^2)",
        "Cube Sort": lambda n: f"O({n} log({n}))"
    }

    if algorithm in complexities:
        return complexities[algorithm](n)
    else:
        return "Algorithm not supported"

# Example usage:
n = 10  # You can change this value to test with different inputs

algorithms = [
    "Selection Sort", "Bubble Sort", "Insertion Sort", "Heap Sort",
    "Quick Sort", "Merge Sort", "Bucket Sort", "Radix Sort",
    "Count Sort", "Shell Sort", "Tim Sort", "Tree Sort", "Cube Sort"
]

for algorithm in algorithms:
    print(f"Worst-case time complexity for {algorithm} with n={n}: {worst_case_time_complexity(algorithm, n)}")
