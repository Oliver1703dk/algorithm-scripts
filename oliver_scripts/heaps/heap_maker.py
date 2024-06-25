import itertools



def __init__(self, data):
    self.data = data


def is_min_heap(data):
    # Check if the data satisfies min-heap properties
    n = len(data)
    for i in range((n - 2) // 2 + 1):
        if data[i] > data[2 * i + 1]:  # Check left child
            return False
        if 2 * i + 2 < n and data[i] > data[2 * i + 2]:  # Check right child
            return False
    return True


def is_max_heap(data):
    # Check if the data satisfies max-heap properties
    n = len(data)
    for i in range((n - 2) // 2 + 1):
        if data[i] < data[2 * i + 1]:  # Check left child
            return False
        if 2 * i + 2 < n and data[i] < data[2 * i + 2]:  # Check right child
            return False
    return True


def find_all_min_heaps():
    min_heaps = []
    for perm in itertools.permutations(data):
        if is_min_heap(perm):
            min_heaps.append(perm)
    return min_heaps


def find_all_max_heaps():
    max_heaps = []
    for perm in itertools.permutations(data):
        if is_max_heap(perm):
            max_heaps.append(perm)
    return max_heaps


# Example usage
if __name__ == "__main__":
    data = [2, 3, 5, 4, 7]


    min_heaps = find_all_min_heaps()
    print(f"All possible min-heaps for {data}:")
    for heap in min_heaps:
        print(heap)

    max_heaps = find_all_max_heaps()
    print(f"\nAll possible max-heaps for {data}:")
    for heap in max_heaps:
        print(heap)