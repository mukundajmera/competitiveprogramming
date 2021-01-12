# User function Template for python3
import sys


# inf has been imported in driver code

def maximumElement(arr, n, ):
    # return required result
    # code here
    max = 0
    for i in arr:
        if max < i:
            max = i
    return max


def minimumElement(arr, n):
    # return required result
    # code here
    min = sys.maxsize
    for i in arr:
        if i < min:
            min = i
    return min


# {
#  Driver Code Starts
# Initial Template for Python 3

# contributed by RavinderSinghPB
if __name__ == '__main__':
    from math import inf

    tcs = int(input())

    for _ in range(tcs):
        n = int(input())
        arr = [int(e) for e in input().split()]

        max = maximumElement(arr, n, )
        min = minimumElement(arr, n)
        print(max, min)
# } Driver Code Ends