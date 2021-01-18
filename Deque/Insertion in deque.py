# User function Template for python3

def deque_Init(arr, n):
    # code here
    dq = deque()
    for i in range(len(arr)):
        dq.append(arr[i])
    return dq


# {
#  Driver Code Starts
# Initial Template for Python 3

# contributed by RavinderSinghPB
if __name__ == '__main__':

    from collections import deque

    tcs = int(input())

    for _ in range(tcs):
        n = int(input())
        arr = [int(x) for x in input().split()]

        dq = deque_Init(arr, n)

        for e in dq:
            print(e, end=' ')
        print()
# } Driver Code Ends