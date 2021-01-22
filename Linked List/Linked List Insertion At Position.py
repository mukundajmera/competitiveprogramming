# User function Template for python3
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''


def insertAtPosition(head, pos, data):
    # code here
    temp = Node(data)
    if pos == 1:
        temp.next = head
        # return temp (ideally condition)
        # head = temp
    else:
        current = head

        # for loop till traversal of position
        for i in range(pos - 1):
            current = current.next
            # overflow of position
            if current == None:
                return head

        temp.next = current.next
        current.next = temp


# {
#  Driver Code Starts
# Initial Template for Python 3

# contributed by RavinderSinghPB
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Llist:
    def __init__(self):
        self.head = None

    def insert(self, data, tail):
        node = Node(data)

        if not self.head:
            self.head = node
            return node

        tail.next = node
        return node


def printList(head):
    while head:
        print(head.data, end=' ')
        head = head.next


if __name__ == '__main__':
    t = int(input())

    for tcs in range(t):

        n = int(input())
        arr = [int(x) for x in input().split()]
        pos, data = [int(x) for x in input().split()]

        ll = Llist()
        tail = None

        for nodeData in arr:
            tail = ll.insert(nodeData, tail)

        insertAtPosition(ll.head, pos, data)
        printList(ll.head)
        print()
# } Driver Code Ends