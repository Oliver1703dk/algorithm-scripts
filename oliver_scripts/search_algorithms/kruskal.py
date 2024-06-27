class DisjointSet:
    def __init__(self, vertices):
        self.parent = {}
        self.rank = {}

        for vertex in vertices:
            self.parent[vertex] = vertex
            self.rank[vertex] = 0

    def find(self, item):
        if self.parent[item] == item:
            return item
        else:
            self.parent[item] = self.find(self.parent[item])  # Path compression
            return self.parent[item]

    def union(self, set1, set2):
        root1 = self.find(set1)
        root2 = self.find(set2)

        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1

def kruskal(graph):
    mst = []
    edges = []

    # Step 1: Sort all edges in non-decreasing order of their weight
    for node in graph:
        for neighbor, weight in graph[node]:
            edges.append((weight, node, neighbor))

    edges.sort()

    disjoint_set = DisjointSet(graph.keys())

    print("Step-by-step description of Kruskal's algorithm:")

    for edge in edges:
        weight, node1, node2 = edge
        print(f"Considering edge {node1}-{node2} with weight {weight}")

        # Step 2: Check if it forms a cycle with the spanning tree formed so far
        root1 = disjoint_set.find(node1)
        root2 = disjoint_set.find(node2)

        if root1 != root2:
            print(f"Adding edge {node1}-{node2} to the MST")
            mst.append(edge)
            disjoint_set.union(node1, node2)
        else:
            print(f"Skipping edge {node1}-{node2} as it forms a cycle")

        print(f"Current MST: {mst}\n")

    return mst

# Example graph with weights
# G = {
#     'a': [('b', 4), ('c', 3), ('d', 4)],
#     'b': [('a', 1), ('c', 2), ('e', 2)],
#     'c': [('a', 3), ('b', 2), ('f', 5)],
#     'd': [('a', 4), ('f', 3)],
#     'e': [('b', 2), ('f', 4)],
#     'f': [('c', 5), ('d', 3), ('e', 4)]
# }


G = {
    'a': [('b', 4), ('f', 3)],
    'b': [('a', 4), ('f', 5), ('g', 2), ('c', 1)],
    'c': [('b', 1), ('g', 6), ('h', 9), ('d', 8)],
    'd': [('c', 8), ('h', 6), ('i', 7), ('e', 7)],
    'e': [('i', 1), ('d', 7)],
    'f': [('a', 3), ('b', 5), ('g', 8)],
    'g': [('f', 8), ('b', 2), ('c', 6)],
    'h': [('c', 9), ('d', 6), ('i', 9)],
    'i': [('h', 9), ('d', 7), ('e', 1)]
}



# Run Kruskal's algorithm
mst = kruskal(G)

# Print the final MST
print("\nFinal Minimum Spanning Tree:")
for weight, node1, node2 in mst:
    print(f"Edge {node1}-{node2} with weight {weight}")
