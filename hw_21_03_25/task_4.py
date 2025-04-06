'''def solve_cubes():
    n = int(input())
    name = input().strip()
    cubes = [input().strip() for _ in range(n)]
    m = len(name)
    graph = [[] for _ in range(m)]
    for i, c in enumerate(name):
        for j, cube in enumerate(cubes):
            if c in cube:
                graph[i].append(j)
    
    match_to = [-1] * m
    used = [False] * n
    
    def dfs(u):
        for v in graph[u]:
            if not used[v]:
                used[v] = True
                if match_to[v] == -1 or dfs(match_to[v]):
                    match_to[v] = u
                    return True
        return False
    
    result = 0
    for u in range(m):
        used = [False] * n
        if dfs(u):
            result += 1
    
    if result != m:
        print("NO")
    else:
        print("YES")
        order = [0] * m
        for j in range(n):
            if match_to[j] != -1:
                order[match_to[j]] = j + 1
        print(' '.join(map(str, order)))

solve_cubes()'''


