# User function Template for python3
import math


class Solution:
    def __init__(self):
        self.dp = []

        def minCoins(self, coins, M, V):
            # code here
            # tabulation
            dp = [math.inf] * (V + 1)
            dp[0] = 0
            for value in range(1, V + 1):
                for coin in range(M):
                    if coins[coin] <= value:
                        sub_res = dp[value - coins[coin]]
                        # check for infinite
                        if sub_res != math.inf:
                            dp[value] = min(dp[value], sub_res + 1)

        # 		print(dp)
        if dp[-1] == math.inf:
            return -1
        else:
            return dp[-1]

        # get difference till end
        # return number of coins


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        v, m = input().split()
        v, m = int(v), int(m)
        coins = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.minCoins(coins, m, v)
        print(ans)

# } Driver Code Ends