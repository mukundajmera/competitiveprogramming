# User function Template for python3

def reverseArray(arr, n):
    len_arr = len(arr)
    # code here
    for i in range(0, len_arr // 2):
        arr[i], arr[len_arr - i - 1] = arr[len_arr - i - 1], arr[i]

    return arr


# {
#  Driver Code Starts
# Initial Template for Python 3

# contributed by RavinderSinghPB
if __name__ == '__main__':
    tcs = int(input())

    for _ in range(tcs):
        n = int(input())
        arr = [int(x) for x in input().split()]

        reverseArray(arr, n)

        for e in arr:
            print(e, end=' ')
        print()
# } Driver Code Ends