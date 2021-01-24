# User function Template for python3

def GCD(a, b):
    # code here
    if a == 0:
        return b
    if b == 0:
        return a

    return GCD(b, a % b)


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    tcs = int(input())

    for _ in range(tcs):
        a, b = [int(x) for x in input().split()]

        print(GCD(a, b))
# } Driver Code Ends