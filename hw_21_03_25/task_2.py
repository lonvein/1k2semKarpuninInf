
n = int(input())
cost = []
for _ in range(n):
    row = list(map(int, input().split()))
    cost.append(row)

big_num = 10**18
row_pot = [0]*(n+1)
col_pot = [0]*(n+1)
way = [0]*(n+1)
pair = [0]*(n+1)

for worker in range(1, n+1):
    min_val = [big_num]*(n+1)
    used = [False]*(n+1)
    job = 0
    pair[job] = worker
    while True:
        used[job] = True
        cur_worker = pair[job]
        delta = big_num
        new_job = 0
        for j in range(1, n+1):
            if not used[j]:
                current = cost[cur_worker-1][j-1] - row_pot[cur_worker] - col_pot[j]
                if current < min_val[j]:
                    min_val[j] = current
                    way[j] = job
                if min_val[j] < delta:
                    delta = min_val[j]
                    new_job = j
        for j in range(n+1):
            if used[j]:
                row_pot[pair[j]] += delta
                col_pot[j] -= delta
            else:
                min_val[j] -= delta
        
        job = new_job
        if pair[job] == 0:
            break
    
    while True:
        temp = way[job]
        pair[job] = pair[temp]
        job = temp
        if job == 0:
            break

print(-col_pot[0])