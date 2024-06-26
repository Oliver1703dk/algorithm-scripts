def dfs_classification(graph):
    time = [0]  # Keep track of the discovery and finishing times
    discovery_time = {}
    finishing_time = {}
    parent = {}
    classification = {
        "tree_edges": [],
        "back_edges": [],
        "forward_edges": [],
        "cross_edges": []
    }

    def dfs_visit(node):
        nonlocal time
        time[0] += 1
        discovery_time[node] = time[0]
        for neighbor in graph[node]:
            if neighbor not in discovery_time:
                parent[neighbor] = node
                classification["tree_edges"].append((node, neighbor))
                dfs_visit(neighbor)
            elif neighbor not in finishing_time:
                classification["back_edges"].append((node, neighbor))
            elif discovery_time[node] < discovery_time[neighbor]:
                classification["forward_edges"].append((node, neighbor))
            else:
                classification["cross_edges"].append((node, neighbor))
        time[0] += 1
        finishing_time[node] = time[0]

    for node in graph:
        if node not in discovery_time:
            parent[node] = None
            dfs_visit(node)

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
    "I": ["A", "B"]
}

# Find edge classifications
edge_classifications = dfs_classification(G)

# Print the results
print("Tree edges:", edge_classifications["tree_edges"])
print("Back edges:", edge_classifications["back_edges"])
print("Forward edges:", edge_classifications["forward_edges"])
print("Cross edges:", edge_classifications["cross_edges"])
