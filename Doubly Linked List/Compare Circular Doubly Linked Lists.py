# User function Template for python3

def compareCLL(head1, head2):
    # code here
    node1 = head1
    node2 = head2
    if node1.data != node2.data:
        return 0
    node1 = node1.next
    node2 = node2.next

    while node1 != head1 and node2 != head2:
        if node1.data != node2.data:
            return 0
        node1 = node1.next
        node2 = node2.next
    return 1


# {
#  Driver Code Starts
# Initial Template for Python 3

# contributed by RavinderSinghPB
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class doublyLL:
    def __init__(self):
        self.head = None

    def insert(self, tail, data):
        head = self.head

        node = Node(data)

        if not head:
            self.head = node
            return node

        tail.next = node
        node.prev = tail
        return node


if __name__ == '__main__':
    tcs = int(input())

    for _ in range(tcs):
        n1 = int(input())
        arr1 = [int(x) for x in input().split()]
        n2 = int(input())
        arr2 = [int(x) for x in input().split()]

        dll1 = doublyLL()
        tail = None
        for nodeData in arr1:
            tail = dll1.insert(tail, nodeData)

        # making circular
        tail.next = dll1.head
        dll1.head.prev = tail

        dll2 = doublyLL()
        tail = None
        for nodeData in arr2:
            tail = dll2.insert(tail, nodeData)

        # making circular
        tail.next = dll2.head
        dll2.head.prev = tail

        print(compareCLL(dll1.head, dll2.head))

# } Driver Code Ends