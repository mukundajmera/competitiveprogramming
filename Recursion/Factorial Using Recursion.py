# User function Template for python3

def factorial(n):
    # code here
    if n <= 1:
        return 1

    return n * factorial(n - 1)


# {
#  Driver Code Starts
# Initial Template for Python 3

# contributed by RavinderSinghPB
if __name__ == '__main__':
    tcs = int(input())

    for _ in range(tcs):
        n = int(input())

        print(factorial(n))
# } Driver Code Ends