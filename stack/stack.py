#!/usr/bin/python3

from abc import ABC, abstractmethod

class Stack(ABC):
    """
        Stack is a linear data structure which follows a particular order in which the operations are performed. The order may be LIFO(Last In First Out) or FILO(First In Last Out).
    """
    @abstractmethod
    def push(self, data):
        """
            Abstract method for push operations
        """
        pass

    @abstractmethod
    def pop(self):
        """
            Abstract method for pop operations
        """
        pass

    @abstractmethod
    def display(self):
        """
            Abstract method for printing out the whole stack contents
        """
        pass

    @abstractmethod
    def seek(self):
        """
            Abstract method for seek operations
        """
        pass

    @abstractmethod
    def clear(self):
        """
            Abstract method for cleaning up the stack contents
        """
        pass

    @abstractmethod
    def get_stack(self):
        """
            Abstract method for returning the stack contents as a list
        """
        pass
