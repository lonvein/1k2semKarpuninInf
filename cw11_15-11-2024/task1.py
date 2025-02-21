# 1. Для заданного бинарного дерева напишите эффективный алгоритм, 
# проверяющий, имеет ли оно симметричную структуру или нет, 
# т. е. левое и правое поддерево зеркально отражают друг друга.

# Класс для хранения узла бинарного дерева.
class Node:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
 
 
# Рекурсивная функция для проверки идентичности двух заданных бинарных деревьев.
def isIdentical(x, y):
 
    #, если оба дерева пусты, вернуть true
    if x is None and y is None:
        return True
 
    #, если оба дерева непусты и значение их корневого узла совпадает,
    # повторяются для их левого и правого поддерева
    return (x is not None and y is not None) and (x.key == y.key) and isIdentical(x.left, y.left) and isIdentical(x.right, y.right)


def issim(x):
    return issim_parts(x.left, y.right)
def issim_parts(x, y):
 
    #, если оба дерева пусты, вернуть true
    if x is None and y is None:
        return True
 
    #, если оба дерева непусты и значение их корневого узла совпадает,
    # повторяются для их левого и правого поддерева
    return (x is not None and y is not None) and (x.key == y.key) and issim_parts(x.left, y.right) and issim_parts(x.right, y.left)


# построить первое дерево
x = Node(15)
x.left = Node(10)
x.right = Node(20)
x.left.left = Node(8)
x.left.right = Node(12)
x.right.left = Node(16)
x.right.right = Node(25)

# построить второе дерево
y = Node(15)
y.left = Node(10)
y.right = Node(10)
y.left.left = Node(20)
y.left.right = Node(12)
y.right.left = Node(12)
y.right.right = Node(20)


if issim(x):
    print('The given binary trees is sim')
else:
    print('The given binary trees is not sim')
    
if issim(y):
    print('The given binary trees is sim')
else:
    print('The given binary trees is not sim')