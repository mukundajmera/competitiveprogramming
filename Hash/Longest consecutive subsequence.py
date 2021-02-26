# User function Template for python3

# arr[] : the input array
# N : size of the array arr[]

# return the length of the longest subsequene of consecutive integers
def findLongestConseqSubseq(arr, N):
    # code here
    # use hash approch
    hashM = set(arr)

    longest = 0
    for i in range(N):
        curr = 0
        if (arr[i] - 1) not in hashM:
            curr = 1
            while (arr[i] + curr) in hashM:
                curr += 1
            longest = max(longest, curr)
    return longest


# {
#  Driver Code Starts
# Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        n = int(input())
        a = list(map(int, input().strip().split()))
        print(findLongestConseqSubseq(a, n))
# } Driver Code Ends