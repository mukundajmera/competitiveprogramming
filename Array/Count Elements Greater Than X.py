# User function Template for python3

def greaterThanX(arr, n, x):
    # return required result
    # code here
    count = 0
    for i in arr:
        if i > x:
            count += 1

    return count


# {
#  Driver Code Starts
# Initial Template for Python 3

# contributed by RavinderSinghPB
if __name__ == '__main__':
    tcs = int(input())

    for _ in range(tcs):
        n = int(input())
        arr = [int(e) for e in input().split()]
        x = int(input())

        ans = greaterThanX(arr, n, x)
        print(ans)
# } Driver Code Ends