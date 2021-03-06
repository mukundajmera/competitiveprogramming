# User function Template for python3

'''
Structure of node

# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

'''


def countNodesinLoop(head):
    # Your code here
    if head.next == None:
        return 0
    slow = head
    fast = head
    prev = None
    while fast != None and fast.next != None:
        slow = slow.next
        prev = fast.next
        fast = fast.next.next
        if slow == fast:
            break
    if slow != fast:
        return 0

    slow = head
    while slow.next != fast.next:
        slow = slow.next
        prev = fast
        fast = fast.next
    count = 0
    if fast == head:
        prev.next = None
        count += 1
    else:
        fast.next = None

    while slow.next != None:
        slow = slow.next
        count += 1
    return count


# {
#  Driver Code Starts
# Initial Template for Python 3

# Node Class
class Node:
    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None


# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

    # connects last node to node at position pos from begining.
    def loopHere(self, pos):
        if pos == 0:
            return

        walk = self.head
        for i in range(1, pos):
            walk = walk.next

        self.tail.next = walk


if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())

        LL = LinkedList()
        for i in input().split():
            LL.insert(int(i))

        LL.loopHere(int(input()))

        print(countNodesinLoop(LL.head))

# } Driver Code Ends