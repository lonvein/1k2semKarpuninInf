from collections import defaultdict
import sys
n = int(input("n"))
def doska(n):
    edges = []
    for y in range(n):
        for x in range(n):
            if y - 2 >= 0 and x - 1 >= 0:
                edges.append((y * n + x, (y-2) * n + (x-1)))
            if y - 1 >= 0 and x - 2 >= 0:
                edges.append((y * n + x, (y-1) * n + (x-2)))
            if y - 2 >= 0 and x + 1 < n:
                edges.append((y * n + x, (y-2) * n + (x+1)))
            if y - 1 >= 0 and x + 2 < n:
                edges.append((y * n + x, (y-1) * n + (x+2)))
            if y + 2 < n and x + 1 < n:
                edges.append((y * n + x, (y+2) * n + (x+1)))
            if y + 1 < n and x + 2 < n:
                edges.append((y * n + x, (y+1) * n + (x+2)))
            if y + 2 < n and x - 1 >= 0:
                edges.append((y * n + x, (y+2) * n + (x-1)))
            if y + 1 < n and x - 2 >= 0:
                edges.append((y * n + x, (y+1) * n + (x-2)))
    return edges

from collections import defaultdict
import sys

class Graph:
    def __init__(self):
        # Initialize the graph using defaultdict to store adjacency lists
        self.graph = defaultdict(list)
        self.vertices = set()
    
    def add_edge(self, u, v):
        """Add a directed edge from vertex u to vertex v"""
        self.graph[u].append(v)
        self.vertices.add(u)
        self.vertices.add(v)
    
    def dfs_first_pass(self, vertex, visited, finishing_times):
        """First DFS pass to compute finishing times"""
        visited[vertex] = True
        
        # Recursively visit all adjacent vertices
        for adj_vertex in self.graph[vertex]:
            if not visited[adj_vertex]:
                self.dfs_first_pass(adj_vertex, visited, finishing_times)
        
        # Add vertex to finishing_times after exploring all its neighbors
        finishing_times.append(vertex)
    
    def dfs_second_pass(self, vertex, visited, scc):
        """Second DFS pass to find SCCs"""
        visited[vertex] = True
        scc.append(vertex)
        
        # Recursively visit all adjacent vertices
        for adj_vertex in self.graph[vertex]:
            if not visited[adj_vertex]:
                self.dfs_second_pass(adj_vertex, visited, scc)
   
g = Graph()
edges = doska(n)
for u, v in edges:
        g.add_edge(u, v)
# print(g.graph)

graph = {}

for i in g.graph:
    graph[i] = {}
    for q in g.graph[i]:
        graph[i][q] = 1

def all_vertex(graf):
    return list(graf.keys())

#возвращаем не менее красивым списочком всех соседей данной вершины
def vertex_neighbors(graf, vertex):
    return list(graf[vertex].keys())

#возвращаем длину ребра между двумя вершинами
def value(graf, vertex1, vertex2):
    return(graf[vertex1][vertex2])

def dijkstra(graf, start):
    unvisited_vertexes = all_vertex(graf)
    shortest_path = {}
    previous_vertex = {}

#по умолчанию расстояния между любыми двумя вершинами задаем равным бесконечности,
# а затем в цикле while переопределяем на минимально возможное 
    max_value = sys.maxsize
    for vertex in unvisited_vertexes:
        shortest_path[vertex] = max_value
    shortest_path[start] = 0

    while unvisited_vertexes:
        #ищем вершину с меньшей оценкой
        current_min_vertex = None
        for vertex in unvisited_vertexes:
            if current_min_vertex == None:
                current_min_vertex = vertex
            elif shortest_path[vertex] < shortest_path[current_min_vertex]:
                current_min_vertex = vertex
        neighbors = vertex_neighbors(graf, current_min_vertex)
        for neighbor in neighbors:
            tentative_value = shortest_path[current_min_vertex] + value(graf, current_min_vertex, neighbor)
            if tentative_value < shortest_path[neighbor]:
                shortest_path[neighbor] = tentative_value
                previous_vertex[neighbor] = current_min_vertex
        unvisited_vertexes.remove(current_min_vertex)
    return previous_vertex, shortest_path

for i in range(n ** 2):
    print(dijkstra(graph, i)[1]) 