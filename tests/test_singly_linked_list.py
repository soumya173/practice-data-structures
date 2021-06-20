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

    def test_add_node_at_nth_pos_1(self):
        self.singly_linked_list.add_node_at_last(22)
        self.singly_linked_list.add_node_at_last(33)
        self.singly_linked_list.add_node_at_last(44)
        self.singly_linked_list.add_node_at_last(55)
        self.singly_linked_list.add_node_at_nth_pos(2, 66)
        self.assertEqual(self.singly_linked_list.get_list(), [22, 33, 66, 44, 55])

    def test_add_node_at_nth_pos_2(self):
        self.singly_linked_list.add_node_at_last(22)
        self.singly_linked_list.add_node_at_last(33)
        with self.assertRaises(OverflowError):
            self.singly_linked_list.add_node_at_nth_pos(8, 77)

    def test_add_node_at_nth_pos_3(self):
        self.singly_linked_list.add_node_at_last(22)
        self.singly_linked_list.add_node_at_last(33)
        self.singly_linked_list.add_node_at_nth_pos(0, 66)
        self.assertEqual(self.singly_linked_list.get_list(), [66, 22, 33])

    def test_remove_node_at_last_1(self):
        self.singly_linked_list.add_node_at_last(22)
        self.singly_linked_list.add_node_at_last(33)
        self.singly_linked_list.add_node_at_last(44)
        self.singly_linked_list.add_node_at_last(55)
        self.singly_linked_list.remove_node_at_last()
        self.assertEqual(self.singly_linked_list.get_list(), [22, 33, 44])

    def test_remove_node_at_last_2(self):
        with self.assertRaises(IndexError):
            self.singly_linked_list.remove_node_at_last()

    def test_remove_node_at_beginning_1(self):
        with self.assertRaises(IndexError):
            self.singly_linked_list.remove_node_at_beginning()

    def test_remove_node_at_beginning_2(self):
        self.singly_linked_list.add_node_at_last(22)
        self.singly_linked_list.add_node_at_last(33)
        self.singly_linked_list.add_node_at_last(44)
        self.singly_linked_list.add_node_at_last(55)
        self.singly_linked_list.remove_node_at_beginning()
        self.assertEqual(self.singly_linked_list.get_list(), [33, 44, 55])

    def test_remove_node_at_nth_pos_1(self):
        self.singly_linked_list.add_node_at_last(22)
        self.singly_linked_list.add_node_at_last(33)
        self.singly_linked_list.add_node_at_last(44)
        self.singly_linked_list.add_node_at_last(55)
        self.singly_linked_list.remove_node_at_nth_pos(2)
        self.assertEqual(self.singly_linked_list.get_list(), [22, 44, 55])

    def test_remove_node_at_nth_pos_2(self):
        with self.assertRaises(IndexError):
            self.singly_linked_list.remove_node_at_nth_pos(0)

    def test_remove_node_at_nth_pos_3(self):
        self.singly_linked_list.add_node_at_last(22)
        self.singly_linked_list.add_node_at_last(33)
        self.singly_linked_list.add_node_at_last(44)
        self.singly_linked_list.add_node_at_last(55)
        with self.assertRaises(OverflowError):
            self.singly_linked_list.remove_node_at_nth_pos(8)
