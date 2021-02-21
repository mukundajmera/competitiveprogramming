# User function Template for python3
def leaders(A, N):
    # Your code here
    res = []
    max = -1
    for i in range(N - 1, -1, -1):
        if A[i] >= max:
            max = A[i]
            res.append(A[i])
    res = res[::-1]
    return res


# {
#  Driver Code Starts
# Initial Template for Python 3

import math


def main():
    T = int(input())

    while (T > 0):

        N = int(input())

        A = [int(x) for x in input().strip().split()]

        A = leaders(A, N)

        for i in A:
            print(i, end=" ")
        print()

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends