class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = []

    def add_edge(self, start, end, weight):
        self.edges.append((start, end, weight))

    def bellman_ford(self, start, end):
        # Initialize distances array with infinity for all vertices except start
        distances = {vertex: float('inf') for vertex in range(self.vertices)}
        distances[start] = 0

        # Relax edges repeatedly to find the shortest paths
        for _ in range(self.vertices - 1):
            for start_vertex, end_vertex, weight in self.edges:
                if distances[start_vertex] != float('inf') and distances[start_vertex] + weight < distances[end_vertex]:
                    distances[end_vertex] = distances[start_vertex] + weight

        # Check for negative cycles
        for start_vertex, end_vertex, weight in self.edges:
            if distances[start_vertex] != float('inf') and distances[start_vertex] + weight < distances[end_vertex]:
                print("Graph contains negative cycle, cannot find shortest path.")
                return

        # Return the shortest distance to the end vertex
        if distances[end] == float('inf'):
            print(f"There is no path from vertex {start} to {end}.")
        else:
            return distances[end]

# Example usage:
graph = Graph(5)
graph.add_edge(0, 1, 1)
graph.add_edge(1, 2, -2)
graph.add_edge(2, 3, 3)
graph.add_edge(3, 4, 1)
graph.add_edge(4, 1, -2)

start_vertex = 0
end_vertex = 4

shortest_distance = graph.bellman_ford(start_vertex, end_vertex)
print(f"The shortest distance from vertex {start_vertex} to {end_vertex}: {shortest_distance}")
