"""  list Node is as defined below:

class Node:
    def __init__(self, data):
		self.data = data
		self.next = None

"""


# complete this function
# return head of list after swapping

def pairWiseSwap(head):
    # code here
    # base check
    if head == None or head.next == None:
        return head
    curr = head.next.next
    prev = head
    head = head.next
    head.next = prev
    while curr != None and curr.next != None:
        # connect old list
        prev.next = curr.next
        # move pointer
        prev = curr
        # take hold of next iter
        next = curr.next.next
        # reverse pointer
        curr.next.next = curr
        # move curr pointer
        curr = next

    # cleaner code
    prev.next = curr
    return head


# {
#  Driver Code Starts
# Initial Template for Python 3

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next


def printList(n):
    while n:
        print(n.data, end=' ')
        n = n.next
    print()


if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = [int(x) for x in input().split()]

        lis = LinkedList()
        for i in arr:
            lis.insert(i)

        dict1 = {}
        temp = lis.head
        while temp:
            dict1[temp] = temp.data
            temp = temp.next

        failure = LinkedList()
        failure.insert(-1)

        head = pairWiseSwap(lis.head)

        temp = head
        f = 0
        while temp:
            if dict1[temp] != temp.data:
                f = 1;
            temp = temp.next

        if f:
            printList(failure)
        else:
            printList(head)

# } Driver Code Ends