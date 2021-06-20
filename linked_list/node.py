#!/usr/bin/python3

class Node:
    """
        A node template used to create entries in linked list
    """
    def __init__(self, data=None):
        """
            Initializes field with provided parameter else None
        """
        self.data = data
        self.next = None
