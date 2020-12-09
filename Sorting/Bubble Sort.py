#User function Template for python3

'''Your task is to complete the bubble function
   which is used in bubbleSort() Function'''
'''def bubbleSort(arr, n):
    for i in range(n-1):
        arr = bubble(arr, i, n)
    return arr'''
# Function should return the array

def bubble(arr, i, n):
    # code here
    for j in range(n -i -1):
        if arr[j] > arr[j+1]:
            arr[j+1],arr[j] = arr[j],arr[j+1]
    return arr







#{
#  Driver Code Starts
#Initial Template for Python 3

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

def bubbleSort(arr, n):
    # code here
    for i in range(n-1):
        arr = bubble(arr, i, n)
    return arr

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        arr = bubbleSort(arr, n)
        for i in arr:
            print(i,end=' ')
        print ('')

# } Driver Code Ends