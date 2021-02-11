#User function Template for python3

class Solution:
    def isSubSequence(self, A, B):
        #code here
        strA = list(A)
        strB = list(B)
        posA = 0
        for i in range(len(strB)):
            if  posA < len(strA) and strA[posA] == strB[i]:
                posA += 1
        if len(strA) == posA:
            return True
        else:
            return False


#{
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        A,B = input().split()
        ob = Solution()
        if ob.isSubSequence(A,B):
            print(1)
        else:
            print(0)

# } Driver Code Ends