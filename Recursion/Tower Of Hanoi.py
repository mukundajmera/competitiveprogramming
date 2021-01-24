# User function Template for python3

class Solution:

    def toh(self, n, fromm, to, aux):
        c=0
        if n==1:
            print("move disk",n,"from rod",fromm,"to rod",to)
            return c+1
        c+=self.toh(n-1,fromm,aux,to)
        print("move disk",n,"from rod",fromm,"to rod",to)
        c+=self.toh(n-1,aux,to,fromm)
        return c+1



#{
#  Driver Code Starts
# Initial Template for Python 3


import math


def main():

    T = int(input())

    while(T > 0):

        N = int(input())
        ob = Solution()
        print(ob.toh(N, 1, 3, 2))

        T -= 1

if __name__ == "__main__":
    main()


# } Driver Code Ends