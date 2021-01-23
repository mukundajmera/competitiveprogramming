#User function Template for python3
'''
Function Arguments :
		@param  : queue (given list on which queue is implemented)
		@param  : x (value to be used accordingly)
		@return : None
'''
def enqueue(queue, x):
    # code here
    queue.append(x)

def find(queue, x):
    # code here
    if x in queue:
        return True
    else:
        return False
def front(queue):
    # code here
    if len(queue) > 0:
        return queue[0]
def dequeue(queue):
    # code here
    if len(queue) == 0:
        return -1
    else:
        return queue.pop(0)



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
        a = list(map(str,input().strip().split()))
        queue = [] # our queue to be implemented
        i = 0 #current index
        while i < len(a):
            if a[i]=='i':
                enqueue(queue,a[i+1])
                i+=1
            elif a[i] == 'f' :
                if(find(queue,a[i+1])):
                    print("Yes")
                else:
                    print("No")
                i+=1
            elif a[i] == 'r' :
                (dequeue(queue))
            else:
                print(front(queue))
            i+=1
# } Driver Code Ends