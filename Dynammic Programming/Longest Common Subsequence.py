# User function Template for python3
# memo = [-1 for i in len(m)][-1]
# memo = [[-1 for x in range(m+1)] for y in range(n+1)]
def lcs(m, n, X, Y):
    t = [[0 for x in range(m + 1)] for x in range(n + 1)]
    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0 or j == 0:
                t[i][j] = 0
            elif Y[i - 1] == X[j - 1]:
                t[i][j] = 1 + t[i - 1][j - 1]
            else:
                t[i][j] = max(t[i - 1][j], t[i][j - 1])
    return t[n][m]


# def lcs(m,n,s1,s2):
#     '''
#     :param m: length of string s1
#     :param n: length of string s2
#     :param s1: string s1
#     :param s2: string s2
#     :return: Integer
#     '''
#     memo = [[0 for x in range(m+1)] for y in range(n+1)]
#     for i in range(1,n+1):
#         for j in range(1,m+1):
#             if s2[i-1] == s1[j-1]:
#                 memo[i][j] = 1 + memo[i-1][j-1]
#             else:
#                 memo[i][j] = max(memo[i-1][j], memo[i][j-1])

#     return memo[n][m]


# code here
# print(memo)
# for i in range(m):
#     memo[i][0] = 0
# for i in range(n):
#     memo[0][i] = 0

# #base case
# if m == 0 or n == 0:
#     return 0

# #on equal add and subcheck
# if s1[m-1] == s2[n-1]:
#     return 1 + lcs(m-1,n-1,s1,s2)
# else:
#     #check for sub problem
#     return max(lcs(m-1,n,s1,s2),lcs(m,n-1,s1,s2))


# {
#  Driver Code Starts
# Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        m, n = map(int, input().strip().split())
        X = str(input())
        Y = str(input())
        print(lcs(m, n, X, Y))
# } Driver Code Ends