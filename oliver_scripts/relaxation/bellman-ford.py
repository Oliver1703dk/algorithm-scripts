class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.edges = []

    def add_edge(self, u, v, w):
        self.edges.append((u, v, w))

    def bellman_ford(self, start):
        # Initialize distances from start to all other vertices as INFINITE
        dist = {i: float('inf') for i in range(self.V)}
        dist[start] = 0
        steps = []

        # Step 1: Relax all edges |V| - 1 times.
        for i in range(self.V - 1):
            steps.append(f"Iteration {i+1}")
            for u, v, w in self.edges:
                steps.append(f"Checking edge ({u} -> {v}) with weight {w}")
                if dist[u] != float('inf') and dist[u] + w < dist[v]:
                    steps.append(f"Relaxing edge ({u} -> {v}), updating distance of vertex {v} from {dist[v]} to {dist[u] + w}")
                    dist[v] = dist[u] + w
                else:
                    steps.append(f"No relaxation performed for edge ({u} -> {v})")

        # Step 2: Check for negative-weight cycles.
        for u, v, w in self.edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                steps.append(f"Graph contains negative weight cycle due to edge ({u} -> {v})")
                raise ValueError("Graph contains negative weight cycle")

        return dist, steps


# Example usage
g = Graph(5)
g.add_edge(0, 1, -1)
g.add_edge(0, 2, 4)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 2)
g.add_edge(1, 4, 2)
g.add_edge(3, 2, 5)
g.add_edge(3, 1, 1)
g.add_edge(4, 3, -3)

distances, steps = g.bellman_ford(0)
for step in steps:
    print(step)
print("Vertex distances from source:", distances)
