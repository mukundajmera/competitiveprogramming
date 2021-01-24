# User function Template for python3

def printArrayRecursively(arr, n):
    # code here
    if n <= 0:
        return 0
    printArrayRecursively(arr, n - 1)
    print(arr[(n - 1)], end=" ")


# {
#  Driver Code Starts
# Initial Template for Python 3

# contributed by RavinderSinghPB
if __name__ == '__main__':
    tcs = int(input())

    for _ in range(tcs):
        n = int(input())
        arr = [int(x) for x in input().split()]

        printArrayRecursively(arr, n)
        print()
# } Driver Code Ends