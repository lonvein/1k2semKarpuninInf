
def bfs(graph, start, prev):
    visited = []
    queue = [start]
    print(queue)
    while queue:
        vertex = queue[0]
        queue = queue[1:]
        print(queue)
        
        if vertex not in visited:
            visited.append(vertex)
            
            print(vertex)  

            for neighbor in graph[vertex]:
                if neighbor[0] not in visited:
                    queue.append(neighbor[0])
                    prev[neighbor[0]] = [vertex, neighbor[1] + prev[vertex][1]]

h = [(0, 1, 3), (0, 4, 1), (1, 2, 1), (1, 3, 3), (1, 4, 1), (4, 2, 2), (4, 3, 1)]
graph = { 0 : [[1, 3], [4, 1]],
     1 : [[2, 1], [3, 3], [4, 1]],
     4 : [[2, 2], [3, 1]]}

prev = [[None, 0]]*len(h)
start = 0
end = 2
bfs(graph, start, prev)