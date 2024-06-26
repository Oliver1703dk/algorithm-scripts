def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)

    print(start)  # Print the current node

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


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

# Start DFS from node 'a'
dfs(G, 'A')
