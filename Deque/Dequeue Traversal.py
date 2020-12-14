# User function Template for python3

def printDeque(deq):
    # CODE HERE
    for i in deq:
        print(i, end=" ")


# {
#  Driver Code Starts
# Initial Template for Python 3

# contributed by RavinderSinghPB
if __name__ == '__main__':

    from collections import deque

    tcs = int(input())

    for _ in range(tcs):
        n = int(input())
        arr = [int(x) for x in input().split()]

        deq = deque(arr)

        printDeque(deq)
        print()
# } Driver Code Ends