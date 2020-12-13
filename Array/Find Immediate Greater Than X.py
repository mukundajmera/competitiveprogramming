# User function Template for python3

# inf has been imported in driver code
def immediateGreater(arr, n, x):
    # return required ans
    # code here
    arr.sort(reverse=True)
    if arr[0] <= x:
        return -1
    else:
        for i in range(0, len(arr)):
            if arr[i] <= x:
                return arr[i - 1]
    return arr[-1]


# {
#  Driver Code Starts
# Initial Template for Python 3

# contributed by RavinderSinghPB
if __name__ == '__main__':
    from math import inf

    tcs = int(input())

    for _ in range(tcs):
        n = int(input())
        arr = [int(e) for e in input().split()]
        x = int(input())

        ans = immediateGreater(arr, n, x)
        print(ans)
# } Driver Code Ends