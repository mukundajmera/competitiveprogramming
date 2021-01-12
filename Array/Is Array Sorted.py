# User function Template for python3

def isSorted(arr, n):
    # code here
    point = arr[0]
    order = False
    if n > 1:
        if arr[0] <= arr[1]:
            order = True
        for i in range(1, len(arr)):
            if (order and (arr[i] < point)) or (not order and (arr[i] > point)):
                return 0
            point = arr[i]
    return 1


# {
#  Driver Code Starts
# Initial Template for Python 3

# contributed by RavinderSinghPB

if __name__ == '__main__':
    tcs = int(input())

    for _ in range(tcs):
        n = int(input())
        arr = [int(x) for x in input().split()]

        print(isSorted(arr, n))
# } Driver Code Ends