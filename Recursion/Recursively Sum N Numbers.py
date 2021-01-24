# User function Template for python3

def recursiveSum(n):
    # code here
    if n <= 0:
        return 0
    return n + recursiveSum(n - 1)


# {
#  Driver Code Starts
# Initial Template for Python 3

# contributed by RavinderSinghPB
if __name__ == '__main__':
    tcs = int(input())

    for _ in range(tcs):
        n = int(input())

        print(recursiveSum(n))
# } Driver Code Ends