# User function Template for python3
"""
Function Arguments :
		@param  : s (given string containing parenthesis)
		@return : boolean True or False
"""


def ispar(s):
    stack = []
    # code here
    for char in s:
        if char in '[{(':
            stack.append(char)
        else:
            # condition if empty/ middle checker/ valid pop
            if len(stack) == 0:
                return False
            elif not validPar(stack[-1], char):
                return False
            else:
                stack.pop()
    # if not empty invalid
    if len(stack) > 0:
        return False
    else:
        return True


def validPar(a, b):
    if a == '(' and b == ')' or \
            a == '[' and b == ']' or \
            a == '{' and b == '}':
        return True
    else:
        return False


# {
#  Driver Code Starts
# Initial Template for Python 3

import atexit
import io
import sys

# Contributed by : Nagendra Jha


_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        # n = int(input())
        # n,k = map(int,imput().strip().split())
        # a = list(map(int,input().strip().split()))
        s = str(input())
        if ispar(s):
            print("balanced")
        else:
            print("not balanced")
# } Driver Code Ends
