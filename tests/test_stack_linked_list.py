#!/usr/bin/python3

import unittest
from stack.stack_linked_list import StackLinkedList

class TestStackLinkedList(unittest.TestCase):
    def setUp(self):
        self.stack = StackLinkedList()

    def tearDown(self):
        self.stack.clear()

    def test_push(self):
        self.stack.push(22)
        self.stack.push(33)
        self.stack.push(44)
        self.assertEqual(self.stack.get_stack(), [22, 33, 44])

    def test_pop_1(self):
        with self.assertRaises(IndexError):
            self.stack.pop()

    def test_pop_2(self):
        self.stack.push(22)
        self.stack.push(33)
        self.stack.pop()
        self.stack.push(44)
        self.assertEqual(self.stack.get_stack(), [22, 44])

    def test_seek_1(self):
        with self.assertRaises(IndexError):
            self.stack.seek()

    def test_seek_2(self):
        self.stack.push(22)
        self.stack.push(33)
        self.stack.push(44)
        self.assertEqual(self.stack.seek(), 44)
        self.assertEqual(self.stack.get_stack(), [22, 33, 44])
