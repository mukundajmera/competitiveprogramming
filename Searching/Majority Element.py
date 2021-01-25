# User function Template for python3


# Complete this function
def majorityElement(A, N):
    # Your code here
    count = 1
    potential = A[0]
    for i in A[1:]:
        if (count == 0):
            count = 1
            potential = i
        else:
            if i == potential:
                count += 1
            else:
                count -= 1

    # print(potential)
    ct = 0
    for i in A:
        if i == potential:
            ct += 1

    # print(ct,potential)
    if ct > (N / 2):
        return potential
    else:
        return -1


# {
#  Driver Code Starts
# Initial Template for Python 3

import math

from sys import stdin


def main():
    T = int(input())
    while (T > 0):
        N = int(input())

        A = [int(x) for x in input().strip().split()]

        print(majorityElement(A, N))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends