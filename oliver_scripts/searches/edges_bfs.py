from collections import deque, defaultdict

def bfs_classification(graph):
    discovery_time = {}
    parent = {}
    classification = {
        "tree_edges": [],
        "cross_edges": []
    }

    def bfs_visit(start):
        queue = deque([start])
        discovery_time[start] = 0
        parent[start] = None
        current_time = 0

        while queue:
            node = queue.popleft()
            current_time += 1
            for neighbor in graph[node]:
                if neighbor not in discovery_time:
                    discovery_time[neighbor] = current_time
                    parent[neighbor] = node
                    classification["tree_edges"].append((node, neighbor))
                    queue.append(neighbor)
                elif parent[node] != neighbor:
                    classification["cross_edges"].append((node, neighbor))

    for node in graph:
        if node not in discovery_time:
            bfs_visit(node)

    return classification


# Given graph
G = {
    "A": ["D", "G"],
    "B": ["C"],
    "C": ["B", "F"],
    "D": ["E", "G"],
    "E": ["A", "D"],
    "F": ["B", "G"],
    "G": ["B", "H", "I"],
    "H": ["D", "F", "G"],
    "I": ["A", "G"]
}

# Find edge classifications
edge_classifications = bfs_classification(G)

# Print the results
print("Tree edges:", edge_classifications["tree_edges"])
print("Cross edges:", edge_classifications["cross_edges"])
