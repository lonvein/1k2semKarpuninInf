def ford_fulkerson(graph, source, sink):
    residual = [row for row in graph]
    max_flow = 0
    parent = [-1] * len(residual)
    
    # Пока существует путь из истока в сток
    while dfs(residual, source, sink, parent):
        # Находим минимальную пропускную способность на пути
        path_flow = float('inf')
        v = sink
        while v != source:
            u = parent[v]
            path_flow = min(path_flow, residual[u][v])
            v = u
        
        # Увеличиваем общий поток
        max_flow += path_flow
        
        # Обновляем остаточные пропускные способности
        v = sink
        while v != source:
            u = parent[v]
            residual[u][v] -= path_flow
            residual[v][u] += path_flow
            v = u
    
    return max_flow

def dfs(residual, source, sink, parent):
    visited = [False] * len(residual)
    stack = [source]
    visited[source] = True
    
    while stack:
        u = stack.pop(0)
        # Проверяем всех соседей
        for v in range(len(residual)):
            if not visited[v] and residual[u][v] > 0:
                visited[v] = True
                parent[v] = u
                stack.append(v)
                if v == sink:
                    return True
    return False

number_of_net = 1
while (a := int(input())) != 0:
    graph = [[0 for _ in range(a+1)] for _ in range(a+1)]
    source, sink, amount_of_edges = map(int, input().split())
    for i in range(amount_of_edges):
        vertex_1, vertex_2, weight_of_edge = map(int, input().split())
        graph[vertex_1][vertex_2] = weight_of_edge
        graph[vertex_2][vertex_1] = weight_of_edge
    print('Network', number_of_net, '\nThe bandwidth is', ford_fulkerson(graph, source, sink) , '.')
    number_of_net += 1

'''
4
1 4 5
1 2 20
1 3 10
2 3 5
2 4 10
3 4 20
0
    '''