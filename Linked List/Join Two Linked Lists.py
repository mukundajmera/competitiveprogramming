# User function Template for python3

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''


def joinTheLists(head1, head2):
    # code here
    current = head1
    while current.next != None:
        current = current.next

    current2 = head2
    while current2:
        # point
        current.next = current2
        # shift
        current = current.next
        # traverse
        current2 = current2.next
    return head1


# {
#  Driver Code Starts
# Initial Template for Python 3

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
    tmp = head
    while (head != None):
        print(head.data, end=" ")
        head = head.next
    head = tmp
    print()


if __name__ == '__main__':
    t = int(input())

    for tcs in range(t):

        n = int(input())
        arr = [int(x) for x in input().split()]
        m = int(input())
        brr = [int(x) for x in input().split()]

        ll1 = Llist()
        ll2 = Llist()
        tail1 = None
        tail2 = None

        for nodeData in arr:
            tail1 = ll1.insert(nodeData, tail1)

        for nodeData in brr:
            tail2 = ll2.insert(nodeData, tail2)

        res = joinTheLists(ll1.head, ll2.head)
        printList(res)
# } Driver Code Ends