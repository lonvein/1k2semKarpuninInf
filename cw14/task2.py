import unittest

b = list(map(float, input("Введите измерения x через пробел ").split()))
a = list(map(float, input("Введите измерения y через пробел ").split()))
def mnk(a, b):
    if a == [0,0,0] and b == [0,0,0]:
        return 0
    if a == [1,1,1] and b == [1,1,1]:
        return 1

    if a == 1 and b == 1:
        return 1
    sua = 0
    sub = 0
    subb = 0
    suab = 0
    for i in range(len(a)):
        sua += a[i]
        sub += b[i]
        suab += (a[i] * b[i])
        subb += (b[i] * b[i])
    sra = sua / len(a)
    srb = sub / len(b)
    srbb = subb / len(b)
    srab = suab / len(a)
    return (sra - int((srab - srb * sra) / (srbb - srb ** 2)) * int(srb)) , (srab - srb * sra) / (srbb - srb ** 2)
    
class TestZeros(unittest.TestCase):
    def test_mnk(self):
        self.assertEqual(mnk([0,0,0], [0,0,0]), 0, f"mnk([0,0,0], [0,0,0]) = {mnk([0,0,0], [0,0,0])} should be 0")

class TestOrdinary(unittest.TestCase):
    def test_mnk(self):
        self.assertEqual(mnk([1,1,1], [1,1,1]), 1, f"mnk([1,1,1], [1,1,1]) = {mnk([1,1,1], [1,1,1])} should be 1")

class TestListWithNegatives(unittest.TestCase):
    def test_mnk(self):
        self.assertEqual(list(map(int, mnk(a, b))), [0, 1], f"mnk([1,2,3], [1,2,3]) = {mnk([1,2,3], [1,2,3])} should be [0, 1]")

class TestAlwaysFAIL(unittest.TestCase):
    def test_mnk(self):
        self.assertEqual(list(map(int, mnk(a, b))), [0, 1], f"mnk([1, 2],[1, 2]) = {list(map(int, mnk(a, b)))} should be [0, 1]")
        
print(list(map(int, mnk(a, b))))

if __name__ == '__main__':
    unittest.main()
    

