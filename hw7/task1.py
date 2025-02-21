import numpy
class Vector():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __abs__(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5
    def __add__(self, other): 
        return self.x + other.x, self.y + other.y, self.z + other.z
    def __sub__(self, other): 
        return self.x - other.x, self.y - other.y, self.z - other.z
    def __matmul__(self, other): 
        return self.x * other.x + self.y * other.y + self.z * other.z
    def __mul__(self, o): 
        return self.x * o,  self.y * o, self.z * o
    
    
    @classmethod
    def add(cls, a, b):
        return Vector(a.x + b.x, a.y + b.y, a.z + b.z) 
    @classmethod
    def sub(cls, a, b):
        return Vector(a.x - b.x, a.y - b.y, a.z - b.z) 
    @classmethod
    def mul(cls, a, b): 
        return Vector(a.x * b,  a.y * b, a.z * b)
    @classmethod
    def centermass(cls, list_vec):
        c = Vector(0, 0, 0)
        for i in list_vec:
            c = Vector.add(i, c)
        n = 1/len(list_vec)
        return Vector.mul(c, n).x, Vector.mul(c, n).y, Vector.mul(c, n).z
    @classmethod
    def det(cls, a, b): 
        v = numpy.array([[1, 1, 1], [a.x, a.y, a.z], [b.x, b.y, b.z]])
        return numpy.linalg.det(v)
    @classmethod
    def sq(cls, ll):
        m=0 
        for i in ll:
            indd = ll.index(i)
            ll.pop(indd)
            for j in ll:
                ind = ll.index(j)
                ll.pop(ind)
                for k in ll:
                    a1 = Vector.sub(j, i)
                    a2 = Vector.sub(k, i)
                    m = max(m, Vector.det(a1, a2))
                ll.insert(ind, j)
            ll.insert(indd, i)
        return m
        


print(Vector(1, 2, 3) + Vector(4, 5, 6))
print(Vector(1, 2, 3) - Vector(4, 5, 6))
print(Vector(1, 2, 3) @ Vector(4, 5, 6))
print(Vector(1, 2, 3) * 3)
print(Vector.centermass([Vector(1, 2, 3), Vector(4, 5, 6), Vector(7, 8, 9)]))
print(Vector.sq([Vector(1, 1, 0), Vector(1, 2, 0), Vector(1, 3, 0), Vector(1, 4, 0), Vector(1, 5, 0), Vector(8, 1, 0)]))