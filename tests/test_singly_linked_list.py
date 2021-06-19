#!/usr/bin/python3

import unittest
from linked_list.singly_linked_list import SinglyLinkedList

class TestSinglyLinkedList(unittest.TestCase):
    def setUp(self):
        self.singly_linked_list = SinglyLinkedList()

    def tearDown(self):
        self.singly_linked_list.clear()

    def test_add_node_at_last(self):
        self.singly_linked_list.add_node_at_last(22)
        self.singly_linked_list.add_node_at_last(33)
        self.assertEqual(self.singly_linked_list.get_list(), [22, 33])
        self.assertEqual(self.singly_linked_list.length(), 2)

    def test_add_node_at_beginning(self):
        self.singly_linked_list.add_node_at_last(22)
        self.singly_linked_list.add_node_at_beginning(33)
        self.singly_linked_list.add_node_at_beginning(44)
        self.assertEqual(self.singly_linked_list.get_list(), [44, 33, 22])
        self.assertEqual(self.singly_linked_list.length(), 3)

    def test_add_node_at_nth_pos(self):
        self.singly_linked_list.add_node_at_last(22)
        self.singly_linked_list.add_node_at_last(33)
        self.singly_linked_list.add_node_at_last(44)
        self.singly_linked_list.add_node_at_last(55)
        self.singly_linked_list.add_node_at_nth_pos(3, 66)
        self.singly_linked_list.display()
        # self.assertEqual(self.singly_linked_list.get_list(), [22, 33, 66, 44, 55])
