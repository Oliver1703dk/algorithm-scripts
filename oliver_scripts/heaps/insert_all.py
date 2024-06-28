import heapq

class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, element):
        heapq.heappush(self.heap, element)

    def display(self):
        print("MinHeap:", self.heap)

class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, element):
        # Insert the negative of the element to simulate max heap
        heapq.heappush(self.heap, -element)

    def display(self):
        # Display the elements by converting them back to positive
        print("MaxHeap:", [-x for x in self.heap])

def main():
    # Create instances of MinHeap and MaxHeap
    min_heap = MinHeap()
    max_heap = MaxHeap()

    # Elements to be inserted
    elements = [10, 5, 3, 2, 8, 15, 20]

    # Insert elements into MinHeap
    for elem in elements:
        min_heap.insert(elem)
    min_heap.display()

    # Insert elements into MaxHeap
    for elem in elements:
        max_heap.insert(elem)
    max_heap.display()

if __name__ == "__main__":
    main()
