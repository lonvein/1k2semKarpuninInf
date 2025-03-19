'''
function doDfs(G[n]: Graph): // функция принимает граф G с количеством вершин n и выполняет обход в глубину во всем графе 
   color = array[n, white]
                   
   function dfs(u: int):
      color[u] = gray           
      for v: (u, v) in G                   
         if color[v] == white
            dfs(v)
      color[u] = black   
                   	   
   for i = 1 to n             
      if color[i] == white                
         dfs(i)
         
         '''
n, m = map(int, input().split())
l = [[] for _ in range(n+1)]
for i in range(m):
    q, w = map(int, input().split())
    l[q].append(w)
print(l)

def dodfs(n, l):
    ans = 'YES'
    color = ['w' for i in range(n+1)]
    def dfs(u):
        color[u] = 'g'
        for v in l[u]:
            print('color', color)
            if color[v] == 'g':
                print('Уже серый')
                ans = '-1'
            if color[v] == 'w':
                dfs(v)
        color[v] = 'b'
            
    for i in [p + 1 for p in range(n)]:
        print('i', i)
        if ans == '-1':
            return ans
        if color[i] == 'w':
            dfs(i)
    return ans
print(dodfs(n, l))