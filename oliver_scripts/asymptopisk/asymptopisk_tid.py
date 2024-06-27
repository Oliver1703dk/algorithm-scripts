def count_iterations(n):
    counter = 0
    s = 0
    # for i in range(1, n+1):
    #     s = i + s
    #     counter += 1
    # return counter

    for i in range(1, n*n):
        for j in range(1, n):
            s = s + 1
            counter += 1
    return counter

    # i = 1
    # j = n
    # while i <= j:
    #     j = j - 1
    #     i = 2 * i
    #     counter += 1
    # return counter

    # i = n
    # s = 0
    # while i >= 1:
    #     for j in range(i, 2*i):
    #         s = s + 1
    #         counter = counter + 1
    #     i = i//2
    # return counter


# Example usage:
n = 100
iterations = count_iterations(n)
print(f"Number of iterations for n = {n}: {iterations}")
