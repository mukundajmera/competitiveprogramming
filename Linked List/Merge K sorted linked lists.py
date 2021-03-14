# User function Template for python3
'''
	Your task is to merge the given k sorted
	linked lists into one list and return
	the the new formed linked list class.

	Function Arguments:
	    arr is a list containing the n linkedlist head pointers
	    n is an integer value

    node class:

class Node:
    def __init__(self,x):
        self.data = x
        self.nxt = None
'''
import heapq as hq


def mergeKLists(lists, k):
    heap = [(lists[i].data, i) for i in range(k) if lists[i]]
    hq.heapify(heap)
    head = Node(0)
    curr = head
    while heap:
        tup = hq.heappop(heap)
        node, index = Node(tup[0]), tup[1]
        curr.next = node
        curr = curr.next
        if lists[index].next:
            lists[index] = lists[index].next
            hq.heappush(heap, (lists[index].data, index))
    return head.next


# def mergeKLists(arr,N):
#     # code here
#     # return head of merged list


# {
#  Driver Code Starts
# Initial Template for Python 3

class Node:
    def __init__(self, x):
        self.data = x
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, x):
        if self.head is None:
            self.head = Node(x)
            self.tail = self.head
        else:
            self.tail.next = Node(x)
            self.tail = self.tail.next


def printList(head):
    walk = head
    while walk:
        print(walk.data, end=' ')
        walk = walk.next
    print()


if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        line = [int(x) for x in input().strip().split()]

        heads = []
        index = 0

        for i in range(n):
            size = line[index]
            index += 1

            newList = LinkedList()

            for _ in range(size):
                newList.add(line[index])
                index += 1

            heads.append(newList.head)

        merged_list = mergeKLists(heads, n)
        printList(merged_list)

# } Driver Code Ends