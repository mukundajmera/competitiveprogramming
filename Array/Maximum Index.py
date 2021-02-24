# User function Template for python3
def maxIndexDiff(arr, n):
    maxDiff = 0;
    # to find minimum
    LMin = [0] * n
    # to find maximum
    RMax = [0] * n
    # setting Minimum as first element index
    LMin[0] = arr[0]
    # finding minimum as each index
    for i in range(1, n):
        # print(arr[i], LMin[i - 1])
        LMin[i] = min(arr[i], LMin[i - 1])

    # setting maximum as first element index
    RMax[n - 1] = arr[n - 1]
    # finding maximum as each index
    for j in range(n - 2, -1, -1):
        # print(arr[j], RMax[j + 1])
        RMax[j] = max(arr[j], RMax[j + 1]);

    # print(LMin)
    # print(RMax)
    i, j = 0, 0
    maxDiff = -1
    while (j < n and i < n):
        if (LMin[i] <= RMax[j]):
            # print(LMin[i],RMax[j],j-i)
            maxDiff = max(maxDiff, j - i)
            j = j + 1
        else:
            i = i + 1
    return maxDiff


# {
#  Driver Code Starts
# Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):
        n = int(input())

        arr = [int(x) for x in input().strip().split()]
        print(maxIndexDiff(arr, n))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends