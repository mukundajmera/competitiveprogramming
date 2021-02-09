#User function Template for python3

class Solution:
    def sieveOfEratosthenes(self, N):
    	#code here
    	isPrime = [True for _ in range(N+1)]
    	num = 2
    	#iter over each number
    	while(num * num <= N):
    	    if (isPrime[num] == True):
    	        for multiple in range(num*num,N+1,num):
    	            isPrime[multiple] = False
    	    num += 1
    	result = []
    	for num in range(2,N+1):
    	    if isPrime[num]:
    	        result.append(num)
        return result


#{
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.sieveOfEratosthenes(N)
        for i in ans:
            print(i, end=" ")
        print()
# } Driver Code Ends