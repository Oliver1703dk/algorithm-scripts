import sys

def floyd_warshall(graph):
    # Number of vertices
    vertices = list(graph.keys())
    n = len(vertices)

    # Initialize distance matrix
    dist = {v: {u: float('inf') for u in vertices} for v in vertices}
    next_node = {v: {u: None for u in vertices} for v in vertices}

    # Set the distances based on the graph
    for v in vertices:
        dist[v][v] = 0
        for u, weight in graph[v]:
            dist[v][u] = weight
            next_node[v][u] = u

    print("Initial distance matrix:")
    print_distance_matrix(dist, vertices)

    # Floyd-Warshall algorithm
    for k in vertices:
        print(f"\nConsidering intermediate vertex {k}:")
        for i in vertices:
            for j in vertices:
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    print(f"Updating dist[{i}][{j}] from {dist[i][j]} to {dist[i][k] + dist[k][j]}")
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next_node[i][j] = next_node[i][k]
        print_distance_matrix(dist, vertices)

    return dist, next_node

def print_distance_matrix(dist, vertices):
    print("Distance matrix:")
    for i in vertices:
        for j in vertices:
            if dist[i][j] == float('inf'):
                print("inf", end=" ")
            else:
                print(f"{dist[i][j]:3}", end=" ")
        print()

# Example graph with weights
G = {
    'a': [('b', 3), ('c', 8), ('d', -4)],
    'b': [('e', 1), ('d', 7)],
    'c': [('b', 4)],
    'd': [('c', 2), ('e', 6)],
    'e': [('a', 2)]
}

# Run Floyd-Warshall algorithm
dist, next_node = floyd_warshall(G)

# Print the final distance matrix
print("\nFinal distance matrix:")
print_distance_matrix(dist, list(G.keys()))
