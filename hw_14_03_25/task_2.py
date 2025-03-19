# прим
def prim(graph, start):
    mst = [] 
    visited = set([start]) 
    edges = [] 
    for to, weight in graph[start].items():
        edges.append((weight, start, to))
    while edges:
        min_edge = None
        for edge in edges:
            if min_edge is None or edge[0] < min_edge[0]:
                min_edge = edge
        edges.remove(min_edge)
        weight, frm, to = min_edge
        if to not in visited:
            visited.add(to)
            mst.append((frm, to, weight))
            for to_next, weight_next in graph[to].items():
                if to_next not in visited:
                    edges.append((weight_next, to, to_next))
    return mst

'''
# краскал
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)
    
    if xroot == yroot:
        return False 
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    else:
        parent[yroot] = xroot
        if rank[xroot] == rank[yroot]:
            rank[xroot] += 1
    return True

def kruskal(graph):
    edges = []
    for frm in graph:
        for to, weight in graph[frm].items():
            edges.append((weight, frm, to))
    edges.sort()
    vertices = list(graph.keys())
    parent = {v: v for v in vertices}
    rank = {v: 1 for v in vertices}
    mst = []
    for weight, frm, to in edges:
        if union(parent, rank, frm, to):
            mst.append((frm, to, weight))
    return mst
    
    '''