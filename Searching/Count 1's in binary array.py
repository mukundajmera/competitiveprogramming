# User function Template for python3
def countOnes(arr, N):
    # Your code here
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == 1 and (mid == N - 1 or arr[mid + 1] == 0):
            return mid + 1

        if arr[mid] == 1:
            low = mid + 1
        elif arr[mid] == 0:
            high = mid - 1
    return mid


# {
#  Driver Code Starts
# Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):
        N = int(input())

        A = [int(x) for x in input().strip().split()]

        print(countOnes(A, N))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends