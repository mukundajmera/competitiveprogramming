# User function Template for python3

def smallerThanX(arr, n, x):
    # return required ans
    # code here
    count = 0
    for i in arr:
        if i < x:
            count += 1
    return count


# {
#  Driver Code Starts
# Initial Template for Python 3

# contributed by RavinderSinghPB
if __name__ == '__main__':
    from math import inf

    t = int(input())

    for _ in range(t):
        n = int(input())
        arr = [int(e) for e in input().split()]
        x = int(input())

        ans = smallerThanX(arr, n, x)
        print(ans)
# } Driver Code Ends