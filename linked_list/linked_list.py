#!/usr/bin/python3
from abc import ABC, abstractmethod
from .node import Node

class LinkedList(ABC):
    """
        A linked list is a linear data structure, in which the elements are not stored at contiguous memory locations. The elements in a linked list are linked using pointers
    """
    def __init__(self):
        """
            Initializes the head as None
        """
        self.head = None

    @abstractmethod
    def add_node_at_last(self, data):
        """
            Abstract method for adding a node at the last of the list
        """
        pass

    @abstractmethod
    def add_node_at_beginning(self, data):
        """
            Abstract method for adding a node at the beginning of the list
        """
        pass

    @abstractmethod
    def add_node_at_nth_pos(self, nth):
        """
            Abstract method for adding a node at the nth position of the list
        """
        pass

    @abstractmethod
    def remove_node_at_last(self, data):
        """
            Abstract method for removing the last node of the list
        """
        pass

    @abstractmethod
    def remove_node_at_beginning(self, data):
        """
            Abstract method for removing the first node of the list
        """
        pass

    @abstractmethod
    def remove_node_at_nth_pos(self, nth):
        """
            Abstract method for removing the nth node of the list
        """
        pass

    @abstractmethod
    def length(self):
        """
            Abstract method for getting the length of the list
        """
        pass

    @abstractmethod
    def display(self):
        """
            Abstract method for displaying the contents of the list
        """
        pass

    @abstractmethod
    def clear(self):
        """
            Abstract method for removing all the nodes of the list
        """
        pass

    @abstractmethod
    def get_list(self):
        """
            Abstract method for getting the contents of the list
        """
        pass
