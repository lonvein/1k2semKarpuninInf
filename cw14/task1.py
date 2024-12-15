import unittest

def p(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    if n == -1:
        return -1
    else:
        for c in (range(2, n + 1)):
            if ((n // c) * c == n):
                print(c)
                return (n // c)
a = int(input())
class TestOne(unittest.TestCase):
    def test_p(self):
        self.assertEqual(p(a), 1, f"p(1) = {p(1)} should be 1")

class TestEmpty(unittest.TestCase):
    def test_p(self):
        self.assertEqual(p(a), 0, f"p(0) = {p(0)} should be 0")

class TestListWithNegatives(unittest.TestCase):
    def test_p(self):
        self.assertEqual(p(a), -1, f"p(-1) = {p(-1)} should be -1")


if __name__ == '__main__':
    unittest.main()
    

