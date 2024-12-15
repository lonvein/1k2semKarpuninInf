import unittest
def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1

def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)
        return array
data = list(input().split())

class TestZeros(unittest.TestCase):
    def test_qsort(self):
        self.assertEqual(quickSort([0,0,0,0,0,0], 0, 5), [0,0,0,0,0,0], f"quicksort([0,0,0,0,0,0], 0, 5) = {quickSort([0,0,0,0,0,0], 0, 5)} should be [0,0,0,0,0,0]")
class TestOne(unittest.TestCase):
    def test_qsort(self):
        self.assertEqual(quickSort([1,1,1,1,1,1], 0, 5), [1,1,1,1,1,1], f"quicksort([1,1,1,1,1,1], 0, 5) = {quickSort([1,1,1,1,1,1], 0, 5)} should be [1,1,1,1,1,1]")

class TestBigNum(unittest.TestCase):
    def test_qsort(self):
        self.assertEqual(quickSort([11111, 11111111, 10101010, 111212, 12121, 99999], 0, 7), sorted([11111, 11111111, 10101010, 111212, 12121, 99999]), f"quicksort([11111, 11111111, 10101010, 111212, 12121, 99999], 0, 7) = {quickSort([11111, 11111111, 10101010, 111212, 12121, 99999], 0, 7)} should be {[11111, 11111111, 10101010, 111212, 12121, 99999]}")


print("Unsorted Array ", data)
size = len(data)
print(quickSort(data, 0, size - 1))
print('Sorted Array in Ascending Order: ', data)


if __name__ == '__main__':
    unittest.main()
    

