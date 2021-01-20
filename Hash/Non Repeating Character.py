# User function Template for python3

'''
	Your task is to return the index of lefmost non-repeating
	character or return
	-1 if all characters occur more than once.

	Function Arguments: s (given string)
	Return Type: integer
'''


def nonrepeatingCharacter(s):
    # code here

    array = {item: 0 for item in s}

    for char in s:
        array[char] += 1

    for char in s:
        if array[char] == 1:
            return char

    return '$'


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
    for i in range(t):
        s = str(input())
        ans = nonrepeatingCharacter(s)
        if (ans != '$'):
            print(ans)
        else:
            print(-1)

# } Driver Code Ends