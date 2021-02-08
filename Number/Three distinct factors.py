# User function Template for python3
import math


class Solution:
    def hasThreePrimeFac(self, N):
        # code here
        factor = False
        if N == 1:
            return 0
        for i in range(2, int(math.sqrt(N))):
            # base case
            if factor == True:
                return 0

            if N % i == 0:
                factor = True
        if factor == True:
            return 0
        else:
            return 1


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())

        ob = Solution()
        print(ob.hasThreePrimeFac(N))
# } Driver Code Ends