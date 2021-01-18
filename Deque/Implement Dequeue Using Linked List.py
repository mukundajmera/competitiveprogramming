# User function Template for python3

'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class Deque:
    def __init__(self):
        self.front=None
        self.rear=None


given front and rear of deque in every operation,
return updated front and rear in each operation
'''


def insertFront(front, rear, data):
    # return: (front, rear)
    # code here
    node = Node(data)
    if front == None:
        front = node
        rear = node
    else:
        node.next = front
        front.prev = node
        front = node
    return front, rear


def insertRear(front, rear, data):
    # return: (front,rear)
    # code here
    node = Node(data)
    if rear == None:
        front = node
        rear = node
    else:
        node.prev = rear
        rear.next = node
        rear = node
    return front, rear


def delFront(front, rear):
    # return: (front, rear)
    # code here
    if front != None:
        temp = front
        front = front.next
        if front != None:
            front.prev = None
    if front == None:
        rear = None
        front = None
    return front, rear


def delRear(front, rear):
    # return: (front, rear)
    # code here
    if rear != None:
        temp = rear
        rear = rear.prev
        if rear != None:
            rear.next = None
    if rear == None:
        rear = None
        front = None
    return front, rear


# {
#  Driver Code Starts
# contributed by RavinderSinghPB
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Deque:
    def __init__(self):
        self.front = None
        self.rear = None


if __name__ == '__main__':
    tcs = int(input())

    for _ in range(tcs):
        q = int(input())

        dq = Deque()

        for _ in range(q):

            qry = input().split()

            if qry[0] == 'if':
                x = int(qry[1])
                dq.front, dq.rear = insertFront(dq.front, dq.rear, x)

            elif qry[0] == 'ir':
                x = int(qry[1])
                dq.front, dq.rear = insertRear(dq.front, dq.rear, x)

            elif qry[0] == 'df':
                dq.front, dq.rear = delFront(dq.front, dq.rear)

            else:  # dr
                dq.front, dq.rear = delRear(dq.front, dq.rear)

        if dq.front:
            print(dq.front.data)
            print(dq.rear.data)
        else:
            print(-1)
            print(-1)

# } Driver Code Ends