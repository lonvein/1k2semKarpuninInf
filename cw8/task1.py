def order_of_scobka(k, d, i=0):
    if len(k) == 0:
        return d
    else:
        if k[i][0] != k[i+1][0]:
            d.append([k[i][1], k[i+1][1]])
            k.pop(i)
            k.pop(i)
            return order_of_scobka(k, d, i=0)
        else:
            return order_of_scobka(k, d, i+1)
def list_with_big_num(l, i, k):
    if k == 0:
        while 'N' in l:
            l.remove('N')
        return l
    else:
        if ((l[i] == '1') or (l[i] == '2') or (l[i] == '3') or (l[i] == '4') or (l[i] == '5') or (l[i] == '6') or (l[i] == '7') or (l[i] == '8') or (l[i] == '9')) and ( (l[i+1] == '1') or (l[i+1] == '2') or (l[i+1] == '3') or (l[i+1] == '4') or (l[i+1] == '5') or (l[i+1] == '6') or (l[i+1] == '7') or (l[i+1] == '8') or (l[i+1] == '9')):
            l[i] = l[i] + l[i+1]
            l[i + 1] = 'N'
            return list_with_big_num(l, i, k-1)
        else:
            return list_with_big_num(l, i + 1, k-1)
def resh_zn(l, o, i):
    if l.count('*') != 0:
        if l[i+1] == '*':
            c = [l[i], l[i+2], l[i+1]].copy()
            o = o + [c]
            l.pop(i)
            l.pop(i+1)
            l[i] = c
            return resh_zn(l, o, i=0)
        else:
            return resh_zn(l, o, i + 1)
    else:
        if l.count('/') != 0:
            if l[i+1] == '/':
                cc = [l[i], l[i+2], l[i+1]].copy()
                o = o + [cc]
                l.pop(i)
                l.pop(i+1)
                l[i] = cc

                return resh_zn(l, o, i=0)
            else:
                return resh_zn(l, o, i+1)
        else:
            if l.count('+') != 0 or l.count('-') != 0:
                if l[i+1] == '+' or l[i+1] == '-':
                    ccc = [l[i], l[i+2], l[i+1]].copy()
                    o = o + [ccc]
                    l.pop(i)
                    l.pop(i+1)
                    l[i] = ccc

                    return resh_zn(l, o, i=0)
                else:
                    return resh_zn(l, o, i  +1)
            else:
                o = str(o[-1])
                o = o.replace('[', '')
                o = o.replace(']', '')
                o = o.replace(',', '')
                o = o.replace('\'', '')
                return o
a = ('((12+44)-7*8)/(1+(9-5))')
print(a)
a = '(' + a + ')'
l = list(a)
l = list_with_big_num(l, 0, len(l))
ll = l.copy()

# выводит в скобках ) или ( и ее номер
k = [] 
for i in range(len(l)):
    if l[i] != '(' and l[i] != ')':
        l[i] = ''
    else:
        k.append([l[i], i])
    
por = order_of_scobka(k, [], 0)

    
def resh_v_sk(l, s, o, i):
    if i==len(s):
        return o[-1]
    else: 
        r = []
        for ii in range(s[i][0] + 1, s[i][1]):
            r.append(l[ii])
        o.append(r)
        return resh_v_sk(l, s, o, i+1)

g = []
print(ll)
print(por)
for i in por:
    m = []
    for j in range(i[0]+1, i[1]):
        m.append(ll[j])
    for j in range(i[0]+1, i[1]):
        ll.pop(j-1*j)
        for p in range(len(por)):
            for pp in range(len(por[p])):
                if pp>j:
                    ll[p][pp] -= 1
                else:
                    continue
    print(por)
    mm = resh_zn(m, [], i=0)
    g.append(mm)
print(g)
'''print(ll)
print(resh_v_sk(ll, order_of_scobka(k, d), [], i = 0))'''