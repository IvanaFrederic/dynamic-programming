class Graph:
    def __init__(self):
        self.vertices = {}
        self.edges = []

    def add_vertex(self, name):
        self.vertices[name] = len(self.vertices)

    def add_edge(self, start, end, weight):
        self.edges.append((start, end, weight))

    def bellman_ford(self, start):
        distances = {vertex: float('inf') for vertex in self.vertices}
        distances[start] = 0

        for _ in range(len(self.vertices) - 1):
            for start_vertex, end_vertex, weight in self.edges:
                if distances[start_vertex] + weight < distances[end_vertex]:
                    distances[end_vertex] = distances[start_vertex] + weight

        # Check for negative weight cycles
        for start_vertex, end_vertex, weight in self.edges:
            if distances[start_vertex] + weight < distances[end_vertex]:
                print("Graph contains a negative weight cycle. Bellman-Ford not applicable.")
                return None

        return distances

# Example usage:
g = Graph()
g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')
g.add_vertex('D')

g.add_edge('A', 'B', 5)
g.add_edge('A', 'C', 2)
g.add_edge('B', 'C', 1)
g.add_edge('B', 'D', -4)
g.add_edge('C', 'D', 3)

start_vertex = 'A'
distances = g.bellman_ford(start_vertex)

if distances is not None:
    print(f"Shortest distances from vertex {start_vertex}:")
    for vertex, distance in distances.items():
        print(f"To {vertex}: {distance}")
