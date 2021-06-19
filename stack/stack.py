#!/usr/bin/python3

from abc import ABC, abstractmethod

class Stack(ABC):
    @abstractmethod
    def push(self, data):
        pass

    @abstractmethod
    def pop(self):
        pass

    @abstractmethod
    def display(self):
        pass

    @abstractmethod
    def seek(self):
        pass

    @abstractmethod
    def clear(self):
        pass

    @abstractmethod
    def get_stack(self):
        pass
