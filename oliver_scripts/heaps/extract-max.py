import heapq

def extract_max(heap):
    if not heap:
        return None  # Return None if the heap is empty
    return -heapq.heappop(heap)

# Function to convert a list into a max-heap
def build_max_heap(data):
    max_heap = [-x for x in data]
    heapq.heapify(max_heap)
    return max_heap

# Example usage
if __name__ == "__main__":
    # This is a list that we will convert into a max-heap
    data = [5, 4, 3, 3, 4, 2, 3, 2, 1]
    max_heap = build_max_heap(data)
    print(f"Initial max-heap: {[-x for x in max_heap]}")

    max_value = extract_max(max_heap)
    print(f"The extracted maximum value is: {max_value}")
    print(f"Max-heap after extracting maximum: {[-x for x in max_heap]}")
