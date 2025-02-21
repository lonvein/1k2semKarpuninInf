class Node:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

def mirror(a):
    if a.left == None and a.right == None:
        return a
    else:
        b = Node(a.key, mirror(a.right), mirror(a.left))
        return b

def par(a, n):
    if a.left == None and a.right == None:
        return 'f'
    if a.left == 'f' and a.right == 'f':
        return 'f'
    if a.key == n:
        return a
    else:
        b = Node(a.key, par(a.left, n), par(a.right, n))
        return b
def view(n):
    if n.left and n.right:
        print(n.left.key, n.right.key)
        return view(n.right), view(n.left)
x = Node(15)
x.left = Node(10)
x.right = Node(20)
x.left.left = Node(8)
x.left.right = Node(12)
x.right.left = Node(16)
x.right.right = Node(25)

print(par(x, 12).key, par(x, 12).left.key, par(x, 12).right.key)
view(x)
