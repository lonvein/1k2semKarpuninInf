def main():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    n = int(input[idx]); idx +=1
    m = int(input[idx]); idx +=1
    p = int(input[idx]); idx +=1
    
    unsafe = []
    if p > 0:
        unsafe = list(map(int, input[idx:idx+p]))
        idx += p
    unsafe_set = set(unsafe)
    
    # Список безопасных зданий
    safe = []
    for i in range(1, n+1):
        if i not in unsafe_set:
            safe.append(i)
    
    # Если нет безопасных зданий
    if not safe and n > 0:
        if n == 1:
            print(0)
        else:
            print("impossible")
        return
    
    edges_safe = []
    edges_unsafe = []
    
    for _ in range(m):
        x = int(input[idx]); idx +=1
        y = int(input[idx]); idx +=1
        l = int(input[idx]); idx +=1
        x_in = x in unsafe_set
        y_in = y in unsafe_set
        if x_in or y_in:
            if x_in ^ y_in:
                edges_unsafe.append((l, x, y))
        else:
            edges_safe.append((l, x, y))
    
    # Проверка наличия безопасных зданий
    if not safe:
        print(0)
        return
    
    # Алгоритм Крускала для безопасных зданий
    parent = {}
    rank = {}
    
    def find(u):
        while parent[u] != u:
            parent[u] = parent[parent[u]]
            u = parent[u]
        return u
    
    def union(u, v):
        u_root = find(u)
        v_root = find(v)
        if u_root == v_root:
            return False
        if rank[u_root] < rank[v_root]:
            parent[u_root] = v_root
        else:
            parent[v_root] = u_root
            if rank[u_root] == rank[v_root]:
                rank[u_root] +=1
        return True
    
    for b in safe:
        parent[b] = b
        rank[b] = 1
    
    edges_safe.sort()
    total_safe = 0
    edges_used = 0
    
    for l, x, y in edges_safe:
        if find(x) != find(y):
            union(x, y)
            total_safe += l
            edges_used +=1
    
    # Проверка связности безопасных зданий
    root = find(safe[0])
    all_connected = True
    for b in safe:
        if find(b) != root:
            all_connected = False
            break
    
    if not all_connected:
        print("impossible")
        return
    
    # Обработка небезопасных зданий
    if p == 0:
        print(total_safe)
        return
    
    # Ищем минимальное ребро для каждого небезопасного здания
    if not edges_unsafe:
        print("impossible")
        return
    
    min_unsafe = min(edges_unsafe, key=lambda x: x[0])[0]
    total = total_safe + min_unsafe
    print(total)

if __name__ == "__main__":
    main()