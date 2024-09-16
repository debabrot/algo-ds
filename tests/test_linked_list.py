"""Tests Linked list"""

from data_structures.linked_list import LinkedList


def test_insert():
    llist = LinkedList()
    llist.insert_top(10)
    assert 10 == llist.head.key
