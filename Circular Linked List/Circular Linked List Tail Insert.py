#User function Template for python3

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

def insertInTail(head,x):
    #code here
    node = Node(x)
    if head == None:
        node.next = node
        return node
    else:
        node.next = head.next
        head.next = node
        head.data , node.data =  node.data ,head.data
        return node


#{
#  Driver Code Starts
#Initial Template for Python 3

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



def displayList(head):
    t=head
    while t.next!=head:
        print(t.data,end=' ')
        t=t.next
    print(t.data,end=' ')



if __name__ == '__main__':
    t = int(input())

    for tcs in range(t):

        n = int(input())
        arr = [int(x) for x in input().split()]
        data=int(input())

        ll = Llist()
        tail = None

        for nodeData in arr:
            tail = ll.insert(nodeData, tail)
        #making circular
        tail.next=ll.head

        resHead=insertInTail(ll.head,data)
        displayList(resHead)
        print()
# } Driver Code Ends