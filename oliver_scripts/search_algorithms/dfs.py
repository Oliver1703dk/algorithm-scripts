def dfs(graph, start):
    discovery_time = {}
    visited = set()
    time = [0]  # Mutable container to keep track of time

    def dfs_visit(node):
        time[0] += 1
        discovery_time[node] = time[0]
        visited.add(node)
        print(f"Node {node} discovered at time {time[0]}")

        for neighbor in sorted(graph[node]):
            if neighbor not in visited:
                dfs_visit(neighbor)

    dfs_visit(start)
    return discovery_time


# Define the graph based on the given image
graph = {
    'a': ['b', 'e', 'f'],
    'b': ['c', 'f'],
    'c': ['d', 'g'],
    'd': [],
    'e': ['f'],
    'f': ['g'],
    'g': ['h'],
    'h': []
}

start_node = 'a'
discovery_times = dfs(graph, start_node)

# Print discovery times
print("\nDiscovery times:")
for node, time in discovery_times.items():
    print(f"Node {node}: {time}")

# Find the node with the highest discovery time
last_discovered_node = max(discovery_times, key=discovery_times.get)
print(f"\nThe last discovered node is: {last_discovered_node}")
