#!/usr/bin/python3
from abc import ABC, abstractmethod
from .node import Node

class LinkedList(ABC):
    def __init__(self):
        self.head = None

    @abstractmethod
    def add_node_at_last(self, data):
        pass

    @abstractmethod
    def add_node_at_beginning(self, data):
        pass

    @abstractmethod
    def add_node_at_nth_pos(self, nth):
        pass

    @abstractmethod
    def remove_node_at_last(self, data):
        pass

    @abstractmethod
    def remove_node_at_beginning(self, data):
        pass

    @abstractmethod
    def remove_node_at_nth_pos(self, nth):
        pass

    @abstractmethod
    def length(self):
        pass

    @abstractmethod
    def display(self):
        pass

    @abstractmethod
    def clear(self):
        pass

    @abstractmethod
    def get_list(self):
        pass
