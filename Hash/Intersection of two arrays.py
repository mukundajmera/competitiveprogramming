# User function Template for python3

def NumberofElementsInIntersection(a, b, n, m):
    # return: expected length of the intersection array.
    setA = set(a)
    setB = set(b)
    return len(setA.intersection(setB))
    # code here


# {
#  Driver Code Starts
# Initial Template for Python 3


# contributed by RavinderSinghPB

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = [int(x) for x in input().strip().split()]

        a = [int(x) for x in input().strip().split()]
        b = [int(x) for x in input().strip().split()]

        print(NumberofElementsInIntersection(a, b, n, m))

# } Driver Code Ends