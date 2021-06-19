#!/usr/bin/python3

import unittest
from stack.stack_array import StackArray

class TestStackArray(unittest.TestCase):
    def setUp(self):
        self.stack = StackArray()

    def tearDown(self):
        self.stack.clear()

    def test_push_1(self):
        self.stack.push(22)
        self.assertEqual(self.stack.get_stack(), [22])

    def test_push_2(self):
        for i in range(20):
            self.stack.push(i)
        # self.stack.display()
        with self.assertRaises(OverflowError):
            self.stack.push(55)

    def test_pop_1(self):
        with self.assertRaises(IndexError):
            self.stack.pop()

    def test_pop_2(self):
        self.stack.push(22)
        self.stack.push(33)
        data = self.stack.pop()
        self.assertEqual(data, 33)
        data = self.stack.pop()
        self.assertEqual(data, 22)

    def test_seek_1(self):
        self.stack.push(22)
        self.stack.push(33)
        self.stack.push(44)
        data = self.stack.seek()
        self.assertEqual(data, 44)

    def test_seek_2(self):
        with self.assertRaises(IndexError):
            self.stack.seek()
