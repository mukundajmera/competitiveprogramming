# User function Template for python3

def reverseArray(n, arr):
    # code here
    stack = arr.copy()
    for i in range(n):
        arr.pop()
    for i in range(n):
        arr.append(stack.pop())


# {
#  Driver Code Starts
# Initial Template for Python 3

# contributed by RavinderSinghPB
if __name__ == '__main__':
    tcs = int(input())

    for _ in range(tcs):
        n = int(input())
        arr = [int(x) for x in input().split()]

        reverseArray(n, arr)

        for e in arr:
            print(e, end=' ')
        print()
# } Driver Code Ends