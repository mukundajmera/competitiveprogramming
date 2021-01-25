# User function Template for python3

# Complete the below function
def search(arr, N, X):
    # Your code here
    for i in range(0, len(arr)):
        if X == arr[i]:
            return i
    return -1


# {
#  Driver Code Starts
# Initial Template for Python 3


import math


def main():
    T = int(input())
    while (T > 0):
        N = int(input())

        A = [int(x) for x in input().strip().split()]

        x = int(input())

        print(search(A, N, x))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends