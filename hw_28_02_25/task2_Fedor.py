import math
def h(p1, p2):
    return round((math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)), 3)
a = int(input())
pts = []
mtrx = [[float('inf') for _ in range(a)] for i in range(a)]
for _ in range(a):
    pts.append(list(map(int, input().split())))
for i in range(a):
    for j in range(a):
        mtrx[i][j] = h(pts[i], pts[j])
r = mtrx[0][1]
for k in range(a):
    for i in range(a):
        for j in range(a):
            if mtrx[i][j] > max(mtrx[i][k], mtrx[k][j]) and max(mtrx[i][k], mtrx[k][j]) < r:
                mtrx[i][j] = max(mtrx[i][k], mtrx[k][j])
print(mtrx[0][1])

