class Node:
    def __init__(self, key = None, left = None, right = None):
        self.key = key
        self.left = left
        self.right = right
        
        
def add_list_to_Node(x, l, i = 0):
    if i < len(l):
        if x.key < l[i] and x.right == None:
            x.right = Node(l[i])
            add_list_to_Node(x, l, i + 1)
        elif x.key < l[i] and x.right != None:
            add_list_to_Node(x.right, l, i)
            add_list_to_Node(x, l, i + 1) 
        if x.key > l[i] and x.left == None:
            x.left = Node(l[i])
            add_list_to_Node(x, l, i + 1)
        elif x.key > l[i] and x.left != None:
            add_list_to_Node(x.left, l, i)
            add_list_to_Node(x, l, i + 1)


def outpoot_leaf(x, a = []):
    if not(x.left is None) and x.right is None:
        return outpoot_leaf(x.left, a)
    if x.left is None and not(x.right is None):
        return outpoot_leaf(x.right, a)
    if not(x.left is None) and not(x.right is None):
        return outpoot_leaf(x.right, a), outpoot_leaf(x.left, a)
    if not(x.left and x.right):
        a.append(x.key)
        

a = int(input())
ll = list(map(int, input().split()))
s = set(ll)
d = {}
l = []
for i in s:
    d[i] = 0
for i in ll:
    d[i] += 1
    if d[i] == 1:
        l.append(i)
x = Node(l[0])
l = l[1:]
add_list_to_Node(x, l)
a = []
outpoot_leaf(x, a)
print(x.right.key)
