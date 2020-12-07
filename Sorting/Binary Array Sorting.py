# User function Template for python3


##Complete this function
def binSort(arr, n):
    # Your code here
    right = n
    left = -1

    while True:

        # loop left
        left += 1
        while left < n and arr[left] == 0:
            left += 1

        # loop right
        right -= 1
        while right > -1 and arr[right] == 1:
            right -= 1
        # break condition
        if left > right:
            break
        # swap
        arr[left], arr[right] = arr[right], arr[left]
    '''
    No need to print the array
    '''


# {
#  Driver Code Starts
# Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):
        N = int(input())
        A = list(map(int, input().split()))

        binSort(A, N)

        for i in A:
            print(i, end=" ")
        print()

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends