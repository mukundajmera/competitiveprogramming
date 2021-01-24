# User function Template for python3

def nCr(n, r):
    # code here
    if n <= 0 or r <= 0 or n == r:
        return 1
    else:
        return nCr(n - 1, r - 1) + nCr(n - 1, r)


# {
#  Driver Code Starts
# Initial Template for Python 3

# contributed by RavinderSinghPB
if __name__ == '__main__':
    tcs = int(input())

    for _ in range(tcs):
        n, r = [int(x) for x in input().split()]

        print(nCr(n, r))
# } Driver Code Ends