# User function Template for python3
import math


class Solution:
    def primeRange(self, M, N):
        # code here
        result = []
        for number in range(M, N + 1):
            if number == 1:
                continue
            if number == 2:
                result.append(number)
            isPrime = True
            limit = int(math.sqrt(number))
            if number % 2 == 0:
                continue
            else:
                if limit > 2:
                    iter = 3
                    while iter <= limit:
                        if number % iter == 0:
                            isPrime = False
                            break
                        iter += 2

            if isPrime:
                result.append(number)
        return result


# {
#  Driver Code Starts
# Initial Template for Python 3

import math

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        M, N = map(int, input().strip().split(" "))
        ob = Solution()
        ans = ob.primeRange(M, N)
        for i in ans:
            print(i, end=" ")
        print()
        # } Driver Code Ends