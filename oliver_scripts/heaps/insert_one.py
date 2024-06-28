import heapq

class MinHeap:
    def __init__(self, heap=None):
        self.heap = heap or []
        heapq.heapify(self.heap)

    def insert(self, element):
        heapq.heappush(self.heap, element)

    def display(self):
        print("MinHeap:", self.heap)

class MaxHeap:
    def __init__(self, heap=None):
        self.heap = heap or []
        self.heap = [-elem for elem in self.heap]
        heapq.heapify(self.heap)

    def insert(self, element):
        heapq.heappush(self.heap, -element)

    def display(self):
        print("MaxHeap:", [-x for x in self.heap])

def main():
    # Existing heaps
    min_heap_elements = [10, 5, 3, 2, 8, 15, 20]
    max_heap_elements = [10, 5, 3, 2, 8, 15, 20]

    # Create instances of MinHeap and MaxHeap with existing elements
    min_heap = MinHeap(min_heap_elements)
    max_heap = MaxHeap(max_heap_elements)

    # Display the existing heaps
    min_heap.display()
    max_heap.display()

    # New element to be inserted
    new_element = 7

    # Insert the new element into both heaps
    min_heap.insert(new_element)
    max_heap.insert(new_element)

    # Display the heaps after insertion
    print("\nAfter inserting element:", new_element)
    min_heap.display()
    max_heap.display()

if __name__ == "__main__":
    main()
