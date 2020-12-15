# A linked list (LL) node
# to store a queue entry
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class MyQueue:

    def __init__(self):
        self.front = None
        self.rear = None

    # Method to add an item to the queue
    def push(self, item):
        node = Node(item)
        if self.front == None:
            self.rear = node
            self.front = node
        else:
            self.rear.next = node
            self.rear = node

    # Method to remove an item from queue
    def pop(self):
        if self.front == None:
            return -1
        else:
            data = self.front.data
            self.front = self.front.next
            return data


# {
#  Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = MyQueue()
        q = int(input())
        q1 = list(map(int, input().split()))
        i = 0
        while (i < len(q1)):
            if (q1[i] == 1):
                s.push(q1[i + 1])
                i = i + 2
            elif (q1[i] == 2):
                print(s.pop(), end=" ")
                i = i + 1
            elif (s.isEmpty()):
                print(-1)
                i = i + 1
        print()
        # } Driver Code Ends