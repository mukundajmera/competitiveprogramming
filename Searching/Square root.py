# User function Template for python3
import math


# Complete this function
def floorSqrt(x):
    # Your code here
    return math.floor(math.sqrt(x))


# #Complete this function
# def floorSqrt(x):
#     #Your code here
#     if x == 0 or x == 1:
#         return x
#     start = 1
#     end = x
#     ans = 1
#     while start <= end:
#         mid = start + end // 2
#         if mid ** 2 == x:
#             return mid

#         if mid ** 2 < x:
#             start = mid + 1
#             ans = mid
#         else:
#             end = mid - 1

#     return ans

# {
#  Driver Code Starts
# Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):
        x = int(input())

        print(floorSqrt(x))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends