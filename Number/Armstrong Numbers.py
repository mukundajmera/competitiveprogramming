#User function Template for python3

#User function Template for python3
class Solution:
    def armstrongNumber (ob, n):
        # code here
        sum = 0
        for i in str(n):
            sum += int(i)**3
        if n == sum:
            return "Yes"
        else:
            return "No"



#{
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    t = int (input ())
    for _ in range (t):
        n = input()
        n=int(n)
        ob = Solution()
        print(ob.armstrongNumber(n))
# } Driver Code Ends