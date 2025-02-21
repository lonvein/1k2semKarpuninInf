# a = 'student_10221student_00246student_90789student_10789'
a = input()
a = a.replace('student', '')[1:]
l = list(map(str, a.split('_')))
j = []
h = []
for i in l:
    j.append(i[0:3])
    h.append(i[3:])
maxx = 0
for i in h:
    maxx = max(maxx, int(i))
ll = []
for i in range(len(h)):
    if h[i] == str(maxx):
        ll.append(i)
for i in range(len(ll)):
    ll[i] = j[ll[i]]
lll = ''
for i in ll:
    lll += '-' + i
print(lll[1:])
