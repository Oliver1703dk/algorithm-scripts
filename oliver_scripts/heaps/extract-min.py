import heapq

def extract_min(heap):
    if not heap:
        return None  # Return None if the heap is empty
    return heapq.heappop(heap)


# Function to convert list into a min-heap
def build_min_heap(data):
    min_heap = [x for x in data]
    heapq.heapify(min_heap)
    return min_heap


# Example usage
if __name__ == "__main__":
    # This is a min-heap
    heap = [2, 3, 7, 10, 9, 8, 5]
    min_heap = build_min_heap(heap)
    # heapq.heapify(heap)  # Ensure the list is a heap
    print(f"Initial heap: {heap}")

    min_value = extract_min(heap)
    print(f"The extracted minimum value is: {min_value}")
    print(f"Heap after extracting minimum: {heap}")
