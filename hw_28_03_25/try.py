def dfs(lhn, a, b, v = None, z = 0):
    if v is None and z == 0:
        v = set()
    if a not in v and z == 0:
        v.add(a)
        for nei in lhn[a]:
            if nei == b and z == 0:
                z += 1
            if z == 0:
                z = dfs(lhn, nei, b, v, z)
    return z
    
lhn = [[], [], [3], [2, 4], [3], [5], [4]]
print(dfs(lhn, 2, 5))