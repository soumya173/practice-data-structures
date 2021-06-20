#!/usr/bin/python3

from .stack import Stack
from linked_list.singly_linked_list import SinglyLinkedList

class StackLinkedList(Stack):
    """
        Stack implementation using linked list
    """
    def __init__(self):
        """
            Initializing stack with an empty linked list
        """
        self.stack = SinglyLinkedList()

    def push(self, data):
        """
            Adds an element to the stack
        """
        return self.stack.add_node_at_last(data)

    def pop(self):
        """
            Removes an element from the stack
            - Returns error if the stack is empty
        """
        return self.stack.remove_node_at_last()

    def seek(self):
        """
            Returns the last added entry in the stack
            - Returns error if the stack is empty
        """
        if self.stack.head is None:
            raise IndexError("Stack is empty")
        node = self.stack.head
        while(node.next is not None):
            node = node.next
        return node.data

    def clear(self):
        """
            Removes all the entries from the stack
        """
        self.stack.clear()

    def display(self):
        """
            Prints the stack contents in the stdout
        """
        self.stack.display()

    def get_stack(self):
        """
            Returns the stack contents as a list
        """
        return self.stack.get_list()
