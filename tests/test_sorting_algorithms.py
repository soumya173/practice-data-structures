#!/usr/bin/python3

import unittest
from sorting.selection_sort import selection_sort
from sorting.merge_sort import merge_sort
from sorting.quick_sort import quick_sort

class TestSelectionSort(unittest.TestCase):
    def test_selection_sort_1(self):
        sorted_arr = [1, 3, 3, 5, 22, 23, 45, 45, 67, 75]
        unsorted_arr = [3, 45, 1, 3, 5, 75, 23, 45, 67, 22]
        self.assertEqual(selection_sort(unsorted_arr), sorted_arr)

class TestMergeSort(unittest.TestCase):
    def test_merge_sort_1(self):
        sorted_arr = [1, 3, 3, 5, 22, 23, 45, 45, 67, 75]
        unsorted_arr = [3, 45, 1, 3, 5, 75, 23, 45, 67, 22]
        self.assertEqual(merge_sort(unsorted_arr), sorted_arr)

class TestQuickSort(unittest.TestCase):
    def test_quick_sort_1(self):
        sorted_arr = [1, 3, 3, 5, 22, 23, 45, 45, 67, 75]
        unsorted_arr = [3, 45, 1, 3, 5, 75, 23, 45, 67, 22]
        self.assertEqual(quick_sort(unsorted_arr, 0, len(unsorted_arr)-1), sorted_arr)