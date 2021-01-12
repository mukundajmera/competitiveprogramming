# User function Template for python3
import math

'''
heap = [0 for i in range(101)]  # our heap to be used
'''


def lChild(x):
    return (2 * x) + 1


def rChild(x):
    return (2 * x) + 2


def parent(x):
    return abs((x - 1) // 2)


def insertKey(x):
    '''
    :param x: Insert value in heap.
    :return: None
    '''
    global curr_size
    global heap
    heap.append(x)
    curr_size += 1
    i = curr_size - 1
    while i > 0 and heap[parent(i)] > heap[i]:
        p = parent(i)
        heap[i], heap[p] = heap[p], heap[i]
        i = p


def deleteKey(x):
    '''
    :param x: Index of value to be removed from heap.
    :return: None
    '''
    global curr_size
    global heap

    if x >= curr_size:
        return
    else:
        decreaseKey(x, -math.inf)
        extractMin()


def decreaseKey(i, x):
    heap[i] = x
    while i != 0 and heap[parent(i)] > heap[i]:
        p = parent(i)
        heap[i], heap[p] = heap[p], heap[i]
        i = p


def extractMin():
    '''
    :return: return the minimum element from heap and remove it.
    '''
    global curr_size
    global heap
    if curr_size == 0:
        return -1
    result = heap[0]
    print(heap)
    heap[0] = heap[curr_size - 1]  # assign last and pop
    heap.pop()
    minHeapify(0)
    return result


def minHeapify(i):
    global curr_size
    global heap

    lt = lChild(i)
    rt = rChild(i)
    smallest = i
    n = curr_size
    if lt < n and heap[lt] < heap[smallest]:
        smallest = lt
    if rt < n and heap[rt] < heap[smallest]:
        smallest = rt
    if smallest != i:
        heap[smallest], heap[i] = heap[i], heap[smallest]
        minHeapify(smallest)


# {
#  Driver Code Starts
# Initial Template for Python 3

import atexit
import io
import sys

# Contributed by : Nagendra Jha

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


heap = []  # our heap to be used
curr_size = 0  # current size of heap

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        a = list(map(int, input().strip().split()))
        # initialize every globals
        curr_size = 0
        heap = [0 for i in range(n)]
        i = 0
        while i < len(a):
            if a[i] == 1:
                insertKey(a[i + 1])
                i += 1
            elif a[i] == 2:
                deleteKey(a[i + 1])
                i += 1
            else:
                print(extractMin(), end=" ")
            i += 1
        # reinitialize every globals
        # curr_size = 0
        # heap = [0 for i in range(101)]
        print()
# } Driver Code Ends