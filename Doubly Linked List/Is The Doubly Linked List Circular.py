#User function Template for python3

def isCircular(head):
    #code here
    if head == None:
        return 0
    elif head.next == None:
        return 0
    else:
        current = head
        current = current.next
        while current != head:
            if current.next == None:
                return 0
            if current == head:
                return 1
            current = current.next
        return 1

#{
#  Driver Code Starts
#Initial Template for Python 3

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
        n = int(input())
        arr = [int(x) for x in input().split()]
        x=int(input())


        dll = doublyLL()

        tail = None

        for nodeData in arr:
            tail = dll.insert(tail, nodeData)

        if x==1:
            # making circular
            tail.next = dll.head
            dll.head.prev = tail

        print(isCircular(dll.head))





# } Driver Code Ends