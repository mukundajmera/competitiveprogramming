# User function Template for python3
import sys

memo = [False] * 84
result = []


def printFibb(n):
    a = 1
    b = 1
    res = [1, 1]
    if n == 1:
        return [1]
    elif n == 2:
        return res
    else:
        for i in range(2, n):
            res.append(res[i - 1] + res[i - 2])
        return res


# def printFibb(n):
#     # your code here
#     global memo
#     if memo[n] == False:
#         res = -1
#         if n == 0 or n == -1:
#             res = n
#         else:
#             res = printFibb(n-1) + printFibb(n-2)
#         memo[n] = res
#     return memo[n]


# {
#  Driver Code Starts
# Initial Template for Python 3

# contributed by RavinderSinghPB
if __name__ == '__main__':
    t = int(input())
    for tcs in range(t):

        n = int(input())
        res = printFibb(n)
        for i in range(len(res)):
            print(res[i], end=" ")
        print()
# } Driver Code Ends