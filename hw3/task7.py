import numpy
a, b = map(int, input().split())
s = []
ss = []
sss = []
for i in range(a):
    l = list(map(int, input().split()))
    sss.append(l)
    s.append(l[:-1])
    ss.append([l[-1]])
p = numpy.array(s)
pp = numpy.array(ss)
print(p, pp)
try:
    print(numpy.linalg.solve(p, pp))
except:
    print('Нет ответа')

