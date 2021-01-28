#User function Template for python3

def InsertInStack(n,arr):
    #code here
    stack = []
    for i in range(n):
        stack.append(arr[i])
    return stack



#{
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__=='__main__':
    tcs=int(input())

    for _ in range(tcs):
        n=int(input())
        arr=[int(x) for x in input().split()]

        stack=InsertInStack(n,arr)

        while stack:
            print(stack.pop(),end=' ')
        print()

# } Driver Code Ends