import numpy as np


def convert_to_adjacency_matrix(graph):
    nodes = list(graph.keys())
    num_nodes = len(nodes)
    node_index = {node: idx for idx, node in enumerate(nodes)}

    # Initialize adjacency matrix with infinity
    adj_matrix = np.full((num_nodes, num_nodes), np.inf)

    # Distance from a node to itself is 0
    np.fill_diagonal(adj_matrix, 0)

    # Fill the adjacency matrix with weights
    for node, edges in graph.items():
        for edge in edges:
            adj_matrix[node_index[node]][node_index[edge[0]]] = edge[1]

    return adj_matrix, nodes


def floyd_warshall(graph):
    """
    Implements the Floyd-Warshall algorithm and describes each relaxation step.

    Parameters:
    graph (dict): A dictionary representing the graph.

    Returns:
    dist (2D numpy array): The matrix of shortest paths between every pair of vertices.
    nodes (list): The list of nodes in the graph.
    """
    adj_matrix, nodes = convert_to_adjacency_matrix(graph)
    num_vertices = len(nodes)

    # Initialize the distance matrix with the adjacency matrix
    dist = adj_matrix.copy()

    # Run the Floyd-Warshall algorithm
    for k in range(num_vertices):
        print(f"\nConsidering intermediate vertex {nodes[k]} ({k + 1}/{num_vertices}):\n")
        for i in range(num_vertices):
            for j in range(num_vertices):
                if dist[i, j] > dist[i, k] + dist[k, j]:
                    print(f"Relaxing edge ({nodes[i]}, {nodes[j]}) using vertex {nodes[k]}:")
                    print(
                        f"dist[{nodes[i]}][{nodes[j]}] ({dist[i, j]}) > dist[{nodes[i]}][{nodes[k]}] ({dist[i, k]}) + dist[{nodes[k]}][{nodes[j]}] ({dist[k, j]})")
                    dist[i, j] = dist[i, k] + dist[k, j]
                    print(f"Updated dist[{nodes[i]}][{nodes[j]}] to {dist[i, j]}")
                else:
                    print(f"No relaxation needed for edge ({nodes[i]}, {nodes[j]}) using vertex {nodes[k]}:")
                    print(
                        f"dist[{nodes[i]}][{nodes[j]}] ({dist[i, j]}) <= dist[{nodes[i]}][{nodes[k]}] ({dist[i, k]}) + dist[{nodes[k]}][{nodes[j]}] ({dist[k, j]})")

        print("\nDistance matrix after considering vertex", nodes[k], ":\n", dist)

    return dist, nodes


# Example usage
if __name__ == "__main__":
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

    dist, nodes = floyd_warshall(G)

    print("\nFinal distance matrix:")
    print(dist)

    # Print the matrix with node labels for better readability
    print("\nDistance matrix with node labels:")
    dist_matrix_with_labels = pd.DataFrame(dist, index=nodes, columns=nodes)
    print(dist_matrix_with_labels)
