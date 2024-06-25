from collections import deque

def bfs(graph, start):
    queue = deque([start])
    distances = {node: None for node in graph}
    distances[start] = 0

    while queue:
        current = queue.popleft()
        for neighbor in sorted(graph[current]):
            if distances[neighbor] is None:
                distances[neighbor] = distances[current] + 1
                queue.append(neighbor)
                # Check if the distance is 4
                if distances[neighbor] == 4:
                    return neighbor

    return None

# Define the graph based on the given image
graph = {
    'a': ['e'],
    'b': ['c'],
    'c': ['f', 'h'],
    'd': ['i', 'j'],
    'e': ['d', 'g', 'b'],
    'f': ['g'],
    'g': ['c'],
    'h': ['b'],
    'i': ['j'],
    'j': ['g']
}

start_node = 'a'
node_with_d_value_4 = bfs(graph, start_node)
print(f"The first node with d-value 4 is: {node_with_d_value_4}")
