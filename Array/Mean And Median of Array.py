# {
# Driver Code Starts
# Initial Template for Python 3


import math


# } Driver Code Ends

# User function Template for python3


##Complete the below codes
def median(A, N):
    A.sort()
    ##Your code here
    # If median is fraction then convert the median to integer and return

    if N % 2 == 0:
        return int((A[N // 2] + A[(N // 2) - 1]) / 2)
    else:
        return A[(N // 2)]


def mean(A, N):
    ##Your code here
    return int(sum(A) / N)


# {
# Driver Code Starts.

def main():
    T = int(input())

    while (T > 0):
        N = int(input())
        a = [int(x) for x in input().strip().split()]

        print(mean(a, N), median(a, N))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends