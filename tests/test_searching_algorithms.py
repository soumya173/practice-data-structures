import unittest
from searching.binary_search import binary_search

class TestBinarySearch(unittest.TestCase):
    def test_binary_search_1(self):
        arr = [1, 3, 3, 5, 22, 23, 45, 48, 67, 75]
        element = 67
        self.assertEqual(binary_search(arr, element, 0, len(arr)-1), 8)

    def test_binary_search_2(self):
        arr = [1, 3, 4, 5, 22, 23, 45, 45, 67, 75]
        element = 3
        self.assertEqual(binary_search(arr, element, 0, len(arr)-1), 1)

    def test_binary_search_3(self):
        arr = [1, 3, 3, 5, 22, 23, 45, 45, 67, 75]
        element = 99
        self.assertEqual(binary_search(arr, element, 0, len(arr)-1), -1)