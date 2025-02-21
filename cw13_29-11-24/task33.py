r=[]
class Node:
  def __init__(self, value=None, left = None, right = None):
    self.value = value
    self.left = left
    self.right = right

class AVL:
  def __init__(self, node = None):
    self.node = node
  def insert(self, val):
    if self.node == None:
      self.node = Node(val)
      self.node.left = AVL()
      self.node.right = AVL()
    elif val < self.node.value:
      self.node.left.insert(val)
    elif val == self.node.value:
      pass
    else:
       self.node.right.insert(val)
  def print_tree(self):
    if self.node:
      self.node.left.print_tree()
      if self.node.right.node == None and self.node.left.node == None:
        r.append(self.node.value)
      self.node.right.print_tree()
      
      

m = list(map(int, input().split()))
inter = list(map(int, input().split()))

a = AVL()
for i in range(len(inter)):
  a.insert(inter[i])
a.print_tree()
print(" ".join(map(str, r)))
