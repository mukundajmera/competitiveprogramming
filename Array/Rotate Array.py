# User function Template for python3

# def rotateArr(A,D,N):
#     #Your code here
#     result = A[D:] + A[:D]
#     A[:] = result[:]

def rotateArr(A, D, N):
    # Your code here
    reverse(A, 0, D - 1)
    reverse(A, D, N - 1)
    reverse(A, 0, N - 1)


def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start = start + 1
        end = end - 1


# {
#  Driver Code Starts
# Initial Template for Python 3

import math


def main():
    T = int(input())

    while (T > 0):
        nd = [int(x) for x in input().strip().split()]
        N = nd[0]
        D = nd[1]
        A = [int(x) for x in input().strip().split()]

        rotateArr(A, D, N)

        for i in A:
            print(i, end=" ")

        print()

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends