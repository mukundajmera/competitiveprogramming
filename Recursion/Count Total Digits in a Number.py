#User function Template for python3
def countDigits(n):
    '''
    :param n: given number
    :return: count of digits of n.
    '''
    # code here
    if n < 10:
        return 1
    return 1 + countDigits(n // 10)

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
        print(countDigits(n))
# } Driver Code Ends