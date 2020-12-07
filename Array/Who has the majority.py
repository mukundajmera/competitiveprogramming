# User function Template for python3

# Complete this function
def majorityWins(arr, n, x, y):
    # code here
    x_count = arr.count(x)
    y_count = arr.count(y)
    if x_count == y_count:
        return min(x, y)
    elif x_count > y_count:
        return x
    else:
        return y


# {
#  Driver Code Starts
if __name__ == '__main__':
    T = int(input())
    while (T > 0):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]

        x, y = map(int, input().strip().split())

        print(majorityWins(arr, n, x, y))
        T -= 1

# } Driver Code Ends