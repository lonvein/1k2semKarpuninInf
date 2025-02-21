def dijkstra(s, V, E):
    d = [10000]*len(V)
    used = [False]*len(V)
    
    '''
    for v in V:                    
        d[v] = 10000
        used[v] = False'''
        
        
    d[s] = 0
    for i in V:
        v = 0
        for j in V: 
            if not(used[j]) and (v == 0 or d[j] < d[v]):
                v = j
        if d[v] == 10000:
            break
        used[v] = True
        for e in E[v]: 
            if d[v] + e.len < d[e.to]:
                d[e.to] = d[v] + e.len
                
graph = { 
            0 : [[1, 3], [4, 1]],
            1 : [[2, 1], [3, 3], [4, 1]],
            4 : [[2, 2], [3, 1]]}

V = [0, 1, 2, 3, 4]
