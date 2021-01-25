# User function Template for python3
def lastIndex(arr):
    low = 0
    high = len(l) - 1

    while low <= high:

        mid = (low + high) // 2

        if l[mid] < x:
            low = mid + 1

        elif l[mid] > x:
            high = mid - 1

        else:

            if mid == len(l) - 1 or l[mid] != l[mid + 1]:
                return mid
            else:
                low = mid + 1
    return -1

##Complete this function
def searchInSorted(arr, N, K):
    # Your code here
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if K == arr[mid]:
            return 1

        if arr[mid] > K:
            high = mid - 1
        else:
            low = mid + 1
    return -1


# {
#  Driver Code Starts
# Initial Template for Python 3

import math

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        NK = input().strip().split()
        N = int(NK[0])
        K = int(NK[1])
        A = [int(x) for x in input().strip().split()]
        print(searchInSorted(A, N, K))

# } Driver Code Ends