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
    
x = Node(15)
x.left = Node(10)
x.right = Node(20)
x.left.left = Node(8)
x.left.right = Node(12)
x.right.left = Node(16)
x.right.right = Node(25)

print(mirror(x).left.right.key, x.right.left.key )