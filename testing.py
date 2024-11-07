import unittest
import time

# basic bubble sort algorithm
def bubble_sort(array):
    n = len(array)

    for i in range(n):
        already_sorted = True

        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                already_sorted = False

        if already_sorted:
            break

    return array


# actual testing
class TestBubbleSort(unittest.TestCase):
    def testpositiveCases(self):
        self.assertEqual(bubble_sort([3, 5, 1, 4, 2, 6, 7, 7]), [1, 2, 3, 4, 5, 6, 7, 7])
        self.assertEqual(bubble_sort([1, 2, 3, 4, 5, 6, 7, 8]), [1, 2, 3, 4, 5, 6, 7, 8])
        self.assertEqual(bubble_sort([8, 7, 6, 5, 4, 3, 2, 1]), [1, 2, 3, 4, 5, 6, 7, 8])

    def testnegativeCases(self):
        self.assertRaises(TypeError, lambda: bubble_sort, "hello world")
        self.assertRaises(TypeError, lambda: bubble_sort, "12345")
        self.assertRaises(TypeError, lambda: bubble_sort, ['a','b','c','d'])
    
    def testperformanceCases(self):
        threshold = 1 # threshold for operating should be 1 sec for these tests
        start = time.time()
        bubble_sort([1, 2, 3, 4, 5, 6, 7, 8])
        end = time.time()
        self.assertLess(start-end, threshold)
    
        start = time.time()
        bubble_sort([8, 7, 6, 5, 4, 3, 2, 1])
        end = time.time()
        self.assertLess(start-end, threshold)

    def testboundaryCases(self):
        self.assertEqual(bubble_sort([1, 2, 3, 4, 5, 6, 7, 8]), [1, 2, 3, 4, 5, 6, 7, 8])
        self.assertEqual(bubble_sort([8, 7, 6, 5, 4, 3, 2, 1]), [1, 2, 3, 4, 5, 6, 7, 8])
        self.assertEqual(bubble_sort([1]), [1])
        self.assertEqual(bubble_sort([]), [])
        self.assertEqual(bubble_sort([1,1,1,1,1]), [1,1,1,1,1])
    
    def testidempotencyCases(self):
        arr1 = bubble_sort([3, 5, 1, 4, 2, 6, 7, 7])
        arr2 = bubble_sort([3, 5, 1, 4, 2, 6, 7, 7])
        arr3 = bubble_sort([3, 5, 1, 4, 2, 6, 7, 7])
        arr4 = bubble_sort([3, 5, 1, 4, 2, 6, 7, 7])
        self.assertEqual(arr1, arr2)
        self.assertEqual(arr2, arr3)
        self.assertEqual(arr3, arr4)

# just runs the unit tests
if __name__ == '__main__':
    unittest.main()