#User function Template for python3

def stackMiddle(n,stack):
    #code here
    return stack[-(n//2)-1]


#{
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__=='__main__':
    tcs=int(input())

    for _ in range(tcs):
        n=int(input())
        stack=[int(x) for x in input().split()]

        print(stackMiddle(n, stack))
# } Driver Code Ends