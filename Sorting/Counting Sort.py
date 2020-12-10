#User function Template for python3
'''
Function Arguments :
		@param  : s(given string), n (size of string)
		@return : String, Return the sorted string
'''

def countingSort(s,n):
    # code here
    arr = [0]*26
    output = ["" for _ in range(n)]
    for i in s:
        arr[ord(i)-97] += 1
    for i in range(1,len(arr)):
        arr[i] += arr[i-1]
    for i in s:
        arr[ord(i)-97] -= 1
        output[arr[ord(i)-97]] = i
    return "".join(output)
#{
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

#Contributed by : Nagendra Jha

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        s=str(input())
        print(countingSort(s,n))

# } Driver Code Ends