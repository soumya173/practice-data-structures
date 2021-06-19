#!/usr/bin/python3

from .stack import Stack

class StackArray(Stack):
    def __init__(self, size=20):
        self.__stack = []
        self.__top = 0
        self.__SIZE = size

    def push(self, data):
        if self.__top >= self.__SIZE:
            raise OverflowError(f"Stack is full: {data}")
        self.__stack.append(data)
        self.__top += 1
        return data

    def pop(self):
        if self.__top == 0:
            raise IndexError("Stack is empty")
        data = self.__stack.pop()
        self.__top -= 1
        return data

    def seek(self):
        if self.__top == 0:
            raise IndexError("Stack is empty")
        return self.__stack[self.__top-1]

    def clear(self):
        self.__stack.clear()
        self.__top = 0

    def display(self):
        if self.__top == 0:
            raise IndexError("Stack is empty")
        for data in self.__stack:
            print(data, end=' ')

    def get_stack(self):
        return self.__stack
