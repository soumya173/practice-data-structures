#!/usr/bin/python3

from stack import Stack

class StackArray(Stack):
    def __init__(self, size=20):
        self.__stack = []
        self.__top = 0
        self.__SIZE = size

    def push(self, data):
        if self.__top >= self.__SIZE:
            print("Stack is full")
            return
        self.__stack.append(data)
        self.__top += 1
        print(f"Pushed: {data}")

    def pop(self):
        if self.__top == 0:
            print("Stack is empty")
            return
        data = self.__stack.pop()
        self.__top -= 1
        print(f"Popped: {data}")

    def seek(self):
        if self.__top == 0:
            print("Stack is empty")
            return
        print(f"Seek: {self.__stack[self.__top]}")

    def display(self):
        if self.__top == 0:
            print("Stack is empty")
            return
        for data in self.__stack:
            print(data, end=' ')
