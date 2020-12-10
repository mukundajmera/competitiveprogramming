# User function Template for python3

def countWords(s):
    # code here
    return len(s.split())


# {
#  Driver Code Starts
# Initial Template for Python 3

# contributed by RavinderSinghPB
if __name__ == '__main__':
    tcs = int(input())

    for _ in range(tcs):
        s = input()

        print(countWords(s))
# } Driver Code Ends