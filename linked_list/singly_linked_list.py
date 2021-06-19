#!/usr/bin/python3

from linked_list import LinkedList

class SinglyLinkedList(LinkedList):
    def __init__(self):
        super()

    def add_node_at_last(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            node = self.head
            while(node.next is not None):
                node = node.next
            node.next = new_node

    def add_node_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def add_node_at_nth_pos(self, data):
        pass

    def remove_node_at_last(self, data):
        pass

    def remove_node_at_beginning(self, data):
        pass

    def remove_node_at_nth_pos(self, nth):
        pass

    def display(self):
        if self.head == None:
            print("Singly Linked list is empty")
            return
        node = self.head
        while(node is not None):
            print(node.data, end=' -> ')
            node = node.next
