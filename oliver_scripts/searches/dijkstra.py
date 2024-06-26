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

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        # Skip nodes that have already been processed
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            # Only consider this new path if it's better
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))

    return distances, previous_nodes

def shortest_path(graph, start, end):
    distances, previous_nodes = dijkstra(graph, start)
    path = []
    current_node = end

    while current_node is not None:
        path.append(current_node)
        current_node = previous_nodes[current_node]

    path = path[::-1]  # Reverse the path to get the correct order
    return path, distances[end]

# Example graph with weights
G = {
    'a': [('d', 1), ('g', 2)],
    'b': [('c', 2), ('g', 1)],
    'c': [('b', 2)],
    'd': [('a', 1), ('e', 1), ('g', 2), ('h', 1)],
    'e': [('d', 1)],
    'f': [('b', 3), ('g', 1), ('h', 2)],
    'g': [('a', 2), ('b', 1), ('d', 2), ('f', 1), ('h', 2), ('i', 3)],
    'h': [('d', 1), ('f', 2), ('g', 2)],
    'i': [('a', 4), ('g', 3)]
}

# Find the shortest path from 'a' to 'i'
path, distance = shortest_path(G, 'a', 'i')

# Print the results
print(f"The shortest path from 'a' to 'i' is: {path} with total distance {distance}")
