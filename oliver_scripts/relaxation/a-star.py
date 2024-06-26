import heapq


class Graph:
    def __init__(self):
        self.edges = {}
        self.weights = {}

    def add_edge(self, from_node, to_node, weight):
        if from_node not in self.edges:
            self.edges[from_node] = []
        self.edges[from_node].append(to_node)
        self.weights[(from_node, to_node)] = weight


def heuristic(node, goal):
    # Simple heuristic: Manhattan distance assuming nodes are single characters
    return abs(ord(node) - ord(goal))


def relax(node, neighbor, graph, costs, previous_nodes):
    if costs[neighbor] > costs[node] + graph.weights[(node, neighbor)]:
        costs[neighbor] = costs[node] + graph.weights[(node, neighbor)]
        previous_nodes[neighbor] = node
        return True
    return False


def a_star_algorithm(graph, start, goal):
    open_list = []
    heapq.heappush(open_list, (0, start))
    came_from = {}
    costs = {start: 0}
    f_scores = {start: heuristic(start, goal)}

    while open_list:
        current = heapq.heappop(open_list)[1]

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path, costs

        for neighbor in graph.edges.get(current, []):
            tentative_g_score = costs[current] + graph.weights[(current, neighbor)]

            if neighbor not in costs or tentative_g_score < costs[neighbor]:
                came_from[neighbor] = current
                costs[neighbor] = tentative_g_score
                f_scores[neighbor] = costs[neighbor] + heuristic(neighbor, goal)
                heapq.heappush(open_list, (f_scores[neighbor], neighbor))
                print(f"Relaxation: Node {neighbor} relaxed via {current}. New cost: {costs[neighbor]}")

    return None, costs


# Create the graph
graph = Graph()

# Add edges
graph.add_edge('A', 'B', 1)
graph.add_edge('A', 'C', 4)
graph.add_edge('B', 'C', 2)
graph.add_edge('B', 'D', 5)
graph.add_edge('C', 'D', 1)

# Define start and goal nodes
start = 'A'
goal = 'D'

# Run A* algorithm
path, costs = a_star_algorithm(graph, start, goal)
print("Path found:", path)
print("Costs:", costs)
