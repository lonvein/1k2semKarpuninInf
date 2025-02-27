def has_cycle(V, adj):
    visited = [False] * V  
    parent = [-1] * V      
    def dfs(u):
        visited[u] = True  
        for v in adj[u]:  
            if not visited[v]:  
                parent[v] = u   
                if dfs(v):     
                    return True
            elif v != parent[u]: 
                return True      
        return False
    for u in range(V):
        if not visited[u]:
            if dfs(u): 
                return True
    return False
V, E = map(int, input().split())
adj = eval(input()) 
if has_cycle(V, adj):
    print("YES")
else:
    print("NO")