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
        self.tail = None

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

    def insert_bottom_two_pointers(self, key):
        """
        Inserts value at the bottom of the linked list.
        Not compatible with insert_top
        """
        new_node = Node(key)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def delete_node(self, key):
        """
        Deletes a node from the list
        """
        dummy = Node(0)
        dummy.next = self.head
        current = dummy
        while current.next:
            if current.next.key == key:
                current.next = current.next.next
            else:
                current = current.next
        return dummy.next

    def reverse_list(self):
        """
        Reverses a linked list
        """
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def swap_nodes(self, key1, key2):
        """Swaps 2 nodes"""
        # Find nodes
        prev1 = None
        current1 = self.head
        while current1 and current1.key != key1:
            prev1 = current1
            current1 = current1.next

        prev2 = None
        current2 = self.head
        while current2 and current2.key != key2:
            prev2 = current2
            current2 = current2.next

        if not current1 or not current2:
            return

        # If not head then swap nodes
        if prev1:
            prev1.next = current2
        else:
            self.head = current2

        # If not head then swap nodes
        if prev2:
            prev2.next = current1
        else:
            self.head = current1

        # Swap pointers
        current1.next, current2.next = current2.next, current1.next

    def remove_kth_node_from_end_of_list(self, k):
        """
        Removes kth node from the end of the list
        """
        fast = slow = self.head
        for _ in range(k):
            fast = fast.next
        
        if not fast:
            return self.head.next
        
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return self.head

    def rotate_right(self, k):
        """
        Rotates linked list by k steps from the right
        """
        count = 0
        current = self.head
        while current:
            current = current.next
            count += 1

        if count <= 1 or k == 0:
            return self.head

        if k > count:
            k = k % count

        if k == count or count <= 1 or k == 0:
            return self.head

        fast = slow = self.head
        for _ in range(count - k):
            slow = fast
            fast = fast.next

        slow.next = None
        slow = fast
        while fast.next:
            fast = fast.next

        fast.next = self.head
        return slow

    def print_list(self):
        """Prints the linked list"""
        current = self.head
        while current:
            print(current.key, end=" -> ")
            current = current.next
        print("None")
