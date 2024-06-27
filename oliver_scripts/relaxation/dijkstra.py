import heapq

def dijkstra(graph, start):
    # Priority queue to store the nodes to be explored
    pq = []
    heapq.heappush(pq, (0, start))  # (distance, node)

    # Dictionary to store the shortest distance to each node
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Dictionary to store the previous node in the shortest path
    previous_nodes = {node: None for node in graph}

    # Set to store visited nodes
    visited = set()

    # Counter for relaxation changes
    relax_changes = 0

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        # Skip nodes that have already been processed
        if current_node in visited:
            continue

        visited.add(current_node)

        print(f"Processing node {current_node} with current distance {current_distance}")

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            # Only consider this new path if it's better
            if distance < distances[neighbor]:
                print(f"Relaxing edge {current_node} -> {neighbor} with weight {weight}")
                print(f"Updating distance of node {neighbor} from {distances[neighbor]} to {distance}")
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))
                relax_changes += 1

    return distances, previous_nodes, relax_changes

# Example graph with weights
# G = {
#     'a': [('b', 4), ('g', 7)],
#     'b': [('c', 1), ('d', 2)],
#     'c': [('a', 2), ('f', 6)],
#     'd': [('c', 1), ('f', 4)],
#     'e': [('c', 8)],
#     'f': [('e', 1)],
#     'g': [('c', 4), ('e', 6)],
#     'h': [('d', 1), ('f', 2), ('g', 2)],
#     'i': [('a', 4), ('g', 3)]
# }
G = {
    'a': [('b', 4), ('g', 7)],
    'b': [('c', 1), ('d', 2)],
    'c': [('a', 2), ('f', 6)],
    'd': [('c', 1), ('f', 4)],
    'e': [('c', 8)],
    'f': [('e', 1)],
    'g': [('c', 4), ('e', 6)]
}

# Start node
start_node = 'a'

# Run Dijkstra's algorithm
distances, previous_nodes, relax_changes = dijkstra(G, start_node)

# Print the results
print("\nFinal shortest distances from start node:")
for node, distance in distances.items():
    print(f"Node {node} has distance {distance}")

print(f"\nTotal number of relaxation changes: {relax_changes}")
