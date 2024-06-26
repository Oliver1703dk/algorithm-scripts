from collections import deque

def bfs(graph, start, d_value):
    queue = deque([start])
    distances = {node: None for node in graph}
    distances[start] = 0

    while queue:
        current = queue.popleft()
        for neighbor in sorted(graph[current]):
            if distances[neighbor] is None:
                distances[neighbor] = distances[current] + 1
                queue.append(neighbor)
                print(f"Node: {neighbor}, Distance: {distances[neighbor]}")
                # Check if the distance is d_value
                if distances[neighbor] == d_value:
                    return neighbor

    return None

# Define the graph based on the given image
# graph = {
#     'a': ['e'],
#     'b': ['c'],
#     'c': ['f', 'h'],
#     'd': ['i', 'j'],
#     'e': ['d', 'g', 'b'],
#     'f': ['g'],
#     'g': ['c'],
#     'h': ['b'],
#     'i': ['j'],
#     'j': ['g']
# }

graph = {
    'a': ['b'],
    'b': ['f', 'g'],
    'c': ['b', 'g', 'd'],
    'd': ['h'],
    'e': ['i', 'd'],
    'f': ['g', 'a'],
    'g': [],
    'h': ['c', 'i'],
    'i': ['d']
    # 'j': ['g']
}


start_node = 'c'
d_value = 4
node_with_d_value = bfs(graph, start_node, d_value)
print(f"The first node with d-value {d_value} is: {node_with_d_value}")
