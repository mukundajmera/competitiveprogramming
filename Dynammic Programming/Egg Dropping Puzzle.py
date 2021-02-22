# User function Template for python3

# Function to get minimum number of trials needed in worst
# case with n eggs and k floors
import math


def eggDrop(n, k):
    # code here
    # create table of n+1, k+1
    dp = [[None] * (n + 1) for i in range(k + 1)]
    # fill
    # floor 0 with egg is zero
    # floor 1 with egg is 1
    for i in range(1, n + 1):
        # floor 1 with egg is 1
        dp[1][i] = 1
        # floor 0 with egg is zero
        dp[0][i] = 0

    for j in range(k + 1):
        # egg 1 for each floor is 1
        dp[j][1] = j
    # check for egg with n value with f floors
    # min (max( case1 (break), case2 (do not break))) + 1
    # min(dp[i][j], (max( dp[x-1,n-1], dp[f-x,e])) + 1)
    for floor in range(2, k + 1):
        for egg in range(2, n + 1):
            dp[floor][egg] = math.inf
            # iter for x
            for rem in range(1, floor + 1):
                dp[floor][egg] = min(dp[floor][egg], 1 + max(dp[rem - 1][egg - 1], dp[floor - rem][egg]))
    # print(dp)
    # print(dp[k][n])
    return dp[k][n]


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
        n, k = map(int, input().strip().split())
        print(eggDrop(n, k))
# } Driver Code Ends