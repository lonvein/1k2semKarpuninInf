
t = int(input())
for _ in range(t):
    while True:
        line = input().strip()
        if line: break
    N = int(line)
    cards = [int(input().strip()) for _ in range(N)]
    while True:
        line = input().strip()
        if line: break
    e = int(line)
    adj = {}
    for _ in range(e):
        x, y = map(int, input().split())
        adj.setdefault(x, []).append(y)
        adj.setdefault(y, []).append(x)
    
    count = {}
    for c in cards:
        count[c] = count.get(c, 0) + 1
    missing = [x for x in range(1, N+1) if count.get(x, 0) == 0]
    dup = []
    for k in count:
        dup.extend([k] * (count[k] - 1))
    
    res = 0
    for need in missing:
        min_d, idx = float('inf'), -1
        for i, d in enumerate(dup):
            if d == -1:
                continue
            dist = 0
            if d == need:
                dist = 0
            else:
                visited = {d}
                q = [d]
                found = False
                dist = 0
                while q and not found:
                    dist += 1
                    nq = []
                    for u in q:
                        for v in adj.get(u, []):
                            if v == need:
                                found = True
                                break
                            if v not in visited:
                                visited.add(v)
                                nq.append(v)
                        if found:
                            break
                    q = nq
                if not found:
                    dist = -1
            if dist != -1 and dist < min_d:
                min_d, idx = dist, i
        if idx != -1:
            res += min_d
            dup[idx] = -1
    print(res)
