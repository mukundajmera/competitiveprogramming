# def maxSubArraySum(a,size):

#     max_so_far =a[0]
#     curr_max = a[0]

#     for i in range(1,size):
#         curr_max = max(a[i], curr_max + a[i])
#         max_so_far = max(max_so_far,curr_max)

#     return max_so_far
# User function Template for python3
##Complete this function
def maxSubArraySum(a, size):
    ##Your code here
    # create array for max sum so far
    currMax = a[0]
    result = a[0]
    # iterate loop to find maximum value from 1 to N
    for i in range(1, size):
        currMax = max(a[i], currMax + a[i])
        result = max(result, currMax)
        # print(a[i],currMax,result)
    # last value is answer
    return result


# {
#  Driver Code Starts
# Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):
        n = int(input())

        arr = [int(x) for x in input().strip().split()]

        print(maxSubArraySum(arr, n))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends