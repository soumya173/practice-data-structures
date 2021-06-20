#!/usr/bin/python3

from .linked_list import LinkedList
from .linked_list import Node

class SinglyLinkedList(LinkedList):
    def add_node_at_last(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            node = self.head
            while(node.next is not None):
                node = node.next
            node.next = new_node
        return data

    def add_node_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        return data

    def add_node_at_nth_pos(self, nth, data):
        list_length = self.length()
        if nth > list_length:
            raise OverflowError(f"Nth value ({nth}) is more than list length ({list_length})")
        if self.head == None or nth == 0:
            self.add_node_at_beginning(data)
            return data
        node = self.head
        counter = 1
        new_node = Node(data)
        while(node is not None):
            if counter == nth:
                break
            counter += 1
            node = node.next
        new_node.next = node.next
        node.next = new_node
        return data

    def remove_node_at_last(self):
        if self.head is None:
            raise IndexError("Singly List is empty")
        next_node = self.head
        prev_node = None
        while(next_node.next is not None):
            prev_node = next_node
            next_node = next_node.next
        prev_node.next = None
        return prev_node.data

    def remove_node_at_beginning(self):
        if self.head is None:
            raise IndexError("Singly List is empty")
        node = self.head
        self.head = node.next
        return self.head.data

    def remove_node_at_nth_pos(self, nth):
        if self.head is None:
            raise IndexError("Singly List is empty")
        list_length = self.length()
        if nth > list_length:
            raise OverflowError(f"Nth value ({nth}) is more than list length ({list_length})")
        next_node = self.head
        prev_node = None
        counter = 1
        while(next_node.next is not None):
            if counter == nth:
                break
            counter += 1
            prev_node = next_node
            next_node = next_node.next
        prev_node.next = next_node.next
        next_node.next = None
        return next_node.data

    def length(self):
        counter = 0
        node = self.head
        while(node is not None):
            counter += 1
            node = node.next
        return counter

    def clear(self):
        self.head = None

    def get_list(self):
        node = self.head
        all_elements = []
        while(node is not None):
            all_elements.append(node.data)
            node = node.next
        return all_elements

    def display(self):
        if self.head == None:
            print("Singly Linked list is empty")
            return
        node = self.head
        while(node is not None):
            print(node.data, end=' -> ')
            node = node.next
        print("")
