from collections import defaultdict, deque

def kosaraju_scc(graph):
    def dfs_first(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs_first(neighbor)
        stack.append(node)

    def dfs_second(node, transposed_graph):
        visited.add(node)
        component.append(node)
        for neighbor in transposed_graph[node]:
            if neighbor not in visited:
                dfs_second(neighbor, transposed_graph)

    # Step 1: Perform DFS on the original graph and push nodes onto the stack in the order they finish.
    visited = set()
    stack = []

    for node in graph:
        if node not in visited:
            dfs_first(node)

    # Step 2: Reverse the graph.
    transposed_graph = defaultdict(list)
    for node in graph:
        for neighbor in graph[node]:
            transposed_graph[neighbor].append(node)

    # Step 3: Perform DFS on the reversed graph to find SCCs.
    visited.clear()
    sccs = []

    while stack:
        node = stack.pop()
        if node not in visited:
            component = []
            dfs_second(node, transposed_graph)
            sccs.append(component)

    return sccs

# Given graph
# G = {
#     "a": ["e", "d", "g"],
#     "b": ["c"],
#     "c": ["b"],
#     "d": ["e"],
#     "e": [],
#     "f": ["b", "g", "c"],
#     "g": ["b", "i", "d", "h"],
#     "h": ["d", "f", "g"],
#     "i": ["a", "b"]
# }

G = {
    "a": [],
    "b": ["a", "c", "f"],
    "c": ["d", "g"],
    "d": ["h"],
    "e": ["d", "i"],
    "f": ["a"],
    "g": ["f", "b"],
    "h": ["c"],
    "i": ["h", "d"]
}



# Find SCCs
sccs = kosaraju_scc(G)

# Print the results
print("Strongly connected components:")
for scc in sccs:
    print(scc)
