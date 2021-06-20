#!/usr/bin/python3

from .stack import Stack
from linked_list.singly_linked_list import SinglyLinkedList
from linked_list.node import Node

class StackLinkedList(Stack):
    def __init__(self):
        self.stack = SinglyLinkedList()
        self.__top = 0

    def push(self, data):
        return self.stack.add_node_at_last(data)

    def pop(self):
        return self.stack.remove_node_at_last()

    def seek(self):
        if self.stack.head is None:
            raise IndexError("Stack is empty")
        node = self.stack.head
        while(node.next is not None):
            node = node.next
        return node.data

    def clear(self):
        self.stack.clear()

    def display(self):
        self.stack.display()

    def get_stack(self):
        return self.stack.get_list()
