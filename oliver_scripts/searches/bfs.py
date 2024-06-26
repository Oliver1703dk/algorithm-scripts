from collections import deque


def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()

        if node not in visited:
            print(node)  # Print the current node
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)


# Given graph
G = {
    "a": ["d", "g"],
    "b": ["c", "g"],
    "c": ["b"],
    "d": ["a", "e", "g", "h"],
    "e": ["d"],
    "f": ["b", "g", "h"],
    "g": ["a", "b", "d", "f", "h", "i"],
    "h": ["d", "f", "g"],
    "i": ["a", "g"]
}

# Start BFS from node 'a'
bfs(G, 'a')
