"""Basic Implementation of a linked list in python"""


class Node:
    """
    Node of a linked list. Contains 2 parameters key and next.
        key - Contains the value being stored
        next - refers to the next memory location
    """
    def __init__(self, key):
        self.key = key
        self.next = None


class LinkedList:
    """
    Implementation of a linked list in python. Contains 1 parameter:-
        head - refers to the top value of the linked list
    """
    def __init__(self):
        self.head = None

    def insert_top(self, key):
        """
        Inserts value at the top of the linked list
        """
        new_node = Node(key)
        new_node.next = self.head
        self.head = new_node

    def insert_bottom(self, key):
        """
        Inserts value at the bottom of the linked list
        """
        new_node = Node(key)
        current = self.head
        if self.head is None:
            new_node.next = self.head
            self.head = new_node
        else:
            while current.next:
                current = current.next
            current.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.key)
            current = current.next
