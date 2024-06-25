import heapq


def prims_algorithm(graph, start):
    mst = []
    visited = set()
    min_heap = [(0, start, None)]  # (cost, node, from_node)
    step = 0

    while min_heap:
        step += 1
        cost, node, from_node = heapq.heappop(min_heap)
        if node not in visited:
            visited.add(node)
            if from_node is not None:
                mst.append((from_node, node, cost))
                print(f"Step {step}: Added edge ({from_node}, {node}) with cost {cost} to MST.")
            else:
                print(f"Step {step}: Starting at node {node}.")

            print(f"Current MST: {mst}")
            print(f"Visited nodes: {visited}")
            print(f"Heap: {min_heap}\n")

            for neighbor, weight in graph[node].items():
                if neighbor not in visited:
                    heapq.heappush(min_heap, (weight, neighbor, node))
                    print(f"Step {step}: Adding edge ({node}, {neighbor}) with cost {weight} to heap.")

            print(f"Updated Heap: {min_heap}\n")

    return mst


# Define the graph based on the given image
graph = {
    'a': {'c': 11, 'f': 10, 'h': 2, 'i': 3},
    'b': {'c': 5, 'd': 13},
    'c': {'a': 11, 'b': 5, 'h': 9},
    'd': {'b': 13, 'h': 1},
    'e': {'f': 7, 'g': 8},
    'f': {'a': 10, 'e': 7, 'i': 4},
    'g': {'e': 8, 'i': 12},
    'h': {'a': 2, 'c': 9, 'd': 1, 'i': 6},
    'i': {'a': 3, 'f': 4, 'g': 12, 'h': 6}
}

start_node = 'a'
mst = prims_algorithm(graph, start_node)

print(f"Final Minimum Spanning Tree (edges with weights): {mst}")

# Find the last node added to the MST
last_edge = mst[-1]
last_node = last_edge[1]
print(f"\nThe last node added to the MST is: {last_node}")
