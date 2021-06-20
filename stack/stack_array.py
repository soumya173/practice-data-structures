#!/usr/bin/python3

from .stack import Stack

class StackArray(Stack):
    """
        Stack implementation using array data structure
    """
    def __init__(self, size=20):
        """
            Initializing stack contents
            - Stack             : with empty list
            - Top               : 0
            - Default max side  : 20
        """
        self.__stack = []
        self.__top = 0
        self.__SIZE = size

    def push(self, data):
        """
            Adds an element to the stack
            - Returns error if the stack is full
        """
        if self.__top >= self.__SIZE:
            raise OverflowError(f"Stack is full: {data}")
        self.__stack.append(data)
        self.__top += 1
        return data

    def pop(self):
        """
            Removes an element from the stack
            - Returns error if the stack is empty
        """
        if self.__top == 0:
            raise IndexError("Stack is empty")
        data = self.__stack.pop()
        self.__top -= 1
        return data

    def seek(self):
        """
            Returns the last added entry in the stack
            - Returns error if the stack is empty
        """
        if self.__top == 0:
            raise IndexError("Stack is empty")
        return self.__stack[self.__top-1]

    def clear(self):
        """
            Removes all the entries from the stack
        """
        self.__stack.clear()
        self.__top = 0

    def display(self):
        """
            Prints the stack contents in the stdout
            - Returns error if the stack is empty
        """
        if self.__top == 0:
            raise IndexError("Stack is empty")
        for data in self.__stack:
            print(data, end=' ')

    def get_stack(self):
        """
            Returns the stack contents as a list
        """
        return self.__stack
