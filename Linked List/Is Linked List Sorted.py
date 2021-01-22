#User function Template for python3

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
def isSorted(head):
    isSorted = 1
    if head.next == None or head.next.next == None:
        return isSorted
    prev = head.data
    asce = True
    check = head
    #iterating till the common elements
    while check.data == head.data:
        check = check.next
    #check sort fashion
    if check.data < head.data:
        asce = False
    current = head.next
    while current:
        if (prev > current.data and asce == True) or (prev < current.data and asce == False):
            # print(asce,prev,current.data)
            isSorted = 0
            break
        prev = current.data
        current = current.next
    #code here
    return isSorted


#{
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
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


if __name__ == '__main__':
    t = int(input())

    for tcs in range(t):

        n = int(input())
        arr = [int(x) for x in input().split()]

        ll = Llist()
        tail = None

        for nodeData in arr:
            tail = ll.insert(nodeData, tail)

        res=isSorted(ll.head)
        print(res)
# } Driver Code Ends