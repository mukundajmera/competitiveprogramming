# User function Template for python3

def isPalin(n):
    # code here
    number = str(n)
    if number == number[::-1]:
        return 1
    else:
        return 0


# {
#  Driver Code Starts
# Initial Template for Python 3

# contributed by RavinderSinghPB
if __name__ == '__main__':
    tcs = int(input())

    for _ in range(tcs):
        n = int(input())

        print(isPalin(n))
# } Driver Code Ends