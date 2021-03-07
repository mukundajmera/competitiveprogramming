#!/bin/python3

import math
import os
import random
import re
import sys


class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail

        self.tail = node


def print_doubly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)


# Complete the sortedInsert function below.

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#
def sortedInsert(head, data):
    if head == None:
        node = DoublyLinkedListNode(data)
        return node
    elif head.data > data:
        # insert at head
        node = DoublyLinkedListNode(data)
        node.next = head
        head.prev = node
        return node
    else:
        curr = head
        prev = head
        while (curr != None and data > curr.data):
            prev = curr
            curr = curr.next
        # check if last node
        node = DoublyLinkedListNode(data)
        if prev:
            print(prev.data)
        if curr:
            print(curr.data)
        if prev.next == None:
            prev.next = node
            node.prev = prev
        else:
            temp = prev.next
            # setting new node
            prev.next = node
            node.prev = prev
            # adding in between
            node.next = temp
            temp.prev = node
        return head


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        llist_count = int(input())

        llist = DoublyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        data = int(input())

        llist1 = sortedInsert(llist.head, data)

        print_doubly_linked_list(llist1, ' ', fptr)
        fptr.write('\n')

    fptr.close()
