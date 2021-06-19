#!/usr/bin/python3

from stack import Stack

class StackArray(Stack):
    def __init__(self, size=20):
        self.__stack = []
        self.__SIZE = size

    def push(self, data):
        if len(self.stack) >= self.__SIZE:
            print("Stack is full")
            return
        self.__stack.append(data)
        self.__SIZE += 1
        print(f"Pushed: {data}")

    def pop(self):
        if len(self.__stack) == 0:
            print("Stack is empty")
            return
        data = self.__stack.pop()
        print(f"Popped: {data}")

    def seek(self):
        if len(self.__stack) == 0:
            print("Stack is empty")
            return
        print(f"Seek: {self.__stack[-1]}")

    def display(self):
        if len(self.__stack) == 0:
            print("Stack is empty")
            return
        for data in self.__stack:
            print(data, end=' ')
