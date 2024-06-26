from collections import defaultdict, deque

def all_topological_sorts(graph):
    def backtrack(path):
        if len(path) == len(graph):
            result.append(list(path))
            return

        for node in list(in_degree_zero):
            # Choose
            in_degree_zero.remove(node)
            path.append(node)

            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    in_degree_zero.add(neighbor)

            # Explore
            backtrack(path)

            # Unchoose
            for neighbor in graph[node]:
                if in_degree[neighbor] == 0:
                    in_degree_zero.remove(neighbor)
                in_degree[neighbor] += 1

            path.pop()
            in_degree_zero.add(node)

    in_degree = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1

    in_degree_zero = {node for node in graph if in_degree[node] == 0}
    result = []
    backtrack([])

    return result

# Define the graph
graph = {
    'a': [],
    'b': ['a', 'd', 'e', 'c'],
    'c': ['e'],
    'd': ['a', 'e'],
    'e': [],
    'f': ['c', 'e']
    # 'g': ['c', 'f']
}

# Find all topological sorts
all_sorts = all_topological_sorts(graph)
print(f"All possible topological orders ({len(all_sorts)}):")
for sort in all_sorts:
    print(sort)
