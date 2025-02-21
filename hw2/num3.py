d={'A':'A' , 'H':'H' , 'I':'I' , 'M':'M' , 'O':'O' , 'T':'T' , 'U':'U' , 'V':'V' , 'W':'W' , 'X':'X' , 'Y':'Y' , '1':'1' , '8':'8',  'E': '3', 'J': 'L', 'S': '2', 'Z': '5', '3': 'E', 'L': 'J', '2': 'S', '5': 'Z'}
a=list(input())
print(a)

def f(x):
    b=list()
    for i in range(len(x)):
        b.append(d[x[i]])
    return g(b)
        
def g(y):
    v=list()
    for i in range(len(y)):
        v.append(y[len(y)-i-1])
    return v

def h(u):
    for i in range(len(u)):
        if d.setdefault(u[i], 'eklmn')== 'eklmn':
            return False 
    return True
if g(a)==a:
    if h(a):
        if f(a)==a:
            print('зерк пал')
        else:
            print('зерк')
            
    else: 
        print('палин')
elif h(a):
    if f(a)==a:
        print('зерк')
else:
    print('не палин')
