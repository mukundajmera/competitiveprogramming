# User function Template for python3
import math


class Solution:
    def isPrime(self, N):
        # code here
        num = int(math.sqrt(N))

        isPrime = 1

        if N == 1:
            return 0

        for i in range(2, num + 1):
            if N % i == 0:
                isPrime = 0
                break
        return isPrime


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())

        ob = Solution()
        print(ob.isPrime(N))
# } Driver Code Ends